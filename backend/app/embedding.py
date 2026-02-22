from sentence_transformers import SentenceTransformer
from tqdm import tqdm
class Embedding:
  def __init__(self, model_name= "all-MiniLm-L6-v2"):
    self.model = SentenceTransformer(model_name)
  
  def embedding_chunks(self, chunks):
    text = [chunk['text'] for chunk in chunks]
    embedding = self.model.encode(text, show_progress_bar=True)
    
    for chunk, emb in zip(chunks, embedding):
      chunk["embedding"] = emb
    
    return chunks
    