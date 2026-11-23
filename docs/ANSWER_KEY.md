# Answer key: expected numbers

Use this to check your dashboard. Data covers **1–23 November 2026** (102 transactions).

## Current-month spending

| Metric | Expected |
|---|---|
| Total spent | S$977.90 |
| Monthly budget | S$1,100.00 |
| Budget remaining | S$122.10 |
| Transactions | 102 |
| Budget used | 88.9% (amber) |

## Spending by category

| Category | Spent | Budget | Status |
|---|---|---|---|
| Shopping | S$320.30 | S$200.00 | Over budget |
| Food & Drinks | S$319.39 | S$350.00 | Within budget |
| Transport | S$179.29 | S$180.00 | Within budget |
| Entertainment | S$43.08 | S$60.00 | Within budget |
| Education | S$42.50 | S$80.00 | Within budget |
| Subscriptions | S$34.94 | S$35.00 | Within budget |
| Uncategorized | S$23.40 | — | No budget set |
| Bills | S$15.00 | S$20.00 | Within budget |

Groceries (S$100) and Health (S$40) have budgets but no spending this month, so they may not appear in a chart built from the transactions. That's expected.

## Transactions that need review

**7 transactions**, largest first:

| Date | Merchant | Amount | Reason |
|---|---|---|---|
| 12 Nov | Apple.com/bill | S$128.00 | Amount >= S$50 |
| 21 Nov | Zalora | S$89.00 | Amount >= S$50 |
| 20 Nov | GrabFood | S$64.30 | Amount >= S$50 |
| 05 Nov | Uniqlo | S$59.31 | Amount >= S$50 |
| 14 Nov | SQ*UNKNOWN MERCHANT | S$23.40 | Uncategorized |
| 07 Nov | Netflix | S$11.98 | Possible duplicate |
| 18 Nov | Shopee | -S$24.90 | Refund to confirm |

## Model Showdown answers (Round 2)

| Question | Answer |
|---|---|
| 1. Total spent, including refunds | **S$977.90** |
| 2. Most over-budget category | **Shopping**, over by **S$120.30** (S$320.30 vs S$200.00) |
| 3. Budget used | **88.9%** of S$1,100 |

## Power-up: "Change the spec" (S$40 threshold)

Adding *"also highlight any transaction of S$40 or more"* adds **2** transactions to the review list, making **9** in total:

| Date | Merchant | Amount |
|---|---|---|
| 10 Nov | NUS Co-op | S$42.50 |
| 16 Nov | Shopee | S$42.65 |

## Common mistakes to look for
- **Refund left out:** if total spent shows S$1,002.80, the S$24.90 Shopee refund (a negative amount) was dropped.
- **Uncategorized dropped:** the S$23.40 unknown merchant must still count towards the total.
- **needs_review read as text:** filtering on `== True` without converting from "TRUE"/"FALSE" returns 0 rows.
- **Percentage wrong:** budget used must be total spent ÷ monthly_budget (S$1,100), not ÷ the sum of category budgets.
