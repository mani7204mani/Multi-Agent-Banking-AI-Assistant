from langchain_openai import AzureOpenAIEmbeddings

from src.config import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    EMBEDDING_DEPLOYMENT,
)


class EmbeddingService:

    def __init__(self):

        self.embedding_model = AzureOpenAIEmbeddings(
            azure_endpoint=AZURE_OPENAI_ENDPOINT,
            api_key=AZURE_OPENAI_API_KEY,
            api_version=AZURE_OPENAI_API_VERSION,
            azure_deployment=EMBEDDING_DEPLOYMENT,
        )

    def get_embeddings(self):
        return self.embedding_model