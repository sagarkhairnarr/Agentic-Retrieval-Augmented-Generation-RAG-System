from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings




def create_vectorstore(chunks):
   embeddings = OpenAIEmbeddings()
   vectorstore = Chroma.from_documents(
       documents=chunks,
       embedding=embeddings,
       persist_directory="./chroma_db"
   )
   return vectorstore



