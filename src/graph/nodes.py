from unittest import result

from src.graph.state import BankBotState
from src.mcp.client import MCPClient
from src.agents.intent_agent import IntentAgent
from src.agents.retrieval_agent import RetrievalAgent
from src.agents.transaction_agent import TransactionAgent
from src.agents.compliance_agent import ComplianceAgent
from src.agents.response_agent import ResponseAgent
from src.agents.transfer_agent import TransferAgent
from src.utils.parser import TransferParser
import json

# Initialize agents
intent_agent = IntentAgent()
retrieval_agent = RetrievalAgent()
transaction_agent = TransactionAgent()
compliance_agent = ComplianceAgent()
response_agent = ResponseAgent()
transfer_agent = TransferAgent()
parser = TransferParser()

mcp_client = MCPClient()
def intent_node(state: BankBotState):

    result = intent_agent.classify(state["query"])

    state["intent"] = result.intent

    return state


def retrieval_node(state: BankBotState):

    result = retrieval_agent.answer(state["query"])

    response = response_agent.build_response(
        response=result.answer,
        sources=result.sources,
    )

    state["response"] = response.model_dump()

    return state


def transaction_node(state: BankBotState):

    result = mcp_client.call_tool(
        "balance",
        {
            "customer_id": state["customer_id"]
        }
    )

    data = json.loads(
        result.content[0].text
    )

    if not data["success"]:

        state["response"] = response_agent.build_response(
            response=data["message"]
        ).model_dump()

        return state

    account_details = []

    for account in data["accounts"]:

        account_details.append(
            f"""
Account Number : {account["account_number"]}
Balance        : ₹{account["balance"]}
Branch         : {account["branch"]}
"""
        )

    state["response"] = response_agent.build_response(
        response="\n".join(account_details)
    ).model_dump()

    return state

def compliance_node(state: BankBotState):

    parsed = parser.parse(state["query"])

    amount = parsed["amount"]
    tx_type = parsed["transaction_type"]

    customer = transaction_agent.get_customer_by_id(
        state["customer_id"]
    )

    if customer is None:

        response = response_agent.build_response(
            response="Customer not found."
        )

        state["response"] = response.model_dump()

        return state

    accounts = transaction_agent.get_accounts(customer.id)

    if not accounts:

        response = response_agent.build_response(
            response="No account found."
        )

        state["response"] = response.model_dump()

        return state

    balance = accounts[0].balance

    result = mcp_client.call_tool(
    "compliance",
    {
        "balance": balance,
        "amount": amount,
        "transaction_type": tx_type,
        "kyc_verified": True
    }
    )
    data = json.loads(
       result.content[0].text)

    state["amount"] = amount
    state["transaction_type"] = tx_type
    state["balance"] = balance

    message = f"""
Transfer Amount : ₹{amount:,.2f}

Available Balance : ₹{balance:,.2f}

Transaction Type : {tx_type}

Status : {"Approved" if data["approved"] else "Rejected"}

Reason : {data["reason"]}
"""

    response = response_agent.build_response(
        response=message
    )

    state["response"] = response.model_dump()

    return state
def transfer_node(state: BankBotState):

    parsed = parser.parse(state["query"])

    amount = parsed["amount"]
    tx_type = parsed["transaction_type"]
    beneficiary_name = parsed["beneficiary"]

    # Get customer
    customer = transaction_agent.get_customer_by_id(
        state["customer_id"]
    )

    if customer is None:

        state["response"] = response_agent.build_response(
            response="Customer not found."
        ).model_dump()

        return state

    # Get sender account
    accounts = transaction_agent.get_accounts(customer.id)

    if not accounts:

        state["response"] = response_agent.build_response(
            response="No account found."
        ).model_dump()

        return state

    sender_account = accounts[0]

    # Find beneficiary
    beneficiary = transaction_agent.get_beneficiary(
        customer.id,
        beneficiary_name
    )

    if beneficiary is None:

        state["response"] = response_agent.build_response(
            response=f"Beneficiary '{beneficiary_name}' not found."
        ).model_dump()

        return state

    # Compliance check
    compliance = compliance_agent.check_transfer(
        balance=sender_account.balance,
        amount=amount,
        transaction_type=tx_type,
        kyc_verified=True,
    )

    if not compliance.approved:

        state["response"] = response_agent.build_response(
            response=compliance.reason
        ).model_dump()

        return state

    print("=" * 50)
    print("Sender Account      :", sender_account.account_number)
    print("Beneficiary Name    :", beneficiary.beneficiary_name)
    print("Beneficiary Account :", beneficiary.beneficiary_account)
    print("=" * 50)

    # Execute transfer
    result = mcp_client.call_tool(
    "transfer",
    {
        "sender_account": sender_account.account_number,
        "receiver_account": beneficiary.beneficiary_account,
        "amount": amount,
        "transaction_type": tx_type,
    }
)

    transfer = json.loads(
    result.content[0].text
    )

    print(transfer)

    # Handle failure
    if not transfer["success"]:

        state["response"] = response_agent.build_response(
            response=transfer["message"]
        ).model_dump()

        return state

    # Success response
    state["response"] = response_agent.build_response(
        response=f"""
Transfer Successful

Reference : {transfer['reference']}

Beneficiary : {beneficiary.beneficiary_name}

Amount : ₹{amount}

Available Balance : ₹{transfer['sender_balance']}
"""
    ).model_dump()

    return state