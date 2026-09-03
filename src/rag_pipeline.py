import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer


embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def create_chunks(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = []

    for document in documents:

        split_chunks = text_splitter.split_text(
            document["content"]
        )

        for chunk in split_chunks:

            chunks.append({
                "text": chunk,
                "source": document["source"]
            })

    return chunks


def create_embeddings(chunks):

    texts = [
        chunk["text"]
        for chunk in chunks
    ]

    embeddings = embedding_model.encode(
        texts,
        show_progress_bar=True
    )

    return embeddings


def store_in_chromadb(chunks, embeddings):

    client = chromadb.PersistentClient(
        path="chroma_db"
    )

    try:
        client.delete_collection(
            name="project_documents"
        )
    except Exception:
        pass

    collection = client.get_or_create_collection(
        name="project_documents"
    )

    documents = [
        chunk["text"]
        for chunk in chunks
    ]

    metadatas = [
        {"source": chunk["source"]}
        for chunk in chunks
    ]

    ids = [
        f"chunk_{i}"
        for i in range(len(chunks))
    ]

    collection.add(
        documents=documents,
        embeddings=embeddings.tolist(),
        metadatas=metadatas,
        ids=ids
    )

    return collection


def build_knowledge_base(documents):

    chunks = create_chunks(documents)

    print(f"Total Chunks Created: {len(chunks)}")

    embeddings = create_embeddings(chunks)

    print("Embeddings Generated Successfully")

    collection = store_in_chromadb(
        chunks,
        embeddings
    )

    print("Data Stored in ChromaDB Successfully")

    return collection