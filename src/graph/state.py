from typing import Optional, TypedDict


class BankBotState(TypedDict):

    query: str
    intent: Optional[str]

    customer_id: Optional[int]

    account_number: Optional[str]
    amount: Optional[float]
    transaction_type: Optional[str]

    balance: Optional[float]

    sources: list[str]

    response: Optional[str]