# CLAUDE.md — working notes for Claude

Read this before editing files in this repo. Read `README.md` for the workshop design itself.

## This branch: CAITG Winter School, 30 July 2026

This branch (`caitg_winter_school_2026-07-30`) holds a **45-minute hands-on session** on Wordflow **v0.7.1**'s new **Annotation** tool (GenAI-assisted text coding), delivered at the CAITG (Centre for AI, Trust and Governance) Winter School. Its materials are **new files alongside** the June intro-workshop ones:

- `slides/caitg-annotator.html` — 8-slide minimal intro deck (first ~8 minutes only; the rest is live)
- `facilitator/runbook-caitg.md` — the 45-minute minute-by-minute
- `participant/hands-on-annotator.md` — the participant step sheet

The 3-hour intro-workshop files (`slides/index.html`, `facilitator/runbook.md`, `participant/hands-on-*.md`, …) are the **June 2026 workshop's** materials; on this branch they are reference/reuse sources, not the deliverable. Two notes below are **superseded for this branch**: the Annotation tool is now released and is the session's centrepiece (the "not yet usable" bullet described v0.5), and the session runs on **v0.7.1**, not v0.5.

Known v0.7.1 issue to keep in materials: **Excel spreadsheet and zip-archive import are broken** — participants should use CSV/plain text.

## What this repo is

Materials for a single 3-hour in-person workshop introducing **LDaCA Wordflow** to university researchers — mostly HASS, mostly limited coding capability, ranging from HDR students to senior academics. The workshop is one piece of a larger series Chao is developing.

The **north star** (from README) is: *"text data flows through stackable, single-purpose tools — and the meaning of an analysis is shaped by how you shape your data, not by the tool itself."* Don't soften or rewrite this without checking with Chao.

## How the pieces fit together

Four parallel "channels" of content, each in its own folder:

- `slides/index.html` — what's projected on the screen
- `facilitator/runbook.md` — Chao's minute-by-minute script for the same moments
- `participant/hands-on-*.md` — what attendees follow at their machine for the same sessions
- `communications/` — pre/post emails to attendees

They describe the **same three sessions** from different angles. The session structure is canonical in `README.md` (the table under "Session structure"). When something changes in one channel, it almost always needs to change in the others — see the consistency checklist below.

`facilitator/pre-workshop-checklist.md`, `common-questions.md`, and `timing-recovery.md` are Chao-only references.

## Cross-file consistency — the rule that matters most

When timing, session numbering, tool names, or the demo storyline changes, several files have to move together. Before declaring an edit done, check these match each other:

- **Session timing**: `README.md` table → `slides/index.html` (housekeeping slide + any per-section title slides) → `facilitator/runbook.md` (section headers + minute timestamps) → `facilitator/timing-recovery.md` (cut points reference these times)
- **Session numbering** (`1.0`, `1.5`, `2`, `3.A`, `3.B`, `3.C`, `3.D`): used as section anchors in runbook and hands-on sheets. If a section is renamed, grep the whole repo before saving.
- **Tool names** in the snapshot tour — currently 5: **Frequency, Concordance, Trends, Topic, Quotation**. If the count changes, `README.md` "Tunable parameters" + `hands-on-1.md` + the snapshot-tour slides all need updating.
- **Try this / follow along** markers in `hands-on-2.md` — these are an explicit promise to less-confident participants (key moves to **try this**; the rest to **follow along**, no pressure, with a per-phase checkpoint as the safety net). If a phase's marker changes, the slide badge, the hands-on header, and the runbook header must all match. Current map: A/B/C-1 = follow along; C-2/D/E = try this.
- **Pre-workshop checklist** in `facilitator/pre-workshop-checklist.md` lists the snapshots and the workspace archive. If the demo storyline changes, the list of required snapshots changes.

When in doubt: grep across the whole repo for the thing you're changing before saving.

## Slide deck constraints

`slides/index.html` is a single self-contained HTML file. It must stay **offline-fine** — Chao runs it from a projector in rooms that may not have wifi.

- Do **not** add `<script src="https://cdn...">` or `<link href="https://...">` — no external CDN dependencies.
- Inline everything: CSS in `<style>`, JS in `<script>`, any small image data-uri'd or stored locally next to the file.
- The CSS variables at the top (`--ink`, `--paper`, `--accent`, …) are the design system. Use them rather than hard-coding new colours.
- Keep the file readable as a single document — don't extract CSS/JS to separate files even for "cleanup."

## Wordflow UI specifics worth remembering

A few UI details that are easy to get wrong in materials (and have been corrected once already):

- **Feedback button**: bottom of the **left sidebar**, next to Tutorial. Icon is `MessageSquare` from `lucide-react` (a small square speech-bubble outline, `h-4 w-4`). **Not** a heart, not at the top-right.
- **Snapshot Mode toggle**: the **pencil icon next to the "VIEWS" header** in the left sidebar. **Not** in a top menu. When ON, it enables snapshot save/load in each **analysis tool** only — Frequency, Concordance, Trends, Topic Modelling, Quotation. Data Loader, Preprocessing and Export don't have snapshots. A tool's view goes read-only **only after** a snapshot has been loaded into *that* tool — other tools (and any fresh analysis you start) stay fully editable. **Snapshot Mode can be left ON during workspace-building** — it doesn't lock anything by itself. **Never write "turn off Snapshot Mode before building"** in materials — it's not necessary.
- **Working directory**: shown in the sidebar but only relevant for the local-install desktop app. Ignore it for Binder/cloud workshop demos.
- **Annotation tool** (v0.5-era note, superseded on this branch): was "visible but not yet usable" in v0.5; **released in v0.7** and is this branch's whole session. Sidebar label is exactly **"Annotation"** — not "AI Annotator" / "AI Annotation". Key v0.7.1 UI facts: **Manual/AI** toggle; **Annotation Column → Start new annotation** dialog creates the column (no `.ai` suffix suggested — that's Chao's naming habit); the **Codebook** is a normal data block (**Create New** → **Edit codebook** dialog, Code + Description rows); providers via **Add Provider** (OpenRouter default; API key write-only; Custom = any OpenAI-compatible base URL); **Model** field is a free-text combobox over the provider's live model list (no hard-coded catalogue); **Preview** is display-only (per-page, 10–100 rows); **Compare To** offers Percent Agreement / Cohen's Kappa (default) / Krippendorff's Alpha, with the **confusion matrix in the score badge's hover tooltip**; **Run All processing** radios are **"Reprocess all rows"** (default) vs **"Fill missing only"**; corrections via the **Correction:** dropdown (suggests `<column>.correction`) and **Use as example** feeds them back as few-shot examples. No cost/token estimate is shown anywhere.
- **Visualisation selection** is by **click** (single point) or **click + Shift-click** (range / multi-point), *not* click-and-drag. Topic Modelling bubbles support **multi-click only** — no range, no drag-rectangle. Applies to Trends chart points, Concordance dispersion hit markers, Topic Modelling bubbles.
- **Download / export icons** sit on each individual **visualisation or table** (top-right corner), *not* a single export button in the tool header. Image views save **PNG**, list / table views save **CSV**. Each view exports independently.
- **Right-click is reserved for in-tool visualisation shortcuts, NOT for block/column management.** Specifically: **Frequency cloud/list — right-click a word to add it to stopwords** (it hides instantly). There may be other in-tool right-click actions in future tools. **Block-level actions (Rename, Clone, Tokenise, Undo, Redo, Delete) come from a menu icon on the data block itself.** The same icon shape appears at the end of each column header for column-level actions. **Never write "right-click → Rename / Delete / ..." for block or column management** — use "open the block's menu icon" or "open the column menu" instead. The Frequency stopword shortcut IS an exception worth documenting in materials.
- **"Add to Workspace" is the button name.** Each tool's results panel (Concordance, Frequency comparative, Trends selection, Topic Modelling, Preprocessing operations) has an **`Add to Workspace`** button that turns the current result into a new data block. Don't write "add as data block" / "add as block" / "add as a new block" — write *"click Add to Workspace"* (the button name) and, if needed, *"…which creates a new data block"* for the description. **Never write "Detach"** — that's internal code/API naming only (e.g. `concordanceDetach`, `ConcordanceDetachRequest`), never shown anywhere in the UI; the user-facing action is always "Add to Workspace".
- **Click vs left-click**: Wordflow doesn't distinguish, so write *"click"* not *"left-click"* in materials. The Frequency → Concordance word-jump is just *"click a word"*.
- **QLD Election 2020 dataset join key** is **`username`** (NOT `candidate_id`). The `qldelection2020_candidate_tweets` block and `candidate_info_gender` block both have a `username` column — left join on that.

## Voice and tone

- Concrete, warm, no jargon. The audience is curious researchers, not engineers.
- Address the room as "you," not "users" or "participants" (the facilitator runbook is the exception — it talks *about* participants).
- Avoid hype words ("revolutionary," "powerful," "cutting-edge"). Match the existing tone — see `runbook.md` for the spoken voice and `cheat-sheet.md` for the written voice.
- Time is precious — every sentence in a slide or hands-on sheet should pull its weight.

## Workflow expectations

- Chao is iterating: expect frequent small edits to wording, timing, and slide content. Prefer focused commits over batch ones.
- When making a non-trivial change, summarise what moved and which other files probably need a follow-up pass — don't silently update one channel and leave the others stale.
- Use `git status` and `git diff` to sanity-check before committing on Chao's behalf.

## What lives outside this repo

- The actual Wordflow snapshots and workspace archives referenced in the runbook live in cloud storage (Sydney Box / OneDrive / SharePoint / GitHub release). They're not committed here.
- The feedback form and Binder URL are separate links Chao manages.

## Project repo

Remote: `https://github.com/milysun/wordflow-workshop` (private during development; will be made public later).
