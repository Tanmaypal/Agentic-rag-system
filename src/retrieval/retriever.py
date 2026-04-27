def retrieve(query, retriever):
    return retriever.get_relevant_documents(query)
