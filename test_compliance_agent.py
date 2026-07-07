from src.agents.compliance_agent import ComplianceAgent

agent = ComplianceAgent()

tests = [

    {
        "balance":300000,
        "amount":50000,
        "type":"UPI"
    },

    {
        "balance":300000,
        "amount":150000,
        "type":"UPI"
    },

    {
        "balance":300000,
        "amount":150000,
        "type":"RTGS"
    },

    {
        "balance":300000,
        "amount":250000,
        "type":"RTGS"
    },

    {
        "balance":50000,
        "amount":49050,
        "type":"NEFT"
    },

    {
        "balance":50000,
        "amount":10000,
        "type":"NEFT",
        "kyc_verified":False
    }

]

for test in tests:

    result = agent.check_transfer(

        balance=test["balance"],
        amount=test["amount"],
        transaction_type=test["type"],
        kyc_verified=test.get("kyc_verified", True)

    )

    print("="*60)

    print(test)

    print(result)