
import numpy as np
from tqdm import tqdm
# Indexing the embedded chunks

def indexing(chunks):
  vectors = np.array([chunk['embedding'] for chunk in chunks]).astype('float32')
  print("Vectors ready")
  return vectors
