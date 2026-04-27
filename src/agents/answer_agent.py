from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI()

def answer(query, docs, graph_data=None):
    context = "\n".join([d.page_content for d in docs])
    prompt = f"Answer:\nQuery: {query}\nContext: {context}\nGraph: {graph_data}"
    return llm.predict(prompt)
