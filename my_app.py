
import openai
import streamlit as st
# st.set_page_config(
#     page_title="大学智能助手",
#     page_icon="👻",
#     layout="centered",
#     initial_sidebar_state="collapsed",
# )
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"


st.header('基于LLM&机器学习的大学生Ai智能助手系统', divider='rainbow')
st.title(':blue[大学智能助手] 📝')
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "提出你在大学中遇到的任何问题..."}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    openai.api_key = openai_api_key
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)
