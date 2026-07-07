from langchain_openai import AzureChatOpenAI
from src.observability.callbacks import langfuse_handler
from src.config import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    CHAT_DEPLOYMENT,
)


llm = AzureChatOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_deployment=CHAT_DEPLOYMENT,
    callbacks=[langfuse_handler]
)