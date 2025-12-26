from agents.planner_agent import planner_agent
from agents.retriever_agent import retriever_agent
from agents.synthesis_agent import synthesis_agent


def run_rag(vectorstore, question):
    plan = planner_agent(question)
    docs = retriever_agent(vectorstore, plan["query"])
    answer = synthesis_agent(docs, question)
    return answer
