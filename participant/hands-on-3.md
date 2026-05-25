# Session 3 — Repurpose the lens + Free lab (50 min)

**Time: 3:40 pm – 4:30 pm**

Two halves: a short conceptual demo (3.A), then a free lab (3.C) where you pick what to try.

---

## 3.A — Repurpose the lens (15 min) — 👀 WATCH ONLY

A short demonstration from the facilitator. No keyboards needed. Three quick moves that show **you shape the analysis at every step — in, through, and out.**

### Demo 1 — Export the visualisation (3 min)

The facilitator will open a Session 1.5 visualisation (e.g. the Frequency word cloud) and use the **download icon at the top-right of each visualisation or table** to save it. Image views (cloud, dispersion, bubble chart) save as **PNG**; list / table views save as **CSV** (the data behind the visualisation).

> 🎯 The lesson: your analysis isn't trapped in the tool. The same export options exist in Trends, Topic Modelling, Concordance, and Quotation.

### Demo 2 — Filter the visualisation → Add to Workspace (5 min)

Visualisations aren't just for looking. You can pick parts of them and turn that selection into new analysable data. The facilitator will:

1. Open a Trends snapshot. **Click in the legend** to hide or isolate individual lines (e.g. focus on `lnpcuts` only).
2. **Click** a data point — or **click + Shift-click** to select a range (e.g. a campaign peak or a date window). **Add the selection to the workspace** as a new data block.
3. Quickly mention the same pattern in two other tools:
   - **Topic Modelling**: click bubbles to select topics → Detach → new blocks. (Same move you saw in Session 2.)
   - **Concordance**: click + Shift-click hit markers in the dispersion view to select tweets → Add to Workspace.

> 🎯 The lesson: in every visual tool, *seeing* something interesting and *making it new data* is one move, not two.

### Demo 3 — Create a column → Trends becomes a histogram (5 min)

Trends isn't only a "lines over time" tool. The x-axis doesn't have to be a date column.

The facilitator will:
1. On the **Honi Soit articles** block: **Preprocessing → Create column** = word count per article.
2. **Trends** tool. Set the **x-axis to the new word-count column** (not the date).
3. **Numeric bucketing — 100 intervals.** Fine-grained, so we can see the distribution shape.
4. **Switch the chart from line to bar.** Now Trends is a **histogram** — article count per word-length bucket.

> 🎯 Land: *"The tool didn't change. I changed how I shaped the data."*

That's the most important sentence in this workshop. Every tool in Wordflow is a lens. The interesting research question is always: **which lens, on which slice, will tell me something I didn't already know?** That's your job. Wordflow makes the lens-changing cheap.

### One more thing — feedback

After landing the third demo, the facilitator will click the **Feedback button** (bottom of the left sidebar) on screen to show you the form. **Use it twice today:**
- During the lab in a minute — every time something is confusing, surprising, or broken.
- Later — if you keep using Wordflow after the workshop, send a note about what you'd want next.

---

## 3.B — Lab framing + feedback ask (5 min)

The facilitator will introduce the three lab tracks. Pick one before you start — but you can switch if your track stalls.

**One ask before you start:** as you click around in the lab, every time you hit something **confusing, surprising, or broken**, tap the **Feedback button** (bottom of the left sidebar, next to Tutorial). Even one word. We read every one — you're our v0.5 beta room.

---

## 3.C — Free lab (25 min)

Three tracks. Pick whichever fits where you are.

### Track A — Continue Session 2

You watched some of Session 2 but didn't get to follow every step. Now's the time.

1. Load whichever **checkpoint workspace archive** matches where you stopped following:
   - `Checkpoint_A.zip` — start from the gender-split point.
   - `Checkpoint_C.zip` — start from the aggregated Concordance block.
2. Pick a step you watched and try it yourself:
   - The **regex with three keywords** in Concordance.
   - The **dispersion view + visual select** to make a new block.
   - The **topic modelling + detach + group in Trends** sequence.
3. Save your result as a snapshot when you have something you like.

### Track B — Bring your own data

You brought a CSV. Brave.

1. **Data Loader → Upload your file.** Wordflow expects CSV / TSV / Excel / Parquet. UTF-8 encoded.
2. If you get a Dtype warning: accept it. Wordflow is standardising your column types.
3. Verify the import — click the new block, look at the Data Viewer.
4. **Try one thing.** Not everything. Pick whichever fits your data:
   - **Concordance** on a text column.
   - **Frequency** with stopwords on.
   - A **Filter** to a subset, then any analysis on the subset.

Realistic warning: data ingestion is the most common stumbling block. If you hit a wall after 10 minutes, **switch to Track A or C**. There's value in doing one thing well; less value in fighting a CSV.

The facilitator and helpers are around — flag them down.

### Track C — Open exploration

Pick any sample dataset (Honi Soit, QLD 2020 tweets, or the 2025 Federal Election NewsTalk/Reddit bundle — all imported during Session 1.5). Pick any tool you haven't really used.

Some quick prompts:

- **Comparative Frequency on Honi Soit** by year — what changed between 2021 and 2022?
- **Concordance** for a politically loaded word in QLD tweets — how is it weaponised?
- **Trends on the Federal Election Reddit data** with a different grouping — what hidden patterns emerge?
- **Topic Modelling on the Federal Election Reddit data** — sample to ~5,000 documents first (full corpus is slow).
- **Quotation Extraction on Honi Soit** — who got quoted most? About what?

---

## Wrap-up (4:25 pm – 4:30 pm)

The facilitator will close. Three things to take home:

1. **Install Wordflow locally** — desktop link is on **cutt.ly/wordflow** (same URL you used today). The cloud version is fine for trying; the desktop or Python install is what you want for real research work.
2. **Cite the project** if you publish using it. Citation on the docs site.
3. **Feedback button** — keep using it. Bug reports, improvement advice, "I need more", or "this rocks" — all helpful.

And spread the word. If you have a colleague who works with text and doesn't want to learn code, they should know this exists.

---

## If you remember one phrase from today

> **The text flows. The lens changes.**

That's it.
