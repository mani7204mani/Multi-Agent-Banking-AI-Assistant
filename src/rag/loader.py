import json
from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    WebBaseLoader,
)


class DocumentLoader:
    def __init__(self):
        self.project_root = Path(__file__).resolve().parents[2]
        self.documents_path = self.project_root / "documents"

    def load_pdfs(self):
        """Load all PDFs inside documents/rbi and documents/banking"""
        documents = []

        for folder in ["rbi", "banking"]:
            folder_path = self.documents_path / folder

            if not folder_path.exists():
                continue

            for pdf_file in folder_path.glob("*.pdf"):
                print(f"Loading PDF: {pdf_file.name}")

                loader = PyPDFLoader(str(pdf_file))
                documents.extend(loader.load())

        return documents

    def load_web_pages(self):
        """Load all URLs from sources.json"""
        documents = []

        sources_file = self.documents_path / "sources.json"

        if not sources_file.exists():
            print("sources.json not found")
            return documents

        with open(sources_file, "r", encoding="utf-8") as f:
            sources = json.load(f)

        for source in sources:

            print(f"Loading Web Page: {source['name']}")

            loader = WebBaseLoader(source["url"])

            docs = loader.load()

            # Add metadata
            for doc in docs:
                doc.metadata["source_name"] = source["name"]
                doc.metadata["category"] = source["category"]
                doc.metadata["url"] = source["url"]

            documents.extend(docs)

        return documents

    def load_all(self):
        pdf_docs = self.load_pdfs()
        web_docs = self.load_web_pages()

        print(f"Loaded {len(pdf_docs)} PDF documents")
        print(f"Loaded {len(web_docs)} Web documents")

        return pdf_docs + web_docs