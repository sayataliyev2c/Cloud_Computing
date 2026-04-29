# AI Resume Analyzer

AI-powered resume evaluation tool for small businesses in Kazakhstan.  
Upload a PDF resume and get instant structured feedback from Claude AI in Russian and English.

---

## Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Set your Anthropic API key

**Option A — environment variable (recommended):**
```bash
export ANTHROPIC_API_KEY=sk-ant-...
```

**Option B — enter it directly in the app sidebar** after launching.

### 3. Run the app

```bash
streamlit run app.py
```

The app opens automatically at `http://localhost:8501`.

---

## How to use

1. Open the app in your browser.
2. Paste your API key in the left sidebar (if not set via environment variable).
3. Click **"Загрузите резюме"** and select a PDF file.
4. Click **"Анализировать резюме"**.
5. Read the structured analysis:
   - Strengths (3–5 points)
   - Weaknesses / Red Flags (2–3 points)
   - Score (1–10)
   - Hire / Maybe / Don't Hire recommendation
   - Summary paragraph in Russian
6. Click **"Анализировать другое резюме"** to start over.

---

## Environment Variables

| Variable | Required | Description |
|---|---|---|
| `ANTHROPIC_API_KEY` | Yes | Your Anthropic API key from console.anthropic.com |

---

## File Structure

```
resume-analyzer/
├── app.py           # Streamlit UI — handles file upload and displays results
├── analyzer.py      # PDF parsing and Claude API integration
├── requirements.txt # Python dependencies
└── README.md        # This file
```
