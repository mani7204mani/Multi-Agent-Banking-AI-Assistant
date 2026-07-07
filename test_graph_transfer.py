from src.graph.graph import graph

result = graph.invoke(
    {
        "query": "Transfer 1000 to Banjeet Mutti via UPI",
        "customer_id": 1,
    }
)

print("=" * 60)
print(result["response"])
print("=" * 60)