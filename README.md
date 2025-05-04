# 💬 LangChain + Gemini Chatbot

An interactive terminal chatbot powered by Google's Gemini 1.5 Pro and LangChain. This project allows users to have a natural conversation with an AI assistant and logs the entire session to a JSON file.

---

## 🚀 Features

- Uses **LangChain** for message handling
- Integrated with **Gemini 1.5 Pro** via `langchain-google-genai`
- Persists chat history to `chat_history.json`
- Supports multi-turn dialogue with memory
- Clean exit with `exit` or `quit`

---

## 📦 Requirements

- Python 3.8+
- A Google Gemini API Key
- Dependencies listed in `requirements.txt`

---

## 📁 Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/your-username/langchain-gemini-chatbot.git
cd langchain-gemini-chatbot

    Create a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

    Install dependencies

pip install -r requirements.txt

    Add your Gemini API Key

Create a .env file in the root directory:

cp .env.example .env

Edit .env and add:

GOOGLE_API_KEY=your_google_api_key_here

    Run the chatbot

python chatbot.py

📁 Files

    chatbot.py – Main chatbot script

    chat_history.json – Auto-generated chat logs

    .env.example – Environment variable template

    requirements.txt – Python dependencies

✍️ Example Conversation

You: Hi
AI: How can I help you today?
You: What is Python?
AI: Python is a high-level, interpreted programming language known for its readability and versatility.


🧪 .env.example

GOOGLE_API_KEY=your_google_api_key_here
