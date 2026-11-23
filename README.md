# 💰 Student Budget Dashboard: GitHub Copilot and Spec Kit Workshop (Demo 4)

A hands-on workshop where students build a budget dashboard while exploring **how to get the best out of GitHub Copilot**:

- 🪜 **Prompt Ladder:** ghost text, inline chat, vague vs specific prompts, and image input
- 🥊 **Model Showdown:** fast vs reasoning models and low vs high thinking effort, scored against an answer key
- 📐 **Spec-Driven Development** with [GitHub Spec Kit](https://github.com/github/spec-kit): constitution → spec → clarify → plan → tasks → implement
- ⚡ **Power-ups:** prompt files, sketch-to-UI, tests, AI code review and the Copilot coding agent

> All data in this repo is **synthetic**. It belongs to a fictional student ("Alex Tan") in Singapore, November 2026.

## 👉 Students: start here
1. **Use this template ▸ Create a new repository**
2. **Code ▸ Codespaces ▸ Create codespace on main**
3. Follow **[docs/WORKSHOP_GUIDE.md](docs/WORKSHOP_GUIDE.md)**

<details>
<summary>💻 Running on your own computer instead?</summary>

You need Python 3.11+, Git, VS Code with **GitHub Copilot** and **GitHub Copilot Chat**, and [uv](https://docs.astral.sh/uv/) or pipx.
```bash
git clone <your-repo-url> && cd student-budget-dashboard
python -m venv .venv
# Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
pipx install specify-cli        # or: uv tool install specify-cli
specify version
```
</details>

## 📁 What's in this repo
```
student-budget-dashboard/
├── data/
│   ├── transactions_nov2026.csv      ← 102 synthetic transactions (SGD)
│   ├── budget_nov2026.json           ← S$1,100 monthly budget plus category budgets
│   └── sample_reflection.md          ← sample AI-written monthly reflection
├── docs/
│   ├── WORKSHOP_GUIDE.md             ← 👈 the student guide
│   ├── ANSWER_KEY.md                 ← expected numbers for checking your work
│   ├── FACILITATOR_GUIDE.md          ← run sheet for the host
│   └── dashboard_wireframe.png       ← sketch used for image prompting
├── playground/warmup.py              ← Round 1 Prompt Ladder
├── fallback/app.py                   ← Plan B: TODO starter if Spec Kit isn't working
├── solution/app.py                   ← reference solution
├── .github/
│   ├── copilot-instructions.md       ← project context for Copilot
│   └── prompts/                      ← reusable prompt files: /check-numbers, /explain-simply
├── .devcontainer/                    ← Codespaces setup (installs Spec Kit too)
└── requirements.txt
```
After Round 3, your repo will also contain `.specify/` (Spec Kit setup), `specs/` (your spec, plan and tasks) and `app.py` (your dashboard).

## 🗂️ Data dictionary
| Column | Description |
|---|---|
| `transaction_id` | Unique ID, e.g. `TXN-0001` |
| `date` | `YYYY-MM-DD`, 1–23 Nov 2026 |
| `merchant` | Where the money was spent |
| `amount_sgd` | Amount in S$. **Negative = refund** |
| `category` | Food & Drinks, Transport, Shopping, Subscriptions, Education, Entertainment, Bills or Uncategorized |
| `payment_method` | EZ-Link, PayNow, Debit Card or Credit Card |
| `needs_review` | `TRUE` / `FALSE`, set by the earlier workflow |
| `review_reason` | Why it was flagged |
| `notes` | Free-text notes |

## 🔐 Real data
Use only the synthetic data in the workshop. Put any personal files in `data/private/` (git-ignored) and never commit real financial data.
