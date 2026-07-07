from src.rag.vector_store import VectorStore


class Retriever:

    def __init__(self):
        self.vector_store = VectorStore()

    def retrieve(self, query: str, k: int = 5):
        return self.vector_store.similarity_search(query, k)