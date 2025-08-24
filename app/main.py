from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.triage import router as triage_router

app = FastAPI(title="Healthcare AI (Gemini + Milvus)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(triage_router, prefix="/api/v1/triage", tags=["Triage"])

@app.get("/healthz")
def healthz():
    return {"status": "ok"}
