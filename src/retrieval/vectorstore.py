from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
def create_vectorstore(docs):
    return FAISS.from_documents(docs, OpenAIEmbeddings())
