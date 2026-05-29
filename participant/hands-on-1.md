# Session 1.5 — Snapshot tour

**Time: 30 minutes** *(1:55 pm – 2:25 pm in the schedule)*

You've just finished a tour of the Wordflow interface. Now you'll touch each of the five analytic tools — without setting any of them up. You're loading **pre-baked snapshots** to see what each tool produces, so when we build something together in Session 2 you'll know what you're aiming at.

---

## Setup (first 5 minutes)

Follow the facilitator's screen.

1. **Data Loader → Import sample data.** A modal opens with two tabs that import separately:
   - **Datasets** — select all three (**Honi Soit**, **QLD election 2020 tweets**, and the **2025 Federal Election NewsTalk/Reddit** bundle) and click **Import selected**.
   - **Demo Snapshots** — switch to this tab, select all five (the Session 1.5 tour snapshots), and click **Import selected** again.
   *(You won't use it all today, but it'll be ready later.)*
2. **Click the pencil icon next to the "VIEWS" title in the left sidebar** — that's the **Snapshot Mode** toggle. Turn it ON. This enables saving and loading snapshots inside each analytical tool. Once you load a snapshot into a tool, *that tool's view* becomes read-only (you can hover, click, and switch views, but you can't change parameters). Other tools stay editable as normal.
3. **Create a new workspace** called `Wordflow`. Click **Create workspace** inside the **Data Loader** tool — Wordflow's hint system will highlight the button on first use. You'll keep using this same workspace through Session 2 and Session 3.

Tell your neighbour if anything didn't work. Flag the facilitator if you're stuck.

---

## Tool 1 — Frequency *(2:00 pm – 2:05 pm)*

1. **Frequency** tool in the left sidebar.
2. Click the **folder icon (Load snapshot)** in the tool header.
3. Pick **`Freq_Analysis_Newstalk`**. Wait a second.

**Look at:** the **two-column comparative view**. Each column is a *grouping* of news outlets drawn from the same `newstalk_stories` corpus:

- **Left-leaning** — Guardian Australia + Independent Australia.
- **Right-leaning** — Sky News Australia + PerthNow.

Bigger words = more frequent in that group's stories. Stopwords already filtered.

**Try this:**
- 🔁 Switch from **Cloud** to **List** view to see exact counts.
- 🔁 Find a word that appears high on one side and is small or absent on the other — that's where the lens is doing real work.
- 🔁 Hover over or click a word to see its rank on the opposite side.
- 🔁 **Right-click a word** (cloud or list) — it's added to stopwords and disappears from the display. Handy for hiding tokens you don't care about.

> What you're seeing: comparative frequency, not just frequency. The grouping (left vs right) is a *research assumption* — regroup the same corpus differently and the comparison changes. The data didn't change; the lens did.

---

## Tool 2 — Concordance *(2:05 pm – 2:10 pm)*

1. **Concordance** tool in the left sidebar.
2. **Load snapshot** → **`SCL_Honi_Soit`**.

**Look at:** every match of a **regex pattern** — `student\w*|staff|universit\w+` — across the Honi Soit student-newspaper corpus. That's three patterns at once:

- anything starting with **student** (student, students, studentship…),
- the word **staff** exactly,
- anything starting with **universit** (university, universities, universities'…).

Each pattern gets its own colour, both in the row table and in the dispersion plot.

**Try this:**
- 🔁 Switch view to **Dispersion**. Each bar is one document; the coloured marks show where each pattern lands in that document.
- 🔁 Hover over a row in the table to see the full sentence.
- 🔁 Edit the regex in the search box — results recompute live, no rerun needed.

> What you're seeing: close reading at scale, three concepts at once. The coloured-by-pattern dispersion view tells you at a glance which documents are obsessed with *students*, which with *staff*, which with *the university itself* — and which thread them together.

---

## Tool 3 — Trends *(2:10 pm – 2:15 pm)*

1. **Trends** tool in the left sidebar.
2. **Load snapshot** → **`QLD_Election_Tweets_conc`**.

**Look at:** when three election-time concepts surface across QLD candidate tweets — **`jobs`**, **`cases`**, and **`economic`** — at hourly resolution. This Trends view is built on top of a Concordance search result, so each spike is a real tweet matching one of those patterns.

**Try this:**
- 🔁 Switch the **grouping** control between:
  - **Matched term** — one line per pattern (`jobs` / `cases` / `economic`).
  - **Gender** — one line per candidate gender.
  - **Party** — one line per political party.
- 🔁 Coarsen the **time bin** from hour → day → week. The lines reshape on the fly — no rerun needed.
- 🔁 Hover any line for exact counts at that time.

> What you're seeing: the same matches viewed three different ways. *Whose* tweets, *when*, *about which concept* — same data, three stories. The story you tell depends on the grouping you pick.

---

## Tool 4 — Topic Modelling *(2:15 pm – 2:20 pm)*

1. **Topic Modelling** tool in the left sidebar.
2. **Load snapshot** → **`newstalk_left_vs_right`**.

**Look at:** the bubble chart of **8 discovered topics** across the same newstalk corpus you saw in Tool 1 — but this time we're asking BERTopic to *discover* themes automatically, rather than counting words. Bubble size = how many articles fit each topic; distance between bubbles reflects thematic similarity.

The corpora are **balanced**: 120 right-leaning articles (sampled from a larger pool) and 121 left-leaning, so topic discovery isn't skewed by corpus size.

**Try this:**
- 🔁 Hover over a bubble — the top words for that topic appear.
- 🔁 Click a bubble — the full word ranking opens.
- 🔁 Notice bubbles where the **colours blend** — those are topics with articles from *both* left and right outlets. Solid-coloured bubbles are topics dominated by one side.

> What you're seeing: the same corpus you saw in Tool 1, through a different lens. Tool 1 told you which *words* diverge between sides; Tool 4 tells you which *themes* cluster — and where the two sides talk about the same thing (colour-mixed bubbles) versus where they diverge (solid bubbles).

---

## Tool 5 — Quotation *(2:20 pm – 2:25 pm)*

1. **Quotation** tool in the left sidebar.
2. **Load snapshot** → **`SCL_Honi_Soit`** (the one in the Quotation tool's snapshot list — Wordflow scopes snapshots per tool).

**Look at:** rows of quoted speech extracted from 100 Honi Soit articles. The tool found **~870 quotations across 95 of the 100 documents** — student newspapers turn out to be very quote-rich (interviews, opinion pieces, news with sources). The remaining 5 documents might be genuinely quote-less, or the tool may have missed some.

**Try this:**
- 🔁 Click a row to see the surrounding sentence and source document.
- 🔁 Sort by speaker — see who gets quoted most.
- 🔁 Look for a few mis-hits — the extractor isn't perfect, especially with unusual quote markers or nested speech.

> What you're seeing: structured extraction of attributed speech — who said what, in what context. Useful for newspaper, interview, hansard, or court transcripts where attribution matters. **English-only for now.**

---

## Recap before the break

Same data, five lenses. None of them was *more correct* than the others — they answered different questions about the same texts.

But there's one thing the snapshot tour didn't show: **outside of Snapshot Mode, every analysis result can be added back into the workspace as a new data block** — for another tool to analyse. Filter your corpus → run comparative frequency → click a word to jump to concordance → save the matching contexts as a new block → run topic modelling on that new block → plot the topics over time…

**None of these tools is a dead end.** They feed each other. That's what makes Wordflow a *workflow* tool, not just a visualisation tool.

When we come back, you'll watch — and partly follow — a workflow that does exactly this: **four of these tools chained into one research story**, with all the joins, filters, and slices that connect them.

Break at **2:25 pm to 2:40 pm**. See you back here.
