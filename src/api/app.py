from fastapi import FastAPI
from src.observability.callbacks import langfuse_handler
from src.api.schemas import ChatRequest
from src.graph.graph import graph

app = FastAPI(
    title="BankBot Pro",
    version="1.0.0",
    description="Enterprise Banking AI Assistant"
)


@app.get("/")
def home():

    return {
        "message": "BankBot Pro API is running."
    }


@app.post("/chat")
def chat(request: ChatRequest):

    result = graph.invoke(
    {
        "customer_id": request.customer_id,
        "query": request.query,
    },
    config={
        "callbacks": [langfuse_handler],
        "run_name": "bankbot-chat",
    },
)

    return result["response"]