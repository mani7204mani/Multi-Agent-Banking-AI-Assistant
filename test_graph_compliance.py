from src.graph.graph import graph

result = graph.invoke(
    {
        "query": "Can I transfer 2 lakh through RTGS?",
        "intent": None,
        "customer_id": 1,
        "account_number": None,
        "amount": None,
        "transaction_type": None,
        "balance": None,
        "sources": [],
        "response": None,
    }
)

print(result["response"])