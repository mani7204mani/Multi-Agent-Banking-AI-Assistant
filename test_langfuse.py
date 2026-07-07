from src.observability.langfuse_client import langfuse

trace = langfuse.trace(
    name="bankbot-test"
)

trace.event(
    name="startup",
    input={"message": "BankBot started"},
    output={"status": "success"},
)

langfuse.flush()

print("LangFuse connected successfully.")