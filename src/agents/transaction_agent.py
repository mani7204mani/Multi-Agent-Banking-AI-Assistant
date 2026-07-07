from sqlalchemy.orm import Session
from src.database.models import Beneficiary
from src.database.db import SessionLocal
from src.database.models import (
    Customer,
    Account,
    Transaction,
    Beneficiary,
)


class TransactionAgent:

    def __init__(self):
        self.db: Session = SessionLocal()
    
    def get_customer(self, email: str):

        return (
            self.db.query(Customer)
            .filter(Customer.email == email)
            .first()
        )
    def get_customer_by_id(self, customer_id: int):

        return (
            self.db.query(Customer)
            .filter(Customer.id == customer_id)
            .first()
        )

    def get_accounts(self, customer_id: int):

        return (
            self.db.query(Account)
            .filter(Account.customer_id == customer_id)
            .all()
        )

    def get_balance(self, account_number: str):

        account = (
            self.db.query(Account)
            .filter(Account.account_number == account_number)
            .first()
        )

        if account:
            return account.balance

        return None

    def get_last_transactions(
        self,
        account_number: str,
        limit: int = 5
    ):

        return (
            self.db.query(Transaction)
            .filter(
                (Transaction.from_account == account_number)
                |
                (Transaction.to_account == account_number)
            )
            .order_by(Transaction.timestamp.desc())
            .limit(limit)
            .all()
        )
    def get_beneficiary(self, customer_id, beneficiary_name):
        return (
        self.db.query(Beneficiary)
        .filter(
            Beneficiary.customer_id == customer_id,
            Beneficiary.beneficiary_name.ilike(
                f"%{beneficiary_name}%"
            )
        )
        .first()
    )
    def get_beneficiaries(self, customer_id: int):

        return (
            self.db.query(Beneficiary)
            .filter(Beneficiary.customer_id == customer_id)
            .all()
        )
    

    def close(self):
        self.db.close()