from openai import OpenAI
from core.config import get_settings


def get_openai_client() -> OpenAI:
    settings = get_settings()
    return OpenAI(api_key=settings.openai_api_key)


def generate_recommendation(messages_or_text):
    client = get_openai_client()
    model = get_settings().model_recommend or "gpt-4.1-nano"

    if isinstance(messages_or_text, str):
        messages = [{"role": "user", "content": messages_or_text}]
    else:
        messages = messages_or_text

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()
