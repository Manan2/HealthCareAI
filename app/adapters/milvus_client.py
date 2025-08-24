from typing import List
from app.core.config import settings

def _pm():
    from pymilvus import connections, Collection
    return connections, Collection

class MilvusClient:
    def __init__(self):
        self._ready = False
        self._collection = None

    def _ensure(self):
        if self._ready:
            return
        if not settings.MILVUS_HOST:
            # No Milvus configured; remain not ready
            return
        connections, Collection = _pm()
        connections.connect(alias="default", host=settings.MILVUS_HOST, port=settings.MILVUS_PORT)
        self._collection = Collection(settings.MILVUS_COLLECTION)  # Assumes collection already exists
        self._ready = True

    def retrieve_context(self, query_text: str, limit: int = 3) -> List[str]:
        # Placeholder retrieval: if Milvus isn't configured, returns canned hints.
        # In production: embed query -> similarity search -> fetch documents.
        self._ensure()
        if not self._ready:
            return [
                "If experiencing severe chest pain, shortness of breath, or fainting, seek emergency care.",
                "Fever with stiff neck, confusion, or severe headache warrants urgent evaluation."
            ]
        # TODO: real embedding & search
        return [
            "Chest pain may be cardiac or non-cardiac; assess risk factors and red flags.",
            "Shortness of breath can indicate cardiopulmonary issues; consider severity and onset."
        ]
