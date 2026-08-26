# S1 demo checklist — every click, in order (recorded session)

> Rewritten 2026-08-24 from Chao's handwritten plan: the demo is a **full capability tour in
> eight chapters**, cut for reuse as per-tool tutorial chapters. The QLD tweets + jobs/cuts
> question is a **thread**, not the spine; it returns as the afternoon's Annotation theme.
> Companion files: `run-of-show-online.html` (wall-clock), `runbook-online-s1.md` (spoken script).
> Items marked **TBC** get pinned by the Wednesday test (`pre-workshop-checklist-online.md` §2).
>
> **Chapter discipline for the recording**: say each chapter name out loud as you enter it and
> leave a beat of silence at every boundary; those are the edit points for cutting tutorials.

## The six mistakes that would hurt the recording

1. **Recording**: START at the title slide, STOP after the lunch slide. Nothing else matters if this is wrong.
2. **Join order**: pick `tweets` FIRST in the Join tool. First pick = left table.
3. **Set the Topic Modelling parameters BEFORE the live run** (min topic size 7, topics 40, seed **TBC**): re-running because you forgot costs 2+ minutes on camera.
4. **Kick off the background jobs at the start of Chapter 5** (Honi Soit Topic Modelling + Quotation Run All). Miss it and Chapters 6.5 and 7 have nothing to show.
5. **Drag-and-drop demo uses a CSV.** Excel/zip import was broken in v0.7.1; unless Wednesday proves it fixed, do not drag an xlsx on camera.
6. **Clock gates** (below): when you hit one late, cut in this order: F never starts → Honi Soit TM walkthrough (6.5) → dispersion detail (4b.5–6) → Quotation to 2 min.

## Clock gates (wall time; recording starts 11:00)

| 11:12 | 11:21 | 11:34 | 11:44 | 11:56 | 12:04 | 12:16 | 12:20 | 12:24 |
|---|---|---|---|---|---|---|---|---|
| Ch1 | Ch2 | Ch3 | Ch4 | Ch5 + background jobs | Ch6 | Ch7 | Ch8 | closing slides |

---

## 0 · Pre-flight (before the recording starts)

- [ ] Wordflow final release (v0.7.3 if shipped, else v0.7.2). **Fresh state: no workspace open** — Chapter 1 creates one on camera.
- [ ] **Settings → General → Enable multi-tab = ON**; contextual hints **ON** (Chapter 1 turns them off as a demo).
- [ ] A small demo **CSV** in an easy folder for the drag-and-drop step (file choice TBC).
- [ ] Section backup workspace archives reachable without hunting (rebuild list in the pre-workshop checklist).
- [ ] **Display layout**: Wordflow full screen on the MBP built-in display; deck also presented from the MBP display; this panel + everything else on the external screen. Zoom shares the **entire MBP screen** (needed so cursor/click effects reach the feed and the recording). DND on, notifications off (doubly important with whole-screen share).
- [ ] **Cursor kit active**: macOS pointer enlarged + coloured fill (Accessibility → Display → Pointer) and the click-effect app running (Mouzz or equivalent); effects verified in the Wednesday share test.
- [ ] Zoom: check readability in the Zoom preview at 720p.

**▶ START THE RECORDING at the title slide.** Slides until ~11:12, then live app.

---

## Ch 1 · Getting around · 11:12 (9 min)

- [ ] 1.1 A contextual **hint** is visible on screen; acknowledge it, then Settings cog → **Guidance** → turn **Show contextual hints** OFF. Say where it re-enables (same switch + "Reset Contextual Hint history").
- [ ] 1.2 **Views** sidebar: the tool list top to bottom (point at Annotation: "this afternoon"); click between two tools to show switching.
- [ ] 1.3 Create a new workspace (Data Loader → workspace creation; exact button wording **TBC**).
- [ ] 1.4 **Import sample data** → dialog "Import sample content" → select `ADO — Queensland Election Tweets` AND `SCL — Honi Soit Student Newspaper` → **Import selected**. SEE: blocks appear in Data Blocks.
- [ ] 1.5 **Drag and drop** the demo CSV onto the Data Loader. SEE: upload lands. (CSV only; see mistake #5.)
- [ ] 1.6 **Add to Workspace** the uploaded file; preview it.
- [ ] 1.7 **Graph view + Data view**: select a block to view; **rename a column** and **change a column type** via the column menu; **click one row** to preview the full record.
- [ ] 1.8 Sidebar footer: **Help**, contextual **?** marks, **Feedback** ("under active development; use it").

## Ch 2 · Preparing data · 11:21 (12 min)

- [ ] 2.1 Data view dtype passes: `tweets.created_at` → **datetime**; candidate block `gender`, `party` → **category**. One-sentence explainer for the string dtype label (shows as "Utf8View"; may be renamed in v0.7.3 — **TBC**, has a prepared sentence either way).
- [ ] 2.2 Preprocessing sub-tabs in one breath: Filter, Sample, Join, Stack, Find, Create, Expression.
- [ ] 2.3 **Create**: new column `full_name` = [first_name] + `" "` + [last_name] on the candidate block. Show the **Apply result as** control: "Update" vs "Create new Data Block" — use **Update** here so the join carries it. SEE: real full names, one per row.
- [ ] 2.4 **Join**: `tweets` **FIRST** (left) + candidate block, key `username` both sides, left join → `tweets_full`. SEE: row count unchanged from tweets; gender/party/full_name aboard.
- [ ] 2.5 **Filter** ×2 on `tweets_full`: `gender = F` → `tweets_F`; `gender = M` → `tweets_M`. Then one text filter: regex `^[Rr][Tt]` **negated** → originals block (the afternoon reuses this trick; say so). *(Cut if late: the by-time early/late filter — moved to optional F.4 territory.)*
- [ ] 2.6 Glance at the **graph view**: the derivation tree is growing; point at the node states (red-dot markers **TBC** wording).
- [ ] 2.7 **Sample** and **Find**: one breath each, no build.
- [ ] 2.8 ★ Recap + chat pause (1 min, 11:33). Chapter boundary beat.

## Ch 3 · Frequency · 11:34 (10 min)

### 3a · Single corpus: Honi Soit (6 min)

- [ ] 3.1 Add the Honi Soit block to Frequency: show the ways to add (quick-select · double-click the graph node · in-tool selector — confirm the third **TBC**) and the block **colour picker**.
- [ ] 3.2 Select the text column; **tokeniser selection** (multilingual support in one sentence).
- [ ] 3.3 **Word cloud mode**: word number → **50** · stopwords ON → **English** · **right-click a word** → joins "Stop words filter (N)" and vanishes · open the stopword list, add one manually, remove one.
- [ ] 3.4 **List view mode**: word number → max · **wildcard filter** · token count + rank columns · right-click-to-stopword works here too.
- [ ] 3.5 Change the block colour; SEE: visualisation recolours.

### 3b · Comparative: tweets_F vs tweets_M (4 min)

- [ ] 3.6 **Clear results**; add `tweets_F` + `tweets_M`.
- [ ] 3.7 Side-by-side clouds → the juxtaposed/overuse cloud (mode names **TBC**); explain size, colour, algorithm in two sentences.
- [ ] 3.8 Stopword the campaign noise live: candidate names, `lnpqld`, etc.
- [ ] 3.9 Read the result lightly, no editorialising: mixed words (`cases`, `qldjobs`) vs somewhat polarised (`cuts`, `teachers` / `committed`, `leader`); let people form their own impression. (If asked: party matters more than gender for politicians; the split is just a convenient binary, and grouping works with any variable.)
- [ ] 3.10 Exploration payoff on **cases**: "everywhere in 2020 — can you still say what it meant?" → **click the word** → Concordance opens and the context answers (the pandemic). Suggestive, not conclusive. Chapter boundary beat.

## Ch 4 · Concordance · 11:44 (11 min)

### 4a · Tweets, from "cases" to the jobs/cuts block (6 min)

- [ ] 4.1 SEE: arrived from the word-click with the query prefilled. Interface: left/right **context windows**, search mode **Text / Tokens**, the **RegEx / punctuation / case** options.
- [ ] 4.2 **Preview vs Run All** (name the pattern: "you'll see this pair in many tools").
- [ ] 4.3 Table view: **L1/R1** columns explained; **Show metadata** → bring in `full_name`.
- [ ] 4.4 The thread move: change the query to RegEx `job(s)?|cut(s)?` → Run All. SEE: both patterns coloured.
- [ ] 4.5 ⭐ **Add to Workspace** (say the button name; this is the publication move of the whole app) → block `tweets_jobcut`. Metadata columns selected in 4.3 travel with it.
- [ ] 4.6 View the new node in the Data view: the **conc_extraction** column (**TBC** exact name): for long documents this builds a keyword-centred corpus.
- [ ] 4.7 Sort the review table; filter (**TBC** whether filter exists here).

### 4b · Honi Soit, dispersion mode (5 min)

- [ ] 4.8 **Clear results**; switch block to Honi Soit; RegEx mode, no punctuation; pattern `student(s)?|staff|union` → Run All.
- [ ] 4.9 Switch to **Dispersion view**: aim (where in each document the hits fall), % relative position, colour-coded patterns, uncased option, legend filtering.
- [ ] 4.10 Selection on the plot: **click** a marker, **click + Shift-click** a range · bin size · chart type · **Add to Workspace** after selecting.
- [ ] 4.11 Review the new block: aggregated contexts; contrast with the table-view Add to Workspace from 4.5.
- [ ] 4.12 One-breath summary. ★ Chat pause (1 min, 11:55). Chapter boundary beat.

## Ch 5 · Trends · 11:56 (8 min)

- [ ] 5.0 **FIRST, kick off the background jobs** (mistake #4): new tab → Topic Modelling on Honi Soit → Run; new tab → Quotation on Honi Soit → Run All. Point at sidebar **Tasks**: "long jobs queue in the background; we'll come back to both." *(If Wednesday shows Quotation needs longer than ~20 min, move its kickoff to the start of Ch3.)*
- [ ] 5.1 Trends on `tweets_full`: x = `created_at`, frequency **daily**. SEE: tweet volume over the campaign.
- [ ] 5.2 Add **group: gender**; read the lines.
- [ ] 5.3 Change graph type; change the frequency/count setting.
- [ ] 5.4 Say the meaning line: the trend is whatever the input block makes it.
- [ ] 5.5 Switch the data block to `tweets_jobcut` (from 4.5): same tool, new story.
- [ ] 5.6 Group by the **matched text**: `job(s)` vs `cut(s)` lines over time.
- [ ] 5.7 Add gender → combined legend; read the gap without overselling ("modest difference; the point is that grouping by any column is one click — swap gender for party and it's a different study").
- [ ] 5.8 Legend filtering · click selection · the top bar's meaning.
- [ ] 5.9 Visual selection → **Add to Workspace**. Summary breath. Chapter boundary beat.

## Ch 6 · Topic Modelling · 12:04 (12 min)

- [ ] 6.1 One-slide-worth intro aloud: BERTopic, embedding-based, not bag-of-words.
- [ ] 6.2 Configure the live run on `tweets_F` + `tweets_M` **before running** (mistake #3): no tokeniser (embeddings) · sampling option for large corpora · **segmentation** (tweets too short to segment; articles are where it shines) · **min topic size = 7 · topics = 40 · seed TBC** (must reproduce the 5 job topics).
- [ ] 6.3 **Run.** The 60–90 s wait is the chat-question buffer; point at **Tasks** (three jobs now: this one plus the two from 5.0).
- [ ] 6.4 Bubble chart review: size · colour (**mix by percentage** between the two corpora) · tooltip (representative words, doc count) · number of topics / **re-aggregation** control (**TBC** v0.7.2 wording) · top-topics-per-doc · word number + stopwords · word filter (**not** wildcard — say it).
- [ ] 6.5 Selection: click bubbles · **lasso** (**TBC**: existed nowhere in v0.7.1; confirm before promising) · clear · text filter → type **job** → SEE: 5 topics remain → select all 5 → **Add to Workspace** as `topic_job`. SEE: per-document block + **topic distribution column**. Mention: per-topic detach planned in a future release.
- [ ] 6.6 Open the **background Honi Soit run's tab** (finished by now): topic distribution on long documents; parameters **TBC**. *(First thing cut if late.)*
- [ ] 6.7 The thread pays off: Trends on `topic_job` → job topics **over time × gender**. Chapter boundary beat.

## Ch 7 · Quotation · 12:16 (4 min)

- [ ] 7.1 Open the background Quotation tab. SEE: Run All finished over lunch of chapters.
- [ ] 7.2 Review outcomes; **click one row** to preview quote-in-context.
- [ ] 7.3 **Add to Workspace** → the quote becomes a column (output column names **TBC**).
- [ ] 7.4 One scenario of use, and the honest line: English-only. Chapter boundary beat.

## Ch 8 · Export & workspaces · 12:20 (2 min)

- [ ] 8.1 Flash the per-visualisation download icons: image = PNG, table = CSV, each view independently.
- [ ] 8.2 **Export view → Export Workspace → Export workspace archive** → ZIP.
- [ ] 8.3 **Data Loader → Workspace manager → Upload workspace → Load**: the whole method comes back, tabs included. "That is exactly how this afternoon's checkpoint files work."

## Recap + bridge · 12:22 (2 min)

- [ ] Concordance is word-based; Topic Modelling is powerful but interpretively vague. For precision and confidence you code: manual coding → doesn't scale → AI-assisted coding with human-defined standards. "That's this afternoon: the Annotation tool."
- [ ] Back to slides: landing → takeaways → lunch slide.

**■ STOP THE RECORDING** after the lunch slide. Then the install clinic, starting whenever Session 1 ends (off the record, ~15 min).

---

## F · Optional additions (only if a gate shows you 5+ min ahead)

| # | Item | Where it slots |
|---|---|---|
| F.1 | Stack tool (Preprocessing) | after 2.5 |
| F.2 | Trends histogram of candidate activity (Expression group-by; the two JSONs are in the panel copy bank) | after 5.9 |
| F.3 | Tokenisation on non-English text | after 3.2 |
| F.4 | Advanced filter with combined conditions (and the by-time early/late filter) | after 2.5 |

## If a step breaks mid-recording

| Symptom | Do |
|---|---|
| A build step misbehaves | Load the next section's backup archive (Workspace manager → Upload workspace → Load; re-select blocks/columns) and keep moving. The recording matters more than liveness. |
| Live Topic Modelling run stalls | Show the pre-run backup workspace's finished tab; narrate there. |
| Background job (Honi Soit TM / Quotation) not finished when reached | Say so honestly ("still chewing — that's real"), show the Tasks progress, and pull the result from the backup workspace. |
| You said something wrong | Correct it on camera in one sentence and move on. Don't restart the recording. |
