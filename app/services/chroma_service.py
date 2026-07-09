"""
chroma_service.py

This module handles all ChromaDB operations.

Functions:
1. Create Collection
2. Store Embeddings
3. Search Similar Chunks
4. Clear Collection
5. Count Documents
"""

import chromadb

# Collection Name
COLLECTION_NAME = "pdf_collection"

# Create ChromaDB Client
chroma_client = chromadb.Client()

# Create Collection
collection = chroma_client.get_or_create_collection(
    name=COLLECTION_NAME
)


# ---------------------------------
# Store Document
# ---------------------------------
def store_document(chunk, embedding, chunk_id):

    global collection

    collection.add(
        documents=[chunk],
        embeddings=[embedding.tolist()],
        ids=[chunk_id]
    )


# ---------------------------------
# Search Similar Documents
# ---------------------------------
def search_documents(query_embedding, n_results=5):

    global collection

    return collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=n_results
    )


# ---------------------------------
# Clear Collection
# ---------------------------------
def clear_collection():

    global collection

    try:
        chroma_client.delete_collection(
            name=COLLECTION_NAME
        )
    except Exception:
        pass

    collection = chroma_client.get_or_create_collection(
        name=COLLECTION_NAME
    )


# ---------------------------------
# Count Stored Documents
# ---------------------------------
def document_count():

    global collection

    return collection.count()