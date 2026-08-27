# CLAUDE.md — working notes for Claude

Read this before editing files in this repo. Read `README.md` for the workshop design itself.

## This branch: online workshop, 28 August 2026

This branch (`online_workshop_2026-08-28`) holds a **one-day online workshop on Wordflow v0.7.x** combining the June intro workshop and the July CAITG session: **Session 1** (90 min, morning, demo-only, **recorded**) is a condensed intro — concepts, interface, multi-tool research workflow; **Session 2** (90 min, after lunch, hands-on, **not recorded**) is the Annotation-tool GenAI coding exercise. `README.md` on this branch is the canonical structure. This workshop's deliverables:

- `slides/online-s1-intro.html` + `slides/online-s2-annotation.html`
- `facilitator/runbook-online-s1.md`, `runbook-online-s2.md`, `pre-workshop-checklist-online.md`
- `participant/hands-on-annotation-online.md`
- `communications/pre-workshop-email-online.md`, `post-workshop-email-online.md`

Earlier deliveries' materials (June 3-hour intro, CAITG winter school) were **removed from this branch on 2026-08-27** because participants browse it via the pre-workshop email's link. They live on `intro_workshop_2026-06-03` and `caitg_winter_school_2026-07-30`; consult those branches for v0.5-era sources (check every UI claim against the v0.7 list below) and for the CAITG Annotation-tool files (already v0.7-accurate). Additional deliverables on this branch: `facilitator/demo-checklist-s1.md`, `facilitator/run-of-show-online.html`, `facilitator/stress-test-openrouter.py`, `communications/promo-blurbs-online.*`, `artifacts/online-2026-08-28/`.

Excel and zip-archive import, broken in v0.7.1, are **fixed in the current release** (verified by Chao 2026-08-27); no CSV-only caveats in materials.

## v0.7 UI facts (verified against v0.7.1 code, 2026-08-02) — these override any v0.5-era bullet below

- **Snapshot Mode is GONE.** No per-tool snapshot save/load, no snapshot banners, no "Demo Snapshots" tab in the sample-import dialog, no `.ldaca-snapshot` files. The pencil next to the **Views** header is now only **"Edit visible views"** (view visibility checkboxes — nothing else). Never mention Snapshot Mode in v0.7 materials.
- **Sample data import**: Data Loader → **"Import sample data"** button → dialog **"Import sample content"** — a single flat list of collections (no tabs), status chips **"✓ Imported"** / **"○ Remote"**, button **"Import selected"**. Collections: `ADO — Queensland Election Tweets`, `SCL — Honi Soit Student Newspaper`, `ADO — Reddit (Australian News)`.
- **Sidebar sections**: **Views**, **Data Blocks**, **Tasks**. Tool order: `Data Loader, Preprocessing, Frequency, Concordance, Trends, Topic Modelling, Quotation, Annotation, Export`. **"Topic Modelling" (two Ls) since v0.7.2** (v0.7.1 had the one-L US spelling). Footer buttons: **"Help"** (renamed from v0.5's "Tutorial") and **"Feedback"**. Header icons: About, **"Cite LDaCA Wordflow"**, Settings cog. The working-directory display moved from the sidebar footer to **Settings → Workspace**.
- **Multi-tab system**: analysis views (Frequency, Concordance, Trends, Topic Modelling, Quotation, Annotation) run in Chrome-style tabs. The tab strip shows when **Settings → General → "Enable multi-tab"** is on (default OFF) or when >1 tab exists. "+" = new tab ("Analysis N"); **rename = click the already-active tab a second time** (no double-click, no right-click); X closes; drag reorders. Data Loader, Preprocessing, Export are not tabbed. Facilitator machines should have multi-tab ON.
- **Workspace archive = the checkpoint mechanism.** Export: **Export view → "Export Workspace" → "Export workspace archive"** (or Data Loader → Workspace manager → row **"Download"**) → `<Name>.zip`. Import: **Data Loader → Workspace manager → "Upload workspace"** (only `.zip`; **no drag-and-drop for archives**) → then click **"Load"** on the new row (upload does NOT auto-load). Restores: data blocks (materialised parquet), tabs (name/kind/order), and all *terminal* analyses with parameters + results. Does NOT restore: active tab, per-tab display settings, the tool's **input selections** (device-local), or the **Annotation prompt / tool parameters** (the prompt is not part of the codebook block; verified 2026-08-27) — after loading a checkpoint, participants may need to re-select the data block/columns in the tool. **Archives contain no API keys or credentials** (provider keys live outside the workspace), so checkpoint files are safe to distribute.
- **Preprocessing sub-tabs**: labels unchanged (`Filter, Sample, Join, Stack, Find, Create, Expression`) but v0.7.2 internals were refactored: **Expression takes a closed JSON DSL, not Polars code** (each row is `{"expression": {"op": ...}, "alias": ...}`; ops: arithmetic/comparison/boolean binaries, `not/is_null/is_not_null/abs/lowercase/uppercase/year/month/day/sum/mean/min/max/count/n_unique`, string `contains/starts_with/ends_with`, cast, round, concat_str; contexts filter/with_columns/select/sort/group_by_agg). **Create is a row-wise sum-of-terms builder over the same DSL** (tokens = column chips or literals, joined with `add`, emitted in `with_columns` context; `add` on strings concatenates, so e.g. first_name + ' ' + last_name works per row; optional per-token ops are only Count/Sum/Mean, which broadcast a scalar). **There is NO word-count or string-length operation anywhere** (the v0.5 word-count Create preset is gone; ldaca-wordflow#68 filed for Alex). New **"Apply result as"** control: **"Create new Data Block"** vs **"Update"**.
- **Still true in v0.7**: "Add to Workspace" is the publication button everywhere; right-click a Frequency word adds it to the **"Stop words filter (N)"**; per-visualisation download icons (image→PNG, table→CSV); double-click a graph node adds it to the active tool; block/column actions via menu icons (never right-click).
- **Hints**: v0.5 hint system replaced by **Settings → Guidance** ("Show contextual hints", "Reset Contextual Hint history"). Don't reference the old hint bubbles.
- **In-app docs lag**: `Help` content (ui.md etc.) still describes v0.5 names ("Token Frequency", "Trends and Sequence", working directory in sidebar) and omits Annotation — don't quote in materials without checking, and expect participants to notice discrepancies.

## What this repo is

Materials for Chao's **LDaCA Wordflow** workshop series for university researchers (mostly HASS, mostly limited coding capability, HDR students to senior academics), one branch per delivery. This branch is the 28 August 2026 online workshop; see the top of this file.

The **north star** (from README) is: *"text data flows through stackable, single-purpose tools, and the meaning of an analysis comes from how you shape your data, not from the tool itself."* Don't soften or rewrite this without checking with Chao.

## How the pieces fit together

Four parallel "channels" of content, each in its own folder:

- `slides/online-s1-intro.html`, `slides/online-s2-annotation.html` — what's on screen
- `facilitator/runbook-online-s1.md`, `runbook-online-s2.md`, `demo-checklist-s1.md`, `run-of-show-online.html` — Chao's scripts, click lists, and wall-clock panel for the same moments
- `participant/hands-on-annotation-online.md` — what attendees follow at their machine in Session 2
- `communications/` — pre/post emails and promo copy

They describe the **same two sessions** from different angles. The session structure is canonical in `README.md` (the table under "Session structure"). When something changes in one channel, it almost always needs to change in the others.

`facilitator/pre-workshop-checklist-online.md` is Chao-only.

## Cross-file consistency — the rule that matters most

When timing, chapter structure, tool names, or the demo plan changes, several files have to move together. Before declaring an edit done, check these match each other:

- **Session timing / chapters**: `README.md` tables → deck housekeeping and roadmap slides → `runbook-online-s1.md` / `demo-checklist-s1.md` clock gates → `run-of-show-online.html` rows.
- **S2 task facts** (226 rows, `theme.reference`, codes `Promise`/`Cuts`/`Other`, shared key deleted at 15:30): hands-on sheet → S2 deck → runbook-online-s2 → panel copy bank → pre-workshop checklist.
- **Version wording**: participant-facing files say "the latest v0.7 release" and ask people to accept the in-app update prompt; never pin a patch number in participant materials.
- **Screen-share setup** (full MBP screen, cursor kit): demo checklist pre-flight → panel prep rows → pre-workshop checklist §5.

When in doubt: grep across the whole repo for the thing you're changing before saving.

## Slide deck constraints

Each deck (`slides/online-s1-intro.html`, `slides/online-s2-annotation.html`) is a single self-contained HTML file. It must stay **offline-fine**.

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
- Avoid hype words ("revolutionary," "powerful," "cutting-edge"). Match the existing tone — see `runbook-online-s1.md` for the spoken voice and `hands-on-annotation-online.md` for the written voice.
- Time is precious — every sentence in a slide or hands-on sheet should pull its weight.

## Workflow expectations

- Chao is iterating: expect frequent small edits to wording, timing, and slide content. Prefer focused commits over batch ones.
- When making a non-trivial change, summarise what moved and which other files probably need a follow-up pass — don't silently update one channel and leave the others stale.
- Use `git status` and `git diff` to sanity-check before committing on Chao's behalf.

## Participant data: never commit it

This repo goes public later, so **no file in the tracked tree may carry participant
names, emails, or affiliations.** A printed sign-in sheet (`attendance_sheet.html`,
38 real names) was committed on the June branch and had to be purged from git
history on 2026-08-14. Don't recreate that situation.

- Participant data lives in `private/` only, which is gitignored, along with
  `attendance_sheet*.html`, `participants*.csv` and similar patterns. See
  `private/README.md`.
- `private/participants.csv` is the rolling register across all deliveries: one row
  per person per event, keyed on lowercased email, with a `promo_opt_in` column. It
  answers both "who may be emailed about future workshops" and "who are the return
  participants".
- The authoritative copy belongs in University-approved storage (Sydney Box /
  OneDrive / SharePoint), not a laptop or a personal cloud account.
- **Every workshop's post-workshop email must carry the opt-in block** (see the
  "Hearing about the next one" section in `communications/post-workshop-email-online.md`).
  Registration alone is not consent to be emailed about later events. Blank in the
  register means *never asked*, which is not consent. Open public sessions should
  also ask at registration via an unticked Eventbrite checkbox.
- The June 2026 cohort was never asked and received one one-off email on 2026-08-14
  about the 28 August repeat. That was a directly related follow-up, not a standing
  permission, and it isn't a precedent for later sends.

## What lives outside this repo

- The actual Wordflow snapshots and workspace archives referenced in the runbook live in cloud storage (Sydney Box / OneDrive / SharePoint / GitHub release). They're not committed here.
- The feedback form and Binder URL are separate links Chao manages.
- Participant registers and sign-in sheets: see the section above.

## Project repo

Remote: `https://github.com/milysun/wordflow-workshop` (**public**; participants are linked to this branch, so keep it free of other deliveries' files and of any participant data).
