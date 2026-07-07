from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from datetime import datetime

from src.database.db import Base


# -------------------------
# Customer Table
# -------------------------
class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)

    date_of_birth = Column(String)
    pan_number = Column(String, unique=True)
    aadhaar_number = Column(String, unique=True)

    kyc_verified = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    accounts = relationship("Account", back_populates="customer")
    beneficiaries = relationship("Beneficiary", back_populates="customer")


# -------------------------
# Account Table
# -------------------------
class Account(Base):
    __tablename__ = "accounts"

    account_number = Column(String, primary_key=True)

    customer_id = Column(Integer, ForeignKey("customers.id"))

    account_type = Column(String)

    branch_name = Column(String)

    ifsc_code = Column(String)

    balance = Column(Float, default=0.0)

    status = Column(String, default="ACTIVE")

    created_at = Column(DateTime, default=datetime.utcnow)

    customer = relationship("Customer", back_populates="accounts")


# -------------------------
# Transaction Table
# -------------------------
class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    reference_number = Column(String, unique=True)

    from_account = Column(String)

    to_account = Column(String)

    amount = Column(Float)

    transaction_type = Column(String)

    description = Column(String)

    status = Column(String)

    timestamp = Column(DateTime, default=datetime.utcnow)


# -------------------------
# Beneficiary Table
# -------------------------
class Beneficiary(Base):
    __tablename__ = "beneficiaries"

    id = Column(Integer, primary_key=True, index=True)

    customer_id = Column(Integer, ForeignKey("customers.id"))

    beneficiary_name = Column(String)

    beneficiary_account = Column(String)

    bank_name = Column(String)

    ifsc_code = Column(String)

    customer = relationship("Customer", back_populates="beneficiaries")