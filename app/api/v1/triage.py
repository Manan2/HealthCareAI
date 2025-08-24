from fastapi import APIRouter
from pydantic import BaseModel
from app.services.rag_service import RAGService

router = APIRouter()
rag = RAGService()

class TriageRequest(BaseModel):
    symptoms: str

@router.post("/")
async def preliminary_diagnosis(req: TriageRequest):
    result = await rag.process_triage(req.symptoms)
    return {
        "symptoms_received": req.symptoms,
        "preliminary_assessment": result,
        "disclaimer": "This is not a medical diagnosis. Please consult a qualified healthcare provider."
    }
