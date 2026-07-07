import random
from datetime import datetime

from src.database.db import SessionLocal
from src.database.models import Account, Transaction


class TransferAgent:

    def __init__(self):
        self.db = SessionLocal()

    def execute_transfer(
        self,
        sender_account_number: str,
        receiver_account_number: str,
        amount: float,
        transaction_type: str,
    ):

        sender = (
            self.db.query(Account)
            .filter(Account.account_number == sender_account_number)
            .first()
        )

        receiver = (
            self.db.query(Account)
            .filter(Account.account_number == receiver_account_number)
            .first()
        )

        if sender is None or receiver is None:
            return {
                "success": False,
                "message": "Account not found."
            }

        if sender.balance < amount:
            return {
                "success": False,
                "message": "Insufficient balance."
            }

        sender.balance -= amount
        receiver.balance += amount

        reference = f"REF{random.randint(1000000000,9999999999)}"

        transaction = Transaction(
            reference_number=reference,
            from_account=sender.account_number,
            to_account=receiver.account_number,
            amount=amount,
            transaction_type=transaction_type,
            description=f"Transfer to {receiver.account_number}",
            status="SUCCESS",
            timestamp=datetime.utcnow()
        )

        self.db.add(transaction)
        self.db.commit()

        self.db.refresh(sender)
        self.db.refresh(receiver)

        return {
            "success": True,
            "reference": reference,
            "sender_balance": sender.balance,
            "receiver_balance": receiver.balance,
        }