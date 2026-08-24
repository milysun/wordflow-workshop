# Runbook — Online workshop Session 1 (90 min, recorded)

> **Rewritten 2026-08-24** to Chao's full-capability demo plan: eight per-tool chapters instead of
> the June-derived tour + research story. The QLD tweets + jobs/cuts question is a **thread**
> through the chapters (and the afternoon's Annotation theme), not the spine. Click-level detail
> lives in `demo-checklist-s1.md`; wall-clock rows in `run-of-show-online.html`. Some parameters
> are **TBC** until the Wednesday test.

**Wordflow: concepts, interface, and a full-capability tour · Friday 28 August 2026 · 11:00 am – 12:30 pm AEST (9:00 – 10:30 am AWST) · Zoom**

This session is **all demo, no participant hands-on**, so you control the clock completely. It is **recorded** and the recording is designed for reuse as per-tool tutorial chapters: narrate for the future viewer, say what you're clicking, read short bits of screen text aloud, **say each chapter name as you enter it and leave a beat of silence at every chapter boundary** (those are the edit points). The demo window is a hard **70–75 minutes**.

**Setup before start**: fresh app state (no workspace — you create one on camera), multi-tab ON, contextual hints ON (you turn them off as a demo), a demo CSV ready for drag-and-drop, backup archives reachable. Full list in `pre-workshop-checklist-online.md`.

---

## 11:00 – 11:12 · Slides (title → roadmap)

**START THE RECORDING before you speak.** Title + Acknowledgement of Country (~3 min). How today works: say the recording sentence verbatim and early (*"this session is recorded and shared afterwards; the afternoon hands-on is not"*), the watching contract (*"nothing to install for this half; watch, and put questions in the chat — I'll take them at two marked pauses"*), and the pace warning (*"this morning is deliberately dense; the recording has every click"*). Who built this + why (north-star sentence slowly). Three ways to run it. Then the roadmap slide (eight chapters, one workspace) and the dataset slide, which sets an **exploratory stance**: no research question, no conclusions promised; we poke at the campaign language and follow what looks interesting; the point is what Wordflow lets you notice. Don't forecast the afternoon here (the lunch slide does that; not everyone returns). Privately, your connective tissue is still the jobs/cuts language recurring across chapters, and gender is just a convenient binary split: use both without announcing them as claims.

## 11:12 · Ch 1 — Getting around (9 min)

Live app, empty state. A contextual hint is on screen: acknowledge it, then Settings → Guidance → hints off, saying where they come back. Views sidebar top-to-bottom (pause on Annotation: *"this afternoon's tool"*). Create a workspace. **Import sample data**: QLD Election Tweets + Honi Soit, Import selected. Drag-and-drop the demo CSV (*"any CSV or plain text you have — drop it in"*). Add to Workspace + preview it. Graph view and Data view: rename a column, change a column type, click one row to read a full record (*"management lives here, not in menus you have to hunt for"*). Help, ? marks, Feedback (*"under active development; the Feedback button is how you talk to us"*).

## 11:21 · Ch 2 — Preparing data (12 min + 1 min pause)

Dtype passes: `created_at` → datetime, `gender`/`party` → category; one prepared sentence for the string dtype label (TBC pending v0.7.3). Preprocessing sub-tabs in one breath. **Create** `full_name` (first_name + " " + last_name) with **Update** mode, and name the Update/Create-new-block choice. **Join**: tweets FIRST, on `username`, left join → `tweets_full`; landing line: *"data prep is part of the analysis — the join is a research decision."* **Filter**: gender F, gender M, and the negated `^[Rr][Tt]` regex → originals (*"remember this negate trick; it returns this afternoon"*). Graph view glance: the tree is growing. Sample and Find, one breath each.

**★ Chat pause #1 (11:33, 1 min).** Chapter beat.

## 11:34 · Ch 3 — Frequency (10 min)

**Honi Soit single corpus (6):** add the block (show the ways to add + the colour picker), pick the text column, tokeniser line (multilingual). Word cloud: 50 words, English stopwords, **right-click a word to stopword it** (the crowd-pleaser), manual add/remove in the list. List view: max words, wildcard filter, count + rank. Recolour the block.

**Comparative (4):** clear results, add `tweets_F` + `tweets_M`. Side-by-side then juxtaposed/overuse view; size/colour/algorithm in two sentences. Stopword the campaign noise live (names, `lnpqld`). Read it honestly: mixed words (`cases`, `qldjobs`) vs somewhat polarised ones (`cuts`, `teachers` / `committed`, `leader`) — *"differences exist but they're modest; for politicians, party matters far more than gender — the split is here to show the comparison move."* Then the exploration payoff: *"cases was everywhere in 2020 — years later, can you still say what it meant?"* — **click the word** and let Wordflow carry you into Concordance, where the context gives the answer back (the pandemic). Suggestive, not conclusive; that's what exploration is for. Chapter beat happens mid-flight; still say it.

## 11:44 · Ch 4 — Concordance (11 min + 1 min pause)

**Tweets (6):** you arrived with the query prefilled — that's the point, say it. Context windows, Text/Tokens modes, RegEx/punctuation/case options, **Preview vs Run All** (*"you'll meet this pair everywhere"*), L1/R1 table anatomy, Show metadata → full_name. Then the thread move: query → RegEx `job(s)?|cut(s)?`, Run All, and ⭐ **Add to Workspace** → `tweets_jobcut` (*"this button is the whole design: any result can become data"*). Show the new node's extraction column; for long documents this is a keyword-centred corpus builder. Sort the review table.

**Honi Soit dispersion (5):** clear, switch corpus, RegEx `student(s)?|staff|union`, Run All. Dispersion view: where in each document the hits fall, % position, colours, uncased, legend filtering. Select on the plot (click, Shift-click), bin size, chart type, Add to Workspace from a selection; contrast the aggregated-contexts block with the table-view block from before.

**★ Chat pause #2 (11:55, 1 min).** Chapter beat.

## 11:56 · Ch 5 — Trends (8 min) — and the background kickoff

**First 40 seconds, without ceremony:** new tab → Topic Modelling on Honi Soit → Run; new tab → Quotation on Honi Soit → Run All; point at **Tasks**: *"long jobs run in the background — we'll collect both later."* This is a feature demo disguised as logistics.

Then Trends proper: `tweets_full`, x = `created_at`, daily; group by gender; graph type + frequency/count settings; the meaning line (*"the trend is whatever your input block makes it"*). Switch the block to `tweets_jobcut`: group by matched text (jobs vs cuts over time), then add gender for the combined legend — read whatever gap shows without overselling it (*"a modest difference; the useful thing is that grouping by any column is one click — swap gender for party and it's a different study"*). Legend filtering, click selection, top bar. Visual selection → Add to Workspace. Chapter beat.

## 12:04 · Ch 6 — Topic Modelling (12 min)

BERTopic in three sentences (embeddings, not bag-of-words; no tokeniser to pick). Configure **before** running: sampling, segmentation (*"tweets are too short to segment — this matters for articles"*), **min topic size 7, topics 40, seed TBC**. Run on `tweets_F` + `tweets_M`; the ~90 s wait is your chat buffer, with three jobs visible in Tasks. Bubble chart: size, colour mixed by corpus percentage, tooltips, re-aggregation of topic count, top-topics-per-doc, word number/stopwords, word filter (not wildcard). Selection: clicks (lasso TBC), then **text filter "job" → 5 topics → select all → Add to Workspace** as `topic_job` (per-document rows + topic distribution column; per-topic detach is on the roadmap, say so). Open the finished background Honi Soit run: topic distribution on long documents *(first cut if late)*. Then the thread pays off: Trends on `topic_job`, job topics over time × gender. Chapter beat.

## 12:16 · Ch 7 — Quotation (4 min)

Open the background Quotation tab — finished while we worked. Review, click one row for the quote in context, Add to Workspace (quote becomes a column), one research scenario, and the honest line: English-only. Chapter beat.

## 12:20 · Ch 8 — Export & workspaces (2 min)

Per-visualisation download icons (PNG/CSV). Export workspace archive → ZIP. Upload workspace → Load: everything returns, tabs included — *"exactly how this afternoon's checkpoint files work."*

## 12:22 · Recap + bridge (2 min)

The arc, spoken plainly: Concordance is word-based; Topic Modelling is powerful but interpretively vague; for precision and confidence you **code** your data; manual coding doesn't scale; AI-assisted coding with a human-defined standard does. *"That's this afternoon: the Annotation tool."*

## 12:24 – 12:30 · Closing slides

Landing (say it twice) → three takeaways (name reveal on #3) → lunch slide: walk the install once aloud (Windows SmartScreen More info → Run anyway; macOS first-open Open), afternoon not recorded, keyboards required, model access provided. Flash data acknowledgements.

**STOP THE RECORDING.** Then the **install clinic** (12:30, ~15 min, off the record) with Alex + Seb. Leave the lunch slide up; keep the Zoom meeting open.

---

## Timing discipline

| Gate | Must be starting | If late, cut (in order) |
|---|---|---|
| 11:34 | Ch 3 Frequency | — (trim Ch2's Sample/Find breaths) |
| 11:56 | Ch 5 Trends | dispersion detail 4b.5–6 |
| 12:16 | Ch 7 Quotation | Honi Soit TM walkthrough (6.6) |
| 12:24 | closing slides | Quotation to 2 min; Ch8 to 1 min |

F-list extras (Stack, Trends histogram via Expression, non-English tokenisation, combined filters) only enter if a gate shows 5+ minutes ahead — realistically they won't.

## If things break

| Symptom | Do |
|---|---|
| A build step misbehaves | Load the next section's backup archive and keep the narrative moving; the recording matters more than liveness. |
| Live TM run stalls | Backup workspace's finished tab; narrate there. |
| Background jobs unfinished when reached | Show Tasks honestly, pull the result from the backup workspace. |
| Screen share lags / font small | Bump app zoom (Cmd/Ctrl +); check the Zoom preview. Last resort: drop to window share (keeps the enlarged pointer, loses click ripples). |
