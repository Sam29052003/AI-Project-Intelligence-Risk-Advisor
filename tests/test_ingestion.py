import os
from src.ingestion import load_document, load_all_documents


def test_txt_document_loading():

    file_path = "data/sample_documents/projects_notes.txt"

    assert os.path.exists(file_path)

    content = load_document(file_path)

    assert content is not None
    assert len(content) > 0


def test_load_all_documents():

    folder_path = "data/sample_documents"

    documents = load_all_documents(folder_path)

    assert isinstance(documents, list)
    assert len(documents) > 0


def test_document_structure():

    folder_path = "data/sample_documents"

    documents = load_all_documents(folder_path)

    document = documents[0]

    assert "source" in document
    assert "content" in document