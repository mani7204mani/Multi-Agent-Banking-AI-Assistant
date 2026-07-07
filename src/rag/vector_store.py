from langchain_chroma import Chroma

from src.rag.embedding_service import EmbeddingService


class VectorStore:

    def __init__(self):

        embedding_service = EmbeddingService()

        self.vector_db = Chroma(
            collection_name="bankbot_knowledge_base",
            embedding_function=embedding_service.get_embeddings(),
            persist_directory="chroma_db",
        )

    def reset(self):
        self.vector_db.reset_collection()

    def add_documents(self, documents):
        self.vector_db.add_documents(documents)
        print(f"Stored {len(documents)} chunks into ChromaDB.")

    def similarity_search(self, query, k=5):
        return self.vector_db.similarity_search(query, k=k)

    def get_retriever(self):
        return self.vector_db.as_retriever(search_kwargs={"k": 5})