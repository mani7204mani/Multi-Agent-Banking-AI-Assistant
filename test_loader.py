from src.rag.loader import DocumentLoader

loader = DocumentLoader()

docs = loader.load_all()

print("=" * 60)
print(f"Total Documents Loaded: {len(docs)}")
print("=" * 60)

if docs:
    print("Sample Metadata:")
    print(docs[0].metadata)

    print("\nFirst 500 characters:\n")
    print(docs[0].page_content[:500])