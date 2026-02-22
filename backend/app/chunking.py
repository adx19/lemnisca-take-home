
def chunking_function(text, chunk_size, overlap, doc_name):
  step = chunk_size - overlap
  chunks = []
  for i in range(0, len(text), step):
    chunk = text[i:i + chunk_size]
    chunks.append({
    "text": chunk,
    "doc_name": doc_name
  } )
  return chunks



