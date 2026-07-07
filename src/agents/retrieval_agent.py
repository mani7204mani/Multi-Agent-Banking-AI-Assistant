from pydantic import BaseModel
from pathlib import Path
from src.core.llm import llm
from src.rag.retriever import Retriever


class RetrievalResult(BaseModel):
    answer: str
    sources: list[str]


class RetrievalAgent:

    def __init__(self):
        self.retriever = Retriever()
        self.llm = llm.with_structured_output(RetrievalResult)

    def answer(self, query: str):

        # Retrieve relevant documents
        docs = self.retriever.retrieve(query)

        # Build context with metadata
        context_parts = []

        for doc in docs:
            source = doc.metadata.get("source", "Unknown")
            page = doc.metadata.get("page", "N/A")

            context_parts.append(
                f"""
Source: {source}
Page: {page}

{doc.page_content}
"""
            )

        context = "\n\n------------------------------\n\n".join(context_parts)

        prompt = f"""
You are an enterprise banking assistant.

Answer ONLY using the provided context.

If the answer is not available in the context,
respond with:

'I couldn't find this information in the knowledge base.'

Context
========

{context}

Question
========

{query}

Return:
- answer
- sources
"""

        response = self.llm.invoke(prompt)

        # Build unique sources list
        sources = []

        for doc in docs:


            filename = Path(
            doc.metadata.get("source", "Unknown")
            ).name

            page = doc.metadata.get("page", "N/A")

            sources.append(
                f"{filename} (Page {page})"
            )

            # Remove duplicates
            sources = list(dict.fromkeys(sources))

        return RetrievalResult(
            answer=response.answer,
            sources=sources
        )