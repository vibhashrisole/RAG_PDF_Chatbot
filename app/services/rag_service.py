from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.services.embedding_service import embedding_model
from app.services.chroma_service import (
    store_document,
    clear_collection,
    document_count
)

# Text Splitter Configuration
CHUNK_SIZE = 700
CHUNK_OVERLAP = 150


def process_pdf(pdf_path):

    try:
        # Read PDF
        reader = PdfReader(pdf_path)

        total_pages = len(reader.pages)

        # Extract text from all pages
        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        # Check if PDF contains text
        if not text.strip():
            return {
                "message": "No readable text found in the uploaded PDF."
            }

        # Split text into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )

        chunks = text_splitter.split_text(text)

        # Clear previous vectors
        clear_collection()

        embedding = None

        # Generate embeddings and store in ChromaDB
        for i, chunk in enumerate(chunks):

            embedding = embedding_model.encode(chunk)

            store_document(
                chunk=chunk,
                embedding=embedding,
                chunk_id=f"chunk_{i}"
            )

        return {
            "total_pages": total_pages,
            "total_chunks": len(chunks),
            "embedding_dimension": len(embedding),
            "documents_in_chromadb": document_count(),
            "first_10_values": embedding[:10].tolist()
        }

    except Exception as e:

        return {
            "message": f"Error while processing PDF: {str(e)}"
        }