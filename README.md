# 🍀 Clover AI

Clover AI is a beginner-friendly Retrieval-Augmented Generation (RAG) chatbot built using Python. It allows users to ask questions about PDF documents, retrieves the most relevant information using ChromaDB, and generates answers locally using Ollama and Llama 3.2.

## Features

- 📄 PDF document question answering
- 🔍 Retrieval-Augmented Generation (RAG)
- 🤖 Local LLM with Ollama (Llama 3.2)
- 🧠 HuggingFace embeddings
- 💬 Streamlit chat interface
- 📚 ChromaDB vector database

## Tech Stack

- Python
- Streamlit
- LangChain
- ChromaDB
- Ollama
- Llama 3.2
- HuggingFace Embeddings

## Installation

```bash
pip install -r requirements.txt
```

Run the indexing script:

```bash
python ingest.py
```

Start the application:

```bash
streamlit run app.py
```

## Project Structure

```
Clover-AI/
│
├── app.py
├── rag.py
├── ingest.py
├── config.py
├── requirements.txt
├── README.md
├── styles/
├── components/
├── documents/
└── chroma_db/
```

## How It Works

1. PDFs are loaded from the `documents` folder.
2. Text is split into chunks.
3. Chunks are converted into embeddings.
4. Embeddings are stored in ChromaDB.
5. The most relevant chunks are retrieved for each question.
6. Llama 3.2 generates an answer using only the retrieved context.