from typing import Literal

from pydantic import BaseModel

from src.core.llm import llm
from src.core.prompts import INTENT_SYSTEM_PROMPT


class IntentResult(BaseModel):
    intent: Literal[
        "retrieval",
        "transaction",
        "compliance",
        "greeting",
        "general",
        "transfer"
    ]

    confidence: float
    reason: str


class IntentAgent:

    def __init__(self):
        self.llm = llm.with_structured_output(IntentResult)

    def classify(self, query: str):

        messages = [
            ("system", INTENT_SYSTEM_PROMPT),
            ("human", query)
        ]

        return self.llm.invoke(messages)