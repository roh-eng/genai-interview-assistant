# InterviewGPT 🎯

> AI Interview Coach using RAG + Groq

[![Live App](https://img.shields.io/badge/🚀_Live_App-Open-FF4B4B?style=for-the-badge)](https://genai-interview-assistant-q54rm98e9fqkmxregpvlmh.streamlit.app/)
[![Streamlit](https://img.shields.io/badge/Built_with-Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![Groq](https://img.shields.io/badge/LLM-Groq-F55036?style=flat)](https://groq.com)

InterviewGPT is a Streamlit web app that helps candidates practice technical interviews. Upload your resume and a question bank PDF, and the app extracts your skills, generates interview questions from the document using **Retrieval-Augmented Generation (RAG)**, and evaluates your answers with detailed, scored feedback powered by a **Groq**-hosted LLM.

**🔗 Live demo:** https://genai-interview-assistant-q54rm98e9fqkmxregpvlmh.streamlit.app/

---

## Features

- **📄 Resume parsing** — extracts text from an uploaded resume PDF.
- **🧠 Skill detection** — scans the resume for in-demand technical skills (Python, SQL, ML, DL, NLP, LangChain, RAG, etc.).
- **❓ RAG question generation** — embeds an interview-questions PDF into a Chroma vector store and pulls relevant questions from it.
- **📝 AI answer evaluation** — grades your answer with technical & communication scores, strengths, weaknesses, missing concepts, an improved answer, and a final recommendation.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| UI | [Streamlit](https://streamlit.io) |
| LLM | [Groq](https://groq.com) — `llama-3.3-70b-versatile` |
| RAG / Orchestration | [LangChain](https://www.langchain.com) |
| Vector store | [Chroma](https://www.trychroma.com) |
| Embeddings | `sentence-transformers/all-MiniLM-L6-v2` (HuggingFace) |
| PDF parsing | `pdfplumber`, `pypdf` |

---

## Project Structure

```
genai_prompt/
├── app.py               # Streamlit UI — ties everything together
├── resume_parser.py     # Extracts text from a resume PDF (pdfplumber)
├── skill_extractor.py   # Keyword-based skill detection
├── rag.py               # Builds Chroma vector store + generates questions
├── evaluator.py         # Calls Groq LLM to evaluate answers
├── requirements.txt     # Python dependencies
└── .gitignore
```

---

## Getting Started (Local)

### 1. Prerequisites
- Python 3.9+
- A free Groq API key from [console.groq.com](https://console.groq.com)

### 2. Clone & install
```bash
git clone https://github.com/roh-eng/genai-interview-assistant.git
cd genai-interview-assistant
python -m venv envii
# Windows (PowerShell):
envii\Scripts\Activate.ps1
# macOS/Linux:
# source envii/bin/activate
pip install -r requirements.txt
```

### 3. Set your Groq API key
The app reads the key from the `GROQ_API_KEY` environment variable.

**PowerShell:**
```powershell
$env:GROQ_API_KEY = "gsk_your_actual_key_here"
```

**bash:**
```bash
export GROQ_API_KEY="gsk_your_actual_key_here"
```

> 💡 You can also create `.streamlit/secrets.toml` with `GROQ_API_KEY = "gsk_..."`. This file is gitignored so your key is never committed.

### 4. Run
```bash
streamlit run app.py
```
The app opens at http://localhost:8501.

---

## Usage

1. **Upload your resume PDF** → see a preview and your detected skills.
2. **Upload an interview-questions PDF** → click **Generate Interview Question**.
3. **Type your answer** → click **Evaluate Answer** to get scored AI feedback.

---

## Deployment (Streamlit Community Cloud)

This app is deployed on Streamlit Community Cloud:

1. Push the repo to GitHub (dependencies **must** be in a file named `requirements.txt`).
2. Create the app at [share.streamlit.io](https://share.streamlit.io), pointing to `app.py` on the `main` branch.
3. In **Settings → Secrets**, add your key in TOML format:
   ```toml
   GROQ_API_KEY = "gsk_your_actual_key_here"
   ```
4. Save — Streamlit injects secrets as environment variables, so `os.environ.get("GROQ_API_KEY")` picks it up automatically.

---

## Security Notes

- **Never commit your API key.** `.env`, `*.env`, and `secrets.toml` are gitignored.
- If a key is ever exposed, rotate it immediately at [console.groq.com](https://console.groq.com).

---

## License

This project is provided for educational and portfolio purposes.
