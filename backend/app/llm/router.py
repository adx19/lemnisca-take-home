REASONING_KEYWORDS = ["why", "how", "explain", "compare", "reason", "steps", "process" ]

INTENT_MARKERS = ["issue", "problem", "error", "not working","cannot", "help", "fail", "troubleshoot"]

CONNECTING_MARKERS = [" and ", " or ", " but ", " also ", " furthermore ", " moreover "]
def classify_query(query):
  multiple_questions_check = query.count("?")>1
  word_count = len(query.lower().split())
  reasoning_check = any(word in query.lower() for word in REASONING_KEYWORDS)
  intent_check = any(word in query.lower() for word in INTENT_MARKERS)
  connector_check = any(word in query.lower() for word in CONNECTING_MARKERS)
  
  if reasoning_check:
    return {
      "type" : "complex",
      "model" : "llama-3.3-70b-versatile",
      "reason" : "Reasoning keywords detected"      
    }
  
  if intent_check:
    return {
      "type" : "complex",
      "model" : "llama-3.3-70b-versatile",
      "reason" : "Intent keywords detected"      
    }
  
  if connector_check:
    return {
      "type" : "complex",
      "model" : "llama-3.3-70b-versatile",
      "reason" : "Connector keywords detected"      
    }
    
  if multiple_questions_check:
    return {
      "type" : "complex",
      "model" : "llama-3.3-70b-versatile",
      "reason" : "Multiple questions detected"      
    }
  if word_count >=15:
    return {
      "type" : "complex",
      "model" : "llama-3.3-70b-versatile",
      "reason" : "Long query"
    }
  
  else:
      return {
        "type" : "simple",
        "model" : "llama-3.1-8b-instant",
        "reason" : "Short query without complexity keywords detected"
      }
  
  
