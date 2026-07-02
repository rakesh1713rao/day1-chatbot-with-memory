# 🤖 Day 1 – AI Chatbot with Memory

> **30 Days of AI Projects** | Day 1 of 30

A simple command-line and web chatbot that **remembers past conversations** across sessions using a local JSON file.

---

## ✨ Features

- 💬 Chat with an AI powered by GPT-3.5-turbo
- 🧠 Persistent memory — conversations saved to `memory/chat_history.json`
- 🖥️ Two interfaces: CLI and Streamlit web app
- 🧹 Commands to view history or clear memory
- ✅ Unit tests included

---

## 📁 Project Structure

```
day1-chatbot-with-memory/
├── app/
│   ├── chatbot.py          # CLI chatbot
│   └── streamlit_app.py    # Web UI
├── memory/                 # Auto-created — stores chat history
│   └── chat_history.json
├── tests/
│   └── test_chatbot.py     # Unit tests
├── .env.example            # Environment variable template
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/day1-chatbot-with-memory.git
cd day1-chatbot-with-memory
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your API key
```bash
cp .env.example .env
# Open .env and paste your OpenAI API key
```

Get a free API key at: https://platform.openai.com/api-keys

---

## 🖥️ Run the CLI Chatbot

```bash
cd app
python chatbot.py
```

**Commands inside the chat:**
| Command | Action |
|---------|--------|
| `quit` | Exit the chatbot |
| `clear` | Wipe all memory |
| `history` | Print full chat history |

---

## 🌐 Run the Web App

```bash
streamlit run app/streamlit_app.py
```

Opens at `http://localhost:8501`

---

## 🧪 Run Tests

```bash
pytest tests/ -v
```

---

## 🧠 How Memory Works

Every message (user + assistant) is saved to `memory/chat_history.json`:

```json
[
  { "role": "user", "content": "What is Python?" },
  { "role": "assistant", "content": "Python is a high-level programming language..." }
]
```

On the next session, this history is loaded and sent to the model so it remembers the context. Only the last 20 messages are sent to stay within the token limit.

---

## 💡 What I Learned

- How OpenAI's chat completion API works
- How to maintain conversation context with a message history list
- How to persist data locally with JSON
- How to build a simple web UI with Streamlit

---

## 🔗 Part of the 30 Days of AI Projects Series

| Day | Project | Difficulty |
|-----|---------|------------|
| **1** | **AI Chatbot with Memory** ← you are here | 🟢 Beginner |
| 2 | PDF Q&A with RAG | 🟡 Intermediate |
| 3 | Real-time Object Counter | 🟢 Beginner |
| ... | ... | ... |

---

## 📄 License

MIT License — feel free to use and build on this!
