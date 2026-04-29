import os
import streamlit as st
from analyzer import extract_text_from_pdf, analyze_resume

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered",
)

st.title("📄 AI Resume Analyzer")
st.caption("Мгновенный анализ резюме для малого бизнеса в Казахстане")
st.divider()

# API key input (sidebar)
with st.sidebar:
    st.header("Настройки")
    api_key = st.text_input(
        "Anthropic API Key",
        type="password",
        value=os.environ.get("ANTHROPIC_API_KEY", ""),
        help="Получите ключ на console.anthropic.com",
    )
    st.caption("Ключ не сохраняется и используется только в рамках текущей сессии.")

# Main flow
uploaded_file = st.file_uploader(
    "Загрузите резюме в формате PDF",
    type=["pdf"],
    help="Поддерживаются PDF-файлы на русском и английском языках.",
)

if uploaded_file is not None:
    st.success(f"Файл загружен: **{uploaded_file.name}**")

    if st.button("Анализировать резюме", type="primary", use_container_width=True):
        if not api_key:
            st.error("Введите Anthropic API Key в боковой панели слева.")
            st.stop()

        with st.spinner("Извлекаем текст из PDF…"):
            try:
                pdf_bytes = uploaded_file.read()
                resume_text = extract_text_from_pdf(pdf_bytes)
            except ValueError as e:
                st.error(str(e))
                st.stop()
            except Exception as e:
                st.error(f"Ошибка при чтении PDF: {e}")
                st.stop()

        with st.spinner("Отправляем резюме на анализ Claude AI…"):
            try:
                result = analyze_resume(resume_text, api_key)
            except Exception as e:
                st.error(f"Ошибка при обращении к Claude API: {e}")
                st.stop()

        st.divider()
        st.subheader("Результаты анализа")
        st.markdown(result)

        st.divider()
        if st.button("Анализировать другое резюме", use_container_width=True):
            st.rerun()
