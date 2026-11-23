"""
Student Budget Dashboard: STARTER FILE
=====================================
Run it:   streamlit run app.py

Work through the TODOs in order. Each one has a suggested GitHub Copilot Chat
prompt. Ask Copilot, read what it writes, then run the app and check the result
against docs/ANSWER_KEY.md.
"""

import json
from pathlib import Path

import pandas as pd
import streamlit as st

DATA_DIR = Path(__file__).parent / "data"
TRANSACTIONS_FILE = DATA_DIR / "transactions_nov2026.csv"
BUDGET_FILE = DATA_DIR / "budget_nov2026.json"
REFLECTION_FILE = DATA_DIR / "sample_reflection.md"

st.set_page_config(page_title="Student Budget Dashboard", page_icon="💰", layout="wide")
st.title("💰 Student Budget Dashboard")
st.caption("November 2026 · synthetic data for a fictional student")


# ---------------------------------------------------------------------------
# TODO 1: Load the data
# Copilot prompt:
#   "Write a function load_transactions() that reads TRANSACTIONS_FILE with pandas,
#    parses the date column, and converts needs_review from 'TRUE'/'FALSE' to a boolean.
#    Also write load_budget() that reads BUDGET_FILE as JSON. Cache both with st.cache_data."
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# TODO 2: Current-month spending
# Copilot prompt:
#   "Show three st.metric cards side by side: total spent, budget remaining and
#    number of transactions. Format money as S$ with two decimals."
# ---------------------------------------------------------------------------
st.header("1. Current-month spending")
st.info("TODO 2: show total spent, budget remaining and number of transactions here.")


# ---------------------------------------------------------------------------
# TODO 3: Monthly budget progress indicator
# Copilot prompt:
#   "Add a progress bar showing total spent as a percentage of monthly_budget.
#    Make it green below 75%, amber from 75% to 100% and red above 100%."
# ---------------------------------------------------------------------------
st.header("2. Budget progress")
st.info("TODO 3: show a colour-coded budget progress bar here.")


# ---------------------------------------------------------------------------
# TODO 4: Spending by category
# Copilot prompt:
#   "Group spending by category and show a horizontal bar chart with plotly.
#    Also show a table comparing each category with its budget in category_budgets,
#    and highlight the categories that are over budget."
# ---------------------------------------------------------------------------
st.header("3. Spending by category")
st.info("TODO 4: show a category chart and a budget-vs-actual table here.")


# ---------------------------------------------------------------------------
# TODO 5: Transactions that need review
# Copilot prompt:
#   "Show a table of transactions where needs_review is True with date, merchant,
#    amount_sgd, category and review_reason, sorted by amount (largest first)."
# ---------------------------------------------------------------------------
st.header("4. Transactions that need review")
st.info("TODO 5: show the flagged transactions here.")


# ---------------------------------------------------------------------------
# TODO 6: AI-generated monthly reflection
# Copilot prompt:
#   "Read REFLECTION_FILE and show it inside an st.expander called
#    'Monthly reflection (AI-generated)', expanded by default."
# ---------------------------------------------------------------------------
st.header("5. Monthly reflection")
st.info("TODO 6: show the AI-generated monthly reflection here.")
