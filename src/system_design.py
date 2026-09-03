class ProjectArchitecture:

    def __init__(self):
        self.modules = {
            "document_ingestion": [
                "PDF Loader",
                "DOCX Loader",
                "CSV Loader",
                "TXT Loader"
            ],

            "rag_pipeline": [
                "Text Chunking",
                "Sentence Transformer Embeddings",
                "ChromaDB Vector Storage",
                "Document Retrieval"
            ],

            "agents": [
                "Scope and Deliverable Extraction Agent",
                "Risk Detection Agent",
                "Delivery Forecasting Agent",
                "Blocker and Action Item Agent",
                "Documentation Generation Agent",
                "Project Health Scoring Agent"
            ],

            "assistant": [
                "Conversational Project Intelligence Assistant"
            ],

            "dashboard": [
                "Project Insights",
                "Risk Summary",
                "Project Health Score"
            ]
        }

    def display_architecture(self):

        print("\nAI PROJECT SYSTEM ARCHITECTURE\n")

        for module, components in self.modules.items():

            print(f"{module.upper()}")

            for component in components:
                print(f"  -> {component}")

            print()