from pydantic import BaseModel


class ChatRequest(BaseModel):
    customer_id: int
    query: str


class ChatResponse(BaseModel):
    status: str
    response: str
    sources: list[str]