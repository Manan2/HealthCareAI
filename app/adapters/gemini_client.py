import httpx
from app.core.config import settings

SAFETY_PROMPT = (
    "You are a medical triage assistant. You are NOT a doctor and your output "
    "is for informational purposes only. Always recommend consulting a qualified physician."
)

class GeminiClient:
    def __init__(self, api_key: str | None = None, base_url: str | None = None, model: str | None = None):
        self.api_key = api_key or settings.GEMINI_API_KEY
        self.base_url = base_url or settings.GEMINI_BASE_URL
        self.model = model or settings.GEMINI_MODEL

    async def generate_assessment(self, symptoms: str, retrieved_knowledge: str = "") -> str:
        context_note = f"Relevant knowledge base info: {retrieved_knowledge}" if retrieved_knowledge else ""
        user_message = f"Patient reports: {symptoms}. {context_note} Provide a brief preliminary assessment with triage level and red flags."
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": SAFETY_PROMPT},
                {"role": "user", "content": user_message}
            ],
            "max_tokens": 200,
            "temperature": 0.3
        }
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.post(self.base_url, headers=headers, json=payload)
            resp.raise_for_status()
            data = resp.json()
            return data.get("choices", [{}])[0].get("message", {}).get("content", "No response")
