from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

from config import *

embeddings = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL
)

db = Chroma(
    persist_directory=CHROMA_DB_PATH,
    embedding_function=embeddings
)

retriever = db.as_retriever(
    search_kwargs={"k": TOP_K}
)

llm = Ollama(
    model=LLM_MODEL
)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)


def ask(question):

    result = qa.invoke({"query": question})

    return (
        result["result"],
        result["source_documents"]
    )