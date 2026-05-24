# Facilitator Runbook — Wordflow 3h Workshop

Minute-by-minute script. **Italics = your spoken framing**, plain text = facilitator actions, `> blocks` = teaching points to land before moving on.

---

## Before participants arrive (T-30 min)

- Projector connected; `slides/index.html` open, slide 1 visible.
- Wordflow open on your demo screen, the demo workspace already prepared with five demo snapshots imported.
- **bit.ly/wordflows** is visible on slide 3 (Housekeeping) so people can launch Wordflow as they arrive. (USyd-internal workshop — no separate WiFi login needed.)
- The **Session-2 workspace archive** (`session2-checkpoints.wordflow-workspace`) and the four **Session-2 checkpoint snapshots** published as a GitHub release on `milysun/wordflow-workshop` so the same `bit.ly/wordflows` link gets people to them too.
- The **feedback form URL** open in a browser tab so you can flash it on demand.
- `participant/welcome.md` and `participant/cheat-sheet.md` on every chair.
- Pen and paper on every table.
- A glass of water for you.

---

## Plan B — if Binder is down or overloaded

**Trigger:** at the 0:23 sync check (or earlier if it's obvious from the room), fewer than ~70% of attendees have Wordflow loaded, AND it's not just stragglers — Binder is unreachable, painfully slow, or refusing connections.

**The move:**
- Tell the room: *"Binder isn't cooperating today. Anyone who hasn't gotten in: go to bit.ly/wordflows and click the desktop download link instead. Install takes about 5 minutes — we'll wait."*
- Anyone whose Binder *did* load can keep using it.
- Anyone installing: tell them to keep going, you'll loop them in at the next sync check.

**Time recovery** (installing eats 5–8 minutes — see `timing-recovery.md` for the full list of cuts):
- Shorten the project+team narration at 0:05–0:12 from 7 min to ~3 min — say *"developed by Sydney Informatics Hub and Sydney Corpus Lab, part of LDaCA, funded by ARDC"* and move on. Save the full attribution for the post-workshop email.
- The Quotation tool in Session 1.5 is the easiest cut (it's last and English-only).
- If still over, ask for one volunteer's screen and have everyone watch the Session 2 demo rather than follow along — the checkpoint files cover the catch-up.

**Pre-emptive mitigation:** the pre-workshop email recommends installing the desktop app as a backup before arriving. If many participants do that, Plan B is almost frictionless.

---

## Session 1.0 — Intro + UI tour (0:00 – 0:25, 25 min)

### 0:00 – 0:01 — Welcome + Acknowledgement of Country

Slides 1 → 2. Stand. Speak slowly and sincerely; this isn't boilerplate. About 30–45 seconds total.

*"Welcome — thank you for being here."*

(Advance to slide 2.)

*"Before we begin, I'd like to acknowledge the Gadigal people of the Eora Nation, the Traditional Custodians of the land on which we meet today. I pay my respects to Elders past and present, and extend that respect to any Aboriginal and Torres Strait Islander people in the room."*

> Wait a beat. Don't rush to the next slide.

### 0:01 – 0:05 — Sign-in-while-I-talk + housekeeping

Slide 3 (Housekeeping).

*"Three hours, two breaks, lots of clicking. Before I say a word about Wordflow, please open `bit.ly/wordflows` on your laptop and click 'Launch in Binder' — it'll spin up a copy of Wordflow in the cloud for you, takes a couple of minutes. While that's loading, I'll introduce the project and the team. If Binder hasn't loaded after about five minutes, the same URL has a desktop install link."*

- Pause briefly to make sure people have typed the URL.

> Why parallelise: Binder cold-start takes 1–2 minutes the first time. Don't waste classroom minutes watching it spin.

### 0:05 – 0:12 — Project + team + deployment options

Slide 4 (team), then slide 5 (deployment options).

*"LDaCA Wordflow is developed by a small team at the University of Sydney — myself and Dr Alex Guo at **Sydney Informatics Hub**, with Prof. Monika Bednarek as academic lead at **Sydney Corpus Lab**. It's part of the **Language Data Commons of Australia**, a national HASS and Indigenous research infrastructure project funded by the **Australian Research Data Commons**.*

(Advance to slide 5.)

*Three ways to use it:*
- *Cloud (Binder), which is what you're loading right now — no install, free, but don't put sensitive data on it.*
- *Desktop app (Mac/Windows) — runs everything on your machine.*
- *Python install — `pip install ldaca-wordflow` if you're already a Python user.*

*Today we use the cloud version because it gets everyone running in about a minute. Take the desktop app home for serious work — link is in the post-workshop email."*

### 0:12 – 0:23 — UI tour (live walkthrough on your screen)

Slide 6 has the annotated UI map; switch to your Wordflow window for the live tour and point at the matching regions on screen.

*"There are seven things in the interface that you'll touch today. Let me show each one."*

Walk in this order, pointing at the projection:

1. **Tool sidebar — the left strip, "VIEWS" section.** *"Pick a tool here. Each tool answers a different question of the same data. We'll meet all five analytic tools in the next session."*
2. **Tool interface — the middle panel.** *"When you pick a tool, its controls and results appear here. Right now I have Frequency open, which is why you see Token Frequency Analysis in the middle."*
3. **Workspace graph view — top right.** *"This is your map. Each box is a data block — a table of texts plus metadata. Lines between boxes mean one was derived from the other. The graph is your method section."*
4. **Data viewer — bottom right.** *"Click any data block in the graph above, and this table shows you the rows inside. Click any row, you see the full text of that document. Try it — click on a row and read one."*
5. **Data block quick-select — the "DATA BLOCKS" section in the left sidebar.** *"This 'Selected' dropdown lets you switch the active block without clicking back to the graph. Useful when you're comparing."*
6. **Tutorial anchors — the `?` icons next to controls, plus the Tutorial button at the bottom of the sidebar.** *"See these question marks next to controls? Click any one and the tutorial opens at the matching section. Use these as you go today."*
7. **Feedback button — bottom of the left sidebar, next to Tutorial.** *"This is important. Anywhere you see something confusing, surprising, or buggy — tap Feedback. Even one word is fine. We read every one. Today, we want your feedback specifically; you're some of the first researchers outside our team to use the v0.5 version."*

> Why land the feedback button NOW (before the snapshot tour): every minute they're using the app, they should know there's a low-friction way to report friction. Don't let them save it up for after the workshop.

### 0:23 – 0:25 — Sync check

*"Quick check — show of hands, who has Wordflow loaded?"* (Either Binder finished spinning up, or the desktop app is open if they installed it beforehand.)

- If <70% are up: WiFi or Binder problem. Pair attendees with neighbours who are working; deal with stragglers during Session 1.5 setup. **If most of the room can't reach Binder, fall back to the desktop install** — see "Plan B" at the top of the runbook.
- If 70-100% are up: good, push forward.

---

## Session 1.5 — Snapshot tour (0:25 – 0:55, 30 min)

The goal: every participant touches each of the five analytic tools' visualisations. They are **not** building anything yet — they're seeing what the destination looks like, so Session 2 feels like working towards something real.

### 0:25 – 0:30 — Group setup (5 min)

Drive this from your screen and have everyone follow.

1. *"Data Loader → Import sample content → import all three sample datasets (Honi Soit, QLD election tweets, Reddit). You won't use them all now, but they'll be ready for later."* (~1 min)
2. *"Data Loader → Import demo snapshots → import all five demo snapshots from the catalogue."* (~1 min)
3. *"In the sidebar, click the **pencil icon next to 'VIEWS'** — that turns on Snapshot Mode."* (~30s) *"This enables saving and loading snapshots in each tool. Once you load a snapshot into a tool, that tool's view is read-only — you can hover, click, and switch views, but you can't change the parameters or rerun. Other tools stay editable as normal."*
4. *"Create a new workspace called `tour`."* (~30s)

> If anyone is still stuck on import: keep moving. The snapshots are loaded by tool, not by workspace — they'll catch up at the next tool transition.

### 0:30 – 0:55 — Five tools, five minutes each (25 min)

For each tool: **(a) load the snapshot together, (b) facilitator narrates ~2 min, (c) participants explore ~2 min, (d) 30s pivot to next tool.** Stick to the budget — if a tool fascinates someone, they'll come back in the free lab.

#### Tool 1 — Frequency (0:30 – 0:35)

- *"Click Frequency in the sidebar. Click 'Load snapshot' (folder icon). Pick `Freq_Analysis_Newstalk`."*
- Narrate the comparative view: *"What you're looking at is a comparative frequency — two columns, one corpus. The corpus is a set of Australian news stories. I've filtered by source and grouped them: on the left, two left-leaning outlets — Guardian Australia and Independent Australia. On the right, two right-leaning outlets — Sky News Australia and PerthNow. Bigger word = more frequent in that group's stories. Switch to List view if you want exact counts."*
- 2-min explore: *"The interesting move is to spot a word that's big on one side and small or absent on the other — that's where editorial divergence shows up. The loaded snapshot view is read-only, so feel free to click around — nothing reruns."*

> Frame the grouping as a *research assumption*, not a claim. If anyone challenges it: *"Yes — change the grouping and the comparison changes. That's the point. Wordflow makes the regrouping cheap."*

#### Tool 2 — Concordance (0:35 – 0:40)

- *"Concordance in the sidebar. Load snapshot — `SCL_Honi_Soit`."*
- Narrate the regex search: *"This one's a regex search — three patterns in one query. `student\w*` (anything beginning with 'student'), `staff` exactly, and `universit\w+` (university, universities, etc.). Each pattern gets its own colour."*
- *"Switch to Dispersion view. Each bar is one document; the coloured marks show where each pattern lands in that document — at a glance, which documents talk about students, which about staff, which about the institution itself."*
- 2-min explore: *"Try editing the search to a term of your own. Multi-pattern with coloured-by-term is one of the things that's hard to do by hand on a big corpus and trivial here."*

> Combined view is intentionally OFF on this snapshot — two views (table + dispersion) at a time, not four. Less to parse.

#### Tool 3 — Trends (0:40 – 0:45)

- *"Trends in the sidebar. Load snapshot — `QLD_Election_Tweets_conc`."*
- Narrate: *"This Trends view is built on a Concordance result — three patterns searched across QLD candidate tweets: `job\w*`, `lnp\w*`, and `economic`. Each match is one row underneath; here we're plotting them over time, at hourly resolution."*
- *"The grouping control is the magic — switch between **matched term**, **gender**, and **party** and you get three different stories from the same matches."*
- 2-min explore: *"Try changing the grouping. Try coarsening the time bin from hour → day → week. Everything re-aggregates client-side — no rerun."*

> v0.5 features worth pointing out: client-side re-aggregation (time bin) and live regrouping (categorical axis). They can swap the lens twice in 30 seconds — that's what makes Wordflow feel fluid.

> Heads-up on data: this is a *different* corpus from Tool 1's newstalk media articles. Tool 1 was the **2025 QLD election** as covered by news outlets; this Trends view is **2020 QLD election** tweets posted by candidates themselves. Same broad context, different year, different source. Don't conflate them in narration if a participant asks.

#### Tool 4 — Topic Modelling (0:45 – 0:50)

- *"Topic Modelling in the sidebar. Load snapshot — `newstalk_left_vs_right`."*
- Narrate: *"Same corpus as Tool 1 — left-leaning vs right-leaning Australian news outlets. But this time, we're not comparing word frequencies; we're asking BERTopic to discover thematic clusters automatically. Eight topics. Bubble size = how many articles fit; bubble position reflects how thematically related topics are to each other."*
- *"Watch the colours. Bubbles where the colours blend are topics with articles from BOTH sides — converging themes. Solid-colour bubbles are topics where one side dominates."*
- 2-min explore: *"Hover over a bubble for the top words; click for the full ranking."*

> Why this matters: Tool 1 asked *"which words differ?"*; Tool 4 asks *"which themes cluster?"* — same corpus, different question. That's the lens-shifting message of the whole workshop, sneaked into the snapshot tour. Don't say it explicitly — let participants notice.

> If someone asks about corpus sizes: the right-leaning corpus has 301 articles, the left-leaning 121. I downsampled the right to 40% (120) so topic discovery isn't biased by the larger corpus. The model used `min_topic_size=7` and `seed=46` — tuned for visual interest, not statistical defensibility.

#### Tool 5 — Quotation (0:50 – 0:55)

- *"Quotation in the sidebar. Load snapshot — `SCL_Honi_Soit`."*
- Narrate: *"Quoted speech extracted automatically with the speaker. From 100 Honi Soit articles, the tool pulled around 870 quotations across 95 documents — student newspapers are quote-rich. Each row is one extracted quote with its speaker; click for the surrounding context."*
- 2-min explore: *"Sort by speaker to see who gets quoted most. Click around. The 5 articles with zero hits could be genuinely quote-less or could be mis-misses — the extractor isn't perfect. English only for now."*

> Snapshot name overlap: this is the same filename as the Tool 2 (Concordance) snapshot, since Wordflow scopes snapshots per tool. Participants picking from the Quotation tool's load dialog only see the Quotation-tool version, so there's no actual collision — but if anyone asks *"wait, didn't I already load this?"*, the answer is: same name, different tool, different file.

> Why Quotation last: it's English-only and the narrowest. If you're running over by 5 min already, you can cut it without losing the lesson.

### 0:55 — Recap + hand-off to break

Advance to **Slide 14** (the red "Before the break" slide). Land this bridge clearly — it's the conceptual hinge between the snapshot tour and Session 2. ~45–60 seconds spoken.

*"Quick recap before the break. Five tools, five views — that's what you've just seen. Same data through different lenses.*

*Here's what the snapshot tour didn't show. Right now in Snapshot Mode, every loaded view is read-only — that's why you couldn't change parameters. **Out of Snapshot Mode**, every analysis result you produce can be **added back into the workspace as a new data block** — and that new block can feed into another tool. None of these tools is a dead end. They feed each other.*

*That's what makes Wordflow a workflow tool, not just a visualisation tool. The text flows; the lens changes.*

*Take 15 minutes. When we come back, we'll walk one of those chains end to end."*

> Don't skip this slide even if you're running on time. The whole workshop's north star ("text data flows through stackable, single-purpose tools") lands here for the first time. If you're behind, drop a snapshot tour tool (Quotation is the easiest cut) — but don't cut this.

---

## Break 1 (0:55 – 1:10, 15 min)

---

## Session 2 — Research story (1:10 – 1:55, 45 min)

**The story:** *"Are there gender-based differences in how QLD election candidates tweeted about topical issues during the 2020 campaign?"*

**Mode:** Facilitator demo at full speed + participants follow only the moves marked **try this** in the hands-on-2 sheet. ~25 min demo + ~20 min selective follow-along.

**Recovery:** Four checkpoints. At each, mention the corresponding snapshot/workspace archive on the whiteboard. Anyone who's lost loads it and rejoins. Don't lose more than 60 seconds shepherding stragglers — the archives are the safety net.

### 1:10 – 1:15 — Frame the research question + disable snapshot mode

Slide 17.

*"For the next 45 minutes, I'm going to walk a real research workflow. The question: did female and male candidates in the 2020 QLD election tweet about different topical issues? We'll build a workflow that answers it.*

*You don't have to follow every step. Your hands-on sheet marks some moves as 'try this' — pick up the keyboard for those. Other moves are marked 'watch' — sit back and look at my screen. If you fall behind, the whiteboard has download links for snapshots and workspace archives at four checkpoints; load whichever you need to rejoin.*

*First — turn OFF Snapshot Mode. The toggle is the pencil icon next to 'VIEWS' in the sidebar — same place you turned it on. We're building, not just looking."*

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

1. *Install it locally — desktop link is on bit.ly/wordflows, same URL you used today — and try it on your own work.*
2. *If you publish using it, cite the project — the citation is on the docs site.*
3. *Tap the feedback button as you go. Send us bugs. Send us 'this rocks'. Send us 'this is confusing'. Every one helps.*

*And — spread the word. If you have a colleague who works with text and is allergic to coding, they should know this exists.*

*Tonight you'll get an email with the snapshots and workspace archive from today, the docs, and one question: what would have made today more useful? Reply with one sentence. The desktop install link is on bit.ly/wordflows whenever you want it.*

*Thanks. Have a good evening."*

---

## After participants leave

- Note what timing slipped, what landed, what stumbled. Use it to tune next delivery.
- Send `communications/post-workshop-email.md` within 24 hours with the snapshots and workspace archive attached or linked.
