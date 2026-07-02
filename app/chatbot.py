import json
import os
from datetime import datetime
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

MEMORY_FILE = "memory/chat_history.json"

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def load_memory() -> list:
    """Load chat history from JSON file."""
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return []


def save_memory(history: list):
    """Save chat history to JSON file."""
    os.makedirs("memory", exist_ok=True)
    with open(MEMORY_FILE, "w") as f:
        json.dump(history, f, indent=2)


def chat(user_message: str, history: list) -> str:
    """Send a message and get a reply, maintaining conversation history."""
    history.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a helpful assistant with memory of past conversations."},
            *history[-20:],  # Keep last 20 messages to avoid token limit
        ]
    )

    reply = response.choices[0].message.content
    history.append({"role": "assistant", "content": reply})
    save_memory(history)
    return reply


def clear_memory():
    """Clear all conversation history."""
    if os.path.exists(MEMORY_FILE):
        os.remove(MEMORY_FILE)
    print("🧹 Memory cleared!")


def main():
    print("🤖 AI Chatbot with Memory")
    print("=" * 40)
    print("Commands: 'quit' to exit | 'clear' to reset memory | 'history' to see past chats\n")

    history = load_memory()

    if history:
        print(f"📂 Loaded {len(history) // 2} previous message(s) from memory.\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue
        elif user_input.lower() == "quit":
            print("👋 Goodbye! Your chat history is saved.")
            break
        elif user_input.lower() == "clear":
            clear_memory()
            history = []
        elif user_input.lower() == "history":
            if not history:
                print("📭 No history yet.\n")
            else:
                print("\n--- Chat History ---")
                for msg in history:
                    role = "You" if msg["role"] == "user" else "Bot"
                    print(f"{role}: {msg['content']}")
                print("-------------------\n")
        else:
            print("Bot: ", end="", flush=True)
            reply = chat(user_input, history)
            print(reply + "\n")


if __name__ == "__main__":
    main()
