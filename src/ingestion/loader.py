from langchain.document_loaders import TextLoader
def load_docs(path):
    return TextLoader(path).load()
