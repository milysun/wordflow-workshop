# Session 3 — Repurpose the lens + Free lab (50 min)

**Time: 2:10 – 3:00**

Two halves: a short conceptual demo (3.A), then a free lab (3.C) where you pick what to try.

---

## 3.A — Repurpose the lens (15 min) — 👀 WATCH ONLY

A short demonstration from the facilitator. No keyboards needed.

The point: **the meaning of an analysis isn't fixed by which tool you clicked. It's defined by how you shape the data you put into that tool.**

### Quick word count

Frequency isn't only a "top words" tool. With stopwords off and Top-N very high, the **total token count** in the summary panel IS your word count — per corpus, per group. Word count is just frequency with the words ignored.

### Trends as a histogram

Trends isn't only a "lines over time" tool. The x-axis doesn't have to be a date column.

The facilitator will:
1. **Create a new column** on a tweets block: word count per tweet (number of tokens per row).
2. **Trends** tool — set the x-axis to the new word-count column, not the date.
3. **Numeric bucketing**: 0-10 words, 10-20, 20-30...
4. Now Trends is showing a **histogram** — tweet count per word-length bucket.
5. Add a grouping by gender — histogram of tweet length, split by gender. Are the women writing longer or shorter tweets?

> 🎯 Land: *"The tool didn't change. I changed how I shaped the data."*

That's the most important sentence in this workshop. Every tool in Wordflow is a lens. The interesting research question is always: **which lens, on which slice, will tell me something I didn't already know?** That's your job. Wordflow makes the lens-changing cheap.

---

## 3.B — Lab framing + feedback ask (5 min)

The facilitator will introduce the three lab tracks. Pick one before you start — but you can switch if your track stalls.

**One ask before you start:** as you click around in the lab, every time you hit something **confusing, surprising, or broken**, tap the **feedback heart icon** (top right). Even one word. We read every one — you're our v0.5 beta room.

---

## 3.C — Free lab (25 min)

Three tracks. Pick whichever fits where you are.

### Track A — Continue Session 2

You watched some of Session 2 but didn't get to follow every step. Now's the time.

1. Load whichever **checkpoint workspace archive** matches where you stopped following:
   - `session2-after-A.wordflow-workspace` — start from the gender-split point.
   - `session2-after-C.wordflow-workspace` — start from the aggregated Concordance block.
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

Pick any sample dataset (Honi Soit, Reddit, or QLD tweets — all imported during Session 1.5). Pick any tool you haven't really used.

Some quick prompts:

- **Comparative Frequency on Honi Soit** by year — what changed between 2021 and 2022?
- **Concordance** for a politically loaded word in QLD tweets — how is it weaponised?
- **Trends on Reddit** with a different grouping — what hidden patterns emerge?
- **Topic Modelling on Reddit** — sample to ~5,000 documents first (full corpus is slow).
- **Quotation Extraction on Honi Soit** — who got quoted most? About what?

---

## Wrap-up (2:55 – 3:00)

The facilitator will close. Three things to take home:

1. **Install Wordflow locally** — link in tonight's email. The cloud version is fine for trying; the desktop or Python install is what you want for real research work.
2. **Cite the project** if you publish using it. Citation on the docs site.
3. **Feedback button** — keep using it. Bugs, "this is confusing", "this rocks" — all helpful.

And spread the word. If you have a colleague who works with text and doesn't want to learn code, they should know this exists.

---

## If you remember one phrase from today

> **The text flows. The lens changes.**

That's it.
