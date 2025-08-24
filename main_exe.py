import os, sys, time, tempfile, threading, requests, textwrap
import uvicorn

BACKEND_HOST = "127.0.0.1"
BACKEND_PORT = int(os.getenv("PORT", "8000"))
BACKEND_URL = f"http://{BACKEND_HOST}:{BACKEND_PORT}"

STREAMLIT_SCRIPT = textwrap.dedent("""
import streamlit as st
import requests

BACKEND = f"http://{BACKEND_HOST}:{BACKEND_PORT}/api/v1/triage"

st.set_page_config(page_title="Healthcare AI Triage", layout="centered")
st.title("🩺 AI Healthcare Triage Assistant")
st.write("Enter your symptoms below to receive a **preliminary assessment**. "
         "This is **not a medical diagnosis**—always consult a doctor.")

symptoms = st.text_area("Describe your symptoms:", height=150)

if st.button("Get Preliminary Assessment"):
    if not symptoms.strip():
        st.warning("Please enter your symptoms first.")
    else:
        with st.spinner("Processing your request..."):
            try:
                response = requests.post(BACKEND, json={"symptoms": symptoms})
                response.raise_for_status()
                data = response.json()
                st.subheader("Preliminary Assessment")
                st.write(data.get("preliminary_assessment","(no response)"))
                st.caption(data.get("disclaimer",""))
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
""")

def start_backend():
    config = uvicorn.Config("app.main:app", host=BACKEND_HOST, port=BACKEND_PORT, log_level="info")
    server = uvicorn.Server(config)
    server.run()

def wait_for_backend(timeout=20):
    start = time.time()
    while time.time() - start < timeout:
        try:
            r = requests.get(f"{BACKEND_URL}/healthz", timeout=2)
            if r.ok:
                return True
        except Exception:
            pass
        time.sleep(0.5)
    return False

def run_streamlit():
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
        f.write(STREAMLIT_SCRIPT)
        path = f.name

    from streamlit.web import bootstrap
    os.environ.setdefault("BROWSER", "default")
    os.environ.setdefault("STREAMLIT_SERVER_HEADLESS", "false")
    bootstrap.run(path, "", [], flag_options=set())

if __name__ == "__main__":
    t = threading.Thread(target=start_backend, daemon=True)
    t.start()

    if not wait_for_backend():
        print("Backend failed to start on time.", file=sys.stderr)
        sys.exit(1)

    run_streamlit()
