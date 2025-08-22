from gtts import gTTS
import io

def synthesize_tts_bytes(text: str, fmt: str = "mp3") -> bytes:
    buf = io.BytesIO()
    gTTS(text, lang="en").write_to_fp(buf)
    buf.seek(0)
    return buf.read()
