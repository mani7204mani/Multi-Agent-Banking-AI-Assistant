from datetime import datetime

from langchain_text_splitters import RecursiveCharacterTextSplitter


class DocumentChunker:

    def __init__(
        self,
        chunk_size=1000,
        chunk_overlap=200
    ):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

    def split_documents(self, documents):

        chunks = self.splitter.split_documents(documents)

        # Add metadata
        for i, chunk in enumerate(chunks):
            chunk.metadata["chunk_id"] = i + 1
            chunk.metadata["ingested_at"] = datetime.utcnow().isoformat()

            source = chunk.metadata.get("source", "")

            if source.lower().endswith(".pdf"):
                chunk.metadata["document_type"] = "pdf"
            else:
                chunk.metadata["document_type"] = "web"

        print(f"Created {len(chunks)} chunks.")

        return chunks