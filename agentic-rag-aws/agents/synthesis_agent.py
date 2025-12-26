from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage


def synthesis_agent(docs, question):
    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
Answer the question strictly using the context below.
If the answer is not present, say "Information not available in the document."

Context:
{context}

Question:
{question}
"""

    llm = ChatOpenAI(temperature=0)
    response = llm([HumanMessage(content=prompt)])
    return response.content
