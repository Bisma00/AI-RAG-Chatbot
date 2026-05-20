from langchain_community.vectorstores import FAISS

from langchain_community.embeddings import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(

    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
vector_db = FAISS.load_local(

    "vector_store",

    embedding_model,

    allow_dangerous_deserialization=True
)

def retrieve_context(query):

    results = vector_db.similarity_search(

        query,

        k=2
    )

    return results

if __name__ == "__main__":

    query = "What is the company leave policy?"

    results = retrieve_context(query)

    print("\nRetrieved Context:\n")

    for i, result in enumerate(results):

        print(f"\nResult {i+1}:\n")

        print(result.page_content)