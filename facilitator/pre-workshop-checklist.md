# Pre-Workshop Checklist

Tasks to complete in the week leading up to the workshop, roughly in order.

---

## T-7 days: confirm logistics

- [ ] Venue confirmed; power outlets verified; projector + adapter on hand.
- [ ] WiFi password posted; capacity check on Nectar BinderHub if cloud-hosted.
- [ ] Participant list final. Send `communications/pre-workshop-email.md`.
- [ ] Decide hosting: Binder (cloud) is the default; mention desktop install only in passing.
- [ ] Print `participant/welcome.md` (one per attendee) and `participant/cheat-sheet.md` (double-sided, one per attendee).
- [ ] Decide a stable URL for the Session-2 workspace archive + checkpoint snapshots. Box / OneDrive / SharePoint / GitHub release / Sydney Hub static page all fine. The URL must be short enough to write on a whiteboard.

---

## T-5 days: capture five demo snapshots (Session 1.5)

The Session-1.5 snapshot tour shows each tool's destination visualisation. You need **one demo snapshot per analytical tool**, pre-loaded on every participant's instance via the demo-snapshot catalogue (or hosted at the workshop URL for manual import).

For each below — open Wordflow locally, run the analysis with the listed parameters, click the **Save snapshot** camera in the tool header, use the filename listed, then copy to a publishable location.

### Snapshot 1 — Frequency

- Dataset: Honi Soit
- Tool: Frequency
- Stopwords: English, on
- Top-N: 60
- View at save time: Cloud
- Filename: `token_frequencies-honi-soit-overview.ldaca-snapshot`

### Snapshot 2 — Concordance

- Dataset: Honi Soit
- Tool: Concordance, Text mode
- Search term: `student`
- Context window: 10
- View at save time: Dispersion
- Filename: `concordance-honi-soit-student.ldaca-snapshot`

### Snapshot 3 — Trends

- Dataset: Reddit (download first; ~37 MB)
- Tool: Trends
- Time bin: month
- Group-by: `subreddit`
- Filename: `sequential_analysis-reddit-monthly.ldaca-snapshot`

### Snapshot 4 — Topic Modelling

- Dataset: Honi Soit
- Tool: Topic Modelling
- Defaults. Let BERTopic finish.
- View at save time: bubble chart
- Filename: `topic_modeling-honi-soit-topics.ldaca-snapshot`

### Snapshot 5 — Quotation

- Dataset: Honi Soit
- Tool: Quotation
- Defaults
- Filename: `quotation-honi-soit-speakers.ldaca-snapshot`

---

## T-4 days: build the Session-2 research story + capture checkpoints

This is the big prep block. You'll build the full Session-2 workflow yourself in advance, export workspace archives + snapshots at each checkpoint, and host them for participants to load if they fall behind.

### Build the workflow

Open Wordflow in a fresh workspace called `session2-master`. Walk the full A→B→C→D→E chain (script in `runbook.md` Session 2). As you go:

- **At end of A** (joined-then-split-then-filtered): export the workspace as a portable archive.
  - File: `session2-after-A.wordflow-workspace`
  - Includes: `tweets_with_gender`, `tweets_female`, `tweets_male`, `tweets_female_hashtagged`, `tweets_male_hashtagged`.

- **At end of B** (comparative frequency): save the Frequency snapshot.
  - File: `frequency-tweets-comparative.ldaca-snapshot`

- **At end of C-2** (aggregated Concordance contexts): export the workspace.
  - File: `session2-after-C.wordflow-workspace`
  - Includes everything above plus the aggregated context block.

- **At end of D** (Trends with grouping): save the Trends snapshot.
  - File: `trends-aggregated-by-gender.ldaca-snapshot`

That's **2 workspace archives + 2 snapshots = 4 checkpoints**. Anyone who falls off mid-Session-2 can rejoin from whichever checkpoint matches where you are in the demo.

### Test cross-OS

The workspace-archive portability was recently fixed (May 2026). Before the workshop, **test importing each `.wordflow-workspace` on a different OS than the one you exported from** — Mac → Windows, or Linux → Mac, whichever pair you can manage. If anything breaks, file an issue and fall back to snapshots-only recovery for now.

### Publish

Upload all 5 demo snapshots, the 2 workspace archives, and the 2 checkpoint snapshots to your hosting location. Verify each link works in a fresh browser session (logged out, no cache).

---

## T-3 days: rehearse Session 2 against the wall clock

Session 2 is the most ambitious 45 minutes of the day. Practise it twice.

- [ ] **Run 1 — full demo at your fastest comfortable speed.** Stopwatch on. Note where each phase ends.
  - Target: A ≤ 10 min, B ≤ 10 min, C ≤ 10 min, D ≤ 5 min, E ≤ 5 min, total ≤ 40 min with 5 min buffer.
  - If you blow past 45 min: the most likely cut is E (topic modelling), then C-2 (regex dispersion). Plan which.

- [ ] **Run 2 — practise narrating each step out loud as if to an audience.** Includes the cross-tool moments: the Frequency → Concordance left-click jump, the dispersion-select → aggregated block, the detach topics → group in Trends.

---

## T-2 days: rehearse Sessions 1 and 3

- [ ] Walk through Session 1.0 (slides 1-12) out loud. Time it. Target ≤ 25 min including 3-min for the parallel Binder sign-in.
- [ ] Walk through the Session 1.5 snapshot tour. Five tools, 5 min each. Practise saying *"two more minutes"* and switching cleanly.
- [ ] Rehearse the Session 3.A repurpose-the-lens demo end-to-end. Practise saying *"the tool didn't change; I changed how I shaped the data"* without looking at your notes.

---

## T-1 day: laptop dry run

- [ ] Restart the demo laptop. Confirm Wordflow opens, the master workspace exists, all five demo snapshots are present.
- [ ] Test the projector cable. Extended display is usually better than mirrored — test both.
- [ ] Phone fully charged (backup hotspot if WiFi fails).
- [ ] Charge a backup laptop with the same setup if you have one.
- [ ] Confirm the hosting URL still resolves and downloads aren't broken.

---

## Day of: 30 min before start

- [ ] Doors open 15 min early.
- [ ] Slides on screen at slide 1.
- [ ] Wordflow open in background at the demo workspace.
- [ ] `runbook.md` on a second screen or printed.
- [ ] Whiteboard: **WiFi password**, **Workshop URL**, **Resources URL** (snapshots + archives), **Feedback URL**.
- [ ] `welcome.md` + `cheat-sheet.md` on every chair.
- [ ] Pens / sticky notes on every table.
- [ ] Glass of water for you.
- [ ] At least one helper briefed and at the back of the room.

---

## Optional: publish demo snapshots to the catalogue

If you want post-workshop attendees (or future workshops) to import the **demo snapshots** directly from the in-app Demo Snapshots tab:

1. Copy each `.ldaca-snapshot` file to `ldaca-analytics-sample-data/demo_snapshots/`.
2. Compute SHA-256: `shasum -a 256 <filename>`.
3. Append entries to `ldaca-analytics-sample-data/demo_snapshots/catalogue.json` (schema in that folder's README).
4. Commit and push the `ldaca-analytics-sample-data` submodule, then bump the master submodule pointer.

This is **optional**. Hosting the snapshots at a workshop URL is sufficient for the day.

The **Session-2 checkpoint workspace archives** should **not** go in the demo-snapshot catalogue — they're workshop-specific and not generally useful. Host them at the workshop URL only.
