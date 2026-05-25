# CLAUDE.md — working notes for Claude

Read this before editing files in this repo. Read `README.md` for the workshop design itself.

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
- **Try this / watch only** markers in `hands-on-2.md` — these are an explicit promise to less-confident participants. If the runbook adds a new "try this" moment, the hands-on sheet must mark it too.
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
- **Snapshot Mode toggle**: the **pencil icon next to the "VIEWS" header** in the left sidebar. **Not** in a top menu. When ON, it enables snapshot save/load in each **analysis tool** only — Frequency, Concordance, Trends, Topic Modelling, Quotation. Data Loader, Preprocessing and Export don't have snapshots. A tool's view becomes read-only only after a snapshot is loaded into *that* tool — other tools stay editable.
- **Working directory**: shown in the sidebar but only relevant for the local-install desktop app. Ignore it for Binder/cloud workshop demos.
- **AI Annotation tool**: visible in the sidebar's tool list but **not yet usable** (under development). Excluded from all workshop materials.

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
