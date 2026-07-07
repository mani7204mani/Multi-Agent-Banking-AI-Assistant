import re


class TransferParser:

    def parse(self, query: str):

        query_lower = query.lower()

        amount = None

        lakh = re.search(r"(\d+)\s*lakh", query_lower)

        if lakh:
            amount = float(lakh.group(1)) * 100000

        else:

            number = re.search(r"₹?\s*(\d+)", query_lower)

            if number:
                amount = float(number.group(1))

        if "upi" in query_lower:
            tx_type = "UPI"

        elif "rtgs" in query_lower:
            tx_type = "RTGS"

        elif "neft" in query_lower:
            tx_type = "NEFT"

        else:
            tx_type = "NEFT"

        beneficiary = None

        match = re.search(r"to\s+(.+?)(?:\s+via|\s*$)", query, re.IGNORECASE)

        if match:
            beneficiary = match.group(1).strip()

        return {
            "amount": amount,
            "transaction_type": tx_type,
            "beneficiary": beneficiary
        }