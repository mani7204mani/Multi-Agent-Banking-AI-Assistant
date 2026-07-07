from src.rag.vector_store import VectorStore

vector_store = VectorStore()

results = vector_store.similarity_search(
    "What documents are required for KYC?"
)

print("=" * 60)

for i, doc in enumerate(results):

    print(f"\nResult {i+1}")

    print(doc.page_content[:500])

    print("\nMetadata:")

    print(doc.metadata)

    print("=" * 60)