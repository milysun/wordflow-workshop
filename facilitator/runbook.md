# Facilitator Runbook — Wordflow 3h Workshop

Minute-by-minute script. **Italics = your spoken framing**, plain text = facilitator actions, `> blocks` = teaching points to land before moving on.

---

## Before participants arrive (T-30 min)

- Projector connected; `slides/index.html` open, slide 1 visible.
- Wordflow open on your demo screen, the demo workspace already prepared with five demo snapshots imported.
- Binder URL on the whiteboard. WiFi credentials on the whiteboard.
- The **Session-2 workspace archive** (`session2-checkpoints.wordflow-workspace`) and the four **Session-2 checkpoint snapshots** uploaded somewhere downloadable (Sydney Box / OneDrive / SharePoint / GitHub release). Short link written on the whiteboard.
- The **feedback form URL** open in a browser tab so you can flash it on demand.
- `participant/welcome.md` and `participant/cheat-sheet.md` on every chair.
- Pen and paper on every table.
- A glass of water for you.

---

## Session 1.0 — Intro + UI tour (0:00 – 0:25, 25 min)

### 0:00 – 0:05 — Welcome + sign-in-while-I-talk

*"Welcome. Three hours, two breaks, lots of clicking. Before I say a word about Wordflow, please open the URL on the whiteboard — it'll spin up a copy of Wordflow in the cloud for you, takes about a minute. While that's loading, I'll introduce the project and the team."*

- Slide 1 → slide 2 (housekeeping: wifi, breaks at 0:55 and 1:55, bathrooms, ask anytime).

> Why parallelise: Binder cold-start takes 30-60s the first time. Don't waste classroom minutes watching it spin.

### 0:05 – 0:12 — Project + team + deployment options

Slides 3–5.

*"LDaCA Wordflow is developed by **Sydney Informatics Hub** — a core research facility at USyd — and **Sydney Corpus Lab**. It's part of the **Language Data Commons of Australia**, a national HASS and Indigenous research infrastructure project funded by the **Australian Research Data Commons**.*

*Three ways to use it:*
- *Cloud (Binder), which is what you're loading right now — no install, free, but don't put sensitive data on it.*
- *Desktop app (Mac/Windows) — runs everything on your machine.*
- *Python install — `pip install ldaca-wordflow` if you're already a Python user.*

*Today we use the cloud version because it gets everyone running in one minute. Take the desktop app home for serious work — link is in the post-workshop email."*

### 0:12 – 0:23 — UI tour (live walkthrough on your screen)

Slide 6 has the UI map; switch to your Wordflow window for the live tour.

*"There are seven things in the interface that you'll touch today. Let me show each one."*

Walk in this order, pointing at the projection:

1. **Tool sidebar (left).** *"Pick a tool here. Each tool answers a different question of the same data. We'll meet all five analytic tools in the next session."*
2. **Workspace graph view (centre).** *"This is your map. Each box is a data block — a table of texts plus metadata. Lines between boxes mean one was derived from the other. The graph is your method section."*
3. **Data block — and how to view it.** *"Click any box; the table on the right shows you what's inside. Click any row, you see the full text of that document. Try it — click on a row and read one tweet."*
4. **Tool interface (right).** *"When you pick a tool, its controls and results appear here. Same place every time."*
5. **Data block quick-select in the sidebar.** *"This little dropdown next to the tool name lets you switch the active block without clicking back to the graph. Useful when you're comparing."*
6. **Tutorial anchors — the `?` icons.** *"See these question marks next to controls? Click any one and the tutorial opens at the matching section. Use these as you go today."*
7. **Feedback button (heart icon, top right).** *"This is important. Anywhere you see something confusing, surprising, or buggy — tap the heart. Even one word is fine. We read every one. Today, we want your feedback specifically; you're some of the first researchers outside our team to use the v0.5 version."*

> Why land the feedback button NOW (before the snapshot tour): every minute they're using the app, they should know there's a low-friction way to report friction. Don't let them save it up for after the workshop.

### 0:23 – 0:25 — Sync check

*"Quick check — show of hands, who can see the Wordflow workspace screen?"*

- If <70% are up: WiFi or Binder problem. Pair attendees with neighbours who are working; deal with stragglers during Session 1.5 setup.
- If 70-100% are up: good, push forward.

---

## Session 1.5 — Snapshot tour (0:25 – 0:55, 30 min)

The goal: every participant touches each of the five analytic tools' visualisations. They are **not** building anything yet — they're seeing what the destination looks like, so Session 2 feels like working towards something real.

### 0:25 – 0:30 — Group setup (5 min)

Drive this from your screen and have everyone follow.

1. *"Data Loader → Import sample content → import all three sample datasets (Honi Soit, QLD election tweets, Reddit). You won't use them all now, but they'll be ready for later."* (~1 min)
2. *"Data Loader → Import demo snapshots → import all five demo snapshots from the catalogue."* (~1 min)
3. *"Top menu → enable Snapshot Mode."* (~30s) *"This locks the interface to read-only. You can still hover and click around the visualisation, you can't accidentally change anything."*
4. *"Create a new workspace called `tour`."* (~30s)

> If anyone is still stuck on import: keep moving. The snapshots are loaded by tool, not by workspace — they'll catch up at the next tool transition.

### 0:30 – 0:55 — Five tools, five minutes each (25 min)

For each tool: **(a) load the snapshot together, (b) facilitator narrates ~2 min, (c) participants explore ~2 min, (d) 30s pivot to next tool.** Stick to the budget — if a tool fascinates someone, they'll come back in the free lab.

#### Tool 1 — Frequency (0:30 – 0:35)

- *"Click Frequency in the sidebar. Click 'Load snapshot' (folder icon). Pick the demo one — Honi Soit overview."*
- Narrate the cloud view: *"Bigger words appear more often. Stopwords are already on. Switch to List view to see counts."*
- 2-min explore: *"Hover, click, try different views. Don't worry — Snapshot Mode means nothing breaks."*

#### Tool 2 — Concordance (0:35 – 0:40)

- *"Concordance in the sidebar. Load snapshot — Honi Soit 'student'."*
- Narrate: *"Each row is one match with context. Switch to Dispersion view — see where in each document the word lands."*
- 2-min explore.

#### Tool 3 — Trends (0:40 – 0:45)

- *"Trends in the sidebar. Load snapshot — Reddit monthly volume."*
- Narrate: *"Each line is articles per month, coloured by subreddit. Hover to see exact counts."*
- 2-min explore: *"Try the time-bin and grouping controls — even in Snapshot Mode you can re-aggregate locally."*

> v0.5 feature worth pointing out: client-side re-aggregation. They can coarsen the time axis without re-running the analysis.

#### Tool 4 — Topic Modelling (0:45 – 0:50)

- *"Topic Modelling in the sidebar. Load snapshot — Honi Soit topics."*
- Narrate: *"Each bubble is one topic. Size = how many documents fit it. Hover to see the top words."*
- 2-min explore: *"Click a bubble — the word ranking appears."*

#### Tool 5 — Quotation (0:50 – 0:55)

- *"Quotation in the sidebar. Load snapshot — Honi Soit speakers."*
- Narrate: *"Quoted speech extracted with the speaker. Each row: who said what, in what context. English only — but it's a useful one for newspaper or interview corpora."*
- 2-min explore.

> Why Quotation last: it's English-only and the narrowest. If you're running over by 5 min already, you can cut it without losing the lesson.

### 0:55 — Hand-off to break

*"That's all five tools. Same data, five different lenses. Take 15 minutes. When we come back, we're going to build a workflow like this — but step by step, from raw tweets to a real research finding."*

---

## Break 1 (0:55 – 1:10, 15 min)

---

## Session 2 — Research story (1:10 – 1:55, 45 min)

**The story:** *"Are there gender-based differences in how QLD election candidates tweeted about topical issues during the 2020 campaign?"*

**Mode:** Facilitator demo at full speed + participants follow only the moves marked **try this** in the hands-on-2 sheet. ~25 min demo + ~20 min selective follow-along.

**Recovery:** Four checkpoints. At each, mention the corresponding snapshot/workspace archive on the whiteboard. Anyone who's lost loads it and rejoins. Don't lose more than 60 seconds shepherding stragglers — the archives are the safety net.

### 1:10 – 1:15 — Frame the research question + disable snapshot mode

Slide 13.

*"For the next 45 minutes, I'm going to walk a real research workflow. The question: did female and male candidates in the 2020 QLD election tweet about different topical issues? We'll build a workflow that answers it.*

*You don't have to follow every step. Your hands-on sheet marks some moves as 'try this' — pick up the keyboard for those. Other moves are marked 'watch' — sit back and look at my screen. If you fall behind, the whiteboard has download links for snapshots and workspace archives at four checkpoints; load whichever you need to rejoin.*

*First — turn OFF Snapshot Mode in the top menu. We're building, not just looking."*

### 1:15 – 1:25 — A: Load, join, slice (10 min, mostly WATCH)

On your screen:

1. *Data Loader → use the already-imported QLD candidate tweets corpus.*
2. *Notice we have two blocks — `qldelection2020_candidate_tweets` and `candidate_info_gender`.*
3. **Preprocessing → Join.** *"Join the tweets to the candidate info on `candidate_id`. Left join, so we keep all tweets even if the gender info is missing."* → Add to Workspace as `tweets_with_gender`.
4. *Dtype warning appears.* *"Wordflow noticed some columns are mixed types — it's going to standardise them. Accept. This is the dtype normalisation we saw in the upgrade notes."*
5. *Click `tweets_with_gender` → look at the Data Viewer.* *"Now every tweet has a gender column. Click a row to read one full tweet."*
6. **Preprocessing → Filter** the joined block: `gender = 'F'` → Add to Workspace as `tweets_female`. Then again: `gender = 'M'` → `tweets_male`. *"Two sub-blocks by metadata."*
7. **Preprocessing → Filter** `tweets_female` for `text contains "#"` (any hashtag) → `tweets_female_hashtagged`. Same for male. *"Now we have just the hashtagged tweets per gender — the topical ones."*
8. *(Optional — if time) **Preprocessing → Stack** to merge two distinct hashtag filters back together.* Skip if you're already at 1:25.

> **Checkpoint α** — workspace archive: `session2-after-A.wordflow-workspace`. Mention it explicitly: *"Anyone behind, download checkpoint α from the link on the board."*

### 1:25 – 1:35 — B: Comparative Frequency + jump to Concordance (10 min, TRY THIS)

This is the first place to put the keyboard in participants' hands.

1. **Select both `tweets_female_hashtagged` and `tweets_male_hashtagged`** in the graph.
2. **Frequency tool → comparative mode (Juxtorpus).** *"Wordflow puts the two corpora side-by-side."*
3. *Adjust visualisation word count from default to 40.*
4. *Add stopwords (English).* *"The political words come up.*"
5. *Save the frequency list (Export) and a screenshot.* *"This is how you keep a record."*
6. **Left-click a word** in the frequency list. *"Watch — it jumps me to Concordance with that word pre-loaded. This is what 'tools talk to each other' means in Wordflow."*

> Land here: *"You just stacked. Filter → split-by-metadata → comparative frequency → one click → concordance. Read the graph back: that's your method."*

> **Checkpoint β** — snapshot: `frequency-tweets-comparative.ldaca-snapshot`.

### 1:35 – 1:45 — C: Concordance — simple, then regex+dispersion (10 min, mixed)

#### C-1 — Simple search + add as block (TRY THIS, ~3 min)

1. Your search term is already loaded from the Frequency jump.
2. Run it. *"Look at the contexts — male and female candidates are talking about this differently."*
3. **Add results as a new data block.** *"Right-click on the result → Add as block. We now have a derived block of just the matching contexts. We can analyse this block on its own."*

#### C-2 — Regex with 3 words + dispersion + select (WATCH, ~7 min)

1. **Change search to regex mode.** Search pattern: `(covid|vaccine|mask)` (or similar 3-word OR set).
2. *"Three search terms at once. Each match gets its own colour in the result table."*
3. **Switch view to Dispersion.** *"Bars per document, colour-coded by which term matched where."*
4. **Click-and-drag in the dispersion plot** to select a subset of documents. *"Visual selection."*
5. **Add the selected contexts as an aggregated block** — pick `aggregated` mode (one row per source document, contexts concatenated).
6. *"That's our derived block for the next step."*

> **Checkpoint γ** — workspace archive: `session2-after-C.wordflow-workspace`.

### 1:45 – 1:50 — D: Trends on the aggregated block (5 min, WATCH)

1. Click the aggregated block from C-2.
2. **Trends tool.** Date column: tweet date. Time bin: weekly.
3. Add a grouping by `gender` — *"two lines, one per gender."*
4. Swap grouping to the matched-term column — *"three lines, one per topic."*
5. *"Different grouping, different story from the same data."*

> **Checkpoint δ** — snapshot: `trends-aggregated-by-gender.ldaca-snapshot`.

### 1:50 – 1:55 — E: Topic modelling + back to Trends (5 min, WATCH)

This is the most ambitious move. If you're tight on time, **skip the BERTopic run** and just describe E verbally — the lesson is the cross-tool flow, not the topic model itself.

1. Aggregated block selected → **Topic Modelling**.
2. Mode: **target number of topics** (e.g., 8). Run. ~60-90s wait. *"While this runs, look at the Task Centre — that's where slow tasks show progress."*
3. When done: *"Bubble chart. We have 8 topics."*
4. **Re-aggregation** controls: try 5 instead of 8. *"Fewer topics, broader themes. Re-aggregation is client-side — no re-run."*
5. **Select two or three topics → Detach.** *"A new block appears in the graph — just documents in those topics."*
6. Click the detached block → **Trends**. Group by topic. *"Now I can see how those specific topics evolved over the campaign."*

> Final landing: *"Six tools, one corpus, one question, one workflow. Every step shaped the next. The graph behind me is the whole method."*

---

## Break 2 (1:55 – 2:10, 15 min)

---

## Session 3.A — Repurpose the lens (2:10 – 2:25, 15 min)

The conceptual payoff. Slow down — this is what they'll remember.

### 2:10 – 2:15 — Quick word count

*"Watch one move first. I'll use Frequency, not as a 'top words' tool, but as a counter. Total token count across the corpus, per gender."*

- Frequency tool with stopwords off, top-N very high, show that "total tokens" is right there in the summary.
- *"That's word count. Frequency tool, but I'm not interested in any specific word — I just want totals."*

### 2:15 – 2:25 — Repurpose Trends as a histogram

*"Now watch this. Trends is the time-series tool, right? Line chart over dates. But it doesn't have to be time on the x-axis. Let me show you."*

1. On a tweets block, **add a derived numeric column** = word count per tweet (Preprocessing → Create column → tokens length, or similar).
2. **Trends tool.** Instead of date, set the x-axis to the word-count column. Numeric bucketing.
3. *"Now Trends is showing me distribution — number of tweets per word-count bucket. It's a histogram."*
4. Add a grouping by gender. *"Histogram of tweet length, by gender."*

*"The tool didn't change. I changed how I shaped the data. That's the whole point of Wordflow — the analysis is defined by how you shape the question, not by which tool you clicked.*

*Every tool in Wordflow is a lens. The interesting research question is always: which lens, on which slice of which corpus, will tell me something I didn't already know? That's your job. Wordflow makes the lens-changing cheap."*

> If this is the one slide they tweet about, the workshop succeeded.

---

## Session 3.B — Lab framing + feedback ask (2:25 – 2:30, 5 min)

*"Next 25 minutes: free lab. Three tracks — pick whichever fits.*

- *Track A: keep building on Session 2 — try the moves you watched but didn't follow. Workspace archive is on the board.*
- *Track B: bring your own data. Upload a CSV with at least one text column. My helper and I will be around.*
- *Track C: open exploration — pick a tool, pick a sample dataset, see what falls out.*

*One ask: every time you hit something confusing, weird, or broken — tap the feedback heart icon. Even just 'this is confusing' helps us. You're our v0.5 beta room."*

Slide reminder: feedback URL also accessible directly at the URL on the board.

---

## Session 3.C — Free hands-on (2:30 – 2:55, 25 min)

You and any helpers walk the room. Common questions in `common-questions.md`. Prompts for the three tracks in `hands-on-3.md` for participants.

Time check at 2:50 — start corralling everyone back to their seats with *"five minutes — finish your current click."*

---

## Session 3.D — Thanks + close (2:55 – 3:00, 5 min)

Final slide.

*"Thank you for spending three hours with us. Three asks if Wordflow turned out useful:*

1. *Install it locally — link in tonight's email — and try it on your own work.*
2. *If you publish using it, cite the project — the citation is on the docs site.*
3. *Tap the feedback button as you go. Send us bugs. Send us 'this rocks'. Send us 'this is confusing'. Every one helps.*

*And — spread the word. If you have a colleague who works with text and is allergic to coding, they should know this exists.*

*Tonight you'll get an email with the snapshots and workspace archive from today, the install link, the docs, and one question: what would have made today more useful? Reply with one sentence.*

*Thanks. Have a good evening."*

---

## After participants leave

- Note what timing slipped, what landed, what stumbled. Use it to tune next delivery.
- Send `communications/post-workshop-email.md` within 24 hours with the snapshots and workspace archive attached or linked.
