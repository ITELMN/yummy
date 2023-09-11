import streamlit as st
import openai

st.set_page_config(
    page_title="大学智能助手",
    page_icon="👻",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Set your OpenAI API key here


with st.sidebar:
    uploaded_file = st.file_uploader("Upload an article", type=("txt", "md"))
    openai.api_key = st.text_input("open API Key", key="file_qa_api_key", type="password")
st.header('基于LLM&机器学习的大学生Ai智能助手系统', divider='rainbow')
st.header(':blue[大学智能助手] 📝')

question = st.text_input(
    "提出你在大学中遇到的任何问题",
    placeholder="中南大学国际贸易专业的就业方向怎么样？",
    disabled=not uploaded_file,
)

if uploaded_file and question:
    article = uploaded_file.read().decode()
    prompt = f"Here's an article:\n\n{article}\n\n{question}"

    response = openai.Completion.create(
        engine="davinci",  # Use "davinci" for GPT-3, or other engines as needed
        prompt=prompt,
        max_tokens=100,  # Adjust the max tokens as needed
    )
    st.write("### Answer")
    st.write(response.choices[0].text)

