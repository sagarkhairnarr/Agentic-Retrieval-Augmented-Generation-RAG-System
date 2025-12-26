from dotenv import load_dotenv
load_dotenv()

from ingestion.load_pdf import load_pdf
from ingestion.chunking import chunk_documents
from ingestion.embed_index import create_vectorstore
from graph.rag_graph import run_rag
import sys


def main():
    print("🔄 Loading PDF documents...")
    documents = load_pdf("data")

    print("✂️ Chunking documents...")
    chunks = chunk_documents(documents)

    print("🧠 Creating vector index...")
    vectorstore = create_vectorstore(chunks)

    print("\n✅ Agentic RAG Ready!")
    print("Ask questions (type 'exit' to quit)\n")

    while True:
        query = input("Ask a question: ")
        if query.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            sys.exit()

        answer = run_rag(vectorstore, query)
        print("\n📌 Answer:")
        print(answer)
        print("-" * 50)


if __name__ == "__main__":
    main()
