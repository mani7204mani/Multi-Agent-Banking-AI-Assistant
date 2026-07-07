from src.agents.retrieval_agent import RetrievalAgent

agent = RetrievalAgent()

result = agent.answer(
    "What documents are required for KYC?"
)

print("=" * 60)

print(result.answer)

print("\nSources")

print("-" * 60)

for source in result.sources:
    print(source)