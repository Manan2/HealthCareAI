from app.adapters.gemini_client import GeminiClient
from app.adapters.milvus_client import MilvusClient

class RAGService:
    def __init__(self):
        self.gemini = GeminiClient()
        self.milvus = MilvusClient()

    async def process_triage(self, symptoms: str) -> str:
        retrieved_info = " ".join(self.milvus.retrieve_context(symptoms))
        return await self.gemini.generate_assessment(symptoms, retrieved_info)
