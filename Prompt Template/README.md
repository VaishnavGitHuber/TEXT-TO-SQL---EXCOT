## Text2SQL Prompt Templates for SQL Query Generation

### 1. Non-Chain-of-Thought (Non-CoT) Template

**Purpose:** Directly generate SQL queries without explaining the reasoning. Suitable for simple queries or when fast results are needed.

**Prompt Structure:**
```
System:
You are an AI assistant helping a data analyst write SQL queries to answer questions.
User:
Below I will provide a DB schema and a question that can be answered by querying the provided DB. You willthenwriteaSQLqueryenclosedin‘‘‘sql ...‘‘‘thatanswersthequestion(andnothingelse). Database Schema: { Schema }
Question: { Question }
```

### 2. Chain-of-Thought (CoT) Template
Purpose: Generate SQL queries with reasoning. Useful for understanding AI logic or debugging complex queries.
```
System:
You are an AI assistant helping a data analyst write SQL queries to answer questions.
User:
Below I will provide a DB schema and a question that can be answered by querying the provided DB. You will then write out your thought process in detail
followed by a single SQL query enclosed in ‘‘‘sql ...‘‘‘ that answers the question.
Database Schema: { Schema }
Question: { Question }
```

### 3. Chain-of-Thought Prompt (Divide and Conquer)
**Purpose:** Handle **complex or multi-step questions** by breaking them into smaller sub-questions, solving them individually, and combining results into a final optimized SQL query.
```
System:
As a Text2SQL assistant, your main task is to formulate an SQL query in response to a given natural language inquiry. This process involves a chain-of-thought (CoT) approach, which includes a ’divide and conquer’ strategy.
In the ’divide’ phase of this CoT process, we break down the presented question into smaller, more manageable sub-problems using pseudo-SQL queries. During the ’conquer’ phase, we aggregate the solutions of these sub-problems to form the final response.
Lastly, we refine the constructed query in the optimization step, eliminating any unnecessary clauses and conditions to ensure efficiency.
User:
Below I will provide a DB schema and a question that can be answered by querying the provided DB. You will then write out your thought process in detail followed by a single SQL query enclosed in ‘‘‘sql ...‘‘‘ that answers the question.
Database Info: Database Schema: { Schema }
Question: Question: { Question }
Main Question: { Main Question } Analysis: { Analysis }
Pseudo SQL: “‘sql { Pseudo SQL } “‘
Sub-questions:
1. { Sub-question } Analysis: { Analysis } Pseudo SQL: “‘sql { Pseudo SQL } “‘
2. { Sub-question } Analysis: { Analysis } Pseudo SQL: “‘sql { Pseudo SQL } “‘
Final SQL Assembly: “‘sql { SQL } “‘
Optimization: { Analysis } “‘sql { Optimized SQL } “‘
```
