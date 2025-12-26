def retriever_agent(vectorstore, query):
    return vectorstore.similarity_search(query, k=4)
