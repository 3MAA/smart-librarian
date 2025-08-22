from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.ask import router as ask_router
from routes.summary import router as summary_router
from routes.route_tts import router as tts_router

app = FastAPI(title="Smart Librarian")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ask_router)
app.include_router(summary_router)
app.include_router(tts_router)

@app.get("/health")
def health():
    return {"status": "ok"}
