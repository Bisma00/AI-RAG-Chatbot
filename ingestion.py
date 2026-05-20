import os

from langchain_community.document_loaders import TextLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

DOCUMENTS_PATH = "sample_docs"


def load_documents():

    documents = []

    for file in os.listdir(DOCUMENTS_PATH):

        if file.endswith(".txt"):

            file_path = os.path.join(
                DOCUMENTS_PATH,
                file
            )

            loader = TextLoader(file_path)

            documents.extend(loader.load())

    return documents

def split_documents(documents):

    text_splitter = RecursiveCharacterTextSplitter(

        chunk_size=300,

        chunk_overlap=50
    )

    chunks = text_splitter.split_documents(
        documents
    )

    return chunks

if __name__ == "__main__":

    docs = load_documents()

    chunks = split_documents(docs)

    print(f"Loaded Documents: {len(docs)}")

    print(f"Generated Chunks: {len(chunks)}")

    print("\nSample Chunk:\n")

    print(chunks[0].page_content)