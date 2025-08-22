import logging
from fastapi import APIRouter
from pydantic import BaseModel, Field
from services.retriever import find_best_book
from services.summary_tool import get_summary_by_title
from services.utils import contains_profanity
from core.openai_helper import generate_recommendation
from core.recommendation import build_recommendation_prompt
from better_profanity import profanity
import urllib.parse, traceback

router = APIRouter()
log = logging.getLogger("smart.profanity")

class AskRequest(BaseModel):
    query: str = Field(..., min_length=2)
    tts: bool = False

class AskResponse(BaseModel):
    title: str | None = None
    short_summary: str | None = None
    full_summary: str | None = None
    recommendation: str | None = None
    tts_url: str | None = None
    filtered: bool = False

def _safe_tts_url(text: str, filename_hint: str) -> str:
    enc = urllib.parse.quote_plus(text)
    fname = urllib.parse.quote_plus(f"{filename_hint}.mp3")
    return f"/tts?text={enc}&filename={fname}"

@router.post("/ask", response_model=AskResponse)
def ask(req: AskRequest):
    try:
        if contains_profanity(req.query):
            censored = profanity.censor(req.query)
            log.info("PROFANITY_BLOCK: tts=%s query_censored=%s", req.tts, censored)

            return AskResponse(
                filtered=True,
                recommendation="Let's keep the conversation respectful. Please rephrase your request.",
            )

        title, short_summary = find_best_book(req.query)
        if not title:
            return AskResponse(
                recommendation="I couldn't find a relevant book in the current library. Could you provide more details?"
            )

        msgs = build_recommendation_prompt(req.query, title, short_summary)
        recommendation = generate_recommendation(msgs)

        full_summary = get_summary_by_title(title)
        tts_url = _safe_tts_url(full_summary, title.replace(" ", "_")) if (req.tts and full_summary) else None

        return AskResponse(
            title=title,
            short_summary=short_summary,
            full_summary=full_summary,
            recommendation=recommendation,
            tts_url=tts_url,
            filtered=False,
        )
    except Exception:
        traceback.print_exc()
        return AskResponse(
            recommendation="Server error. Check the console for details.",
            filtered=False,
        )
