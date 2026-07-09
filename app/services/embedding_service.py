from sentence_transformers import SentenceTransformer

# Embedding Model Name
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

# Load Embedding Model
embedding_model = SentenceTransformer(MODEL_NAME)