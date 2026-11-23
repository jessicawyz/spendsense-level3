# Copilot instructions for this repository

This is a beginner workshop project: a Streamlit dashboard for a student's monthly spending,
built with Spec-Driven Development (GitHub Spec Kit).

- Use Python 3.11, Streamlit, pandas and plotly only. Do not add other dependencies unless asked.
- The app lives in `app.py` at the repo root. Keep it in one file, simple and well commented.
- When a spec, plan or tasks file exists under `specs/`, follow it. If code and spec disagree, ask.
- Data lives in `data/`: `transactions_nov2026.csv`, `budget_nov2026.json` and `sample_reflection.md`.
  Never modify the data files.
- Amounts are in Singapore dollars (SGD). Format money as `S$1,234.56` and refunds as `-S$24.90`.
- Negative amounts are refunds and must be included in totals.
- `needs_review` is the text "TRUE" or "FALSE" in the CSV; convert it to a boolean.
- `solution/` and `fallback/` are reference files for the facilitator. Don't edit or copy from them
  unless the student asks.
