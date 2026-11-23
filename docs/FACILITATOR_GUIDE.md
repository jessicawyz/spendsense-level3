# Facilitator guide: Demo 4 (about 90 minutes)

**Goal:** Turn the automated workflow into a complete student project, and along the way show *how* to get the best out of GitHub Copilot: prompting styles, models and thinking effort, and Spec-Driven Development with GitHub Spec Kit.

## What makes this session interactive
| Mechanic | Where | Why it works |
|---|---|---|
| 🪜 **Prompt Ladder**, ending in a class vote | Round 1 | Students *feel* the difference between ghost text, inline chat, vague vs specific prompts and image input |
| 🥊 **Model Showdown** in four teams, timed and scored on a live board | Round 2 | Turns "models and effort" into a visible experiment with a right answer |
| 🗳️ **Class-built constitution** | Round 3.2 | Every team contributes a rule, so they own the spec |
| 🤝 **Clarify pair-check** | Round 3.4 | Copilot interviews students, and the questions differ between pairs |
| ⚡ **Power-up cards and points** | Round 4 | Self-paced challenges show different Copilot surfaces; fast students stay busy |
| 🎤 **Show and tell plus awards** | Wrap-up | Ends on a high with peer recognition |

## Before the session
- [ ] Push this repo to GitHub and turn on **Settings ▸ Template repository**.
- [ ] **Pin Spec Kit.** Do a dry run, note the version from `specify version`, and change the devcontainer's `pipx install specify-cli` to `pipx install specify-cli==<that version>` so everyone gets the same behaviour.
- [ ] In the dry run, note whether the slash commands appear as `/speckit-specify` or `/speckit.specify`, and tell students which one at the start.
- [ ] Check **which models and effort levels** the students' Copilot plan offers. Pick a concrete model name for each Round 2 team card and write them on a slide.
- [ ] Optional: turn on Codespaces **prebuilds** so setup takes seconds.
- [ ] Set up a **live board** for Round 2 and the leaderboard: a shared spreadsheet, whiteboard or poll.
- [ ] Have `solution/app.py` running (`streamlit run solution/app.py`) for the opening demo.
- [ ] Optional: replace `data/sample_reflection.md` with the real reflection from Demo 3.

## Run sheet

| Time | Segment | Facilitator moves |
|---|---|---|
| 0–5 | **Hook and setup** | Demo the finished dashboard for 60 seconds. Ask: *"How would you tell an AI to build this?"* Students start Codespaces while you talk. |
| 5–17 | **Round 1: Prompt Ladder** | Live-demo rung 1 (ghost text), then let them go. At 15 min, run a quick hands-up vote: *which rung for which job?* |
| 17–27 | **Round 2: Model Showdown** | Split the room into four teams. Show the team-card slide with model names. Start a visible timer. Fill the board live, then reveal the answers (S$977.90, Shopping over by S$120.30, 88.9%). Run the bonus "run code" round. **Key message:** pick model and effort per task, and ask for code when exact numbers matter. |
| 27–29 | **Why specs?** | One slide: vibe coding vs Spec-Driven Development. Constitution → Specify → Clarify → Plan → Tasks → Implement. |
| 29–32 | **3.1 Init** | Everyone runs `specify init` together. Wait for the `/speckit` commands checkpoint. |
| 32–36 | **3.2 Constitution** | Collect one rule from each team on the board (look for accessibility, privacy and "explain the code"). Students add one to their prompt. |
| 36–41 | **3.3 Specify** | Stress: *what and why, no tech*. Ask a student to read out one acceptance criterion from their `spec.md`. |
| 41–46 | **3.4 Clarify** | Pair-check. Ask: *"Who got a question nobody else got?"* |
| 46–51 | **3.5 Plan** | Reasoning model at **High** effort. Point out the "Constitution Check" in `plan.md`. |
| 51–54 | **3.6 Tasks** | Fast model. *"How many tasks did you get?"* Compare the range across the room. |
| 54–67 | **3.7 Implement** | Circulate. Watch for people blindly clicking **Allow**. Move stragglers to **Plan B** by 62 min. |
| 67–80 | **Round 4** | Everyone runs `/check-numbers` first. Then power-ups are self-paced. Keep the leaderboard updated. |
| 80–90 | **Show and tell** | 2–3 demos, three awards, reflection questions, `git push`. |

## 60-minute version
Cut Round 1 to rungs 3 and 4 (6 min), keep Round 2 without the bonus (8 min), skip Analyze, give the constitution text as-is (no class rules), and do only `/check-numbers` plus one power-up.

## Teaching points to land
1. **Context beats cleverness.** The specific prompt with `#file`, criteria and output format wins (Round 1).
2. **Right model, right effort, right job.** Fast for simple, reasoning and high effort for planning, *code* for exact arithmetic (Round 2).
3. **Spec is the source of truth.** When something's wrong, ask "spec or code?" The *Change the spec* power-up proves the loop works.
4. **Humans stay in charge.** Read before you accept, read before you **Allow**, and verify every number.
5. **Responsible AI.** Synthetic data only. Discuss what should never go to a model.

## Built-in "gotchas" in the data
A Shopee **refund** (negative amount), an **uncategorized** unknown merchant, a possible **duplicate** Netflix charge, and `needs_review` stored as **text**. These show up naturally in the Model Showdown and `/check-numbers`.

## Troubleshooting (facilitator)
| Problem | Fix |
|---|---|
| Spec Kit install fails in Codespaces | `pipx install specify-cli` manually. If it still fails, switch the student to Plan B (`fallback/app.py`) |
| `specify init` refuses because the folder isn't empty | Make sure `--force` is included |
| Implement creates files in odd places or ignores the constitution | Ask the student to run `/speckit-analyze`, then re-run implement. The fallback is `solution/app.py` |
| Students run out of AI credits or hit rate limits | Move them to a fast model or Auto. High effort uses more credits, so keep it to the Plan step |
| Copilot coding agent or PR review isn't available | Depends on the plan, so treat these as optional power-ups |
