from src.rag.loader import DocumentLoader
from src.rag.chunker import DocumentChunker

loader = DocumentLoader()
documents = loader.load_all()

chunker = DocumentChunker()

chunks = chunker.split_documents(documents)

print("=" * 60)
print(f"Total Chunks: {len(chunks)}")

print("=" * 60)

print(chunks[0].page_content)

print("=" * 60)

print(chunks[0].metadata)