import fitz
from pathlib import Path

def extracting_docs(file_name):
  try:
    doc = fitz.open(file_name)
    content = ""
    for page in doc:
      content += page.get_text()
    return{
      "file_name": Path(file_name).stem,
      "content": content
    }
  except Exception as e:
    print(f"Error reading {file_name}: {e}")
    return None