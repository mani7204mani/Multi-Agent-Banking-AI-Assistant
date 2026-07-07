from src.agents.intent_agent import IntentAgent

agent = IntentAgent()

queries = [
    "Hi",
    "Show my last 5 transactions",
    "What is KYC?",
    "Can I transfer 10 lakh today?",
    "Thank you",
    "Transfer ₹1000 to Banjeet Mutti via UPI",
    "send 5000 to rahul",
]

for query in queries:

    result = agent.classify(query)

    print("=" * 60)
    print("Query:", query)
    print("Intent:", result.intent)
    print("Confidence:", result.confidence)
    print("Reason:", result.reason)