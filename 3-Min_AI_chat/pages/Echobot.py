import time
import streamlit as st

st.set_page_config("Чат с ИИ", layout='wide')

st.title("Чат с ИИ")

def stream_text(text: str):
    for char in text:
        yield char
        time.sleep(0.03)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

messages = st.container(height=600)

for msg in st.session_state.chat_history:
    messages.chat_message(msg["role"]).write(msg["content"])


req = st.chat_input("Скажите что-нибудь?")

if req:
    user_msg = {
        "role": "user",
        "content": req,
    }
    st.session_state.chat_history.append(user_msg)
    messages.chat_message("user").write(req)

    assistant_text = f"сам {req}!"

    with messages.chat_message("assistant"):
        streamed_text = st.write_stream(stream_text(assistant_text))

    assistant_msg = {
        "role": "assistant",
        "content": streamed_text,
    }
    st.session_state.chat_history.append(assistant_msg)