# 🛠️ Workshop guide: Build a budget dashboard with GitHub Copilot

**Demo 4 · Hands-on session · about 60 minutes**

Welcome! In this session you'll use **GitHub Copilot** to turn a month of spending data into a working web app. You don't need to be an expert programmer. Copilot writes most of the code, and **your job is to guide it, read what it writes and check that the results are right.**

---

## 📋 Contents
1. [What you'll build](#-what-youll-build)
2. [Before you start](#-before-you-start)
3. [Agenda](#-agenda)
4. [Part 1: Set up your project](#part-1-set-up-your-project-5-min)
5. [Part 2: Get to know the data](#part-2-get-to-know-the-data-3-min)
6. [Part 3: How to work with Copilot](#part-3-how-to-work-with-copilot-2-min)
7. [Part 4: Build the dashboard](#part-4-build-the-dashboard-35-min)
8. [Part 5: Check your work](#part-5-check-your-work-5-min)
9. [Part 6: Improve your app](#part-6-improve-your-app-5-min)
10. [Stretch goals](#-stretch-goals-if-you-finish-early)
11. [Troubleshooting](#-troubleshooting)
12. [Wrap-up and reflection](#-wrap-up-and-reflection)

---

## 🎯 What you'll build

A dashboard for **Alex Tan**, a fictional university student in Singapore, showing his spending for **November 2026**. It has five sections:

| # | Section | What it shows |
|---|---|---|
| 1 | **Current-month spending** | Total spent, budget remaining and number of transactions |
| 2 | **Budget progress** | A coloured bar showing how much of the monthly budget is used |
| 3 | **Spending by category** | A chart and a table comparing each category with its budget |
| 4 | **Transactions to review** | Purchases flagged as unusual by the earlier workflow |
| 5 | **Monthly reflection** | The AI-generated summary of the month |

> 💡 This builds on the earlier demos: the automated workflow flagged transactions and wrote a monthly reflection. Now you'll make an app to show it all.

---

## ✅ Before you start

Make sure you have:
- [ ] A **GitHub account**, signed in
- [ ] **GitHub Copilot** access (for example through GitHub Education). Ask the facilitator if you're not sure.
- [ ] The **workshop repository link** from your facilitator

You **don't** need to install anything if you use GitHub Codespaces (recommended).

---

## ⏱️ Agenda

| Time | Part | What you'll do |
|---|---|---|
| 0–5 min | Intro | See the finished dashboard |
| 5–10 min | Part 1 | Set up your project and run the starter app |
| 10–15 min | Parts 2–3 | Look at the data and learn the Copilot workflow |
| 15–50 min | Part 4 | Build the six steps of the dashboard |
| 50–55 min | Part 5 | Check your numbers against the answer key |
| 55–60 min | Part 6 and wrap-up | Improve your app and reflect |

---

## Part 1: Set up your project (5 min)

### Step 1.1: Make your own copy
1. Open the workshop repository link.
2. Click **Use this template ▸ Create a new repository**.
3. Name it `student-budget-dashboard`, keep it under **your** account and click **Create repository**.

### Step 1.2: Open it in Codespaces
1. In your new repository, click the green **Code** button.
2. Choose the **Codespaces** tab ▸ **Create codespace on main**.
3. Wait 1–3 minutes while it sets up. A VS Code editor opens in your browser and installs everything you need.

<details>
<summary>💻 Prefer your own computer? Click here.</summary>

You need Python 3.10+, VS Code, and the **GitHub Copilot** and **GitHub Copilot Chat** extensions.

```bash
git clone https://github.com/<your-username>/student-budget-dashboard.git
cd student-budget-dashboard
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate
pip install -r requirements.txt
```
</details>

### Step 1.3: Run the starter app
In the **terminal** at the bottom of the screen, type:

```bash
streamlit run app.py
```

When a pop-up says the app is running on **port 8501**, click **Open in Browser** (or **Preview**).

### 🏁 Checkpoint 1
You should see a page titled **💰 Student Budget Dashboard** with **five blue "TODO" boxes**. That's correct: you'll replace each box with a working section.

> 📌 Keep the app open in one tab and the code in another. Each time you save `app.py`, click **Rerun** in the app (or press `R`) to see your changes.

---

## Part 2: Get to know the data (3 min)

Open the `data` folder in the file explorer on the left. There are three files:

| File | What's in it |
|---|---|
| `transactions_nov2026.csv` | 102 transactions from 1–23 November 2026, in Singapore dollars |
| `budget_nov2026.json` | A monthly budget of **S$1,100** and a budget for each category |
| `sample_reflection.md` | The AI-written monthly reflection from the earlier workflow |

Open `transactions_nov2026.csv` and look at the columns:

| Column | Meaning |
|---|---|
| `date` | When the purchase happened |
| `merchant` | Where Alex spent the money |
| `amount_sgd` | How much, in S$. ⚠️ **A negative number is a refund.** |
| `category` | Food & Drinks, Transport, Shopping, and so on |
| `needs_review` | `TRUE` if the workflow flagged it, otherwise `FALSE` |
| `review_reason` | Why it was flagged |

### 🤔 Quick question
Scroll through the file. Can you spot a transaction that looks suspicious? Keep it in mind for Step 5.

---

## Part 3: How to work with Copilot (2 min)

1. Open **Copilot Chat**: click the chat icon at the top of VS Code, or press `Ctrl+Alt+I` (Windows/Linux) or `⌃⌘I` (Mac).
2. At the bottom of the chat box, switch to **Agent** mode (or **Edit** mode if you see it). This lets Copilot change `app.py` for you.
3. Make sure **`app.py`** is attached as context. Click **Add Context** or type `#file:app.py`.
4. **Copy and paste** the prompt for each step, then press Enter.
5. **Read the changes** Copilot suggests. Then click **Keep** (or **Accept**) and save.
6. Rerun the app and **compare it with the checkpoint**.

> 🧠 **Golden rule:** Copilot is your pair programmer, not your autopilot. If you don't understand something it wrote, ask: *"Explain this code to me."*

> 🛠️ **If something goes wrong**, don't start over. Tell Copilot what you see, for example:
> *"I get this error: [paste error]. Please fix it."*
> *"The total looks wrong. It should include refunds."*

---

## Part 4: Build the dashboard (35 min)

Open `app.py`. You'll see **TODO 1** to **TODO 6**. Work through them in order.

---

### Step 1: Load the data (TODO 1) · ~5 min

**📝 Prompt:**
```text
In app.py, complete TODO 1. Write a function load_transactions() that reads
TRANSACTIONS_FILE with pandas, parses the date column, and converts the
needs_review column from "TRUE"/"FALSE" text into a boolean. Also write
load_budget() that reads BUDGET_FILE as JSON. Cache both with st.cache_data.
Then call them and store the results in variables called transactions and budget.
```

**🔎 Test it:** Ask Copilot to *"temporarily show the transactions table under the title"*, or add `st.dataframe(transactions)` yourself.

### 🏁 Checkpoint: Step 1
- [ ] The app runs without errors.
- [ ] The table has **102 rows**.

> Delete the temporary table once you've checked it.

---

### Step 2: Current-month spending (TODO 2) · ~5 min

**📝 Prompt:**
```text
Complete TODO 2. Replace the info box under "1. Current-month spending" with
three st.metric cards side by side: total spent, budget remaining
(monthly_budget minus total spent), and number of transactions.
Format money as S$ with two decimals and a thousands separator, e.g. S$1,234.56.
Remember that negative amounts are refunds and must be included in the total.
```

### 🏁 Checkpoint: Step 2

| Metric | You should see |
|---|---|
| Total spent | **S$977.90** |
| Budget remaining | **S$122.10** |
| Transactions | **102** |

> ❓ Got **S$1,002.80**? Your total is missing the S$24.90 refund. Ask Copilot to fix it.

---

### Step 3: Budget progress bar (TODO 3) · ~5 min

**📝 Prompt:**
```text
Complete TODO 3. Replace the info box under "2. Budget progress" with a
progress bar showing total spent as a percentage of monthly_budget.
Make the bar green below 75%, amber from 75% to 100%, and red above 100%.
Show the percentage on the bar and a caption like "S$977.90 of S$1,100.00".
```

> 💡 Streamlit's built-in `st.progress` can't change colour. If Copilot uses it, ask:
> *"Make a custom coloured bar with st.markdown and HTML instead."*

### 🏁 Checkpoint: Step 3
- [ ] The bar shows **88.9%**.
- [ ] The bar is **amber**.

---

### Step 4: Spending by category (TODO 4) · ~8 min

**📝 Prompt:**
```text
Complete TODO 4. Replace the info box under "3. Spending by category" with
two columns. On the left, a horizontal bar chart (plotly express) of total
spending by category. On the right, a table comparing each category's
spending with its budget from category_budgets, with columns: category,
spent, budget, difference, and status ("Over budget", "Within budget",
or "No budget set" if the category has no budget). Colour over-budget bars red.
```

### 🏁 Checkpoint: Step 4

| Category | Spent | Budget | Status |
|---|---|---|---|
| Shopping | S$320.30 | S$200.00 | 🔴 Over budget |
| Food & Drinks | S$319.39 | S$350.00 | Within budget |
| Transport | S$179.29 | S$180.00 | Within budget |
| Uncategorized | S$23.40 | — | No budget set |

> 🤔 **Think:** Transport is only S$0.71 under budget, with a week of the month still to go. What would you tell Alex?

---

### Step 5: Transactions that need review (TODO 5) · ~6 min

**📝 Prompt:**
```text
Complete TODO 5. Replace the info box under "4. Transactions that need review"
with a table of transactions where needs_review is True. Show date (formatted
like "12 Nov"), merchant, amount_sgd (formatted as S$), category and
review_reason, sorted by amount from largest to smallest. Above the table,
write how many transactions need review.
```

### 🏁 Checkpoint: Step 5
- [ ] It says **7 transactions** need review.
- [ ] **Apple.com/bill (S$128.00)** is at the top.
- [ ] You can see the **Netflix possible duplicate**, the **SQ\*UNKNOWN MERCHANT** and the **Shopee refund**.

> ❓ Seeing **0 rows**? `needs_review` is probably still text. Go back to Step 1 and make sure it's converted to True/False.

> 🤔 Did you spot any of these in Part 2?

---

### Step 6: AI monthly reflection (TODO 6) · ~4 min

**📝 Prompt:**
```text
Complete TODO 6. Replace the info box under "5. Monthly reflection" by
reading REFLECTION_FILE and displaying it as markdown inside an st.expander
titled "Monthly reflection (AI-generated)", expanded by default.
If the file doesn't exist, show a friendly st.warning instead.
```

### 🏁 Checkpoint: Step 6
- [ ] The reflection appears in an expandable box.
- [ ] It mentions **S$977.90** and **88.9%**. **Do these match your dashboard?**

> 🔐 **Responsible AI moment:** The reflection was written by AI from spending data. If this were *your* real bank data, what would you be comfortable sending to an AI model? What wouldn't you send?

---

### 🎉 You've built the whole dashboard!
Save, rerun and scroll through all five sections.

---

## Part 5: Check your work (5 min)

1. Open `docs/ANSWER_KEY.md` and compare **every number** with your app.
2. If something doesn't match, check the **Common mistakes** section at the bottom of the answer key.
3. Ask Copilot to review your code:

```text
Review app.py for bugs. In particular, check that refunds (negative amounts)
and uncategorized transactions are included in the totals, and that the
budget percentage is total spent divided by monthly_budget.
```

### 🏁 Checkpoint 5
- [ ] All my numbers match the answer key.

---

## Part 6: Improve your app (5 min)

Pick **at least one**:

**🧾 Understand the code**
```text
Explain what each section of app.py does, as if I'm new to Python.
```

**📅 Add a date filter**
```text
Add a date-range filter in the sidebar. All five sections should update
to show only transactions in the selected range.
```

**🧹 Tidy up**
```text
Refactor app.py to make it easier to read, with clear comments, without
changing what the app shows.
```

**💾 Save your work to GitHub**
In the terminal:
```bash
git add .
git commit -m "Complete budget dashboard"
git push
```

---

## 🚀 Stretch goals (if you finish early)

| Challenge | Starter prompt |
|---|---|
| **Daily trend** | *"Add a line chart of cumulative daily spending, with a dashed 'ideal pace' line of monthly_budget ÷ 30 per day."* |
| **Mark as reviewed** | *"Add a checkbox next to each flagged transaction so I can mark it reviewed, and remember the choice using st.session_state."* |
| **Upload your own CSV** | *"Add an st.file_uploader so the dashboard can use any CSV with the same columns, and fall back to the sample data if none is uploaded."* |
| **Live AI reflection** | *"Build a short text summary of the month (totals, top three categories, flagged items) and show how it could be sent to an AI model to write a reflection with sections: What went well, Watch out, Suggestion."* Send **summary numbers only**, never raw personal data. |

---

## 🧯 Troubleshooting

| Problem | Try this |
|---|---|
| `streamlit: command not found` | Run `pip install -r requirements.txt`, then `python -m streamlit run app.py` |
| The app doesn't open | Open the **Ports** tab at the bottom, find **8501** and click the 🌐 globe icon |
| `FileNotFoundError` for the data | Make sure you run the command from the main project folder, not inside `data/` |
| The app doesn't change after an edit | Save the file (`Ctrl+S` / `⌘S`), then click **Rerun** in the app |
| A red error box appears in the app | Copy the error and ask Copilot: *"I get this error: … Please fix it."* |
| Copilot doesn't respond | Check you're signed in to GitHub and the Copilot icon in the status bar is active |
| Things are really broken | Compare with `solution/app.py`, or run it with `streamlit run solution/app.py` to see the finished version |

---

## 🧠 Wrap-up and reflection

Take two minutes to think about (or discuss with the person next to you):

1. **Where did Copilot save you the most time?**
2. **Where did you have to correct it, and how did you notice?**
3. **How did you know your numbers were right?**
4. **What would you add to make this app useful for your own budget?**

### What you practised today
- ✅ Turning a written requirement into a working app with an AI pair programmer
- ✅ Writing clear, specific prompts
- ✅ Checking AI-generated code and numbers against an answer key
- ✅ Thinking about responsible use of personal data with AI

> 🔐 **Final reminder:** if you try this app with your own bank data, put the file in `data/private/` (it's excluded from Git) and **never push real financial data to GitHub**.

**Great work! 🎉**
