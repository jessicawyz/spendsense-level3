# 🛠️ Workshop guide: Grow a budget app with GitHub Copilot and Spec Kit

**Demo 4 · Hands-on session · about 100 minutes**

You're joining a "team" that already has a **semi-working app**: a budget dashboard (v0.1) for a student. Your job is to **add features** the way real teams do. You'll describe the feature in a spec, plan it, build it, and then deal with the moment every developer knows: ***"Oh no, we forgot something."***

Along the way you'll test how *the way you ask*, *the model you pick* and *how hard it thinks* change what GitHub Copilot gives you.

> 🎯 **By the end you will have:** a dashboard where you can **add your own spending** and watch it update, a spec you **revised twice**, and first-hand evidence of which Copilot techniques work best for which job.

---

## 📋 Contents
- [The app you're joining](#-the-app-youre-joining)
- [How today works](#-how-today-works)
- [Setup and tour](#-setup-and-tour-5-min)
- [Round 1: The Prompt Ladder](#-round-1-the-prompt-ladder-10-min)
- [Round 2: Model Showdown](#-round-2-model-showdown-10-min)
- [Round 3: Build a feature with Spec Kit, then revise it](#-round-3-build-a-feature-with-spec-kit-then-revise-it-57-min)
- [Round 4: Verify and Power-ups](#-round-4-verify-and-power-ups-10-min)
- [Show and tell](#-show-and-tell-and-reflection-8-min)
- [Plan B](#-plan-b-if-spec-kit-isnt-working)
- [Troubleshooting](#-troubleshooting)
- [Cheat sheet and scorecard](#-copilot-cheat-sheet)

---

## 🏗️ The app you're joining

**Alex Tan**, a fictional university student in Singapore, tracks his November 2026 spending. The data is in `data/transactions_nov2026.csv` (it opens in Excel too).

| Part of the app | Status in v0.1 |
|---|---|
| 📊 Current-month spending, budget progress, category chart, transactions to review | ✅ Working |
| ➕ **Add a transaction**: a form that saves your spending to the CSV and updates the dashboard | ⏳ **You'll build this in Round 3** |
| Monthly reflection, budget vs actual table, date filter, undo… | ⏳ On the backlog (`docs/BACKLOG.md`). Power-ups in Round 4 |

---

## 🗺️ How today works

| Time | Round | What you'll learn |
|---|---|---|
| 0–5 | Setup and tour | Run the existing app and find what's missing |
| 5–15 | 🪜 **Round 1: The Prompt Ladder** | Four ways to ask Copilot, including asking about an existing codebase |
| 15–25 | 🥊 **Round 2: Model Showdown** | How the model and thinking effort change answers |
| 25–82 | 📐 **Round 3: Spec Kit** | Spec → plan → **plan revision** → tasks → build → **spec revision** → rebuild |
| 82–92 | ⚡ **Round 4: Verify and Power-ups** | Check your numbers, then pick features from the backlog |
| 92–100 | 🎤 **Show and tell** | Demo, vote and reflect |

**Points 🏆:** You earn points along the way. Track them in the [scorecard](#-my-scorecard) at the end.

---

## ⚙️ Setup and tour (5 min)

1. Open the workshop repository link. Click **Use this template ▸ Create a new repository** and name it `student-budget-dashboard` under your account.
2. **Code ▸ Codespaces ▸ Create codespace on main**. Wait 2–3 minutes for setup.
3. In the terminal:
   ```bash
   specify version
   streamlit run app.py
   ```
4. Open the app preview on port **8501**. Click around:
   - 📊 **Dashboard** tab: Total spent should be **S$977.90**.
   - ➕ **Add a transaction** tab: it just says *"Coming soon"*. That's your job today.

### 🏁 Checkpoint
- [ ] `specify version` prints a version number.
- [ ] The app shows **S$977.90** and a "Coming soon" tab.
- [ ] Copilot Chat opens (`Ctrl+Alt+I` / `⌃⌘I`) and you can see the **model picker** under the chat box.

> 💡 Leave the app running in its own terminal. Open a **second terminal** (the **+** icon) for commands.

---

## 🪜 Round 1: The Prompt Ladder (10 min)

Four "rungs", each giving Copilot more context and you more control.

### Rung 1: Ghost text ✨ (2 min)
Open **`playground/warmup.py`**. Put your cursor at the end of the comment `# A function called is_big_purchase...`, press **Enter** and wait. Press **Tab** to accept the grey suggestion.
> 💬 *Your comment **was** the prompt.*

### Rung 2: Inline chat ✏️ (2 min)
Select the new function, press **`Ctrl+I`** (`⌘I` on Mac) and paste the instruction from the comment under **RUNG 2** in the file. Review, then **Accept**.
> 💬 *Small, focused edits right where you're looking.* (Remember this function. 👀 It might be useful later…)

### Rung 3: Vague vs specific, on a real codebase 🎯 (3 min)
In the **Chat view**, choose **Ask** mode. First, the **vague** version:
```text
explain the code
```
Then start a **new chat** (`+`) and try the **specific** version:
```text
#codebase Give me a tour of this project as a table with one row per section of app.py:
section name | what it shows | which data file it reads | working or "coming soon".
Then tell me where in app.py a new "add a transaction" form should go, and which
existing function would need to change so the dashboard updates after saving.
```
> 🤔 Which answer helps you start work on the app? The specific prompt adds **scope** (`#codebase`), **structure** (a table) and **a goal** (where the new feature goes).

### Rung 4: Show, don't tell 🖼️ (3 min)
Drag **`docs/dashboard_wireframe.png`** into the chat box, then ask:
```text
Compare this sketch with the current app.py. Which parts of the sketch already exist,
and which are missing? Answer as a checklist.
```
> 💬 *Copilot can read images. A sketch is a fast way to say "this is what I want".*

🗳️ **Class vote:** Which rung would you use for a quick fix? For understanding someone else's code? For a new screen?

**🏆 +1 point** for completing all four rungs.

---

## 🥊 Round 2: Model Showdown (10 min)

Some AI models are **fast**, some **reason** more deeply. Some also let you set **thinking effort**: how hard the model thinks before answering.

### Step 1: Team cards
The facilitator puts you in a team and tells you the exact model names.

| Team | Model setting | How to set it |
|---|---|---|
| 🟦 **Team Fast** | A **fast / lightweight** model | Model picker ▸ the fast model named on the slide |
| 🟩 **Team Think-Low** | A **reasoning** model at **Low** effort | Model picker ▸ reasoning model ▸ click **>** next to it ▸ **Low** |
| 🟥 **Team Think-High** | The **same reasoning** model at **High** effort | Same model ▸ **>** ▸ **High** |
| 🟨 **Team Auto** | **Auto** | Model picker ▸ **Auto** |

> 💡 No **>** next to your model? It doesn't support effort settings. Pick another reasoning model.

### Step 2: Same question, every team
New chat, **Ask** mode:
```text
Using #file:data/transactions_nov2026.csv and #file:data/budget_nov2026.json, answer:
1. What is the total amount spent in November, including refunds?
2. Which category is the most over its budget, and by how much?
3. What percentage of the monthly budget has been used?
Show your working briefly.
```
⏱️ Time it, then add your row to the class board.

| Team | Time (sec) | Q1 ✅/❌ | Q2 ✅/❌ | Q3 ✅/❌ |
|---|---|---|---|---|
| Fast | | | | |
| Think-Low | | | | |
| Think-High | | | | |
| Auto | | | | |

### Step 3: Bonus 🧮
Switch to **Agent** mode and ask: *"Write and run a short Python script to calculate those three answers exactly."* Did the answers change?

> 🤔 Adding up 102 numbers "in its head" is hard for any language model. **When exact numbers matter, ask Copilot to run code.** When would you pick speed, and when deep thinking?

**🏆 +1** for your team's row, **+1** if all three answers were correct.

---

## 📐 Round 3: Build a feature with Spec Kit, then revise it (57 min)

### Why specs? (2 min)
Asking for code and hoping it matches what's in your head is "vibe coding". **Spec-Driven Development (SDD)** writes the intent down first, so you can **review it, change it and rebuild from it**:

```
Constitution → Specify → Clarify → Plan → ✏️ revise plan → Tasks → Implement → Test
                  ▲                                                             │
                  └─────────────── ✏️ revise spec  ◄── "we forgot something!" ──┘
```

Today's feature is backlog item **B1: Add a transaction**. Read it in `docs/BACKLOG.md`.

> 📝 **Command names:** this guide uses `/speckit-specify` style. If yours show `/speckit.specify` (with a dot), use that. Type `/speckit` in chat to see the list.

---

### 3.1 Add Spec Kit to the existing project (3 min)
In your second terminal:
```bash
specify init --here --integration copilot --script sh --force
```
`--here` means "this folder". `--force` is needed because the project already has files.

Then save a "before" snapshot, so you can see later exactly what Spec Kit and Copilot change:
```bash
git add . && git commit -m "chore: add Spec Kit"
```
### 🏁 Checkpoint
- [ ] Typing `/speckit` in Copilot Chat lists the Spec Kit commands.

---

### 3.2 Constitution from an existing codebase (4 min) · 🧠 *Any model, Agent mode*

The constitution holds the project's ground rules. In a project that already exists, Copilot can **read the code first**.

🗳️ **Class activity:** each team suggests one rule. Add **one** to the end of the prompt below.

```text
/speckit-constitution Read the existing app.py, README.md and docs/BACKLOG.md first, then write
the constitution for this project:
- Extend the existing app; don't rewrite it. One Python file, Streamlit, pandas and plotly only.
- Correctness first: every number shown must be reproducible from the data; refunds count.
- The app may only APPEND rows to data/transactions_nov2026.csv, using the existing column order.
  Never change or delete existing rows, and never touch data/seed/.
- Money is shown as S$1,234.56. Code must be readable by a first-year student.
- [ADD YOUR TEAM'S RULE HERE]
```
📂 Open `.specify/memory/constitution.md`. Is your rule there?

---

### 3.3 Specify feature B1 (5 min) · 🧠 *Any model*

Describe **what** and **why**, no technology. Optionally drag in **`docs/add_transaction_wireframe.png`** as well.

```text
/speckit-specify Add a feature to the existing Student Budget Dashboard: in the existing
"Add a transaction" tab, a student can record a spending as soon as it happens instead of
waiting for their bank statement. They enter the date, merchant, amount (negative for a
refund), category, payment method and optional notes. When they save, the transaction is
added to the transactions data with the next transaction ID, the dashboard immediately
reflects it, and they see a confirmation and their most recent transactions. Invalid input
(for example a missing merchant or a zero amount) is rejected with a clear message.
```
📂 Open the new `spec.md` under `specs/`. Find the **user stories**, **functional requirements** (FR-001…) and **acceptance criteria**.

---

### 3.4 Clarify (4 min) · 🧠 *Reasoning model, Medium effort*
```text
/speckit-clarify
```
Answer Copilot's questions. **You** decide.

> ⚠️ **Important for today:** if Copilot asks how new transactions should be **flagged for review** (the `needs_review` / `review_reason` columns), answer:
> **"Not decided yet. The product owner will confirm. For now, set needs_review to FALSE and leave review_reason empty."**
> *(Remember you said this… 👀)*

🤝 **Pair-check:** did your neighbour get the same questions?

**🏆 +1 point** per question answered (max 3).

---

### 3.5 Plan (4 min) · 🧠 *Reasoning model, **High** effort*
```text
/speckit-plan Extend the existing app.py (Python 3.11, Streamlit, pandas, plotly). Put the form
in the existing "Add a transaction" tab using st.form. Write to data/transactions_nov2026.csv
in the column order of TRANSACTION_COLUMNS. No new dependencies, no database.
```
📂 Open `plan.md`. Look for the **Constitution Check** section.

---

### 3.6 ✏️ Revision #1: the tech lead reviews your plan (5 min)

Before anyone writes code, your **tech lead** reviews the plan. Tick each item **only if `plan.md` clearly covers it**:

| # | 🧑‍💻 Tech lead's checklist | In my plan? |
|---|---|---|
| 1 | **Refreshing the dashboard after saving.** `app.py` caches the data with `@st.cache_data`, so the plan must say how the cache gets cleared, or the dashboard will show old numbers | ☐ |
| 2 | **Transaction ID:** the next number after the highest existing ID (TXN-0102 → TXN-0103) | ☐ |
| 3 | **Column order:** new rows follow `TRANSACTION_COLUMNS` exactly, and dates are `YYYY-MM-DD` | ☐ |
| 4 | **Safe writing:** only append, and show an error if saving fails, without leaving a half-written row | ☐ |
| 5 | **Resetting test data** from `data/seed/` | ☐ |

Unticked boxes mean **your plan forgot something**. Fix it **now**, while it's cheap. In Agent mode:
```text
Update the plan.md for the current feature: add a section "Data refresh and file safety"
covering these items the plan is missing: [LIST YOUR UNTICKED ITEMS]. Keep everything else
the same, and re-check the Constitution Check.
```
👀 **See the revision:** open **Source Control** (`Ctrl+Shift+G`) and click `plan.md`. Green lines are what you added.

> 💬 **Lesson:** a gap caught in the **plan** costs one prompt. The same gap caught after the code is written costs a debugging session.

**🏆 +2 points** if you found and fixed at least one gap.

---

### 3.7 Tasks (3 min) · 🧠 *Fast model*
```text
/speckit-tasks
```
📂 Open `tasks.md`. How many tasks? ____ Can you find the ones that came from your plan revision?

---

### 3.8 Implement v1 and test it (12 min) · 🧠 *Your choice (write it down!)*
**Agent** mode:
```text
/speckit-implement
```
Read each terminal command before clicking **Allow**. When it's finished, refresh the app.

**Test it.** First reset the data, then use **your form** to add the four test transactions (all dated **23 Nov 2026**):
```bash
cp data/seed/transactions_nov2026.csv data/transactions_nov2026.csv
```
| # | Merchant | Amount | Category | Payment | Notes |
|---|---|---|---|---|---|
| T1 | Kopitiam Hawker Centre | 5.20 | Food & Drinks | PayNow | Chicken rice |
| T2 | Uniqlo | 79.90 | Shopping | Credit Card | Winter jacket |
| T3 | Shopee | -12.00 | Shopping | Debit Card | Refund for phone case |
| T4 | Starbucks | 7.13 | Food & Drinks | Debit Card | *(blank)* |

Also try saving with a **blank merchant** and with an amount of **0**. Both should be rejected.

### 🏁 Checkpoint v1
| Check | Expected |
|---|---|
| Total spent | **S$1,058.13** |
| Transactions | **106** |
| Budget progress | **96.2%**, amber |
| New IDs | **TXN-0103 … TXN-0106** |
| Open `data/transactions_nov2026.csv` | 4 new rows at the bottom, same columns as the rest |

> 💡 Saved, but the numbers didn't change? That's tech lead item 1 (caching). Go back to 3.6.

Save your v1:
```bash
git add . && git commit -m "feat(B1): add transaction form v1"
```
**🏆 +3 points** for a working v1.

---

### 3.9 ✏️ Revision #2: "We forgot something!" 📣 (15 min)

Look at **Transactions that need review** on the dashboard. How many are there? ____

You just added a **S$79.90** jacket and a **refund**, yet the review list didn't change. Is that a **code bug**? 🤔

#### Step 1: Spec or code? (2 min)
Open your `spec.md` and search (`Ctrl+F`) for **"review"**. Then ask Copilot to play product owner:
```text
/review-spec
```
Was it the code, or did the **spec** never ask for it? *(Hint: what did you answer in Clarify?)*

#### Step 2: The product owner's message 📣 (1 min)
> **From:** Product Owner
> **Subject:** Sorry, we forgot to tell you!
>
> New transactions must be checked with **the same review rules as our workflow**. Set `needs_review` to TRUE if any rule matches, and put **all** matching reasons in `review_reason`, separated by `; `:
> 1. Amount of **S$50 or more** → `Amount >= S$50`
> 2. Category is **Uncategorized** → `Uncategorized`
> 3. **Negative** amount (refund) → `Refund to confirm`
> 4. **Same merchant and same amount** within the **previous 7 days** → `Possible duplicate`. **Except Transport**: repeated MRT and bus fares are normal.
>
> When a saved transaction is flagged, the confirmation should say so and give the reason.

#### Step 3: Update the spec, not the code (3 min) · 🧠 *Reasoning model, Medium*
```text
/speckit-clarify Our product owner has confirmed how new transactions are flagged for review.
Replace the earlier "needs_review is FALSE for now" decision with these rules: [PASTE THE 4 RULES
AND THE CONFIRMATION REQUIREMENT FROM THE MESSAGE]. Update the functional requirements and
acceptance criteria, and add an acceptance scenario for each rule.
```
👀 **Source Control ▸ `spec.md`:** red lines are the old decision, green lines are the new requirements.

#### Step 4: Ripple the change through (5 min)
Run these one at a time and **read what changes** in each file:
```text
/speckit-plan Update the existing plan for the revised review-flag requirements. Keep all existing
technical decisions, including the "Data refresh and file safety" section.
```
```text
/speckit-tasks Add tasks only for the new review-flag requirements. Keep the existing completed
tasks marked as done.
```
```text
/speckit-analyze
```
> 🔍 `/speckit-analyze` checks that the spec, plan and tasks agree. Did it find any inconsistencies? Fix them before building.
>
> 💡 If your Spec Kit version has **`/speckit-converge`**, try it too. It compares the code with the spec and adds tasks for whatever is missing.

#### Step 5: Build v2 and retest (4 min)
```text
/speckit-implement Implement only the tasks that are not done yet.
```
Reset the data and add **T1–T4** again:
```bash
cp data/seed/transactions_nov2026.csv data/transactions_nov2026.csv
```

### 🏁 Checkpoint v2
| Test | Expected `review_reason` |
|---|---|
| T1 Kopitiam S$5.20 | *(not flagged)* |
| T2 Uniqlo S$79.90 | `Amount >= S$50` |
| T3 Shopee -S$12.00 | `Refund to confirm` |
| T4 Starbucks S$7.13 | `Possible duplicate` (same as a 22 Nov purchase) |
| **Transactions that need review** | **10** (was 7) |

```bash
git add . && git commit -m "feat(B1): flag new transactions for review (v2)"
```
**🏆 +3 points** for a working v2.

> 💬 **The big idea:** requirements change all the time. With SDD you **changed one paragraph of the spec**, and the plan, tasks and code followed. The spec still matches what the app actually does.

---

## ⚡ Round 4: Verify and Power-ups (10 min)

### 4.1 Verify (2 min)
Agent mode:
```text
/check-numbers
```
Copilot recalculates everything from the CSV and compares it with your app and the answer key, labelling any problem as a **spec**, **plan** or **code** issue.

**🏆 +2 points** if everything is ✅.

### 4.2 Power-ups from the backlog
| | Challenge | How | 🏆 |
|---|---|---|---|
| 📝 | **B2 Monthly reflection** | Agent mode: *"Implement backlog item B2 from docs/BACKLOG.md."* | 1 |
| 📊 | **B3 Budget vs actual** | Same, for B3. Check it against the answer key | 2 |
| 🖼️ | **B4 Sketch to UI** | Attach `docs/dashboard_wireframe.png`: *"Add the sidebar date filter from this sketch (B4)."* | 2 |
| 🔁 | **B5 Undo, your own SDD loop** | Run the whole loop yourself: `/speckit-specify` → `/speckit-plan` → `/speckit-tasks` → `/speckit-implement` | 3 |
| 🧪 | **B6 Tests** | *"Write pytest tests for the review rules using T1–T4 from docs/ANSWER_KEY.md, then run them."* | 2 |
| 📖 | **Explain it** | Select the code Copilot wrote for saving and run `/explain-simply` | 1 |
| 🔍 | **AI code review** | Push a branch, open a pull request and request a review from **Copilot** | 2 |
| 🤖 | **Coding agent** | Create a GitHub issue for a backlog item and assign it to **Copilot** *(if your plan supports it)* | 3 |

---

## 🎤 Show and tell and reflection (8 min)

**Show and tell:** 2–3 volunteers add **one real (or made-up) spending from this week** live, on screen. The class votes:
- 🎨 Best-looking app
- 🧠 Best constitution rule or clarify answer
- 🔍 Best "gap caught" story

**Reflect** (one sentence each):
1. Which rung of the prompt ladder will you use most?
2. When would you choose a fast model, and when a reasoning model at high effort?
3. Which revision cost less: fixing the **plan** before code, or fixing the **spec** after code? Why?
4. Where did Copilot get something wrong, and how did you catch it?

```bash
git push
```

> 🔐 If you enter **your own real spending**, don't push it to a public repo. Reset with `cp data/seed/transactions_nov2026.csv data/transactions_nov2026.csv` before you push, or keep the repo private.

---

## 🅱️ Plan B: if Spec Kit isn't working

You can still build B1 and go through the same "we forgot something" moment, using **Agent mode** prompts:

1. **Build v1:**
   ```text
   Implement backlog item B1 from docs/BACKLOG.md in app.py: a form in the "Add a transaction" tab
   with date, merchant, amount (negative = refund), category, payment method and notes. Validate
   (merchant required, amount not zero), append to data/transactions_nov2026.csv in the
   TRANSACTION_COLUMNS order with the next TXN ID, set needs_review to FALSE, clear the cached data
   so the dashboard updates, and show a confirmation plus the 5 most recent transactions.
   ```
2. Test with T1–T4 (section 3.8).
3. Read the **product owner's message** (3.9, Step 2) and ask Copilot to implement those rules.
4. Retest against **Checkpoint v2**.

> 🤔 Afterwards, compare with a Spec Kit user: where is *your* record of the product owner's decision?

---

## 🧯 Troubleshooting

| Problem | Try this |
|---|---|
| `specify: command not found` | `pipx install specify-cli`, then open a new terminal |
| `/speckit…` commands missing | Reload the window: `Ctrl+Shift+P` ▸ **Developer: Reload Window**. Or try the dot form `/speckit.specify` |
| Model picker only shows **Auto** | Trust the workspace: `Ctrl+Shift+P` ▸ **Workspaces: Manage Workspace Trust** |
| Saved, but the dashboard shows old numbers | The cache wasn't cleared (tech lead item 1). Add it to the plan, then re-implement |
| Every MRT fare is flagged as a duplicate | The Transport exception is missing. Check that the spec says it |
| New IDs are wrong (e.g. TXN-0001 or random) | ID rule (tech lead item 2): highest existing number plus one |
| The CSV looks broken | Reset: `cp data/seed/transactions_nov2026.csv data/transactions_nov2026.csv` |
| `/speckit-tasks` re-created every task | Tell it: *"Keep completed tasks marked done; only add new ones"*, then `/speckit-implement Implement only the tasks that are not done yet` |
| Implement went off track | Stop it, check `git diff`, undo with `git checkout -- app.py`, then re-run |
| App doesn't open | **Ports** tab ▸ **8501** ▸ 🌐 |

---

## 📇 Copilot cheat sheet

| I want to… | Use |
|---|---|
| Finish the line I'm typing | **Ghost text** (`Tab`) |
| Edit the code I've selected | **Inline chat** (`Ctrl+I` / `⌘I`) |
| Understand a project | **Ask mode** + `#codebase` |
| Let Copilot change files and run commands | **Agent mode** |
| Show what I want | Drag an **image** into chat |
| Reuse a team prompt | **Prompt files**: `/check-numbers`, `/review-spec`, `/explain-simply` |
| Build from intent | **Spec Kit**: `/speckit-…` |
| Quick, simple job | **Fast model** |
| Hard thinking (plans, tricky bugs) | **Reasoning model, higher effort** (model picker ▸ **>**) |
| Exact numbers | Ask Copilot to **run code** |

---

## 🏆 My scorecard

| Activity | Max | Mine |
|---|---|---|
| Round 1: all four rungs | 1 | |
| Round 2: team row and all correct | 2 | |
| 3.4 Clarify answers | 3 | |
| 3.6 Plan revision: found and fixed a gap | 2 | |
| 3.8 Working v1 | 3 | |
| 3.9 Working v2 | 3 | |
| 4.1 `/check-numbers` all ✅ | 2 | |
| 4.2 Power-ups | 16 | |
| **Total** | **32** | |
