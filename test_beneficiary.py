from src.agents.transaction_agent import TransactionAgent

agent = TransactionAgent()

customer = agent.get_customer_by_id(1)

print("=" * 50)
print("Customer:", customer.full_name)
print("=" * 50)

beneficiaries = agent.get_beneficiaries(customer.id)

for b in beneficiaries:
    print(
        b.beneficiary_name,
        b.beneficiary_account
    )