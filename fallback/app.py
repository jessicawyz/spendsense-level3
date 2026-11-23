"""
Student Budget Dashboard: PLAN B STARTER FILE
=============================================
Use this only if Spec Kit isn't working for you.
Run it from the repo root:   streamlit run fallback/app.py

Work through the TODOs in order. Each one has a suggested GitHub Copilot Chat
prompt. Ask Copilot, read what it writes, then run the app and check the result
against docs/ANSWER_KEY.md.
"""

import json
from pathlib import Path

import pandas as pd
import streamlit as st

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
TRANSACTIONS_FILE = DATA_DIR / "transactions_nov2026.csv"
BUDGET_FILE = DATA_DIR / "budget_nov2026.json"
REFLECTION_FILE = DATA_DIR / "sample_reflection.md"

st.set_page_config(page_title="Student Budget Dashboard", page_icon="💰", layout="wide")
st.title("💰 Student Budget Dashboard")
st.caption("November 2026 · synthetic data for a fictional student")

# TODO 1: Load the data
#   "Write load_transactions() that reads TRANSACTIONS_FILE with pandas, parses the date
#    column and converts needs_review from 'TRUE'/'FALSE' to a boolean. Write load_budget()
#    that reads BUDGET_FILE as JSON. Cache both with st.cache_data and call them."

st.header("1. Current-month spending")
# TODO 2: "Show three st.metric cards: total spent (refunds included), budget remaining
#          and number of transactions. Format money as S$1,234.56."
st.info("TODO 2: total spent, budget remaining and number of transactions.")

st.header("2. Budget progress")
# TODO 3: "Add a progress bar of total spent as % of monthly_budget: green below 75%,
#          amber 75-100%, red above 100%. Use st.markdown with HTML so it can change colour."
st.info("TODO 3: colour-coded budget progress bar.")

st.header("3. Spending by category")
# TODO 4: "Show a horizontal plotly bar chart of spending by category and a table comparing
#          each category with category_budgets (spent, budget, difference, status)."
st.info("TODO 4: category chart and budget-vs-actual table.")

st.header("4. Transactions that need review")
# TODO 5: "Show transactions where needs_review is True (date, merchant, amount, category,
#          review_reason), largest amount first, with a count above the table."
st.info("TODO 5: flagged transactions.")

st.header("5. Monthly reflection")
# TODO 6: "Show REFLECTION_FILE as markdown inside an st.expander titled
#          'Monthly reflection (AI-generated)', expanded by default."
st.info("TODO 6: AI-generated monthly reflection.")
