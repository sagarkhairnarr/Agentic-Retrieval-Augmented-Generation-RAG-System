# 📚 Agentic Retrieval-Augmented Generation (RAG) System — AWS Guidance

This project implements an **Agentic RAG (Retrieval Augmented Generation) System** that answers user questions using information strictly extracted from the **AWS Prescriptive Guidance RAG PDF**.
The system retrieves relevant document chunks and generates grounded responses while preventing hallucination.

---

## 🚀 Features

* 📄 PDF ingestion & preprocessing
* ✂️ Semantic chunking into overlapping text blocks
* 🧠 Local HuggingFace embeddings (no OpenAI quota needed for embeddings)
* 🔎 Vector search using ChromaDB
* 🤖 Three-agent architecture:

  * **Planner Agent** — Understands query & decides retrieval
  * **Retriever Agent** — Searches relevant chunks
  * **Synthesis Agent** — Generates grounded answer using LLM
* 🛑 Zero hallucination enforcement
* 🧪 Terminal-based user interaction for runtime questions

---

## 🏗️ Architecture Overview

```
User Question
     ↓
Planner Agent ─── Determines intent & retrieval plan
     ↓
Retriever Agent ─── Fetches relevant chunks from vector DB
     ↓
Synthesis Agent ─── Generates grounded response using LLM
     ↓
Grounded Final Answer
```

---

## 📂 Project Structure

```
agentic-rag-aws/
│
├── app.py
├── requirements.txt
├── .env.example
│
├── data/
│   └── aws_rag_guide.pdf
│
├── ingestion/
│   ├── load_pdf.py
│   ├── chunking.py
│   └── embed_index.py
│
├── agents/
│   ├── planner_agent.py
│   ├── retriever_agent.py
│   └── synthesis_agent.py
│
└── graph/
    └── rag_graph.py
```

---

## ⚙️ Setup Instructions

### 1️⃣ Create Environment (Anaconda recommended)

```bash
conda create -n agentic-rag python=3.10
conda activate agentic-rag
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Add API Key (required for generation step)

Copy the example file and set your key:

```bash
cp .env.example .env
```

Edit `.env` and paste your OpenAI key:

```
OPENAI_API_KEY=your_api_key_here
```

> 💡 Embeddings run locally — only synthesis uses OpenAI.

### 4️⃣ Run the System

```bash
python app.py
```

The system will:

* load the PDF
* chunk documents
* build vector index
* start interactive question mode

---

## 📥 Ingestion Process (PDF → Vector Index)

Manually:

```python
from ingestion.load_pdf import load_pdf
from ingestion.chunking import chunk_documents
from ingestion.embed_index import create_vectorstore

docs = load_pdf("data")
chunks = chunk_documents(docs)
store = create_vectorstore(chunks)
```

Automatically: `python app.py`

---

## 💬 Example Queries

```
Compare fully managed RAG and custom RAG
What are the retrieval options mentioned in the guide?
How does RAG differ from fine-tuning?
Is WhatsApp integration mentioned?
```

Expected behavior:

* 🔍 **If answer exists** → grounded response
* ❓ **If not found** → `Information not available in the document.`

---



## 🧑‍💻 Author

**Sagar Khairnar**
Data Scientist | Python | Machine Learning | RAG Systems

---

