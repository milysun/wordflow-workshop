# Wordflow Cheat Sheet

*Printable double-sided handout. Page 1 = glossary, Page 2 = UI map + shortcuts.*

---

## Page 1 — Glossary

### Workspace
Your project folder, saved automatically. Holds all your data and analyses for one project. You can have many. Switch between them in the top bar.

### Data block
A spreadsheet of texts. One row = one document. One column = the text; other columns = metadata (date, author, category, etc.). The fundamental analytic unit in Wordflow.

### Graph (workspace graph view)
The visual map of all data blocks in your workspace and how they're derived from each other. Each transformation creates a new child block; originals are never modified. **Read the graph back-to-front to see your method.**

### Tool
A way of asking a question of a data block. Tools include:

| Tool | What it answers |
|---|---|
| **Data Loader** | "Where does my data come from? What language is it in?" |
| **Preprocessing** | "What subset / combination / transformation of my data do I want?" — Filter, Sample, Join, Stack, Find, Create |
| **Concordance** | "Where does this word appear, and what comes before and after?" |
| **Frequency** | "What words appear most often?" (and: comparative mode for two blocks) |
| **Trends** | "How does this corpus change over time, or over any numeric axis?" |
| **Topic Modelling** | "What themes group these documents?" |
| **Quotation** | "What are people quoted as saying, and who said it?" (English only) |
| **Export** | "Get my data and results out of Wordflow." |

### Stacking
The most important verb in this workshop. You stack tools by taking the output of one and feeding it to another. Filter your tweets to one gender → run comparative frequency vs the other gender → left-click a word → jump to concordance → switch to a multi-pattern regex → add results as a new block → run topic modelling on that. You build a workflow by chaining blocks.

### Snapshot
A small file (`.ldaca-snapshot`) that captures a finished analysis — tool, parameters, results — so you can re-open it or send it to a colleague without re-running. Saved per tool from the camera icon.

### Snapshot Mode
A sidebar toggle (the **pencil icon next to the "VIEWS" title**) that enables saving and loading snapshots inside each analytical tool. Once you load a snapshot into a tool, *that tool's view* becomes read-only — you can still hover, click visualisations, and switch views, but you can't change parameters or rerun. Other tools stay editable as normal. **Turn it OFF for general workspace-building.**

### Workspace archive
A portable export of your entire workspace — all data blocks, derivations, and metadata — as a single file. Different from snapshots: a snapshot captures one tool's view; a workspace archive captures the whole project. Import to recreate the workspace on another machine (or another participant's instance).

### Feedback button
The heart icon at the top right. Tap it any time something is confusing, surprising, or broken. Even one word helps the developers — they read every one.

### Detach
A right-click action on a data block (or on selected topics in Topic Modelling) that splits selection into a new derived block. Useful for "I want to analyse just these rows further."

### Tokenise
A right-click action that pre-computes a word-tokenised version of your text column. Required for Tokens-mode Concordance, especially for languages like Chinese / Japanese where there's no space between words. For English you usually don't need this manually.

### Stopword
A common word like "the", "a", "is", that's frequent enough to drown out everything else. Most analyses can hide them with one toggle.

---

## Page 2 — UI map

```
┌──────────────────────────────────────────────────────────────┐
│  [TOOL CHOICE]  [DATA SELECTION]  [TASK CENTRE]  [♥ FEEDBACK]│
│                                                              │
│  ┌──────────────────────┐    ┌──────────────────────────┐    │
│  │ Tool list (sidebar)  │    │ Workspace graph view     │    │
│  │ - Data Loader        │    │  (your data blocks here) │    │
│  │ - Preprocessing      │    │                          │    │
│  │ - Concordance        │    └──────────────────────────┘    │
│  │ - Frequency          │    ┌──────────────────────────┐    │
│  │ - Trends             │    │ Data viewer              │    │
│  │ - Topic Modelling    │    │  (selected block as      │    │
│  │ - Quotation          │    │   a table; click a row   │    │
│  │ - Export             │    │   for full content)      │    │
│  └──────────────────────┘    └──────────────────────────┘    │
│                              ┌──────────────────────────┐    │
│                              │ Tool interface           │    │
│                              │  (controls + results,    │    │
│                              │   camera = save snapshot)│    │
│                              └──────────────────────────┘    │
│                                                              │
│  [WORKING DIRECTORY]               [HELP & FEEDBACK ?]       │
└──────────────────────────────────────────────────────────────┘
```

### Numbered guide

1. **Tool sidebar** — pick a tool. Each asks a different question.
2. **Workspace graph view** — all your data blocks; arrows show derivations.
3. **Task Centre** — progress for slow tasks (Topic Modelling, large imports).
4. **Data Viewer** — selected block as a scrollable table. **Click a row to see full document content.**
5. **Tool Interface** — controls and output. **Camera icon** = save snapshot. **Folder icon** = load snapshot.
6. **Help (`?`)** — every control with a `?` opens the relevant tutorial section.
7. **Feedback (♥)** — top right. Use it. Often.
8. **Top menu** — workspace switcher, workspace archive import/export. (The **Snapshot Mode toggle** lives in the sidebar — pencil icon next to the "VIEWS" title.)

### Three-second moves

| To do this | … click here |
|---|---|
| Run an analysis | a tool in the sidebar + a data block in the graph |
| Make a new data block | Preprocessing → Filter/Sample/Join/Stack/Find/Create → Add to Workspace |
| Comparative frequency | select two blocks, then Frequency tool |
| Jump from a word to its context | left-click the word in Frequency's list/cloud |
| Make Concordance results a new block | right-click results → Add as data block |
| Select from a Dispersion plot | click-and-drag in the visual |
| Save a result | camera icon in the tool header |
| Re-open a saved result | folder icon in the tool header → Load snapshot |
| Import a workspace archive | Workspace switcher → Import workspace archive |
| Export a workspace archive | Workspace switcher → Export workspace archive |
| Rename a block | double-click its name in the graph |
| Delete a block | right-click → Delete (children get deleted too) |
| Toggle Snapshot Mode | sidebar → pencil icon next to "VIEWS" |
| Send feedback | heart icon, top right |

### One-line rule

> **A tool always asks a question. A preprocessing step always makes a new block. Read the graph back-to-front to see what you did.**
