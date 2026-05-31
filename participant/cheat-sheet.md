# Wordflow Cheat Sheet

*Printable double-sided handout. Page 1 = glossary, Page 2 = UI map + shortcuts.*

---

## Page 1 — Glossary

### Workspace
Your project folder, saved automatically. Holds all your data and analyses for one project. You can have many — create, switch, import or export workspaces inside the **Data Loader** tool.

### Data block
A spreadsheet of texts. One row = one document. For each analysis you choose **one string column** as the text to analyse; the remaining columns then act as metadata (date, author, category, etc.). That choice isn't fixed to the block — a block can hold several text columns (e.g. title, abstract, body), and you can analyse any of them the same way. The fundamental analytic unit in Wordflow.

### Graph (workspace graph view)
The visual map of all data blocks in your workspace and how they're derived from each other. Most transformations create a new child block, leaving the parent intact; a few operations (adding, renaming or removing a column) change a block in place — but every in-place change is easily undone, so nothing is destructive. **Read the graph back-to-front to see your method.**

### Tool
A way of working with a data block. Wordflow's tools come in three kinds:

- **Data in / out** — **Data Loader** and **Export**.
- **Shaping the data** — **Preprocessing**, plus column-level edits in the **Data Viewer**.
- **Asking questions** — the five analysis tools (Concordance, Frequency, Trends, Topic Modelling, Quotation), each asking a different question of a chosen text column.

| Tool | What it's for |
|---|---|
| **Data Loader** | Bring data in — import sample data or your own files, set the text language, and create / switch / import / export workspaces. |
| **Preprocessing** | Reshape a block — Filter, Sample, Join, Stack, Find, Create. Each step makes a new block or column. |
| **Concordance** | "Where does this word appear, and what comes before and after?" |
| **Frequency** | "What words appear most often?" (and: comparative mode for two blocks) |
| **Trends** | "How does this corpus change over time, or over any numeric axis?" |
| **Topic Modelling** | "What themes group these documents?" |
| **Quotation** | "What are people quoted as saying, and who said it?" (English only) |
| **Export** | Take your data with you — download one or more data blocks in your chosen file format, individually or bundled as a zip archive. |

### Stacking
The core idea of this workshop: you build a workflow by taking the output of one tool and feeding it into the next. Filter your tweets to one gender → run comparative frequency vs the other → click a word → jump to Concordance → switch to a multi-pattern regex → **Add to Workspace** as a new block → run Topic Modelling on that. Chaining blocks and tools like this *is* your method.

*Don't confuse this with the **Stack** step in Preprocessing — that's one specific operation that combines the rows of two blocks into a single block. "Stacking" the concept is the whole chaining idea.*

### Snapshot
A saved capture of a finished analysis — the tool, its parameters, and its results — so you can re-open it later or share it with a colleague without re-running anything.

Turn on **Snapshot Mode** (the **pencil icon next to the "VIEWS" title** in the sidebar) to save and load snapshots inside each analysis tool: **camera icon** = save, **folder icon** = load. Once you load a snapshot into a tool, *that tool's view* becomes read-only — you can still hover, click visualisations, and switch views, but not change parameters or rerun. Other tools (and any new analysis) stay fully editable, and Snapshot Mode can stay on the whole time — it only locks a tool *after* you load a snapshot into it.

### Workspace archive
A portable export of your entire workspace — all data blocks, derivations, and metadata — as a single file. Different from snapshots: a snapshot captures one tool's view; a workspace archive captures the whole project. Import to recreate the workspace on another machine (or another participant's instance).

### Feedback button
The **Feedback** button at the bottom of the left sidebar (next to Tutorial). Tap it any time something is confusing, surprising, or broken. Even one word helps the developers — they read every one.

### Add to Workspace
The button in each tool's results panel (Concordance, Frequency comparative, Trends selection, Topic Modelling, Preprocessing). Turns the current result or selection into a new derived data block in your workspace. Useful for "I want to take these results and analyse them further in another tool."

### Tokenise
Available from the data-block **menu icon**. Pre-computes a word-tokenised version of your text column. Required for Tokens-mode Concordance, especially for languages like Chinese / Japanese where there's no space between words. For English you usually don't need this manually.

### Stopword
A common word like "the", "a", "is" — frequent enough to drown out everything else. **Important:** stopwords are always included when an analysis runs; hiding them is a *post-processing* step applied to the results afterwards, not a removal before the analysis. The stopword toggle (and the right-click → add-to-stopwords shortcut) only changes what's displayed — the underlying computation still counts every word.

---

## Page 2 — UI map

```
Wordflow  
┌──────────────────┬────────────────────────┬──────────────────────┐
│                  │ Tool interface         │ Workspace graph view │
│ VIEWS            │  controls + results    │  your data blocks,   │
│  Data Loader     │  for the selected      │  linked left → right │
│  Preprocessing   │  tool                  │                      │
│  Frequency       │  Load / Save           ├──────────────────────┤
│  Concordance     │  snapshot top-right    │ Data view            │
│  Trends          │                        │  selected block as   │
│  Topic Modelling │                        │  a table — click a   │
│  Quotation       │                        │  row for full text   │
│  Export          │                        │                      │
│                  │                        │                      │
│ DATA BLOCKS      │                        │                      │
│ TASKS            │                        │                      │
│ Tutorial·Feedback│                        │                      │
└──────────────────┴────────────────────────┴──────────────────────┘
```

### Numbered guide

1. **Tool sidebar** — pick a tool. Each asks a different question.
2. **Workspace graph view** — all your data blocks and the links showing how they're derived; the graph flows left → right.
3. **Tasks** (left sidebar) — live progress for slow tasks (Topic Modelling, large imports).
4. **Data Viewer** — selected block as a scrollable table. **Click a row to see full document content.**
5. **Tool interface** (the central panel) — controls and output. **Camera icon** = save snapshot, **folder icon** = load snapshot.
6. **Help (`?`)** — every control with a `?` opens the relevant tutorial section.
7. **Feedback** — bottom of the left sidebar, next to Tutorial. Use it. Often.
8. **Data Loader** also hosts workspace operations — **Create workspace**, switch active workspace, **Import / Export workspace archive**. (The **Snapshot Mode toggle** is the pencil icon next to the "VIEWS" title in the sidebar.)

### Common tasks — where to click

| To do this | … click here |
|---|---|
| Run an analysis | a tool in the sidebar + a data block in the graph |
| Make a new data block | Preprocessing → Filter/Sample/Join/Stack/Find/Create → Add to Workspace |
| Comparative frequency | select two blocks, then Frequency tool |
| Jump from a word to its context | click the word in Frequency's list/cloud |
| Make Concordance results a new block | click **Add to Workspace** on the results panel |
| Select from a visualisation | click a point, or click + Shift-click for a range |
| Save a result | camera icon in the tool header |
| Re-open a saved result | folder icon in the tool header → Load snapshot |
| Import a workspace archive | Data Loader → Import workspace archive |
| Export a workspace archive | Data Loader → Export workspace archive |
| Rename a block | block's menu icon → Rename |
| Delete a block | block's menu icon → Delete (children get deleted too) |
| Toggle Snapshot Mode | sidebar → pencil icon next to "VIEWS" |
| Send feedback | Feedback button, bottom of the left sidebar |
