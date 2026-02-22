class Evaluator:
  def __init__(self, query, retrieved_chunks, llm_answer):
    #Arguments used to evaluate the response
    self.query = query
    self.retrieved_chunks = retrieved_chunks
    self.llm_answer = llm_answer
    
    #Evaluation result variables
    self.flags = []
    self.confidence = "high"
    
    #Refusal indicators
    self.REFUSAL_INDICATORS = ["i cannot", "i can't", "unable to", "not enough information","i do not know", "i don't know"]
    
  def evaluate(self):
    context_text = ""
    answer_lower = self.llm_answer.lower()
    words = answer_lower.split()
    
    keywords = []
    
    for word in words:
      if len(word) > 3:
        keywords.append(word)
    
    for i in range(len(self.retrieved_chunks)):
      context_text += self.retrieved_chunks[i]['text']
    
    
    if len(self.retrieved_chunks) == 0 or self.llm_answer.lower().startswith("i cannot answer"):
      self.flags.append("no_context")
    
    elif any(indicator in self.llm_answer.lower() for indicator in self.REFUSAL_INDICATORS):
      self.flags.append("refusal")
    
    elif keywords:
      count = sum(1 for word in keywords if word not in context_text.lower())
      if count/len(keywords) >= 0.3:
        self.flags.append("domain_mismatch")
    
    if "no_context" in self.flags or "refusal" in self.flags:
      self.confidence = "low"
    elif "domain_mismatch" in self.flags:
      self.confidence = "medium"
    else:
      self.confidence = "high"
    
    return {
      "confidence" : self.confidence,
      "flags" : self.flags
    }