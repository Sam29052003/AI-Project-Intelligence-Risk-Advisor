from src.ingestion import load_all_documents
from src.rag_pipeline import build_knowledge_base
from src.chatbot import generate_answer


def main():

    folder_path = "data/sample_documents"

    print("Loading documents...\n")

    documents = load_all_documents(folder_path)

    print(f"\nDocuments found: {len(documents)}")

    if len(documents) == 0:
        print("No supported documents found.")
        return

    print("\nBuilding knowledge base...\n")

    collection = build_knowledge_base(documents)

    print("\nKnowledge Base Ready!")
    print(f"Total Chunks Stored: {collection.count()}")

    print("\nAI Project Intelligence Assistant Ready!")
    print("Type exit to stop.\n")

    while True:

        question = input("Ask a question: ").strip()

        # Remove quotes if user types 'exit' or "exit"
        clean_question = question.strip("'\"").lower()

        if clean_question == "exit":
            print("Assistant closed successfully.")
            break

        if not question:
            print("Please enter a question.")
            continue

        try:
            answer = generate_answer(question)

            print("\nAnswer:")
            print(answer)
            print()

        except Exception as error:
            print("\nError:", error)
            print("Please try again.\n")


if __name__ == "__main__":
    main()