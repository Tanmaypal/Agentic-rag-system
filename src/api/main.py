from fastapi import FastAPI
from src.ingestion.loader import load_docs
from src.ingestion.splitter import split_docs
from src.retrieval.vectorstore import create_vectorstore
from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI

app = FastAPI()

docs = split_docs(load_docs("data/sample.txt"))
vs = create_vectorstore(docs)
retriever = vs.as_retriever()

def search(q):
    docs = retriever.get_relevant_documents(q)
    return "\n".join([d.page_content for d in docs])

agent = initialize_agent(
    [Tool(name="Search", func=search, description="search docs")],
    ChatOpenAI(),
    agent="zero-shot-react-description"
)

@app.get("/ask")
def ask(query: str):
    return {"answer": agent.run(query)}
