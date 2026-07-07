from mcp.server.fastmcp import FastMCP
from src.mcp.tools import check_compliance
from src.mcp.tools import get_balance
from src.mcp.tools import get_transactions
from src.mcp.tools import transfer_money
mcp = FastMCP("BankBot MCP Server")


@mcp.tool()
def balance(customer_id: int):
    return get_balance(customer_id)

@mcp.tool()
def transactions(customer_id: int):
    return get_transactions(customer_id)
@mcp.tool()
def compliance(
    balance: float,
    amount: float,
    transaction_type: str,
    kyc_verified: bool = True
):
    return check_compliance(
        balance,
        amount,
        transaction_type,
        kyc_verified
    )
@mcp.tool()
def transfer(
    sender_account: str,
    receiver_account: str,
    amount: float,
    transaction_type: str,
):
    return transfer_money(
        sender_account,
        receiver_account,
        amount,
        transaction_type,
    )
if __name__ == "__main__":
    print("Starting BankBot MCP Server...")
    mcp.run(transport="streamable-http")