from src.agents.transaction_agent import TransactionAgent

agent = TransactionAgent()

customer = agent.get_customer("vargheseamruta@example.org")

print("=" * 60)

print(customer.full_name)

accounts = agent.get_accounts(customer.id)

print(accounts)

print("=" * 60)

for account in accounts:

    print(account.account_number)

    print("Balance:", account.balance)

    txns = agent.get_last_transactions(
        account.account_number
    )

    print("Transactions")

    for txn in txns:

        print(
            txn.reference_number,
            txn.amount,
            txn.transaction_type
        )

print("=" * 60)

beneficiaries = agent.get_beneficiaries(customer.id)

for b in beneficiaries:

    print(
        b.beneficiary_name,
        b.bank_name
    )

agent.close()