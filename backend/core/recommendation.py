from typing import List, Dict

def build_recommendation_prompt(user_query: str, title: str, short_summary: str | None = None) -> List[Dict[str, str]]:
    system = (
        "You are a helpful book-recommendation assistant. "
        "Always respond in clear, idiomatic **English** only. "
        "Write a concise recommendation in ~120–130 words, grounded in the provided context. "
        "If something is uncertain, say so briefly."
        "Only recommend from the provided context title. "
        "If the context is missing or irrelevant, say you cannot find a match."
    )

    context = f"Book title: {title}"
    if short_summary:
        context += f"\nShort summary: {short_summary}"

    user = (
        "User request:\n"
        f"{user_query}\n\n"
        "Write the recommendation (one tight paragraph, no bullets)."
    )

    return [
        {"role": "system", "content": system},
        {"role": "user", "content": context},
        {"role": "user", "content": user},
    ]
