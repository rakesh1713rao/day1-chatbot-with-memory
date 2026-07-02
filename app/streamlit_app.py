import json
import os
import streamlit as st
from openai import OpenAI

MEMORY_FILE = "memory/chat_history.json"

st.set_page_config(page_title="AI Chatbot with Memory", page_icon="🤖")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def load_memory() -> list:
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return []


def save_memory(history: list):
    os.makedirs("memory", exist_ok=True)
    with open(MEMORY_FILE, "w") as f:
        json.dump(history, f, indent=2)


def get_reply(history: list) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant with memory of past conversations."},
            *history[-20:],
        ]
    )
    return response.choices[0].message.content


# --- UI ---
st.title("🤖 AI Chatbot with Memory")
st.caption("Your conversations are saved and remembered across sessions.")

if "messages" not in st.session_state:
    st.session_state.messages = load_memory()

# Sidebar
with st.sidebar:
    st.header("Controls")
    if st.button("🧹 Clear Memory"):
        st.session_state.messages = []
        save_memory([])
        st.success("Memory cleared!")
    st.markdown(f"**Messages stored:** {len(st.session_state.messages)}")
    st.info("Chat history is saved in `memory/chat_history.json`")

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input
if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            reply = get_reply(st.session_state.messages)
        st.write(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    save_memory(st.session_state.messages)
