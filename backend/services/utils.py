import logging
from better_profanity import profanity

log = logging.getLogger("smart.profanity")

profanity.load_censor_words()

WHITELIST = {
    "book", "books", "novel", "novels", "library", "librarian",
    "recommend", "recommendation", "about", "on", "love",
    "genre", "dystopia", "dystopian", "utopia", "utopian",
}

def contains_profanity(text: str) -> bool:

    if not text:
        return False

    if not profanity.contains_profanity(text):
        return False

    tokens = {t.lower() for t in text.split()}
    if tokens.issubset(WHITELIST):
        return False

    try:
        censored = profanity.censor(text)
        log.info("PROFANITY_BLOCK: %s", censored)
    except Exception:
        pass

    return True
