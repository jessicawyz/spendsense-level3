---
description: Check the dashboard's numbers against the workshop answer key
agent: agent
---
You are checking a student's budget dashboard for correctness.

1. Read the app code (app.py at the repo root, or the file the student has open).
2. Read docs/ANSWER_KEY.md.
3. Write and run a short Python snippet that loads data/transactions_nov2026.csv and
   data/budget_nov2026.json and calculates the same figures the app shows:
   total spent, budget remaining, % of budget used, spending per category,
   and the number of transactions that need review.
4. Show a table: Metric | App's logic gives | Answer key | Match? (✅/❌)
5. For any ❌, explain the likely cause in one sentence (for example a refund left out,
   or needs_review compared as text) and suggest the smallest fix. Do not change any
   files unless the student asks.
