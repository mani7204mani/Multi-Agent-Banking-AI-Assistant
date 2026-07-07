from src.mcp.client import MCPClient

client = MCPClient()

result = client.call_tool(
    "balance",
    {
        "customer_id": 1
    }
)

print(result)