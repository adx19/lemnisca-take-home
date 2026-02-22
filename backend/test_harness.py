from app.pipeline import Pipeline
from app.loading_chunks import load_and_chunk_docs
from app.embedding import Embedding
from app.build_index import indexing
from app.faiss_index import FaissIndex


chunks = load_and_chunk_docs()
embedder = Embedding()
embedded_chunks = embedder.embedding_chunks(chunks)
vectors = indexing(embedded_chunks)
faiss = FaissIndex(vectors.shape[1])
metadata = [
    {"text": c["text"], "doc_name": c["doc_name"]}
    for c in embedded_chunks
]
faiss.build(vectors, metadata)

pipeline = Pipeline(embedder, faiss)

tests = [

    {
        "name": "Dress Code Lookup",
        "query": "what is the dress code",
        "expected_keywords": ["casual", "comfortable"],
        "expected_confidence": "high"
    },

    {
        "name": "Reset Password Flow",
        "query": "how do i reset my password",
        "expected_keywords": ["forgot", "reset", "email"],
        "expected_confidence": "high"
    },

    {
        "name": "Out of Scope Weather",
        "query": "what is the weather today",
        "expected_keywords": ["cannot"],
        "expected_confidence": "low"
    },

    {
        "name": "Unknown Company Info",
        "query": "what is the company ceo salary",
        "expected_keywords": ["cannot"],
        "expected_confidence": "low"
    }

]

print("\nRunning evaluation tests...\n")

passed_tests = 0

for test in tests:
  print(f"Test: {test['name']}")
  print(f"Query: {test['query']}")
  
  result = pipeline.run(test['query'])
  
  answer = result["answer"].lower()
  confidence = result["confidence"].lower()

  keyword_match = any(keyword in answer for keyword in test["expected_keywords"])

  confidence_match = confidence == test["expected_confidence"]

  test_pass = keyword_match and confidence_match

  if test_pass:
      passed_tests += 1

  print(f"Expected confidence: {test['expected_confidence']}")
  print(f"Actual confidence: {confidence}")
  print(f"Keyword match: {'PASS' if keyword_match else 'FAIL'}")
  print(f"Confidence match: {'PASS' if confidence_match else 'FAIL'}")
  print(f"Result: {'PASS' if test_pass else 'FAIL'}")
  print("-" * 40)


print("\nEvaluation Summary")
print(f"Passed {passed_tests} out of {len(tests)} tests")

accuracy = (passed_tests / len(tests)) * 100
print(f"Accuracy: {accuracy:.2f}%")