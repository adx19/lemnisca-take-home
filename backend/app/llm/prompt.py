def prompt_builder(query, context):
  context_text = "\n\n".join(chunk["text"] for chunk in context)
  prompt = f"""
  You are a customer support assistant for ClearPath.

  You MUST answer the question ONLY using the information provided in the CONTEXT below.

  DO NOT use any outside knowledge.
  DO NOT make assumptions.
  DO NOT generate generic responses.

  If the answer is not explicitly found in the context, respond exactly with:
  "I cannot answer the question based on the provided context."
  Context: {context_text}
  Question: {query}
  Answer:
  """
  
  return prompt.strip()