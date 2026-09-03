from src.rag_pipeline import create_chunks


def test_chunk_creation():

    documents = [
        {
            "source": "test.txt",
            "content": "This is a test project document. " * 50
        }
    ]

    chunks = create_chunks(documents)

    assert len(chunks) > 0
    assert "text" in chunks[0]
    assert "source" in chunks[0]