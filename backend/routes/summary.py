from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse
from services.summary_tool import get_summary_by_title

router = APIRouter()

@router.get("/summary")
def summary(title: str = Query(..., min_length=1)):
    full = get_summary_by_title(title)
    if not full or full.startswith("Sorry,"):
        raise HTTPException(status_code=404, detail="Summary not found for this title.")
    return JSONResponse({"title": title, "summary": full})
