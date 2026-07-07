from langgraph.graph import StateGraph, END

from src.graph.state import BankBotState
from src.graph.nodes import (
    intent_node,
    retrieval_node,
    transaction_node,
    compliance_node,
    transfer_node
)

def router(state: BankBotState):

    if state["intent"] == "retrieval":
        return "retrieval"

    if state["intent"] == "transaction":
        return "transaction"

    if state["intent"] == "compliance":
        return "compliance"
    if state["intent"] == "transfer":
        return "transfer"

    return END


builder = StateGraph(BankBotState)

builder.add_node("intent", intent_node)
builder.add_node("retrieval", retrieval_node)
builder.add_node("transaction", transaction_node)
builder.add_node("compliance",compliance_node)
builder.add_node("transfer", transfer_node)
builder.set_entry_point("intent")

builder.add_conditional_edges(
    "intent",
    router,
    {
        "retrieval": "retrieval",
        "transaction": "transaction",
        "compliance": "compliance",
        "transfer": "transfer",
        END: END,
    },
)

builder.add_edge("retrieval", END)
builder.add_edge("transaction", END)
builder.add_edge("compliance", END)
builder.add_edge("transfer", END)
graph = builder.compile()