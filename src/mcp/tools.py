from src.agents.transaction_agent import TransactionAgent
from src.agents.compliance_agent import ComplianceAgent
from src.agents.transfer_agent import TransferAgent
transaction_agent = TransactionAgent()
transfer_agent = TransferAgent()

def get_balance(customer_id: int):

    customer = transaction_agent.get_customer_by_id(customer_id)

    if customer is None:
        return {
            "success": False,
            "message": "Customer not found."
        }

    accounts = transaction_agent.get_accounts(customer.id)

    balances = []

    for account in accounts:

        balances.append({
            "account_number": account.account_number,
            "balance": account.balance,
            "branch": account.branch_name
        })

    return {
        "success": True,
        "accounts": balances
    }
def get_transactions(customer_id: int):

    customer = transaction_agent.get_customer_by_id(customer_id)

    if customer is None:
        return {
            "success": False,
            "message": "Customer not found."
        }

    accounts = transaction_agent.get_accounts(customer.id)

    if not accounts:
        return {
            "success": False,
            "message": "No accounts found."
        }

    transactions = transaction_agent.get_transactions(
        accounts[0].account_number
    )

    result = []

    for txn in transactions:

        result.append({
            "reference": txn.reference_number,
            "amount": txn.amount,
            "type": txn.transaction_type,
            "status": txn.status
        })

    return {
        "success": True,
        "transactions": result
    }


compliance_agent = ComplianceAgent()


def check_compliance(
    balance: float,
    amount: float,
    transaction_type: str,
    kyc_verified: bool = True
):

    result = compliance_agent.check_transfer(
        balance=balance,
        amount=amount,
        transaction_type=transaction_type,
        kyc_verified=kyc_verified
    )

    return {
        "approved": result.approved,
        "reason": result.reason
    }
def transfer_money(
    sender_account: str,
    receiver_account: str,
    amount: float,
    transaction_type: str,
):

    result = transfer_agent.execute_transfer(
        sender_account,
        receiver_account,
        amount,
        transaction_type,
    )

    return result
