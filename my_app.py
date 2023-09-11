import openai
import streamlit as st

# 在环境变量中设置您的 OpenAI API 密钥，避免硬编码
# export OPENAI_API_KEY="YOUR_API_KEY"
openai_api_key = st.secrets["openai_api_key"] if "openai_api_key" in st.secrets else ""

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", type="password", value=openai_api_key)

st.set_page_config(
    page_title="大学智能助手",
    page_icon="👻",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.title("💬大学智能助手")
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
    else:
        openai.api_key = openai_api_key
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
        msg = response.choices[0].message
        st.session_state.messages.append(msg)
        st.chat_message("assistant").write(msg["content"])
