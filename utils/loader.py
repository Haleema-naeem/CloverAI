from langchain_community.document_loaders import PyPDFDirectoryLoader

from config import DOCUMENTS_PATH


def load_documents():
    loader = PyPDFDirectoryLoader(DOCUMENTS_PATH)

    documents = loader.load()

    return documents