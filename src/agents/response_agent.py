from pydantic import BaseModel


class FinalResponse(BaseModel):
    status: str
    response: str
    sources: list[str]


class ResponseAgent:

    def build_response(
        self,
        response: str,
        sources: list[str] | None = None,
    ):

        return FinalResponse(
            status="success",
            response=response,
            sources=sources or [],
        )