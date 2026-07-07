from faker import Faker
import random
import string
from datetime import datetime, timedelta

fake = Faker("en_IN")

BRANCHES = [
    ("SBI Hyderabad", "SBIN0001234"),
    ("HDFC Bangalore", "HDFC0002345"),
    ("ICICI Chennai", "ICIC0003456"),
    ("Axis Mumbai", "UTIB0004567"),
]

TRANSACTION_TYPES = [
    "UPI",
    "NEFT",
    "RTGS",
    "ATM",
    "Salary",
    "Bill Payment",
    "Shopping",
]

DESCRIPTIONS = [
    "Amazon Purchase",
    "Salary Credit",
    "Electricity Bill",
    "Swiggy Order",
    "Fuel Payment",
    "ATM Withdrawal",
    "UPI Transfer",
]


def generate_account_number():
    return "".join(random.choices(string.digits, k=12))


def generate_pan():
    letters = "".join(random.choices(string.ascii_uppercase, k=5))
    digits = "".join(random.choices(string.digits, k=4))
    last = random.choice(string.ascii_uppercase)
    return letters + digits + last


def generate_aadhaar():
    return "".join(random.choices(string.digits, k=12))


def generate_customer():
    return {
        "full_name": fake.name(),
        "email": fake.unique.email(),
        "phone": fake.msisdn()[-10:],
        "date_of_birth": str(fake.date_of_birth(minimum_age=18, maximum_age=65)),
        "pan_number": generate_pan(),
        "aadhaar_number": generate_aadhaar(),
        "kyc_verified": random.choice([True, True, True, False]),
    }


def generate_account():
    branch, ifsc = random.choice(BRANCHES)

    return {
        "account_number": generate_account_number(),
        "account_type": random.choice(["Savings", "Current"]),
        "branch_name": branch,
        "ifsc_code": ifsc,
        "balance": round(random.uniform(5000, 500000), 2),
        "status": "ACTIVE",
    }


def generate_transaction(from_acc, to_acc):
    return {
        "reference_number": "REF" + "".join(random.choices(string.digits, k=10)),
        "from_account": from_acc,
        "to_account": to_acc,
        "amount": round(random.uniform(100, 50000), 2),
        "transaction_type": random.choice(TRANSACTION_TYPES),
        "description": random.choice(DESCRIPTIONS),
        "status": random.choice(["SUCCESS", "SUCCESS", "SUCCESS", "PENDING"]),
        "timestamp": datetime.now() - timedelta(days=random.randint(0, 365)),
    }


def generate_beneficiary(account_number):
    branch, ifsc = random.choice(BRANCHES)

    return {
        "beneficiary_name": fake.name(),
        "beneficiary_account": account_number,
        "bank_name": branch.split()[0],
        "ifsc_code": ifsc,
    }