from app.loading_chunks import load_and_chunk_docs
from app.embedding import Embedding
from app.build_index import indexing
from app.pipeline import Pipeline
from fastapi import FastAPI
from app.faiss_index import FaissIndex
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for local dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
print("Starting application...")
embedder = Embedding()


print("\n[1/4] Loading and chunking documents...")
chunks = load_and_chunk_docs()

print("\n[2/4] Embedding chunks...")
embedded_chunks = embedder.embedding_chunks(chunks)

print("\n[3/4] Preparing vectors...")
vectors = indexing(embedded_chunks)

print("\n[4/4] Building Faiss index...")
faiss = FaissIndex(vectors.shape[1])


metadata = [
    {"text": c["text"], "doc_name": c["doc_name"]}
    for c in embedded_chunks
]

faiss.build(vectors, metadata)

pipeline = Pipeline(embedder, faiss)


print("\nApplication is ready to accept queries")

@app.get("/")
def home():
  return {"message": "Welcome to the ClearPath customer support assistant API. Use the /query endpoint to ask questions."}


@app.get("/status")
def status():
    return {
        "total_chunks": len(chunks),
        "embedding_dim": list(vectors.shape)
    }
    
@app.get("/query")
def search(query: str):
  result = pipeline.run(query)
  
  return result