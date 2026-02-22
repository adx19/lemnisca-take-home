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
-

### Improvement Without LLM
-


---

## Q2 — Retrieval Failures

### Failure Case
(write)

### What Was Retrieved
(write)

### Why It Failed
(write)

### Fix
(write)


---

## Q3 — Cost and Scale

(write full answer)


---

## Q4 — What Is Broken

### Biggest Limitation
(write)

### Why I Shipped With It
(write)

### Fix With More Time
(write)


---

## AI Usage

Below are the exact prompts used while building and debugging the system.