# ClearPath Customer Support Assistant

A Retrieval-Augmented Generation (RAG) chatbot built for a fictional SaaS company called **ClearPath**.  
The assistant answers user questions by retrieving relevant content from internal documents and generating grounded responses using LLMs.

---

## Overview

This project implements a full RAG pipeline with:

- Document chunking and embedding
- Semantic search using FAISS
- Deterministic model routing
- LLM response generation via Groq
- Output evaluation with confidence scoring
- Caching for performance optimization
- Basic chat UI with debug panel
- Evaluation test harness

The system is designed to provide reliable, context-grounded answers while detecting potential hallucinations or low-confidence responses.

---

## Features Implemented

- RAG Pipeline
- Rule-based Model Router
- Output Evaluator
- Confidence Scoring
- Logging of model usage and latency
- Basic Chat UI
- Response Caching
- Evaluation Harness (test suite)

---

## Tech Stack

### Backend:
- Python
- FastAPI
- Sentence Transformers
- FAISS (IndexFlatL2)
- Groq API

### Frontend:
- HTML
- CSS
- Vanilla JavaScript

---

## Groq Models Used

- **llama-3.1-8b-instant** → Simple queries
- **llama-3.3-70b-versatile** → Complex queries

Environment variables are stored in a `.env` file.

---

## How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd <repo-folder>
```

### 2️⃣ Navigate to backend

```bash
cd backend
```

### 3️⃣ Create virtual environment

```bash
python -m venv venv
```

**Activate:**

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Create .env file inside backend

```
GROQ_API_KEY=your_api_key_here
```

### 6️⃣ Run backend server

```bash
uvicorn app.main:app --reload
```

Backend runs at:
```
http://localhost:8000
```

### 7️⃣ Run UI

Open `index.html` in browser.

---

## Architecture

### Chunking Strategy

- **Chunk size:** 500 characters
- **Overlap:** 100 characters

This size ensures each chunk captures meaningful context while overlap prevents information loss when sentences span chunk boundaries.

### Embedding + Retrieval

- Sentence Transformers used for embeddings
- FAISS IndexFlatL2 used for similarity search
- Top K = 5 retrieved chunks

### Model Router Logic

Query classification is deterministic using:

- Query length
- Presence of reasoning keywords
- Intent keywords
- Connector words
- Multi-question detection

**Routing Decision:**
- Simple queries → fast model
- Complex queries → more capable model

### Output Evaluator Design

The evaluator performs three checks:

#### 1️⃣ No Context
If no chunks are retrieved

#### 2️⃣ Refusal Detection
If model responds with phrases like "I cannot answer"

#### 3️⃣ Grounding Check (Domain Check)
Extracts keywords from the answer and compares against retrieved context.
If ≥30% keywords are missing → flagged as domain mismatch.

**Confidence levels:**
- High
- Medium
- Low

### Caching Strategy

An in-memory cache stores previous query results to:

- Reduce latency
- Reduce API usage
- Improve responsiveness

### Evaluation Harness

Custom test suite with expected outputs and confidence levels.

**Example tests include:**
- Dress code lookup
- Password reset flow
- Out-of-scope queries
- Unknown company info

System achieved **100% pass rate** on defined tests.

### UI Features

- Chat interface
- Debug panel showing:
  - Model used
  - Confidence
  - Latency
  - Evaluator status

---

## Bonus Challenges Attempted

- Evaluation Harness
- Response Caching

---

## Known Limitations

- Chunking may still miss edge-case context across documents
- No conversation memory implemented
- Cache is in-memory only (not persistent)
- UI is minimal
- Grounding check is heuristic-based

---

## If I Had More Time

- Implement conversation memory
- Deploy to cloud (AWS/GCP)
- Improve UI design
- Add persistent cache (Redis)
- Improve evaluator with semantic similarity scoring
- Implement streaming responses

---

## Project Structure

```
backend/
  app/
    llm/
    evaluator/
    pipeline.py
    main.py
  .env

frontend/
  index.html
  script.js
  styles.css
```

---

## Demo

Add screenshots here:
- Chat UI
- Debug panel
- Example queries

---

## Author

Built as part of a take-home assignment to demonstrate:

- RAG system design
- LLM integration
- Backend architecture
- Evaluation strategies