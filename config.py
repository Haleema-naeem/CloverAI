# ==========================================
# Clover AI Configuration
# ==========================================

# Folder containing PDF documents
DOCUMENTS_PATH = "documents"

# Folder where ChromaDB stores vectors
CHROMA_DB_PATH = "chroma_db"

# HuggingFace embedding model
EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

# Ollama model
LLM_MODEL = "llama3.2:3b"

# Text splitting
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

# Number of chunks to retrieve
TOP_K = 3