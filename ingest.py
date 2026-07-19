from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from config import *

loader = PyPDFDirectoryLoader(DOCUMENTS_PATH)
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP
)

chunks = splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL
)

db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=CHROMA_DB_PATH
)

print("Database created successfully!")