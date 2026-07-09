# AI PDF Chatbot

An AI-powered chatbot that answers questions from PDF documents using Retrieval-Augmented Generation (RAG).

The idea behind this project was to understand how Large Language Models can answer questions from private documents instead of relying only on their pre-trained knowledge. The application processes uploaded PDF files, converts the content into embeddings, stores them in a vector database, and retrieves the most relevant information to generate accurate responses.

---

## Why I Built This Project

While learning Generative AI and RAG, I wanted to build a complete end-to-end application instead of only understanding the theory.

Through this project I learned:

- How RAG works
- How embeddings are generated
- How vector databases store document knowledge
- How semantic search retrieves relevant information
- How an LLM generates answers using retrieved context
- How to build REST APIs using FastAPI
- How to containerize an AI application using Docker

---

## Features

- Upload PDF documents
- Extract text from PDFs
- Automatic text chunking
- Generate embeddings using Hugging Face
- Store embeddings in ChromaDB
- Semantic similarity search
- AI-powered question answering using Ollama
- FastAPI REST APIs
- Simple web interface
- Docker support

---

## Tech Stack

**Backend**

- Python
- FastAPI

**Generative AI**

- LangChain
- Ollama
- Hugging Face Embeddings

**Vector Database**

- ChromaDB

**PDF Processing**

- PyPDF2

**Frontend**

- HTML
- CSS
- JavaScript

**Deployment**

- Docker
- Docker Compose

---

## Project Structure

RAG_PDF_CHATBOT
│
├── app
│   ├── models
│   ├── routes
│   ├── services
│   ├── static
│   ├── templates
│   └── uploads
│
├── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
└── .gitignore


---

## Project Workflow


PDF Upload
     │
     ▼
Extract Text
     │
     ▼
Text Chunking
     │
     ▼
Generate Embeddings
     │
     ▼
Store in ChromaDB
     │
     ▼
User Question
     │
     ▼
Similarity Search
     │
     ▼
Relevant Chunks
     │
     ▼
Ollama LLM
     │
     ▼
Final Answer


---

## Installation

Clone the repository

cmd
git clone https://github.com/your-username/AI-PDF-Chatbot.git


Move into the project directory

cmd
cd AI-PDF-Chatbot


Create a virtual environment

cmd
python -m venv chatenv


Activate it

Windows

cmd
chatenv\Scripts\activate


Install dependencies

cmd
pip install -r requirements.txt


Run the application

cmd
uvicorn main:app --reload


Open

http://127.0.0.1:8000


Swagger API

http://127.0.0.1:8000/docs


---

## What I Learned

This project helped me gain practical experience in:

- Retrieval-Augmented Generation (RAG)
- Embedding models
- Vector databases
- Semantic search
- Prompt-based question answering
- FastAPI backend development
- Docker basics
- Building AI applications end-to-end

---

## Future Improvements

- Support multiple PDF documents
- Chat history
- User authentication
- OpenAI API integration
- Source citation for responses
- Streaming responses

---

## Author

**Vibhashri Sole**
Data Science | Machine Learning | Generative AI
