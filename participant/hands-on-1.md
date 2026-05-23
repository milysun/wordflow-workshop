# Session 1.5 — Snapshot tour

**Time: 30 minutes** *(0:25 – 0:55 in the schedule)*

You've just finished a tour of the Wordflow interface. Now you'll touch each of the five analytic tools — without setting any of them up. You're loading **pre-baked snapshots** to see what each tool produces, so when we build something together in Session 2 you'll know what you're aiming at.

---

## Setup (first 5 minutes)

Follow the facilitator's screen.

1. **Data Loader → Import sample content.** Import **all three** sample datasets: Honi Soit, QLD election tweets, and Reddit. (You won't use them all now, but they'll be ready later.)
2. **Data Loader → Import demo snapshots.** Import **all five** snapshots from the catalogue. If the catalogue tab is empty, the facilitator will share a download link — drop the files into your snapshot folder via the same dialog.
3. **Top menu → Enable Snapshot Mode.** Look for the **lock icon** or "Snapshot Mode" toggle. When it's on, the interface is read-only — you can still hover, click on visualisations, and switch views, but you can't accidentally change anything.
4. **Create a new workspace** called `tour`. (Top bar → workspace switcher → Create.)

Tell your neighbour if anything didn't work. Flag the facilitator if you're stuck.

---

## Tool 1 — Frequency *(0:30 – 0:35)*

1. **Frequency** tool in the left sidebar.
2. Click the **folder icon (Load snapshot)** in the tool header.
3. Pick the **Honi Soit overview** snapshot. Wait a second.

**Look at:** the word cloud. Bigger words = more frequent in the corpus.

**Try this:**
- 🔁 Switch from **Cloud** to **List** view.
- 🔁 Hover over a word in the list. Click it.

> What you're seeing: the most common content words in 100 articles from a student newspaper. Stopwords (the, a, is, etc.) are already filtered out.

---

## Tool 2 — Concordance *(0:35 – 0:40)*

1. **Concordance** tool in the left sidebar.
2. **Load snapshot** → **Honi Soit `student`**.

**Look at:** every appearance of the word "student" with the words before and after.

**Try this:**
- 🔁 Switch view to **Dispersion**. Each bar is one article; the marks show where in that article the word appears.
- 🔁 Hover over a row to see the full sentence.

> What you're seeing: close reading at scale. You can read every instance of a word without losing the context — and the dispersion view shows you whether it's an obsession, a passing mention, or evenly spread.

---

## Tool 3 — Trends *(0:40 – 0:45)*

1. **Trends** tool in the left sidebar.
2. **Load snapshot** → **Reddit monthly volume**.

**Look at:** how many submissions appeared per month, separated into different subreddits.

**Try this:**
- 🔁 Change the **time bin** from month to week (or year). The lines reshape on the fly — no re-running needed.
- 🔁 Hover over a line to see exact counts.

> What you're seeing: temporal patterns. When did topics surge? When did a subreddit go quiet? The grouping splits a single corpus into stories told side by side.

---

## Tool 4 — Topic Modelling *(0:45 – 0:50)*

1. **Topic Modelling** tool in the left sidebar.
2. **Load snapshot** → **Honi Soit topics**.

**Look at:** the bubble chart. Each bubble is one discovered topic; size = how many articles fit it.

**Try this:**
- 🔁 Hover over a bubble — top words for that topic appear.
- 🔁 Click a bubble — the word ranking opens.

> What you're seeing: automatic theme discovery. BERTopic grouped the 100 articles into thematic clusters based on what they're about, without you telling it what to look for.

---

## Tool 5 — Quotation *(0:50 – 0:55)*

1. **Quotation** tool in the left sidebar.
2. **Load snapshot** → **Honi Soit speakers**.

**Look at:** rows of quoted speech, each labelled with the speaker.

**Try this:**
- 🔁 Click a row to see the surrounding sentence in context.
- 🔁 Sort by speaker — who got quoted most?

> What you're seeing: structured extraction of attributed speech. Useful for newspaper, interview, or hansard corpora where "who said what" matters. (English-only for now.)

---

## Recap before the break

Same data, five lenses. None of them were *more correct* than the others — they answered different questions about the same texts.

When we come back, you'll watch — and partly follow — a workflow that uses **four of these tools in a single research story**, with all the joins, filters, and slices that connect them.

Break at **0:55 to 1:10**. See you back here.
