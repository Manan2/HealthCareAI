# Healthcare AI — Single EXE (FastAPI + Streamlit)

This repo builds a **single Windows .exe** that launches the FastAPI backend (Gemini + Milvus ready) and a Streamlit UI.

## Quick start (build in GitHub Actions)

1. Create a new repo and push these files.
2. In GitHub, run the workflow **Build Windows One-File EXE (Backend + Streamlit)**.
3. Download the artifact `HealthcareAI_OneFile.exe`.

## Run locally (without building)

```bash
pip install -r requirements.txt
python main_exe.py
```

Then your browser should open to the Streamlit UI. The backend runs on `http://127.0.0.1:8000`.

## Configure

- Set `GEMINI_API_KEY` to enable real LLM calls.
- (Optional) Set `MILVUS_HOST` and `MILVUS_PORT` to enable Milvus retrieval; otherwise a safe stub is used.
- If your Gemini endpoint differs, set `GEMINI_BASE_URL` and `GEMINI_MODEL` env vars.

## Disclaimer

This is not a medical device. Content is informational and must not replace professional medical advice.
