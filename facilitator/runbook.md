# Facilitator Runbook — Wordflow 3h Workshop

Minute-by-minute script. **Italics = your spoken framing**, plain text = facilitator actions, `> blocks` = teaching points to land before moving on.

---

## Before participants arrive (T-30 min)

- Projector connected; `slides/index.html` open, slide 1 visible.
- Wordflow open on your demo screen, the demo workspace already prepared with five demo snapshots imported.
- **sih.tools/wordflow** is visible on slide 3 (Housekeeping) so people can launch Wordflow as they arrive. (USyd-internal workshop — no separate WiFi login needed.)
- The **five Session-2 checkpoint workspace archives** (`Checkpoint_A.zip` through `Checkpoint_E.zip`) published as a GitHub release on `milysun/wordflow-workshop` so the same `sih.tools/wordflow` link gets people to them too.
- The **feedback form URL** open in a browser tab so you can flash it on demand.
- `participant/welcome.md` and `participant/cheat-sheet.md` on every chair.
- Pen and paper on every table.
- A glass of water for you.

---

## Plan B — if Binder is down or overloaded

**Trigger:** at the 1:53 pm sync check (or earlier if it's obvious from the room), fewer than ~70% of attendees have Wordflow loaded, AND it's not just stragglers — Binder is unreachable, painfully slow, or refusing connections.

**The move:**
- Tell the room: *"Binder isn't cooperating today. Anyone who hasn't gotten in: go to sih.tools/wordflow and click the desktop download link instead. Install takes about 5 minutes — we'll wait."*
- Anyone whose Binder *did* load can keep using it.
- Anyone installing: tell them to keep going, you'll loop them in at the next sync check.

**Time recovery** (installing eats 5–8 minutes — see `timing-recovery.md` for the full list of cuts):
- Shorten the project+team narration at 1:35 pm–1:42 pm from 7 min to ~3 min — say *"developed by Sydney Informatics Hub and Sydney Corpus Lab, part of LDaCA, funded by ARDC"* and move on. Save the full attribution for the post-workshop email.
- The Quotation tool in Session 1.5 is the easiest cut (it's last and English-only).
- If still over, ask for one volunteer's screen and have everyone watch the Session 2 demo rather than follow along — the checkpoint files cover the catch-up.

**Pre-emptive mitigation:** the pre-workshop email recommends installing the desktop app as a backup before arriving. If many participants do that, Plan B is almost frictionless.

---

## Session 1.0 — Intro + UI tour (1:30 pm – 1:55 pm, 25 min)

### 1:30 pm – 1:31 pm — Welcome + Acknowledgement of Country

Slides 1 → 2. Stand. Speak slowly and sincerely; this isn't boilerplate. About 30–45 seconds total.

*"Welcome — thank you for being here."*

(Advance to slide 2.)

*"Before we begin, I'd like to acknowledge the Gadigal people of the Eora Nation, the Traditional Custodians of the land on which we meet today. I pay my respects to Elders past and present, and extend that respect to any Aboriginal and Torres Strait Islander people in the room."*

> Wait a beat. Don't rush to the next slide.

### 1:31 pm – 1:35 pm — Sign-in-while-I-talk + housekeeping

Slide 3 (Housekeeping).

*"Three hours, two breaks, lots of clicking. Before I say a word about Wordflow, please open `sih.tools/wordflow` on your laptop and click 'Launch in Binder' — it'll spin up a copy of Wordflow in the cloud for you, takes a couple of minutes. While that's loading, I'll introduce the project and the team. If Binder hasn't loaded after about five minutes, the same URL has a desktop install link."*

- Pause briefly to make sure people have typed the URL.

> Why parallelise: Binder cold-start takes 1–2 minutes the first time. Don't waste classroom minutes watching it spin.

### 1:35 pm – 1:42 pm — Project + team + deployment options

Slide 4 (team), then slide 5 (deployment options).

*"LDaCA Wordflow is developed by a small team at the University of Sydney — myself and Dr Alex Guo at **Sydney Informatics Hub**, with Prof. Monika Bednarek as academic lead at **Sydney Corpus Lab**. It's part of the **Language Data Commons of Australia**, a national HASS and Indigenous research infrastructure project funded by the **Australian Research Data Commons**.*

(Advance to slide 5.)

*Three ways to use it:*
- *Cloud (Binder), which is what you're loading right now — no install, free, but don't put sensitive data on it.*
- *Desktop app (Mac/Windows) — runs everything on your machine.*
- *Python install — `pip install ldaca-wordflow` if you're already a Python user.*

*Today we use the cloud version because it gets everyone running in about a minute. Take the desktop app home for serious work — link is in the post-workshop email."*

### 1:42 pm – 1:53 pm — UI tour (live walkthrough on your screen)

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

### 1:53 pm – 1:55 pm — Sync check

*"Quick check — show of hands, who has Wordflow loaded?"* (Either Binder finished spinning up, or the desktop app is open if they installed it beforehand.)

- If <70% are up: WiFi or Binder problem. Pair attendees with neighbours who are working; deal with stragglers during Session 1.5 setup. **If most of the room can't reach Binder, fall back to the desktop install** — see "Plan B" at the top of the runbook.
- If 70-100% are up: good, push forward.

---

## Session 1.5 — Snapshot tour (1:55 pm – 2:25 pm, 30 min)

The goal: every participant touches each of the five analytic tools' visualisations. They are **not** building anything yet — they're seeing what the destination looks like, so Session 2 feels like working towards something real.

### 1:55 pm – 2:00 pm — Group setup (5 min)

Drive this from your screen and have everyone follow.

1. *"In Data Loader, click **Import sample data**. A modal opens with two tabs."* (~1.5 min)
   - *"**Datasets** tab — select all three: Honi Soit, QLD election 2020 tweets, and the 2025 Federal Election NewsTalk/Reddit bundle."*
   - *"**Demo Snapshots** tab — select all five (the snapshots we'll tour in a minute)."*
   - *"Then click **Import selected** — everything imports together. You won't use it all today, but it'll be ready for later."*
3. *"In the sidebar, click the **pencil icon next to 'VIEWS'** — that turns on Snapshot Mode."* (~30s) *"This enables saving and loading snapshots in each **analysis tool** — Frequency, Concordance, Trends, Topic Modelling, Quotation. (Data Loader, Preprocessing and Export don't have snapshots — those tools build the data, they don't produce views.) Once you load a snapshot into an analysis tool, that tool's view is read-only — you can hover, click, and switch views, but you can't change the parameters or rerun. Other tools stay editable as normal."*
4. *"Create a new workspace called `Wordflow`."* (~30s)

> If anyone is still stuck on import: keep moving. The snapshots are loaded by tool, not by workspace — they'll catch up at the next tool transition.

### 2:00 pm – 2:25 pm — Five tools, five minutes each (25 min)

For each tool: **(a) load the snapshot together, (b) facilitator narrates ~2 min, (c) participants explore ~2 min, (d) 30s pivot to next tool.** Stick to the budget — if a tool fascinates someone, they'll come back in the free lab.

#### Tool 1 — Frequency (2:00 pm – 2:05 pm)

- *"Click Frequency in the sidebar. Click 'Load snapshot' (folder icon). Pick `Freq_Analysis_Newstalk`."*
- Narrate the comparative view: *"What you're looking at is a comparative frequency — two columns, one corpus. The corpus is a set of Australian news stories. I've filtered by source and grouped them: on the left, two left-leaning outlets — Guardian Australia and Independent Australia. On the right, two right-leaning outlets — Sky News Australia and PerthNow. Bigger word = more frequent in that group's stories."*
- *"Switch between **Cloud** and **List** views — same data, just a different visual. List gives you exact counts."*
- Show the stopword shortcut: *"One little gem — **right-click any word** in the cloud or list and it gets added to stopwords. Watch — *[right-click a word]* — gone. Useful for hiding tokens you don't care about without re-running anything."*
- 2-min explore: *"Try the view switch, try right-clicking a few words. Spot a word that's big on one side and small or absent on the other — that's where editorial divergence shows up. The loaded snapshot view is read-only otherwise, so feel free to click around — nothing reruns."*

> Frame the grouping as a *research assumption*, not a claim. If anyone challenges it: *"Yes — change the grouping and the comparison changes. That's the point. Wordflow makes the regrouping cheap."*

#### Tool 2 — Concordance (2:05 pm – 2:10 pm)

- *"Concordance in the sidebar. Load snapshot — `SCL_Honi_Soit`."*
- Narrate the regex search: *"This one's a regex search — three patterns in one query. `student\w*` (anything beginning with 'student'), `staff` exactly, and `universit\w+` (university, universities, etc.). Each pattern gets its own colour."*
- *"Switch to Dispersion view. Each bar is one document; the coloured marks show where each pattern lands in that document — at a glance, which documents talk about students, which about staff, which about the institution itself."*
- 2-min explore: *"Try editing the search to a term of your own. Multi-pattern with coloured-by-term is one of the things that's hard to do by hand on a big corpus and trivial here."*

> Combined view is intentionally OFF on this snapshot — two views (table + dispersion) at a time, not four. Less to parse.

#### Tool 3 — Trends (2:10 pm – 2:15 pm)

- *"Trends in the sidebar. Load snapshot — `QLD_Election_Tweets_conc`."*
- Narrate: *"This Trends view is built on a Concordance result — three patterns searched across QLD candidate tweets: `job\w*`, `lnp\w*`, and `economic`. Each match is one row underneath; here we're plotting them over time, at hourly resolution."*
- *"The grouping control is the magic — switch between **matched term**, **gender**, and **party** and you get three different stories from the same matches."*
- 2-min explore: *"Try changing the grouping. Try coarsening the time bin from hour → day → week. Everything re-aggregates client-side — no rerun."*

> v0.5 features worth pointing out: client-side re-aggregation (time bin) and live regrouping (categorical axis). They can swap the lens twice in 30 seconds — that's what makes Wordflow feel fluid.

> Heads-up on data: this is a *different* corpus from Tool 1's newstalk media articles. Tool 1 was the **2025 QLD election** as covered by news outlets; this Trends view is **2020 QLD election** tweets posted by candidates themselves. Same broad context, different year, different source. Don't conflate them in narration if a participant asks.

#### Tool 4 — Topic Modelling (2:15 pm – 2:20 pm)

- *"Topic Modelling in the sidebar. Load snapshot — `newstalk_left_vs_right`."*
- Narrate: *"Same corpus as Tool 1 — left-leaning vs right-leaning Australian news outlets. But this time, we're not comparing word frequencies; we're asking BERTopic to discover thematic clusters automatically. Eight topics. Bubble size = how many articles fit; bubble position reflects how thematically related topics are to each other."*
- *"Watch the colours. Bubbles where the colours blend are topics with articles from BOTH sides — converging themes. Solid-colour bubbles are topics where one side dominates."*
- 2-min explore: *"Hover over a bubble for the top words; click for the full ranking."*

> Why this matters: Tool 1 asked *"which words differ?"*; Tool 4 asks *"which themes cluster?"* — same corpus, different question. That's the lens-shifting message of the whole workshop, sneaked into the snapshot tour. Don't say it explicitly — let participants notice.

> If someone asks about corpus sizes: the right-leaning corpus has 301 articles, the left-leaning 121. I downsampled the right to 40% (120) so topic discovery isn't biased by the larger corpus. The model used `min_topic_size=7` and `seed=46` — tuned for visual interest, not statistical defensibility.

#### Tool 5 — Quotation (2:20 pm – 2:25 pm)

- *"Quotation in the sidebar. Load snapshot — `SCL_Honi_Soit`."*
- Narrate: *"Quoted speech extracted automatically with the speaker. From 100 Honi Soit articles, the tool pulled around 870 quotations across 95 documents — student newspapers are quote-rich. Each row is one extracted quote with its speaker; click for the surrounding context."*
- 2-min explore: *"Sort by speaker to see who gets quoted most. Click around. The 5 articles with zero hits could be genuinely quote-less or could be mis-misses — the extractor isn't perfect. English only for now."*

> Snapshot name overlap: this is the same filename as the Tool 2 (Concordance) snapshot, since Wordflow scopes snapshots per tool. Participants picking from the Quotation tool's load dialog only see the Quotation-tool version, so there's no actual collision — but if anyone asks *"wait, didn't I already load this?"*, the answer is: same name, different tool, different file.

> Why Quotation last: it's English-only and the narrowest. If you're running over by 5 min already, you can cut it without losing the lesson.

### 2:25 pm — Recap + hand-off to break

Advance to **Slide 14** (the red "Before the break" slide). Land this bridge clearly — it's the conceptual hinge between the snapshot tour and Session 2. ~45–60 seconds spoken.

*"Quick recap before the break. Five tools, five views — that's what you've just seen. Same data through different lenses.*

*Here's what the snapshot tour didn't show. Right now in Snapshot Mode, every loaded view is read-only — that's why you couldn't change parameters. **Out of Snapshot Mode**, every analysis result you produce can be **added back into the workspace as a new data block** — and that new block can feed into another tool. None of these tools is a dead end. They feed each other.*

*That's what makes Wordflow a workflow tool, not just a visualisation tool. The text flows; the lens changes.*

*Take 15 minutes. When we come back, we'll walk one of those chains end to end."*

> Don't skip this slide even if you're running on time. The whole workshop's north star ("text data flows through stackable, single-purpose tools") lands here for the first time. If you're behind, drop a snapshot tour tool (Quotation is the easiest cut) — but don't cut this.

---

## Break 1 (2:25 pm – 2:40 pm, 15 min)

---

## Session 2 — Research story (2:40 pm – 3:25 pm, 45 min)

**The story:** *"Are there gender-based differences in how QLD election candidates tweeted about topical issues during the 2020 campaign?"*

**Mode:** Facilitator demo at full speed + participants follow only the moves marked **try this** in the hands-on-2 sheet. ~30 min demo + ~15 min selective follow-along.

**Recovery:** Five checkpoint workspace archives (A → E), one per phase. At each, mention the corresponding file on **sih.tools/wordflow → Releases**. Anyone who's lost loads it and rejoins. Don't lose more than 60 seconds shepherding stragglers — the archives are the safety net.

### 2:40 pm – 2:45 pm — Frame the research question + disable snapshot mode

Slide 17.

*"For the next 45 minutes, I'm going to walk a real research workflow. The question: did female and male candidates in the 2020 QLD election tweet about different topical issues? We'll build a workflow that answers it — and along the way surface one small empirical finding.*

*You don't have to follow every step. Your hands-on sheet marks some moves as 'try this' — pick up the keyboard for those. Other moves are marked 'watch' — sit back and look at my screen. If you fall behind, **sih.tools/wordflow → Releases** has five checkpoint files (A–E, one per phase); load whichever you need to rejoin.*

*From here on, we're building, not just looking. Snapshot Mode can stay on — it only locks a tool's view once you load a snapshot into that tool. New analyses you start are fine."*

### 2:45 pm – 2:52 pm — A: Load, prepare, join (7 min, WATCH)

There's more to a "load" step than just clicking import. Walk through the typical first-time-user prep moves calmly — narrate each so the room doesn't panic about catching up.

1. **Data Loader** → import (or open) the two source blocks: `qldelection2020_candidate_tweets` and `candidate_info_gender`. *"These are the two starting blocks. The first is one row per tweet; the second is one row per candidate with a gender column."*
2. **Rename** the long block name (optional but worth showing). Open the block's **menu icon** (the small icon on the block) → Rename. `qldelection2020_candidate_tweets` → `tweets`. *"Block names show up in every later step — shorter is better. Wordflow doesn't use right-click — everything is in the menu icon on the block, and the same icon shape sits on each column header for column operations."*
3. **Delete unused columns** (optional but worth showing). Click the **menu icon at the end of a column header** to open that column's menu, then delete. Drop anything you don't need (URLs, retweet counts, whatever doesn't matter for this analysis). *"Smaller blocks load faster, and the column list in later tools is less noisy."*
4. **Set column dtypes** — open a column's menu (or use the dtype dropdown next to its name) and confirm `username` is the same type in both blocks before joining. *"Mixed types break joins and group-bys silently — set them now and you avoid surprises later."*
5. **Preprocessing → Join.** Left join on `username` → Add to Workspace as `tweets_with_gender`. *"The join key is `username` — both blocks have a username column for the candidate. Left join, so we keep all tweets even if the gender info is missing."*
6. If a dtype warning appears at this stage: *"Wordflow noticed something we missed. Accept the auto-standardisation."*
7. *Click `tweets_with_gender` → look at the Data Viewer.* *"Now every tweet has a gender column. Click a row to read one full tweet."*

> Phase A is short on minutes but long on steps — five-to-seven moves, depending on whether you do the optional cleanups. The lesson here is *the data prep work is part of the analysis*; people who skip it often pay later with mysterious bugs. The checkpoint catches anyone who fell off mid-way.

> **Checkpoint A** — workspace archive: `Checkpoint_A.zip`. Mention it explicitly: *"Anyone behind, download checkpoint A from sih.tools/wordflow → Releases."*

### 2:52 pm – 3:01 pm — B: Filter by gender + iterative Freq ↔ Concordance (9 min, TRY THIS)

This is where participants pick up the keyboard.

1. **Preprocessing → Filter** the joined block: `gender = 'F'` → `tweets_female`. Then `gender = 'M'` → `tweets_male`. *"Two sub-blocks by metadata."*

> **Why no hashtag filter?** The dataset is small. Filtering by `text contains "#"` would chop ~half the tweets and weaken the comparison. We keep the full gender corpora.

2. **Select both** in the graph. **Frequency tool → comparative mode (Juxtorpus).** Word count 40, stopwords on.
3. **Iterative exploration**: click a topical word → jumps to Concordance with that word pre-loaded. Read a few contexts. Go back to Frequency, pick a different word. *Repeat — this is the exploration before settling on a final pattern.*
4. After a few rounds, narrate aloud: *"I've been jumping between Frequency and Concordance to spot meaningful patterns. Words I keep coming back to: `cases`, `covid`, and anything starting with `lnp`. Two themes are emerging — health and energy/policy. In the next phase, I'll build a regex that captures all three terms in one search."*

> Land here: *"You just stacked twice — Frequency to Concordance, and back again. Read the graph: that's your method. The regex in Phase C didn't fall from the sky; it came from this iteration."*

> **Checkpoint B** — workspace archive: `Checkpoint_B.zip`.

### 3:01 pm – 3:11 pm — C: Multi-pattern regex → detach → Trends (10 min, MIXED)

#### C-1 — Set the regex, dispersion view, detach as block (WATCH, ~4 min)

1. In Concordance, switch to **Regex mode**. Pattern: `cases|covid|lnp\w*`.
   *"Three patterns covering two themes — health (`cases`, `covid`) and energy/policy (`lnp\w*`)."*
2. Each match coloured by which pattern hit. **Switch view to Dispersion** — bars per tweet, colour-coded.
3. **Click a point** in the dispersion plot, then **Shift-click** another point to extend the selection to a range. Repeat to build up the subset of tweets you want.
4. Click **Add to Workspace** — the matched contexts become a new data block (matched-term column preserved alongside the gender column, ready for Trends).

> The hypothesis we're testing (informally): *do female candidates tweet more about health, and male candidates more about LNP/policy?* Made-up hypothesis on a small dataset — useful as a worked example, not a finding.

#### C-2 — Trends on the matched block, find the lnpcuts skew (TRY THIS, ~6 min)

1. Click the matched block → **Trends tool.** Date column: tweet date. Time bin: weekly.
2. Group by **matched-term × gender** so each combination (e.g. `lnp-M`, `lnp-F`, `lnpqld-M`, `lnpcuts-F`, …) is its own line.
3. Narrate while looking at the chart: *"Lots of pro-LNP terms — `lnp`, `lnpqld`, `lnpgov`. But one stands out as anti-LNP — `lnpcuts`. Let's take a closer look."*
4. **Hide the other lines via the legend** — click the major pro-LNP and health combinations off, one by one, until only `lnpcuts-M` and `lnpcuts-F` remain. *"Female candidates mention `lnpcuts` around 20 times across the campaign; male candidates 4. A 5× skew on a small dataset — suggestive not definitive, but the one term that doesn't fit the pro-LNP pattern shows the strongest gender split."*

> This is the empirical hook of Session 2. The visual punch is the legend-hide sequence — pro-LNP lines disappear one by one until only the anti-LNP `lnpcuts` is left, and the gender gap is suddenly visible. Don't pre-explain; let the chart land it.

> Don't oversell ("we discovered something!") but don't undersell either: *"end-to-end in 30 minutes, and there's something here to dig into."*

> **Checkpoint C** — workspace archive: `Checkpoint_C.zip`.

### 3:11 pm – 3:20 pm — D: Topic modelling on two corpora (9 min, WATCH)

Topic Modelling accepts **two data blocks** as input and produces a fused bubble chart — bubble colours blend in topics that draw documents from both corpora, stay solid in topics dominated by one.

1. **Select both `tweets_female` and `tweets_male`.**
2. **Topic Modelling.** Target = 8 topics, seed = 42. Run. ~60-90s wait.
3. While it runs: *"Look at the Task Centre — that's where slow tasks show progress."*
4. When done: BERTopic actually produces ~23 topics. **Drag the re-aggregation slider to 16** — bubbles spread out, themes become distinguishable.
5. Narrate the colour mixing: *"Solid bubbles are gender-dominant topics; blended bubbles are themes shared across both. Hover for top words."*
6. **Select 2–3 interesting topics → Detach.** Because the topic model ran on two parents, detaching produces *per-gender child blocks* — one set under `tweets_female`, one under `tweets_male`.

> Numbers checked on this corpus: target=8 + seed=42 produces ~23 topics; re-aggregating to **16 spreads the bubbles cleanly**, 5 crushes them. The lesson is interactive tuning, not the magic number.

> **Checkpoint D** — workspace archive: `Checkpoint_D.zip`.

### 3:20 pm – 3:25 pm — E: Stack → final Trends (5 min, WATCH)

The closing move. Stack the per-gender topic blocks back together so the final Trends view can compare topics across genders.

1. **Preprocessing → Stack** the detached topic blocks from `tweets_female` and `tweets_male`. Result: a unified block where each row carries both its topic label and its gender column.
2. Click the stacked block → **Trends.** Time bin weekly. Group by `topic` (or `gender × topic` if the tool supports a two-key group).
3. *"Final view. Selected topics from the two-corpus model, evolving across the campaign, split by gender. End to end — that's our method."*

> **Final landing**: *"Four analysis tools — Frequency, Concordance, Trends (twice), Topic Modelling — across one corpus, one made-up hypothesis, one workflow. We went from raw tweets to a finding — small, suggestive, but real — in 45 minutes. The graph behind me is the whole method, captured as a picture."*

> **Checkpoint E** — workspace archive: `Checkpoint_E.zip`.

---

## Break 2 (3:25 pm – 3:40 pm, 15 min)

---

## Session 3.A — Repurpose the lens (3:40 pm – 3:55 pm, 15 min)

The conceptual payoff. Three short demos showing **you shape the analysis at every step — in, through, and out.** Slow down for Demo 3, that's the one they'll remember.

> No fresh workspace needed — keep using the workshop's `Wordflow` workspace (or wherever you ended Session 2). The snapshots and blocks already there are exactly what the demos use.

### 3:40 pm – 3:43 pm — Demo 1: Export the visualisation (3 min)

*"First, a small but useful thing. Everything you analyse can come back out — as an image or as data."*

1. Open one of the Session 1.5 snapshots — the word cloud (Frequency tool, `Freq_Analysis_Newstalk`) is good because it's visually distinct.
2. **Click the download icon at the top-right corner of the word cloud** — it saves a **PNG** of the cloud. Then switch to the **List view** and use *its* download icon — that saves the underlying ranking as a **CSV**. *"Each visualisation or table has its own download button. Image views give you images, data views give you data."*
3. *"PNG for the slide deck, CSV for the supplementary materials. The same export pattern works in every analytical tool — Trends, Topic Modelling, Concordance, Quotation."*

> The lesson: *your analysis is not trapped in the tool*. Don't dwell.

### 3:43 pm – 3:48 pm — Demo 2: Filter the visualisation → Add to Workspace (5 min)

*"Visualisations aren't just for looking. You can pick parts of them and turn that selection into new analysable data."*

1. Open the **Trends** snapshot — `QLD_Election_Tweets_conc` or your Session 2 final Trends. Has multiple lines (matched terms × gender, or similar).
2. **Legend filtering**: click in the legend to toggle individual lines on and off. Narrate: *"I can hide everything except `lnpcuts` to focus on one term."*
3. **Visual selection**: **click a point** on the chart, then **Shift-click** another to select a range — say, the campaign peak. Click **Add to Workspace**. *"Now I've selected a slice and turned it into a new data block."*
4. *"Same idea, same operation, different tools — quickly:"*
   - Topic Modelling: **click bubbles** to select interesting topics → Detach → new blocks. *(We saw this in Session 2.)*
   - Concordance: **dispersion view** — click + Shift-click on hit markers to select tweets → **Add to Workspace**. *(We saw this too.)*
5. *"In every visual tool: see something interesting, select it, make it new data. That's reading and analysing in one move."*

### 3:48 pm – 3:53 pm — Demo 3: Create a column → Trends becomes a histogram (5 min)

*"Now the big one. Trends is the time-series tool, right? Line chart over dates. But the x-axis doesn't have to be time."*

1. Pick the **Honi Soit articles block** — they're longer and more varied in length than tweets, so the histogram is interesting.
2. **Preprocessing → Create column.** New column: **word count per article** (number of tokens in the text column).
3. **Trends tool.** Set the **x-axis to the new word-count column** (not the date).
4. **Numeric bucketing: 100 intervals.** *"Fine-grained — we want to see the shape of the distribution."*
5. **Switch chart type from line to bar.** *"Now Trends is showing a histogram — article count per word-length bucket."*
6. (Optional) Add a grouping by year or section if available. *"Histogram of article length, split by something else. Same chart, different question."*

### 3:53 pm – 3:55 pm — Land it + click feedback (2 min)

Advance to the landing slide. Speak slowly:

*"The tool didn't change. **I** changed how I shaped the data."*

Pause. Let it sit. Then:

*"Every tool in Wordflow is a lens. The interesting research question is always: which lens, on which slice of which corpus, will tell me something I didn't already know? That's your job. Wordflow makes the lens-changing cheap."*

Then — **click the Feedback button on screen** to open the form. Don't fill it in; just show the form is there:

*"While I'm here — this is the feedback button. I want you to use it twice today: once during the lab in a minute, every time something is confusing or surprising; and again later, if you keep using Wordflow, send us a note about what you'd want next."*

> If this is the moment they tweet about, the workshop succeeded.

---

## Session 3.B — Lab framing + feedback ask (3:55 pm – 4:00 pm, 5 min)

*"Next 25 minutes: free lab. Three tracks — pick whichever fits.*

- *Track A: keep building on Session 2 — try the moves you watched but didn't follow. Workspace archive is on the board.*
- *Track B: bring your own data. Upload a CSV with at least one text column. My helper and I will be around.*
- *Track C: open exploration — pick a tool, pick a sample dataset, see what falls out.*

*One ask: every time you hit something confusing, weird, or broken — tap the Feedback button at the bottom of the left sidebar. Even just 'this is confusing' helps us. You're our v0.5 beta room."*

Slide reminder: feedback URL also accessible directly at the URL on the board.

---

## Session 3.C — Free hands-on (4:00 pm – 4:25 pm, 25 min)

You and any helpers walk the room. Common questions in `common-questions.md`. Prompts for the three tracks in `hands-on-3.md` for participants.

Time check at 4:20 pm — start corralling everyone back to their seats with *"five minutes — finish your current click."*

---

## Session 3.D — Thanks + close (4:25 pm – 4:30 pm, 5 min)

Two slides: **Slide 31 (Thank you)** for the three asks, then **Slide 32 (Data acknowledgements)** as the final reference slide that stays up while people gather their things.

*"Thank you for spending three hours with us. Three asks if Wordflow turned out useful:*

1. *Install it locally — desktop link is on sih.tools/wordflow, same URL you used today — and try it on your own work.*
2. *If you publish using it, cite the project — the citation is on the docs site.*
3. *Tap the feedback button as you go. Bug reports, improvement advice, "I need more", or just "this rocks" — all helpful.*

*And — spread the word. If you have a colleague who works with text and is allergic to coding, they should know this exists.*

*Tonight you'll get an email with the snapshots and workspace archive from today, the docs, and one question: what would have made today more useful? Reply with one sentence. The desktop install link is on sih.tools/wordflow whenever you want it.*

*Thanks. Have a good evening."*

---

## After participants leave

- Note what timing slipped, what landed, what stumbled. Use it to tune next delivery.
- Send `communications/post-workshop-email.md` within 24 hours with the snapshots and workspace archive attached or linked.
