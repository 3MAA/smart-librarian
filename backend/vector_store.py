from __future__ import annotations
import os, shutil, logging
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from services.summary_tool import book_summaries_dict

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
PERSIST_DIR = "chroma_db"
COLLECTION  = "books"
EMBED_MODEL = "text-embedding-3-small"

def wipe_dir(path: str) -> None:
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path, exist_ok=True)

def rebuild() -> None:
    wipe_dir(PERSIST_DIR)
    emb = OpenAIEmbeddings(model=EMBED_MODEL)

    texts = [f"{title}. {summary}" for title, summary in book_summaries_dict.items()]
    metas = [{"title": title} for title in book_summaries_dict.keys()]

    Chroma.from_texts(
        texts=texts,
        embedding=emb,
        metadatas=metas,
        persist_directory=PERSIST_DIR,
        collection_name=COLLECTION,
    )
    logging.info("Rebuilt index with %d items.", len(texts))

if __name__ == "__main__":
    rebuild()
