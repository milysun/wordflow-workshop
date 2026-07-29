# Runbook — CAITG Winter School hands-on (45 min)

**Coding text with GenAI: the Annotation tool in Wordflow · Thursday 30 July 2026**

Context: you are the **second half** of the session. The first speaker has just covered LLM-assisted coding in theory — limitations, pitfalls, prompting, intercoder reliability. Don't re-teach it; *point back at it* ("you just heard why we measure agreement — now watch the number appear"). Slides: `slides/caitg-annotator.html` (8 slides, deck is done by minute ~8). Participant sheet: `participant/hands-on-annotator.md`.

**Before you start**: check `sih.tools/api` is live and the OpenRouter key on it has credit; have Wordflow 0.7.1 desktop open with a clean workspace; have the sample data downloadable (or pre-imported on the projector machine).

---

## 0:00 – 0:02 · Title + "start this now" (slides 1–2)

Greet, one sentence of who you are. **Immediately** put up slide 2 and get every laptop launching:

> "Before I say anything else — open **sih.tools/wordflow**. Desktop installer if you can, v0.7.1. If you have an Australian university login, the Binder button also works. International visitors: desktop app, the cloud one needs Australian credentials. Get it downloading — it'll be ready by the time I stop talking."

Helpers (if any) start circulating now.

## 0:02 – 0:08 · Intro slides (slides 3–6)

- **Slide 3, Who built this** (~1 min): team → University of Sydney → LDaCA → ARDC/NCRIS. One line on LDaCA: national research infrastructure for Australian language data; Wordflow is one of its text analytics tools.
- **Slide 4, Why Wordflow** (~2 min): the methods live in Python/R; that's a wall for most researchers who work with text. Say the north-star sentence slowly. Land the bridge: *"Everything you heard in the last 40 minutes assumed you can call an API. This tool is that theory with the coding removed — not the thinking removed."*
- **Slide 5, interface** (~2 min): if your Wordflow is already up, do this on the live app instead of the slide. Sidebar → tool interface → workspace graph → data viewer → quick-select. Point at **Tutorial** and **Feedback** once each.
- **Slide 6, everything is a data block** (~1 min): the one concept. Annotation writes columns onto a block — AI codes become ordinary data.

## 0:08 – 0:10 · Roadmap (slide 7), then leave the deck

Show the arc once, tell them the participant sheet mirrors it, and switch to live Wordflow. Sweep the room: everyone has Wordflow open? Anyone stuck on install pairs up with a neighbour — the task works fine watched-then-repeated.

## 0:10 – 0:15 · Workspace, data, and the 60-second tour (live)

1. **Create workspace** in Data Loader.
2. **Import sample data** → Datasets tab → **ADO — Queensland Election Tweets** → **Import selected**.
3. Mention own-data upload: drag & drop, CSV and text fine. **Say the known issue out loud**: *"Excel and zip import are broken in 0.7.1 — export to CSV first."*
4. Show the **three ways to add a block to a tool** quickly: Add data block in the tool; the node's **+** in the graph; the sidebar Data Blocks add button. Ten seconds each.
5. **Preprocessing flash** (mention, don't do): joins, dtype conversion, filtering all live in Preprocessing — "that's a whole other workshop." One sweep of the sidebar: Frequency, Concordance, Trends, Topic Modeling, Quotation — the classic corpus toolkit. *"Today: the newest one."*

Timing check: at 0:15 you should be clicking **Annotation**. If not, cut step 4 to one method.

## 0:15 – 0:23 · Annotation setup: column, codebook, manual (live, everyone follows)

1. Sidebar → **Annotation**. Add **`candidate_info_gender`** under Selected Data Blocks. **Text Column = `first_name`** — say why: that's all the model gets to read.
2. **Annotation Column → Start new annotation** → name it **`gender.ai`** → Create. Explain the `.ai` naming habit (yours, not the tool's).
3. **Codebook → Create New**, then **Edit**: add **M / F / U** with one-sentence descriptions. Script the teaching point: *"The description field is your codebook definition — the model reads it verbatim. Write it like instructions to a new RA. Vague codebook, vague coder — human or machine."*
4. **Manual mode → Start**: code 3–4 rows yourself on screen, invite them to do 5. Point out this is also the multi-coder workflow — one column per coder, each continues via the Annotation Column dropdown.
5. **Close** manual mode.

## 0:23 – 0:27 · Provider + model (live)

1. Toggle **AI**, expand **Advanced settings** (chevron).
2. **+ Add Provider** → OpenRouter → paste key. **Put `sih.tools/api` on the projector and say it twice** — this is the step that loses people.
3. **Model**: search the live list. Recommend `google/gemini-2.5-flash-lite` for the room (fast, cheap on the shared key); `google/gemini-2.5-flash` or a free `gemma` as alternatives. Warn: *"the key is shared and temporary — it dies tonight."*

Contingency: if the shared key rate-limits (429s — you'll see failed batches or slow previews), move the room to the `:free` gemma models and shrink to preview-only work.

## 0:27 – 0:33 · The preview loop — the heart of the session (live)

1. **Prompt** field: press Tab to take the default, then edit — add context (Australian candidates' first names) and an escape hatch (when unsure → `U`).
2. **Preview** → 10 rows coded, display-only. *"Nothing has touched the data yet — this is your pilot study."*
3. **Compare To** → tick **`gender`** (the human coding) → default **Cohen's Kappa**. Badge appears. **Hover it → confusion matrix.** Tie back explicitly: *"This is the intercoder reliability you heard about before the break — the AI is just another coder, and it earns trust the same way."*
4. Click **Filter any difference** → read 2–3 disagreements aloud. Ask the room: model wrong, or human coding debatable? (With names, `U` boundary cases always surface — that's the point.)
5. Edit the prompt or a codebook description → **Update Preview** → the κ moves. Do one full loop on screen; then give the room ~2 minutes to loop on their own. Caveat if asked: preview reliability is computed on the visible page only — bump Rows per page to 100 for a steadier number.

## 0:33 – 0:37 · Run All + review (live)

1. **Run All**. While it runs, open **Advanced settings → Run All processing** and explain the two radios: **Reprocess all rows** (default, replaces the column) vs **Fill missing only** (keeps your manual codes, fills the gaps). Mention Temperature (0 = deterministic) in one breath.
2. Progress in the banner + sidebar **Tasks**; **Stop** exists.
3. **Annotation Review**: same Compare To / matrix / filters, now full-table. Set a **Correction** column (`gender.ai.correction` is auto-suggested), correct one row, mention **Use as example** feeds corrections back as few-shot examples.
4. One-liner to close the loop: the coded column is ordinary data now — filter it, chart it in Trends, or export CSV from the Export view.

## 0:37 – 0:42 · Your own data

Free play: own CSV, harder problem than names — stance, sentiment, topic, policy claims. You and helpers circulate. Anyone without data: try improving κ on the names task, or code the tweets block (`text` column) for topic instead.

## 0:42 – 0:45 · Take it home (slide 8)

Say these plainly, in order:

1. **The workshop key dies today.** Own key, or a local model (Add Provider → Custom → any OpenAI-compatible local server: Ollama, LM Studio) — then data never leaves the machine.
2. **Ethics, slowly**: *"Which model, which provider, and whether your data may leave your machine at all — that's your ethics approval's call, not the tool's. Check before you code real data."*
3. Pilot → measure agreement → revise → document. Prompt, codebook, model, κ — all belong in the methods section.
4. Keep Wordflow: `sih.tools/wordflow`; Feedback button freely; cite via the sidebar quote icon.

Thank the room. Done on time.

---

## If things break

| Symptom | Do |
|---|---|
| Binder won't start / no AAF | Desktop app; if neither, pair with a neighbour |
| Excel/zip import fails | Expected in 0.7.1 — CSV instead |
| Shared key rate-limited (429 / failed batches) | Switch room to `:free` gemma models; preview-only is still a complete lesson |
| Provider error strip in Preview | **Retry** button; check the key was pasted whole |
| Model list won't load | Free-type the exact model id (e.g. `google/gemini-2.5-flash-lite`) — the field accepts typed names |
| Run All finishes "with N failed batches" | Rows left blank — rerun with **Fill missing only** |
| Way behind at 0:33 | Skip Run All; the preview loop already carried the payload. Jump to slide 8 at 0:42 sharp |
