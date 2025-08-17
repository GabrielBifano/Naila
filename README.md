# 🗨️ Simple Chatbot Flask API with RAG

This project is a **Flask-based chatbot API** that integrates **RAG (Retrieval-Augmented Generation)** with **CrewAI** and **Groq’s LLaMA-3.1-8B-Instant** model.  
It allows you to ask questions via a simple chat interface, and the backend uses both a local knowledge base and a language model to generate answers.

---

## 🚀 Features
- Flask web server with **Socket.IO** for real-time chat.
- Retrieval-Augmented Generation (RAG) using:
  - Knowledge from local .txt scrape file
  - Website data (`https://www.signa.pt/`)
- LLM inference via **Groq API**.
- Cross-platform setup scripts:
  - **Linux/macOS:** `run.sh`
  - **Windows (PowerShell):** `run.ps1`

---

## 📦 What you will need
- Python **3.12+**
- Dependencies listed in `requirements.txt`
- API keys:
  - **Hugging Face API Key** (if using Hugging Face models)
  - **Groq API Key** (for LLaMA-3.1-8B-Instant)

---

## 🔧 Installation & Setup

### 🐧 Linux / macOS
Run the provided bash script:
```bash
chmod +x run.sh
source ./run.sh
```

### 🪟 Windows (PowerShell)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
. .\setup.ps1
```

### 🌍 Running the Server without script

Create a virtual environment (.nailavenv) if it doesn’t exist:
```
python3 -m venv .nailavenv
```

Activate the environment:
```
source .nailavenv/bin/activate
```

Install dependencies with requirements:
```
pip install -r requirements.txt
```

Or, if for some ungodly reason, the line above doesn't work:
```
pip install flask flask-socketio langchain langchain-community langchain-huggingface langchain-groq crewai sentence-transformers faiss-cpu beautifulsoup4
```

Run the app with (make sure .nailavenv is active):
```
python3 app.py
```