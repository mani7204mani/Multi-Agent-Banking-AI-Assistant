from src.agents.transfer_agent import TransferAgent
from src.database.models import Account
from src.database.db import SessionLocal

db = SessionLocal()

# Get any two accounts from the database
accounts = db.query(Account).limit(2).all()

sender = accounts[0]
receiver = accounts[1]

print("=" * 50)
print("Before Transfer")
print(sender.account_number, sender.balance)
print(receiver.account_number, receiver.balance)

agent = TransferAgent()

result = agent.execute_transfer(
    sender_account_number=sender.account_number,
    receiver_account_number=receiver.account_number,
    amount=1000,
    transaction_type="UPI"
)

print(result)

# Reload balances
db.refresh(sender)
db.refresh(receiver)

print("=" * 50)
print("After Transfer")
print(sender.account_number, sender.balance)
print(receiver.account_number, receiver.balance)