import anthropic
import pdfplumber
import io


def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
        pages = [page.extract_text() or "" for page in pdf.pages]
    text = "\n".join(pages).strip()
    if not text:
        raise ValueError("Не удалось извлечь текст из PDF. Возможно, файл содержит только изображения.")
    return text


def analyze_resume(resume_text: str, api_key: str) -> str:
    client = anthropic.Anthropic(api_key=api_key)

    system_prompt = """You are an experienced HR expert helping small businesses in Kazakhstan evaluate candidates.
Analyze the provided resume and respond ONLY in the following structured format (use the exact headers below):

## Сильные стороны (Strengths)
- (3–5 bullet points)

## Слабые стороны / Красные флаги (Weaknesses / Red Flags)
- (2–3 bullet points)

## Оценка (Score)
X/10

## Рекомендация (Recommendation)
Hire / Maybe / Don't Hire

## Краткое резюме (Summary)
(One paragraph in Russian summarizing the candidate and the hiring recommendation)
"""

    message = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=1024,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": f"Here is the resume to analyze:\n\n{resume_text}",
            }
        ],
    )

    return message.content[0].text
