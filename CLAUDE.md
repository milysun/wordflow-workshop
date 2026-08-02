# CLAUDE.md — working notes for Claude

Read this before editing files in this repo. Read `README.md` for the workshop design itself.

## This branch: online workshop, 28 August 2026

This branch (`online_workshop_2026-08-28`) holds a **one-day online workshop on Wordflow v0.7.x** combining the June intro workshop and the July CAITG session: **Session 1** (90 min, morning, demo-only, **recorded**) is a condensed intro — concepts, interface, multi-tool research workflow; **Session 2** (90 min, after lunch, hands-on, **not recorded**) is the Annotation-tool GenAI coding exercise. `README.md` on this branch is the canonical structure. This workshop's deliverables:

- `slides/online-s1-intro.html` + `slides/online-s2-annotation.html`
- `facilitator/runbook-online-s1.md`, `runbook-online-s2.md`, `pre-workshop-checklist-online.md`
- `participant/hands-on-annotation-online.md`
- `communications/pre-workshop-email-online.md`, `post-workshop-email-online.md`

Older files are sources, not deliverables: the June 3-hour materials (`slides/index.html`, `facilitator/runbook.md`, `participant/hands-on-*.md`) are **v0.5-era** — check every UI claim against the v0.7 list below before reusing; the CAITG files (`slides/caitg-annotator.html`, `facilitator/runbook-caitg.md`, `participant/hands-on-annotator.md`) are already v0.7-accurate for the Annotation tool.

Known v0.7.1 issue to keep in materials until fixed: **Excel spreadsheet and zip-archive import are broken** — participants should use CSV/plain text. (Verify against the shipping 0.7.x before the day.)

## v0.7 UI facts (verified against v0.7.1 code, 2026-08-02) — these override any v0.5-era bullet below

- **Snapshot Mode is GONE.** No per-tool snapshot save/load, no snapshot banners, no "Demo Snapshots" tab in the sample-import dialog, no `.ldaca-snapshot` files. The pencil next to the **Views** header is now only **"Edit visible views"** (view visibility checkboxes — nothing else). Never mention Snapshot Mode in v0.7 materials.
- **Sample data import**: Data Loader → **"Import sample data"** button → dialog **"Import sample content"** — a single flat list of collections (no tabs), status chips **"✓ Imported"** / **"○ Remote"**, button **"Import selected"**. Collections: `ADO — Queensland Election Tweets`, `SCL — Honi Soit Student Newspaper`, `ADO — Reddit (Australian News)`.
- **Sidebar sections**: **Views**, **Data Blocks**, **Tasks**. Tool order: `Data Loader, Preprocessing, Frequency, Concordance, Trends, Topic Modeling, Quotation, Annotation, Export`. **"Topic Modeling" is one-L in the sidebar.** Footer buttons: **"Help"** (renamed from v0.5's "Tutorial") and **"Feedback"**. Header icons: About, **"Cite LDaCA Wordflow"**, Settings cog. The working-directory display moved from the sidebar footer to **Settings → Workspace**.
- **Multi-tab system**: analysis views (Frequency, Concordance, Trends, Topic Modeling, Quotation, Annotation) run in Chrome-style tabs. The tab strip shows when **Settings → General → "Enable multi-tab"** is on (default OFF) or when >1 tab exists. "+" = new tab ("Analysis N"); **rename = click the already-active tab a second time** (no double-click, no right-click); X closes; drag reorders. Data Loader, Preprocessing, Export are not tabbed. Facilitator machines should have multi-tab ON.
- **Workspace archive = the checkpoint mechanism.** Export: **Export view → "Export Workspace" → "Export workspace archive"** (or Data Loader → Workspace manager → row **"Download"**) → `<Name>.zip`. Import: **Data Loader → Workspace manager → "Upload workspace"** (only `.zip`; **no drag-and-drop for archives**) → then click **"Load"** on the new row (upload does NOT auto-load). Restores: data blocks (materialised parquet), tabs (name/kind/order), and all *terminal* analyses with parameters + results. Does NOT restore: active tab, per-tab display settings, or the tool's **input selections** (device-local) — after loading a checkpoint, participants may need to re-select the data block/columns in the tool. **Archives contain no API keys or credentials** (provider keys live outside the workspace), so checkpoint files are safe to distribute.
- **Preprocessing sub-tabs**: `Filter, Sample, Join, Stack, Find, Create, Expression` (v0.5's "Polars Expression" → "Expression"). New **"Apply result as"** control: **"Create new Data Block"** vs **"Update"**.
- **Still true in v0.7**: "Add to Workspace" is the publication button everywhere; right-click a Frequency word adds it to the **"Stop words filter (N)"**; per-visualisation download icons (image→PNG, table→CSV); double-click a graph node adds it to the active tool; block/column actions via menu icons (never right-click).
- **Hints**: v0.5 hint system replaced by **Settings → Guidance** ("Show contextual hints", "Reset Contextual Hint history"). Don't reference the old hint bubbles.
- **In-app docs lag**: `Help` content (ui.md etc.) still describes v0.5 names ("Token Frequency", "Trends and Sequence", working directory in sidebar) and omits Annotation — don't quote in materials without checking, and expect participants to notice discrepancies.
- **Slide asset warning**: `slides/images/ui-overview.png` is a v0.5 screenshot — retake on v0.7 before the day (sidebar differences are visible: Annotation entry, Help button, no working-directory footer).

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
