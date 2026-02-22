from pathlib import Path
from app.extracting_pdf import extracting_docs
from app.chunking import chunking_function
from tqdm import tqdm

def load_and_chunk_docs(folder="../docs"):
  folder_path = Path(folder)
  all_chunk = []
  extracted = {}
  
  for file_path in tqdm(folder_path.iterdir(), desc="Processing files"):
    if file_path.suffix.lower() == ".pdf":
      print(f"Processing {file_path.stem}...")
      extracted = extracting_docs(file_path)
      if extracted:
        chunks = chunking_function(
          extracted['content'],
          chunk_size = 500,
          overlap = 100,
          doc_name = file_path.stem
        )
        all_chunk.extend(chunks)
  return all_chunk