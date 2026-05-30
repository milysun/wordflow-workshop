# Session 2 — Research story (45 min)

**Time: 2:40 pm – 3:25 pm**

This is the heart of the workshop. The facilitator will walk a real multi-tool workflow, end to end, answering a research question. The key moves are marked **✋ TRY THIS**; the rest are **👣 FOLLOW ALONG** — have a go at them too, and don't worry if you fall behind. The markers below tell you which is which, and there's a checkpoint for every phase if you need to catch up.

If you fall behind, there are **five checkpoint workspace archives (A → E)** — one per phase — under **sih.tools/wordflow → Materials → Session 2 checkpoint files**. Download whichever matches where the facilitator is, then import it as a workspace (Data Loader → Import workspace archive) and you're back in sync. Don't stress about following every click.

---

## The research question

> *Are there gender-based differences in how Queensland election candidates tweeted about topical issues during the 2020 campaign?*

We'll answer it by:
1. Joining tweets with candidate gender data.
2. Filtering into female and male sub-corpora.
3. Comparing them with frequency analysis and reading specific terms in context — iterating between the two tools to settle on a search pattern.
4. Running that pattern as a regex covering a **COVID** theme (`covid`, `case(s)`) and a **spending-cuts** theme (`cut(s)`); detaching the matches and looking at temporal trends, including the gender gap on *cut(s)*.
5. Topic modelling on both gender corpora together — fused bubbles, then detach.
6. Stacking the detached topic blocks and viewing the final cross-gender trends.

That's a six-step workflow across **four analysis tools** (Frequency, Concordance, Trends — used twice — and Topic Modelling), one corpus, one question — and one *made-up hypothesis* about which gender tweets more about which theme.

---

## A — Load, prepare, join (7 min) — 👣 FOLLOW ALONG

Follow along on your machine if you can. **There's more to "load" than just clicking import** — for first-time users this is the most procedurally dense phase, so it's fine to just watch the projector here. Checkpoint A catches you up before Phase B.

What's happening:
1. **Add** the two CSV files as data blocks: `qldelection2020_candidate_tweets` and `candidate_info_gender`. (They were already downloaded in the start-of-workshop **Import sample data** step — in the Data Loader file list, click **Add** on each. No re-importing here.)
2. **Rename** the longer block to `tweets` — click the **menu icon** on the data block → Rename. (Wordflow doesn't use right-click; the menu icon is a tiny icon on the block itself.)
3. **Delete unused columns** that aren't relevant to this analysis — click the **menu icon at the end of a column header** to open the column menu. *(Optional — not essential for the analysis.)*
4. **Set column dtypes** — make sure the join key (`username`) is the **same type** in both blocks, or the join won't match the rows.
5. **Join** the two on `username`: select `tweets` **first** so it becomes the *left* table (the first block you select is the left side), then choose **left join** → new block `tweets_with_gender`, keeping every tweet. Accept any dtype warning Wordflow shows.
6. **Click `tweets_with_gender`** → look at the Data Viewer. Click a row to read one full tweet.

> Data prep work *is* part of the analysis. People who rush through it often pay later with mysterious bugs.

✅ **Checkpoint A** — if you got lost: download `Checkpoint_A.zip` from **sih.tools/wordflow → Materials → Session 2 checkpoint files**. In Wordflow: **Data Loader → Import workspace archive →** select the file. Your workspace now matches the facilitator's.

---

## B — Filter by gender + iterative Frequency ↔ Concordance (9 min) — 👣 FOLLOW ALONG

A good place to pick up the keyboard and follow along — no pressure if you can't keep pace.

1. **Preprocessing → Filter** the joined block: `gender = 'F'` → block called `tweets_female`. Again for `gender = 'M'` → `tweets_male`. *(No hashtag filter — the dataset is small and filtering by `#` would chop too many tweets.)*
2. **Select both** in the graph (click one, Cmd/Ctrl-click the other). **Frequency** tool — opens in **comparative mode (Juxtorpus)**. Word count 40, stopwords on.
3. **Iterate**: click a topical word → Wordflow jumps to **Concordance** with that word pre-loaded. Read a few contexts. Go back to Frequency, pick a different word. Repeat — this is the *exploration* before settling on a final pattern.
4. The facilitator will narrate the moves they keep coming back to: `covid`, `case(s)`, `cut(s)`. **Two themes** are emerging — *COVID* and *spending cuts*. That sets up the regex in Phase C.

> 🎯 Insight to land: you stacked twice — Frequency to Concordance, and back again. The regex in Phase C grew straight out of this iteration. **Reading shapes searching shapes reading.**

✅ **Checkpoint B** — `Checkpoint_B.zip`.

---

## C — Multi-pattern regex → Add to Workspace → Trends (10 min) — mixed

### C-1 — Set the regex, view dispersion, Add to Workspace (4 min) — 👣 FOLLOW ALONG

The facilitator will:
1. Switch search to **Regex mode**. Pattern: `covid|case(s)?|cut(s)?` — three patterns covering two themes:
   - **COVID** — `covid` + `case(s)?` (case / cases, mostly meaning COVID case counts in 2020).
   - **Spending cuts** — `cut(s)?` (cut / cuts).
2. Each match gets its **own colour**. Switch to **Dispersion view** — bars per tweet, colour-coded — to see how the matches spread across the corpus.
3. Switch back to **Table view**, then click **Add to Workspace** — each matched hit becomes its own row (matched-term column preserved alongside the gender column), ready for Trends. *Add from the Table view, **not** Dispersion: the Dispersion view aggregates hits per document, which would collapse the hit-level detail the Trends comparison needs.*

> 🎯 Insight to land: one tool's result becomes the next tool's structured input. Reading and analysing are two sides of one workflow.

### C-2 — Trends, find the cut(s) gender gap (6 min) — ✋ TRY THIS

You're picking up the keyboard again.

1. Click the matched block → **Trends** tool. Time axis: tweet date. Time bin: daily to start.
2. Group by **matched term × gender** — each combination (e.g. `covid-F`, `covid-M`, `case-F`, `cuts-F`, `cuts-M`, …) is its own line.
3. **Filter the COVID lines off via the legend** — click the `covid`, `case`, and `cases` combinations off, one by one, until only the `cut` / `cuts` lines remain. The legend is an interactive filter, not just a colour key.
4. **Switch the chart from line to bar.** Now you're comparing male vs female on `cut(s)` directly — and male candidates mention spending cuts more often than female. **Set the time bin to weekly** and the contrast sharpens further. A pattern on a small dataset — suggestive, not definitive.

> 🎯 Insight to land: the legend isn't just a colour key — it's an interactive filter. And switching the chart type (line → bar) reshapes the same data into the comparison you actually want.

✅ **Checkpoint C** — `Checkpoint_C.zip`.

---

## D — Topic modelling on two corpora (9 min) — ✋ TRY THIS

The Topic Modelling tool accepts **two data blocks as input** and produces a fused bubble chart — colours blend in topics that draw documents from both corpora, stay solid in topics dominated by one.

Try this one with the facilitator — it's worth running yourself:

1. **Select both** `tweets_female` and `tweets_male`.
2. **Topic Modelling.** Target = 8 topics, seed = 42. Run. Wait ~60-90s.
3. While it runs, look at the **Task Centre** — that's where slow analyses show progress.
4. When done: BERTopic actually produces **~23 topics** (the "target" is a hint, not a cap). Crowded.
5. **Drag the re-aggregation slider to 16 topics** — bubbles spread out, themes become distinguishable. Re-aggregation is client-side — no re-run. (Trying further down to 5 would crush the topics together.)
6. **Look at the colour mixing**: solid bubbles = gender-dominant; blended = shared themes. Hover for top words.
7. **Select 2-3 interesting topics → Detach.** Because Topic Modelling ran on two parents, detaching produces *per-gender child blocks* — one set under `tweets_female`, one under `tweets_male`.

> 🎯 Insight to land: themes can be discovered automatically, and the *colour mixing* tells you immediately which themes are shared vs gender-dominant.

✅ **Checkpoint D** — `Checkpoint_D.zip`.

---

## E — Stack → final Trends (5 min) — ✋ TRY THIS

The closing move — try it with the facilitator:

1. **Preprocessing → Stack** the per-gender topic blocks from D back together. Result: a unified block where each row carries both its topic label and its gender column.
2. Click the stacked block → **Trends.** Time bin weekly. Group by `topic` (or `gender × topic`).
3. Final view: the topics from D, evolving across the campaign, split by gender. End to end — that's our method.

> 🎯 Final landing: four analysis tools (Trends used twice), one corpus, one made-up hypothesis, one connected workflow. Every step shaped the next. The graph behind the facilitator is your whole method section, captured as a picture — and there's a small finding sitting inside it.

✅ **Checkpoint E** — `Checkpoint_E.zip`.

---

## You don't have to have followed every step

If you got lost mid-stream — that's fine. The point isn't to have your screen match the facilitator's at minute 45. The point is to **see what's possible**, recognise the cross-tool moves (click jump, add-as-block, detach, stack, group), and trust you can build something like it yourself.

In the free lab (Session 3.C), you can:
- Load any checkpoint (C, D, or E) and continue the chain at your own pace.
- Try the regex + dispersion move on a different word set.
- Replace QLD tweets with Honi Soit or the Federal Election NewsTalk/Reddit bundle and see what changes.

---

## Reflection — 1 minute before break

Look at the graph view. **Read it back to front, aloud or silently:**

> *"Starting from QLD tweets joined with gender data, I filtered by gender, jumped between Frequency and Concordance to find a search pattern, ran it as a regex, detached the matches, found a gender gap on `cut(s)` in Trends, topic-modelled the two corpora together, detached selected topics, stacked them, and looked at the trends of those topics. What I found is ____."*

That sentence is your method section. Wordflow wrote most of it for you.

Break at **3:25 pm to 3:40 pm**.
