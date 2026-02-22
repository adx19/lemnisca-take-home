import faiss
import numpy as np

class FaissIndex:
  def __init__(self, dimension: int):
    self.dimension = dimension
    self.index = faiss.IndexFlatL2(dimension)
    self.metadata = []
  
  def build(self, embeddings: np.ndarray, metadata: list):
    
    self.index.add(embeddings)
    self.metadata = metadata
  
  def search(self, query_vector: np.ndarray, top_k: int = 3):
    query_vector = np.array([query_vector]).astype('float32')
    distances, indices = self.index.search(query_vector, top_k)
    
    result = []
    for idx in indices[0]:
      result.append(self.metadata[idx])
    return result