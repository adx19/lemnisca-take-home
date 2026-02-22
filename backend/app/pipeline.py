from app.llm.router import classify_query
from app.llm.prompt import prompt_builder
from app.llm.llm_call import call_llm
from app.evaluator.evaluator import Evaluator


class Pipeline:
  def __init__(self, embedder, faiss_index):
    self.embedder = embedder
    self.faiss_index = faiss_index
    self.cache = {}
  def run(self, query):
    if query in self.cache:
      print(f"[CACHE HIT] {query}")
      return self.cache[query]
    route = classify_query(query)
    query_vector = self.embedder.model.encode(query)
    retrieved_chunks = self.faiss_index.search(query_vector, top_k=5)
    prompt = prompt_builder(query, retrieved_chunks)
    llm_result = call_llm(prompt, route["model"])
    
    evaluation = Evaluator(query, retrieved_chunks, llm_result["answer"]).evaluate()
    final_result = {
    "query" : query,
    "classification" : route["type"],
    "model_used" : route["model"],
    "reason" : route["reason"],
    "answer" : llm_result["answer"],
    "tokens_input" : llm_result["tokens_input"],
    "tokens_output" : llm_result["tokens_output"],
    "latency_ms" : llm_result["latency_ms"],
    "confidence": evaluation["confidence"],
    "flags": evaluation["flags"]  
    }
    
    self.cache[query] = final_result
    return final_result
    