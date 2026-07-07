from pydantic import BaseModel

from src.rules.compliance_rules import (
    MIN_BALANCE,
    UPI_LIMIT,
    NEFT_LIMIT,
    RTGS_MINIMUM,
    MAX_DAILY_TRANSFER,
)


class ComplianceResult(BaseModel):
    approved: bool
    reason: str


class ComplianceAgent:

    def check_transfer(
        self,
        balance: float,
        amount: float,
        transaction_type: str,
        kyc_verified: bool = True,
    ):

        if not kyc_verified:
            return ComplianceResult(
                approved=False,
                reason="Customer KYC is not verified."
            )

        if amount > balance:
            return ComplianceResult(
                approved=False,
                reason="Insufficient account balance."
            )

        if balance - amount < MIN_BALANCE:
            return ComplianceResult(
                approved=False,
                reason="Minimum balance requirement violated."
            )

        if amount > MAX_DAILY_TRANSFER:
            return ComplianceResult(
                approved=False,
                reason="Daily transfer limit exceeded."
            )

        transaction_type = transaction_type.upper()

        if transaction_type == "UPI":

            if amount > UPI_LIMIT:

                return ComplianceResult(
                    approved=False,
                    reason="UPI transaction limit exceeded."
                )

        elif transaction_type == "RTGS":

            if amount < RTGS_MINIMUM:

                return ComplianceResult(
                    approved=False,
                    reason="RTGS requires a minimum amount of ₹2,00,000."
                )

        elif transaction_type == "NEFT":

            if amount > NEFT_LIMIT:

                return ComplianceResult(
                    approved=False,
                    reason="NEFT transfer limit exceeded."
                )

        return ComplianceResult(
            approved=True,
            reason="Transfer complies with all banking rules."
        )