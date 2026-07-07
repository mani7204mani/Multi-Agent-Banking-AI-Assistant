# 🏦 Multi-Agent Banking AI Assistant

An intelligent **Multi-Agent Banking Assistant** built using **LangGraph, LangChain, FastAPI, ChromaDB, SQLite, and LLMs**. The system uses specialized AI agents to perform banking operations such as fund transfers, transaction history, compliance checks, document retrieval, and question answering through a coordinated agent workflow.

---

# 🚀 Features

- 🤖 Multi-Agent Architecture using LangGraph
- 💳 Bank Account & Transaction Management
- 💸 Money Transfer Agent
- 📜 Transaction History Agent
- ⚖️ Compliance & Rule Validation Agent
- 📄 RAG-based Document Question Answering
- 🧠 LLM-powered Intent Detection
- 🗂 SQLite Database Integration
- 🔍 ChromaDB Vector Database
- 🌐 FastAPI REST API
- 📊 Modular and Scalable Architecture
- 🐳 Docker Support

---

# 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| LLM Framework | LangChain |
| Multi-Agent | LangGraph |
| API | FastAPI |
| Vector Database | ChromaDB |
| Database | SQLite |
| Embeddings | HuggingFace |
| Model | Groq / OpenAI Compatible LLM |
| Containerization | Docker |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```
LangGraph-Project/
│
├── src/
│   ├── agents/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── graph/
│   ├── mcp/
│   ├── observability/
│   ├── rag/
│   ├── rules/
│   ├── services/
│   ├── tools/
│   └── utils/
│
├── documents/
├── chroma_db/
├── database/
├── logs/
├── Dockerfile
├── requirements.txt
├── README.md
└── .env
```

---

# 🤖 AI Agents

The project consists of multiple specialized agents.

### 🔹 Intent Agent

- Detects user intent
- Routes request to appropriate agent

---

### 🔹 Transaction Agent

- Retrieves transaction history
- Performs balance lookup
- Account information

---

### 🔹 Transfer Agent

- Validates beneficiary
- Performs fund transfer
- Updates account balance

---

### 🔹 Retrieval Agent

- Retrieves relevant banking documents
- Uses RAG pipeline
- Generates context-aware answers

---

### 🔹 Compliance Agent

- Validates banking policies
- Checks regulatory constraints
- Prevents invalid operations

---

### 🔹 Response Agent

- Collects outputs from all agents
- Generates final natural language response

---

# 🔄 Workflow

```
User Query
     │
     ▼
Intent Detection Agent
     │
     ▼
LangGraph Router
     │
 ┌───┼───────────────┐
 │   │               │
 ▼   ▼               ▼
Transfer      Retrieval     Compliance
 Agent          Agent          Agent
 │               │              │
 └───────┬───────┘
         ▼
 Response Agent
         ▼
      FastAPI
```

---

# 🧠 RAG Pipeline

1. Load Banking Documents
2. Chunk Documents
3. Generate Embeddings
4. Store Embeddings in ChromaDB
5. Retrieve Relevant Chunks
6. Generate LLM Response

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Multi-Agent-Banking-AI-Assistant.git

cd Multi-Agent-Banking-AI-Assistant
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ⚙ Environment Variables

Create a `.env` file.

Example

```env
OPENAI_API_KEY=xxxxxxxx

GROQ_API_KEY=xxxxxxxx

LANGSMITH_API_KEY=xxxxxxxx

LANGFUSE_PUBLIC_KEY=xxxxxxxx

LANGFUSE_SECRET_KEY=xxxxxxxx

DATABASE_URL=sqlite:///bank.db
```

---

# ▶ Run the Project

```bash
python src/database/seed.py
```

```bash
python src/rag/ingest.py
```

```bash
uvicorn src.api.app:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

# 🐳 Docker

Build

```bash
docker build -t banking-ai .
```

Run

```bash
docker run -p 8000:8000 banking-ai
```

---

# 📡 API Endpoints

## Health Check

```
GET /health
```

---

## Banking Chat

```
POST /chat
```

---

## Transfer Money

```
POST /transfer
```

---

## Transaction History

```
GET /transactions
```

---

## Document QA

```
POST /rag/query
```

---

# 📈 Future Improvements

- Voice Banking Assistant
- OTP Authentication
- Redis Caching
- Kubernetes Deployment
- CI/CD Pipeline
- Monitoring with Prometheus & Grafana
- Multi-language Support
- Agent Memory
- Human-in-the-loop Approval
- Streaming Responses

---

# 📸 Screenshots

<img width="940" height="550" alt="image" src="https://github.com/user-attachments/assets/5c411638-fb75-4622-9e68-ef2e8b4737ba" />
<img width="940" height="535" alt="image" src="https://github.com/user-attachments/assets/757dd37c-9b96-4a8d-b531-134a22ab47d7" />
<img width="1917" height="937" alt="image" src="https://github.com/user-attachments/assets/35cda9b8-99fd-4c91-a94d-4f986dd5ddba" />
<img width="1917" height="955" alt="image" src="https://github.com/user-attachments/assets/f64b9e99-538c-4633-8a04-6b022d5fb70a" />


---

# 👨‍💻 Author

**Mani Shankar Reddy**

GitHub: https://github.com/mani7204mani

LinkedIn: https://www.linkedin.com/in/mani7204/

---

# ⭐ If you found this project useful, consider giving it a Star.
