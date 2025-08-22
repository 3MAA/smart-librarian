from __future__ import annotations
from typing import List, Tuple, Dict, Any
import logging

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

from core.openai_helper import get_openai_client
from core.config import get_settings

log = logging.getLogger("smart.retriever")

PERSIST_DIR = "chroma_db"
COLLECTION  = "books"
EMBED_MODEL = "text-embedding-3-small"

_embeddings = OpenAIEmbeddings(model=EMBED_MODEL)
_vs = Chroma(
    persist_directory=PERSIST_DIR,
    collection_name=COLLECTION,
    embedding_function=_embeddings,
)

def retrieve_candidates(query: str, k: int = 6) -> List[Dict[str, Any]]:
    try:
        if hasattr(_vs, "max_marginal_relevance_search"):
            docs = _vs.max_marginal_relevance_search(query, k=k, fetch_k=max(2*k, 8))
        else:
            docs = _vs.similarity_search(query, k=k)

        out = []
        for d in docs:
            out.append({
                "title": d.metadata.get("title"),
                "text":  d.page_content,
                "vs_score": None
            })
        return out
    except Exception as e:
        log.exception("Vector search failed: %s", e)
        return []

def rerank_with_llm(query: str, candidates: List[Dict[str, Any]]) -> Tuple[str|None, str|None]:
    if not candidates:
        return None, None

    sys = (
        "You are a helpful book recommender. "
        "Given a user query and N candidate books (title + description), "
        "score each candidate from 0 to 1 for relevance, then pick the single best title. "
        "Respond ONLY in JSON with: {\"scores\": [{\"title\":\"...\",\"score\":0.0}], \"winner\":\"...\"}."
    )

    items = [{"title": c["title"], "text": c["text"][:900]} for c in candidates]

    user = {
        "query": query,
        "candidates": items
    }

    client = get_openai_client()
    model = get_settings().model_recommend
    completion = client.chat.completions.create(
        model=model,
        temperature=0.2,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": sys},
            {"role": "user", "content": str(user)}
        ],
    )

    import json
    data = json.loads(completion.choices[0].message.content)

    scores = {d["title"].strip().lower(): d["score"] for d in data.get("scores", [])}
    winner = (data.get("winner") or "").strip()

    if scores.get(winner.lower(), 0.0) < 0.5:
        return None, None

    for c in candidates:
        if (c["title"] or "").strip().lower() == winner.lower():
            short = (c["text"] or "")[:280]
            return c["title"], short

    short = (candidates[0]["text"] or "")[:280]
    return candidates[0]["title"], short


def find_best_book(query: str, k: int = 6) -> Tuple[str|None, str|None]:
    cands = retrieve_candidates(query, k=k)
    return rerank_with_llm(query, cands)
