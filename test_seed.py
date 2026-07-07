from src.database.db import SessionLocal
from src.database.models import Customer, Account, Transaction, Beneficiary

db = SessionLocal()

print("=" * 50)

print(f"Customers      : {db.query(Customer).count()}")
print(f"Accounts       : {db.query(Account).count()}")
print(f"Transactions   : {db.query(Transaction).count()}")
print(f"Beneficiaries  : {db.query(Beneficiary).count()}")

print("=" * 50)

customer = db.query(Customer).first()

print("Sample Customer")
print(customer.full_name)
print(customer.email)
print(customer.phone)

print("=" * 50)

account = db.query(Account).first()

print("Sample Account")
print(account.account_number)
print(account.balance)
print(account.branch_name)

print("=" * 50)

txn = db.query(Transaction).first()

print("Sample Transaction")
print(txn.reference_number)
print(txn.amount)
print(txn.transaction_type)
print(txn.description)

db.close()