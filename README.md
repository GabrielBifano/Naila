# 🗨️ Naila - Simple Chatbot Flask API with RAG

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

## 🔧 Quick Setup & Running

### API keys setup

You will need two API keys for this project: **Groq** and **Huggingface** both free and easy to setup.
There are two scripts in the project: **run.sh** and **run.ps1**, for Linux and Windows respectively. Open the disered one for your case in a code editor (we recommend using the Linux .sh). You will find the following commented lines:
```
# # Uncomment the code below if you do not have your
# # API keys as environment variables in your system:

# echo "Setting API key variables"
# export HF_API_KEY="your_huggingface_key"
# export GROQ_API_KEY="your_groq_key"
```
To run the server it is necessary to export your API keys for **Groq** and **Huggingface** as environment variables. For that, uncomment the code above and substitute your keys, for example:
```
echo "Setting API key variables"
export HF_API_KEY="hf_abcdefghijklmnopq..."
export GROQ_API_KEY="gsk_abcdefghijklmnopq..."
```

### 🐧 Linux / macOS
**Recommended.** Run the provided bash script:
```bash
chmod +x run.sh
source ./run.sh
```

### 🪟 Windows (PowerShell)
**Not recommended.** You may find version incompatibilities.
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
. .\run.ps1
```

### 🌍 Running the Server without script

If the scripts provided before are not working, or you prefer doing it by hand, use the following steps to setup and run the project:

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