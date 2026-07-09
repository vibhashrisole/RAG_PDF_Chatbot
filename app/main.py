from fastapi import FastAPI, UploadFile, File
from app.models.login_model import LoginRequest
from app.models.question_model import QuestionRequest

from app.services.rag_service import process_pdf
from app.services.embedding_service import embedding_model
from app.services.chroma_service import search_documents
from app.services.llm_service import generate_answer

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import HTMLResponse

import shutil
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "request": request
        }
    )


@app.post("/login")
def login(request: LoginRequest):
    return {
        "message": f"Welcome {request.username}"
    }


@app.post("/upload")
def upload_pdf(file: UploadFile = File(...)):

    file_path = os.path.join(
        "app",
        "uploads",
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = process_pdf(file_path)

    return {
        "message": "PDF Uploaded & Processed Successfully",
        "filename": file.filename,
        "details": result
    }

@app.post("/ask")
def ask_question(request: QuestionRequest):

    query_embedding = embedding_model.encode(
        request.question
    )

    results = search_documents(query_embedding)

    documents = results.get("documents", [])

    if not documents or not documents[0]:
        return {
            "answer": "No relevant information found in the uploaded PDF."
        }

    # ==========================
    # DEBUG: Retrieved Chunks
    # ==========================
    print("\n" + "=" * 80)
    print("QUESTION :", request.question)
    print("=" * 80)

    for i, doc in enumerate(documents[0], start=1):
        print(f"\nCHUNK {i}\n")
        print(doc)
        print("-" * 80)

    context = "\n\n".join(documents[0])

    answer = generate_answer(
        question=request.question,
        context=context
    )

    return {
        "question": request.question,
        "answer": answer
    }