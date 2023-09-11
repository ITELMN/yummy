
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

# 修改生成的回复内容，使其看起来像一个大学生的回应
    msg["content"] = "嘿，没问题！我认为你的问题是这样的：[用户问题]。在大学里，我们通常这样解决它：[建议或解决方法]。还有其他什么我可以帮助你的吗？"

# 添加修改后的回复到对话历史
    st.session_state.messages.append({"role": "assistant", "content": msg["content"]})
    st.chat_message("assistant").write(msg["content"])
    # response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    # msg = response.choices[0].message
    # st.session_state.messages.append(msg)
    # st.chat_message("assistant").write(msg.content)
