from src.rag.loader import DocumentLoader
from src.rag.chunker import DocumentChunker
from src.rag.vector_store import VectorStore


class KnowledgeBaseIngestor:

    def __init__(self):
        self.loader = DocumentLoader()
        self.chunker = DocumentChunker()
        self.vector_store = VectorStore()
        self.vector_store.reset()

    def ingest(self):

        print("=" * 60)
        print("Starting Knowledge Base Ingestion...")
        print("=" * 60)

        # Step 1: Load documents
        documents = self.loader.load_all()

        print(f"Loaded {len(documents)} documents")

        # Step 2: Split into chunks
        chunks = self.chunker.split_documents(documents)

        print(f"Created {len(chunks)} chunks")

        # Step 3: Store in ChromaDB
        self.vector_store.add_documents(chunks)

        print("=" * 60)
        print("Knowledge Base Successfully Created!")
        print("=" * 60)


if __name__ == "__main__":

    ingestor = KnowledgeBaseIngestor()

    ingestor.ingest()