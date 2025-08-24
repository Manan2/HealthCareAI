import os

class Settings:
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    GEMINI_BASE_URL: str = os.getenv("GEMINI_BASE_URL", "https://api.gemini.google.com/v1/chat/completions")
    GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "gemini-pro")

    MILVUS_HOST: str = os.getenv("MILVUS_HOST", "localhost")
    MILVUS_PORT: str = os.getenv("MILVUS_PORT", "19530")
    MILVUS_COLLECTION: str = os.getenv("MILVUS_COLLECTION", "medical_knowledge")

settings = Settings()
