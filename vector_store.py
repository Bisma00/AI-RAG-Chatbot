from langchain_community.vectorstores import FAISS

from langchain_community.embeddings import HuggingFaceEmbeddings

from ingestion import load_documents, split_documents

embedding_model = HuggingFaceEmbeddings(

    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

documents = load_documents()

chunks = split_documents(documents)

vector_db = FAISS.from_documents(

    chunks,

    embedding_model
)

vector_db.save_local("vector_store")

print("FAISS vector database created successfully.")