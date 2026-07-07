from src.database.db import Base, engine, SessionLocal
from src.database.models import Customer, Account, Transaction, Beneficiary
from src.database.data_generator import (
    generate_customer,
    generate_account,
    generate_transaction,
    generate_beneficiary,
)
import random
Base.metadata.create_all(bind=engine)

db = SessionLocal()

print("Generating sample banking data...")

NUM_CUSTOMERS = 100

accounts_created = []

for _ in range(NUM_CUSTOMERS):

    # ---------------- Customer ----------------
    customer_data = generate_customer()

    customer = Customer(**customer_data)

    db.add(customer)
    db.commit()
    db.refresh(customer)

    # ---------------- Accounts ----------------
    for _ in range(2):

        account_data = generate_account()

        account = Account(
            customer_id=customer.id,
            **account_data
        )

        db.add(account)
        db.commit()

        accounts_created.append(account.account_number)

    # ---------------- Beneficiaries ----------------
    for _ in range(2):
        beneficiary_account = random.choice(accounts_created)

        beneficiary_data = generate_beneficiary(
            beneficiary_account
        )

        beneficiary = Beneficiary(
            customer_id=customer.id,
            **beneficiary_data
        )

    db.add(beneficiary)

db.commit()

print("Customers, Accounts and Beneficiaries created.")

# ---------------- Transactions ----------------

for _ in range(1000):

    from_acc = accounts_created[
        __import__("random").randint(0, len(accounts_created)-1)
    ]

    to_acc = accounts_created[
        __import__("random").randint(0, len(accounts_created)-1)
    ]

    while from_acc == to_acc:
        to_acc = accounts_created[
            __import__("random").randint(0, len(accounts_created)-1)
        ]

    txn = Transaction(
        **generate_transaction(from_acc, to_acc)
    )

    db.add(txn)

db.commit()

db.close()

print("=" * 40)
print("Database seeded successfully!")
print(f"Customers      : {NUM_CUSTOMERS}")
print(f"Accounts       : {len(accounts_created)}")
print("Beneficiaries  : 200")
print("Transactions   : 1000")
print("=" * 40)