from src.core.llm import llm

response = llm.invoke("Say: BankBot LLM is working.")

print(response.content)