import os
import time
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

client = Groq(api_key = os.getenv("GROQ_API_KEY"))

def call_llm(prompt, model_name):
  start_time = time.time()
  response = client.chat.completions.create(
    model = model_name,
    messages = [
      {"role" : "user", "content":prompt}
    ]
    
  )
  
  latency = (time.time() - start_time)*1000
  answer = response.choices[0].message.content
  usage = response.usage
  
  
  return{
    "answer" : answer,
    "tokens_input" : usage.prompt_tokens,
    "tokens_output" : usage.completion_tokens,
    "latency_ms" : round(latency, 2)
  }