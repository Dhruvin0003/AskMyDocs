
# 📚 AskMyDocs – AI-Powered PDF Q&A App

AskMyDocs is a Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask context-aware questions based on their contents. It uses LangChain, Cohere’s command-r-plus LLM, and FAISS for semantic search.

---

## 🚀 Features

- Upload and query multiple PDFs
- Uses sentence-transformers for embedding PDF content
- Answers generated using Cohere’s `command-r-plus` model
- Smart fallback agent using Google Search if answer isn't found in PDFs
- Built with Streamlit for interactive UI
- Docker-ready and deployable on AWS EC2 or local machine

---

## 🛠 Folder Setup

Before running the app, ensure the following folders exist in your project root:

AskMyDocs/
│
├── data/          # Required: Stores uploaded PDFs
├── models/        # Required: Stores locally downloaded embedding model

Create them using:

mkdir data models

---

## 📦 Installation

### 1. Clone the Repository

git clone https://github.com/Dhruvin0003/AskMyDocs.git
cd AskMyDocs

### 2. Install Python Dependencies

pip install -r requirements.txt

---

## 🤖 Model Download

This app uses the sentence-transformers/all-MiniLM-L6-v2 embedding model.

Download it locally using this script:

✏️ Create a script: download_model.py

from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="sentence-transformers/all-MiniLM-L6-v2",
    local_dir="models/minilm"
)

Then run:

pip install huggingface-hub
python download_model.py

✅ This will download the model into models/minilm/, where your app expects it.

---

## 🔐 Environment Variables

Create a `.env` file in the project root with the following content:

CO_API_KEY=your-cohere-api-key
GOOGLE_CSE_ID=your-google-cse-id
GOOGLE_API_KEY=your-google-api-key

> Replace the placeholders with your actual API keys for Cohere and Google Search API.

---

## ▶️ Running the App

After setting up everything, run:

streamlit run app.py

Open your browser to:  
📎 http://localhost:8501

---

## 🐳 Docker Usage (Optional)

If you'd like to run it via Docker:

docker build -t askmydocs .
docker run -p 8501:8501 askmydocs

---

## 🧠 Tech Stack

- Python
- Streamlit
- LangChain
- FAISS
- Cohere LLMs (langchain-cohere)
- HuggingFace Transformers
- Google Search API
- Docker (optional)
- AWS EC2 (for deployment)

---

## 💡 Future Improvements

- Support for multiple LLM providers
- UI enhancements
- Context-aware follow-up questions
- Streamlit Cloud or serverless deployment

---

## 👤 Author

**Dhruvin Dedakiya**  
Generative AI Engineer | NLP + RAG Systems Developer  
🔗 https://www.linkedin.com/in/dhruvin-dedakiya-4b834a251


