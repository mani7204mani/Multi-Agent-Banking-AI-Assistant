from openai import AzureOpenAI
from src.config import *

client = AzureOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
)

# Test chat model
print("Testing gpt-5-mini...")
response = client.chat.completions.create(
    model=AZURE_OPENAI_DEPLOYMENT,
    messages=[{"role": "user", "content": "Say: BankBot connected successfully"}],
    max_completion_tokens=100,
)
print("Chat:", response.choices[0].message.content)

# Test embedding model
print("\nTesting text-embedding-3-small...")
embedding = client.embeddings.create(
    model=AZURE_EMBEDDING_DEPLOYMENT,
    input="test banking query",
)
print(f"Embedding dims: {len(embedding.data[0].embedding)}")
print("\nAll connections working!")