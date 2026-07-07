from langfuse import get_client
from langfuse.langchain import CallbackHandler

# Initializes using your LANGFUSE_* environment variables
langfuse = get_client()

langfuse_handler = CallbackHandler()