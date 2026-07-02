# 🤖 Day 1 – AI Chatbot with Memory

> **30 Days of AI Projects** | Day 1 of 30

A simple command-line and web chatbot that **remembers past conversations** across sessions using a local JSON file — powered by **Groq (Free)**.

---

## ✨ Features

- 💬 Chat with an AI powered by **Llama 3.1** via Groq (100% free)
- 🧠 Persistent memory — conversations saved to `memory/chat_history.json`
- 🖥️ Two interfaces: CLI and Streamlit web app
- 🧹 Commands to view history or wipe memory
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
│   └── test_chatbot.py
├── .env.example
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

### 4. Get a FREE Groq API key
👉 Go to **https://console.groq.com** → Sign up (no credit card needed) → API Keys → Create key

### 5. Set up your `.env` file
```bash
cp .env.example .env
```
Open `.env` and add your key:
```
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxx
```

---

## 🖥️ Run the CLI Chatbot

```bash
python app/chatbot.py
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

Every message is saved to `memory/chat_history.json`:

```json
[
  { "role": "user", "content": "What is Python?" },
  { "role": "assistant", "content": "Python is a high-level programming language..." }
]
```

On the next session, this history is reloaded and sent to the model so it remembers your past conversation. Only the last 20 messages are sent to stay within token limits.

---

## ⚙️ Model Used

| Provider | Model | Cost |
|----------|-------|------|
| [Groq](https://console.groq.com) | `llama-3.1-8b-instant` | ✅ Free (14,400 req/day) |

---

## 🐛 Common Errors & Fixes

| Error | Fix |
|-------|-----|
| `Missing credentials` | Make sure `.env` file exists with your `GROQ_API_KEY` |
| `model_decommissioned` | Use `llama-3.1-8b-instant` (not `llama3-8b-8192`) |
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |

---

## 💡 What I Learned

- How LLM chat completion APIs work (messages array with roles)
- How to maintain conversation context across turns
- How to persist data locally with JSON
- How to build a simple web UI with Streamlit
- How to use environment variables safely with `python-dotenv`

---

## 🔗 Part of the 30 Days of AI Projects Series

| Day | Project | Difficulty |
|-----|---------|------------|
| **1** | **AI Chatbot with Memory** ← you are here | 🟢 Beginner |
| 2 | PDF Q&A with RAG | 🟡 Intermediate |
| 3 | Real-time Object Counter | 🟢 Beginner |
| 4 | Sentiment Dashboard | 🟢 Beginner |
| 5 | AI Cover Letter Generator | 🟢 Beginner |

---

## 📄 License

MIT License — free to use, modify, and build on!
