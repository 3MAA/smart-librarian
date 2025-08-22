from fastapi import APIRouter, Query
from fastapi.responses import StreamingResponse
from services.service_tts import synthesize_tts_bytes
import io

router = APIRouter()

@router.get("/tts")
def tts(
    text: str = Query(..., min_length=2),
    filename: str = Query("speech.mp3"),
    download: bool = Query(False),
):
    audio_bytes = synthesize_tts_bytes(text, "mp3")
    disp = "attachment" if download else "inline"
    headers = {"Content-Disposition": f'{disp}; filename="{filename}"'}
    return StreamingResponse(io.BytesIO(audio_bytes), media_type="audio/mpeg", headers=headers)
