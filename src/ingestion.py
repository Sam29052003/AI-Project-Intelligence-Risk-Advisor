import os
import pandas as pd
from pypdf import PdfReader
from unstructured.partition.auto import partition


def load_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def load_csv(file_path):
    df = pd.read_csv(file_path)
    return df.to_string(index=False)


def load_docx_txt(file_path):
    elements = partition(filename=file_path)

    text = "\n".join(
        str(element) for element in elements
    )

    return text


def load_document(file_path):
    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return load_pdf(file_path)

    elif extension == ".csv":
        return load_csv(file_path)

    elif extension in [".docx", ".txt"]:
        return load_docx_txt(file_path)

    else:
        raise ValueError(
            f"Unsupported file type: {extension}"
        )


def load_all_documents(folder_path):
    documents = []

    for file_name in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file_name)

        if not os.path.isfile(file_path):
            continue

        try:
            content = load_document(file_path)

            if content and content.strip():

                document = {
                    "source": file_name,
                    "content": content
                }

                documents.append(document)

                print(f"Loaded: {file_name}")

        except Exception as error:
            print(f"Error loading {file_name}: {error}")

    return documents