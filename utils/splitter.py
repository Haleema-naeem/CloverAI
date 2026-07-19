from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import CHUNK_SIZE
from config import CHUNK_OVERLAP


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=CHUNK_SIZE,

        chunk_overlap=CHUNK_OVERLAP

    )

    chunks = splitter.split_documents(documents)

    return chunks