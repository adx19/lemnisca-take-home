# Written Answers

## Q1 — Routing Logic

### Rules Used
Rules that I used in the routing is:
- First we classify the query that contains words of reasoning like why, how , explain etc as complex.
- Second we check for intent in the query. Inent is decided by some common key words like "not working", "error", "troubleshoot" etc. These queries are classified as complex.
- Third we check for connecting words such as "and", "or", "also" etc. If these exist we classify the corresponding queries as complex
- Fourth we check if the query contains multiple '?'. If more than one '?' is there in the query we classify it as complex
- Finally we check for word count. If the number of words is more than or equal to 15 we classify it as complex. 
- Every other query which doesn't not follow any of the condition above is classified as simple.
### Why This Boundary
- The reasoning word boundary is used because reasoning requires a bit more explained solution than grounded so we should classify it as complex.
- The intent word boundary is used because most of the troubleshooting or not working queries require a set of instruction to fix it.
- As for connecting words, we keep this boundary because this indicate there are more than 1 question in the given query. Since it contains multiple question we classify it as complex.
- The '?' boundary has the same reason as connecting words. In this some of the queries may not be using connector words but rather they ask 2 question at a time by seperating them using a '?'.
- And we kept the word count at 15 because for a grounded question word count , in most cases, is at max 12. We choose 15 as a fail safe because people can eloborate simple question.

### Misclassification Example
- One example of misclassification would be a query like "can you tell me the password requirements".Even though this is a simple lookup question, it may get classified as complex because of the word "can".This happens because the router relies on keyword detection instead of better intent understanding.

### Improvement Without LLM
- If I had to improve the router without using an LLM, I would add better keyword grouping and maybe a scoring system instead of binary checks.For example, instead of marking a query complex if it contains just one reasoning keyword, I would require multiple signals.Another improvement would be to normalize queries better before classification to reduce false positives.


---

## Q2 — Retrieval Failures

### Failure Case
One realistic failure case would be the query "what is the formal dress code".  

### What Was Retrieved
The system retrieved chunks related to dress code from the employee handbook, but the context only mentions that the company maintains a casual dress code and does not mention anything about formal dress code.

### Why It Failed
The retrieval did not technically fail, but the query used wording that does not exactly match the documents. Since embeddings are semantic, it still retrieved the closest chunk, but the user intent was slightly different. This shows a limitation where the system cannot distinguish between absence of information and closest semantic match.

### Fix
A possible fix would be to add a stricter evaluator grounding check that detects when the answer is only partially supported by context. Another improvement would be to add a semantic similarity threshold so that if similarity is too low, the system treats it as no context instead of returning closest match.


---

## Q3 — Cost and Scale

If the system handles 5,000 queries per day, we can estimate token usage based on average numbers observed during testing.Simple queries using llama-3.1-8b-instant used around 600 input tokens and 30 output tokens on average.Complex queries using llama-3.3-70b-versatile used around 680 input tokens and 80 output tokens.  

Assuming around 70% queries are simple and 30% are complex: 
Simple queries per day = 3,500  
Total tokens ≈ 3,500 × 630 ≈ 2.2 million tokens  

Complex queries per day = 1,500  
Total tokens ≈ 1,500 × 760 ≈ 1.14 million tokens  

Total daily tokens ≈ 3.34 million tokens  

The biggest cost driver is prompt size because retrieved context adds a large number of tokens to every request.  

The single highest ROI change would be reducing the number of retrieved chunks or summarizing chunks before sending them to the LLM. This would significantly reduce input tokens without hurting answer quality.  

One optimisation I would avoid is aggressive caching of all queries because user queries can vary slightly in wording and stale cache could reduce accuracy.


---

## Q4 — What Is Broken

### Biggest Limitation
The biggest limitation of the system is that the evaluator grounding check is keyword based and not semantic. This means it may incorrectly mark some grounded answers as medium confidence or miss subtle hallucinations.  

### Why I Shipped With It
I shipped with this approach because it satisfies the assignment requirement of a deterministic evaluator and works reliably for most queries. Implementing a semantic grounding check would require additional embedding comparisons which would increase complexity and time.

### Fix With More Time
With more time, I would implement semantic grounding by embedding both the answer and retrieved chunks and measuring similarity. This would provide a more reliable hallucination detection mechanism and improve confidence scoring accuracy.


---

## AI Usage

AI was used as a development assistant for architectural guidance, debugging, and design validation. Below are representative prompts used during development.

## Architecture and Retrieval

- How do I implement embedding and indexing of document chunks in Python without using RAG libraries like LangChain?
- Now that I have embeddings, how should I set up FAISS and structure the index?
- Should embeddings and indexes be loaded at application startup to avoid recomputation?

## Prompt and Pipeline Design

- After retrieving chunks, how should I structure the prompt so the model only answers using context?
- Should I build a pipeline abstraction now or after everything is working?

## Router Logic

- What is a logical rule-based approach to classify queries as simple vs complex without using an LLM?

## Evaluator Design

- What decisions should be made before designing an output evaluator?
- What does a grounded answer mean and how can we detect hallucinations?

## Testing and Improvements

- How should I design test cases to validate my evaluator and overall pipeline?
- Can caching improve performance and where should it be implemented?