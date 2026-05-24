# Session 2 — Research story (45 min)

**Time: 1:10 – 1:55**

This is the heart of the workshop. The facilitator will walk a real multi-tool workflow, end to end, answering a research question. Some moves you **try yourself** (✋ TRY THIS), others you **watch on the projector** (👀 WATCH ONLY). The markers below tell you which is which.

If you fall behind, there are **four checkpoint files** on the whiteboard URL — download whichever matches where the facilitator is, load it, you're back in sync. Don't stress about following every click.

---

## The research question

> *Are there gender-based differences in how Queensland election candidates tweeted about topical issues during the 2020 campaign?*

We'll answer it by:
1. Joining tweets with candidate gender data.
2. Splitting into female and male sub-corpora.
3. Comparing their hashtagged content with frequency analysis.
4. Reading specific terms in context.
5. Looking at temporal trends.
6. Discovering thematic topics.

That's six tools, one workflow, one question.

---

## Pre-flight: turn off Snapshot Mode

You enabled Snapshot Mode in Session 1.5 so you could load the demo snapshots. Now we're building — **turn Snapshot Mode OFF** (the pencil icon next to "VIEWS" in the sidebar). Your facilitator will pause until everyone has done this.

---

## A — Load, join, slice (10 min) — 👀 WATCH ONLY

The facilitator drives this. You watch the projector. The data setup is fiddly and one wrong click can derail your screen — let the facilitator demonstrate, and if you want to try yourself, do it in the free lab.

What's happening:
1. **Join** the two QLD datasets (`qldelection2020_candidate_tweets` and `candidate_info_gender`) on the candidate ID. Result: every tweet now has a gender column.
2. **Dtype warning** — Wordflow notices some columns are mixed types and offers to standardise. Accept.
3. **Filter** the joined block by `gender = 'F'` → block called `tweets_female`. Again for `gender = 'M'` → `tweets_male`.
4. **Filter** each by `text contains "#"` to keep just the hashtagged (topical) tweets.

✅ **Checkpoint α** — if you got lost: download `session2-after-A.wordflow-workspace` from the URL on the board. **Workspace switcher → Import workspace archive →** select the file. Your workspace now matches the facilitator's.

---

## B — Comparative Frequency + jump to Concordance (10 min) — ✋ TRY THIS

You'll do this with the facilitator. Pick up the keyboard.

1. **Select both** `tweets_female_hashtagged` and `tweets_male_hashtagged` in the graph (click one, Cmd/Ctrl-click the other).
2. **Frequency** tool. It opens in **comparative mode (Juxtorpus)** — two corpora side by side.
3. Set the **word count** to 40. Toggle **stopwords (English)** on.
4. **Save** the frequency list (export icon) and take a screenshot. *This is your record.*
5. **Left-click** a word that intrigues you in the comparative list. Watch what happens — Wordflow **jumps to the Concordance tool** with that word pre-loaded. **This is the cross-tool magic.**

> 🎯 Insight to land: you stacked. Filter → split-by-gender → filter-by-content → comparative frequency → one click → concordance. Read the graph from left to right; that's your method section.

✅ **Checkpoint β** — `frequency-tweets-comparative.ldaca-snapshot` if you need to re-sync.

---

## C — Concordance: simple, then advanced (10 min)

### C-1 — Simple search + add as block (3 min) — ✋ TRY THIS

The word you jumped on is already loaded. Just run it.

1. Look at the result table. Each row = one tweet matching your word, with the context.
2. **Right-click → Add results as data block.** A new derived block appears in your graph — *just the matching tweets*.

> 🎯 Insight to land: Concordance is not only a search tool. Its results can become a new analysable corpus, which the next tool can analyse.

### C-2 — Regex with three words + dispersion + visual select (7 min) — 👀 WATCH ONLY

This is more advanced. Watch the projector. Try it yourself in the free lab.

The facilitator will:
1. Switch search to **Regex mode**. Pattern: `(covid|vaccine|mask)` (or another 3-way OR set).
2. Each match gets its **own colour** in the results.
3. Switch to **Dispersion view** — bars per tweet, colour-coded by which term matched.
4. **Click-and-drag** in the dispersion plot to select a subset of tweets.
5. **Add selected contexts as a new aggregated block** (one row per source tweet, all matched contexts concatenated).

> 🎯 Insight to land: visual selection in any tool can become structured data for the next tool. Reading and analysing are two sides of one workflow.

✅ **Checkpoint γ** — `session2-after-C.wordflow-workspace` if you need to re-sync.

---

## D — Trends on the aggregated block (5 min) — 👀 WATCH ONLY

Same block as the output of C-2. The facilitator will:

1. Open **Trends** tool. Time axis: the tweet date column. Time bin: weekly.
2. Add a grouping by `gender` — two lines, one per gender.
3. Swap the grouping to the matched-term column (the colour from C-2) — three lines, one per topic.

> 🎯 Insight to land: same data, swap one parameter (the grouping), get a different story. Trends doesn't have one "right" view — it has as many as you have questions.

✅ **Checkpoint δ** — `trends-aggregated-by-gender.ldaca-snapshot`.

---

## E — Topic modelling + return to Trends (5 min) — 👀 WATCH ONLY

Most ambitious. The facilitator will:

1. With the aggregated block selected → **Topic Modelling**.
2. Set mode to **target number of topics** = 8. Run. Wait ~60-90s.
3. While it runs, look at the **Task Centre** — that's where slow analyses show progress.
4. When done: bubble chart appears. **Re-aggregate** to 5 topics — fewer, broader. (Re-aggregation is client-side — no re-run.)
5. **Select 2-3 topics → Detach.** A new block appears in the graph, containing only documents in those topics.
6. Click the detached block → **Trends** tool. Group by topic.

> 🎯 Final landing: six tools, one corpus, one research question, one connected workflow. Every step shaped the next. The graph behind the facilitator is your whole method section, captured as a picture.

---

## You don't have to have followed every step

If you got lost in C-2 and never came back — that's fine. The point isn't to have your screen match the facilitator's at minute 45. The point is to **see what's possible**, recognise the cross-tool moves (left-click jump, add-as-block, detach, group), and trust you can build something like it yourself.

In the free lab (Session 3.C), you can:
- Load checkpoint γ or δ and continue the chain at your own pace.
- Try the regex + dispersion move on a different word set.
- Replace QLD tweets with Honi Soit or Reddit and see what changes.

---

## Reflection — 1 minute before break

Look at the graph view. **Read it back to front, aloud or silently:**

> *"Starting from QLD tweets joined with gender data, I filtered to hashtagged tweets per gender, ran a comparative frequency, jumped to concordance, aggregated the matched contexts, looked at trends, and grouped by topic. What I found is ____."*

That sentence is your method section. Wordflow wrote most of it for you.

Break at **1:55 to 2:10**.
