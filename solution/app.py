"""
Student Budget Dashboard: REFERENCE SOLUTION
===========================================
Run it from the repository root:   streamlit run solution/app.py
"""

import json
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
TRANSACTIONS_FILE = DATA_DIR / "transactions_nov2026.csv"
BUDGET_FILE = DATA_DIR / "budget_nov2026.json"
REFLECTION_FILE = DATA_DIR / "sample_reflection.md"


def money(value: float) -> str:
    """Format a number as Singapore dollars, e.g. S$1,234.56 (or -S$24.90)."""
    sign = "-" if value < 0 else ""
    return f"{sign}S${abs(value):,.2f}"


@st.cache_data
def load_transactions() -> pd.DataFrame:
    df = pd.read_csv(TRANSACTIONS_FILE, parse_dates=["date"])
    df["needs_review"] = df["needs_review"].astype(str).str.upper().eq("TRUE")
    df["review_reason"] = df["review_reason"].fillna("")
    df["notes"] = df["notes"].fillna("")
    return df


@st.cache_data
def load_budget() -> dict:
    return json.loads(BUDGET_FILE.read_text())


def progress_bar(percent: float) -> str:
    """Return HTML for a colour-coded progress bar."""
    if percent < 75:
        colour = "#2e7d32"   # green
    elif percent <= 100:
        colour = "#f9a825"   # amber
    else:
        colour = "#c62828"   # red
    width = min(percent, 100)
    return f"""
    <div style="background:#e0e0e0;border-radius:8px;height:28px;width:100%;">
      <div style="background:{colour};width:{width:.1f}%;height:28px;border-radius:8px;
                  color:white;font-weight:600;display:flex;align-items:center;
                  justify-content:flex-end;padding-right:10px;box-sizing:border-box;">
        {percent:.1f}%
      </div>
    </div>
    """


st.set_page_config(page_title="Student Budget Dashboard", page_icon="💰", layout="wide")

transactions = load_transactions()
budget = load_budget()
monthly_budget = float(budget["monthly_budget"])
category_budgets = budget["category_budgets"]

st.title("💰 Student Budget Dashboard")
st.caption(f"{budget['student']} · {budget['month']} · synthetic data")

# Sidebar filter (an extra: lets students explore a date range)
min_date, max_date = transactions["date"].min().date(), transactions["date"].max().date()
start, end = st.sidebar.date_input("Date range", (min_date, max_date),
                                   min_value=min_date, max_value=max_date)
if isinstance(start, type(min_date)) and isinstance(end, type(min_date)):
    mask = transactions["date"].dt.date.between(start, end)
    view = transactions[mask]
else:
    view = transactions

# 1. Current-month spending
st.header("1. Current-month spending")
total_spent = view["amount_sgd"].sum()
remaining = monthly_budget - total_spent
c1, c2, c3 = st.columns(3)
c1.metric("Total spent", money(total_spent))
c2.metric("Budget remaining", money(remaining))
c3.metric("Transactions", f"{len(view)}")

# 2. Budget progress
st.header("2. Budget progress")
percent_used = total_spent / monthly_budget * 100
st.markdown(progress_bar(percent_used), unsafe_allow_html=True)
st.caption(f"{money(total_spent)} of {money(monthly_budget)} monthly budget")

# 3. Spending by category
st.header("3. Spending by category")
by_category = (view.groupby("category", as_index=False)["amount_sgd"].sum()
               .rename(columns={"amount_sgd": "spent"}))
by_category["budget"] = by_category["category"].map(category_budgets).fillna(0)
by_category["difference"] = by_category["budget"] - by_category["spent"]
by_category["status"] = by_category.apply(
    lambda r: "No budget set" if r["budget"] == 0
    else ("Over budget" if r["spent"] > r["budget"] else "Within budget"), axis=1)
by_category = by_category.sort_values("spent", ascending=True)

left, right = st.columns([3, 2])
with left:
    fig = px.bar(by_category, x="spent", y="category", orientation="h", color="status",
                 color_discrete_map={"Over budget": "#c62828", "Within budget": "#2e7d32",
                                     "No budget set": "#757575"},
                 labels={"spent": "Spent (S$)", "category": ""})
    fig.update_layout(height=380, margin=dict(l=0, r=0, t=10, b=0), legend_title_text="")
    st.plotly_chart(fig, use_container_width=True)
with right:
    table = by_category.sort_values("spent", ascending=False).copy()
    for col in ["spent", "budget", "difference"]:
        table[col] = table[col].map(money)
    st.dataframe(table, hide_index=True, use_container_width=True)

# 4. Transactions that need review
st.header("4. Transactions that need review")
flagged = view[view["needs_review"]].sort_values("amount_sgd", ascending=False)
st.write(f"**{len(flagged)}** transaction(s) need a second look.")
st.dataframe(
    flagged[["date", "merchant", "amount_sgd", "category", "review_reason", "notes"]]
    .assign(date=lambda d: d["date"].dt.strftime("%d %b"),
            amount_sgd=lambda d: d["amount_sgd"].map(money)),
    hide_index=True, use_container_width=True)

# 5. Monthly reflection
st.header("5. Monthly reflection")
with st.expander("Monthly reflection (AI-generated)", expanded=True):
    if REFLECTION_FILE.exists():
        st.markdown(REFLECTION_FILE.read_text())
    else:
        st.warning("No reflection found. Run the Demo 3 workflow or add data/sample_reflection.md.")
