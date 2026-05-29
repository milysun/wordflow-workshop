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

## T-5 days: verify the Session-1.5 demo snapshots

The Session-1.5 snapshot tour shows each tool's destination visualisation. The five demo snapshots ship with the **`ldaca-analytics-sample-data`** repo and get imported automatically alongside the sample datasets during Session 1.5's group-setup step — you don't need to upload them anywhere yourself.

What you *do* need to do, a few days out: **open Wordflow locally, import the sample data, load each demo snapshot, and confirm it still matches the spec below.** If anything has drifted (filename change, parameter change, dataset shape change in upstream sample data), flag it and update the matching slide / hands-on bullet so the runbook stays accurate. The specs below are the source of truth for what *should* be in each snapshot:

### Snapshot 1 — Frequency (comparative)

- Dataset: `newstalk_stories`
- Preprocessing: filter by source, then **group into two blocks**:
  - **Left-leaning block** — Guardian (`guardian`) + Independent Australia (`ia`)
  - **Right-leaning block** — Sky News (`sky`) + PerthNow (`perthnow`)
  - (Set aside `msn`, `riotact`, `acm` — aggregator + local + mixed regional.)
- Tool: Frequency, **comparative mode** (select both blocks before opening Frequency)
- Stopwords: English, on
- Top-N: 60
- View at save time: Cloud
- Filename: `Freq_Analysis_Newstalk.ldaca-snapshot`

### Snapshot 2 — Concordance (regex, multi-pattern)

- Dataset: SCL / Honi Soit
- Tool: Concordance, **Regex mode**
- Pattern: `student\w*|staff|universit\w+` — three patterns; each match coloured by which pattern it hit
- Context window: 10
- **Combined view: OFF** (so participants see one view at a time, not 2×2 = 4)
- View at save time: Dispersion (with the row table alongside)
- Filename: `SCL_Honi_Soit.ldaca-snapshot`

### Snapshot 3 — Trends (built on a Concordance export)

- Dataset: **2020 QLD election candidate tweets**, joined with `candidate_info_gender` — distinct from the 2025 newstalk media stories used in Snapshot 1, even though both touch QLD politics
- Preprocessing:
  1. Run **Concordance** on the joined block with regex pattern `jobs|cases|economic`.
  2. **Add the Concordance results as a new data block** so the matched-term column is preserved alongside `gender` and `party`.
- Tool: Trends on the matched block
- Time bin at save time: **hour** (the smallest available — participants can coarsen during the demo)
- Available groupings (must be preserved in the snapshot): **matched term**, **gender**, **party**
- Filename: `QLD_Election_Tweets_conc.ldaca-snapshot`

> Confirm before saving: in Snapshot Mode, all three grouping options can still be switched live. If a column gets dropped during export, the demo loses its punch.

### Snapshot 4 — Topic Modelling (newstalk, balanced)

- Dataset: **same** `newstalk_stories` source as Snapshot 1 (left vs right groupings)
- Preprocessing — **balance the corpora** before topic modelling:
  - Left (`guardian` + `ia`): 121 articles, use all
  - Right (`sky` + `perthnow`): 301 articles → **apply 40% sample → 120 articles**
- Tool: Topic Modelling on the combined balanced corpus
- Parameters: **`min_topic_size = 7`**, **`seed = 46`**
- Expected result: **~8 topics** with fair distances on the bubble plot; some bubbles should show colour blending (articles from both sides) and some should be solid (one side dominant)
- View at save time: bubble chart
- Filename: `newstalk_left_vs_right.ldaca-snapshot`

> The sampling matters. If you regenerate without the 40% sample, topic discovery will be biased by the larger right-leaning corpus. The balanced input (120 vs 121) makes the colour mixing on bubbles meaningful.

> The seed (`46`) and `min_topic_size` (`7`) are tuned for **visual interest** in the demo — fair topic distances on the plot and meaningful word clusters in each topic — not necessarily for a "right" topic model. The lesson is "themes can be discovered automatically", not "BERTopic found the truth."

### Snapshot 5 — Quotation

- Dataset: 100-article Honi Soit sample
- Tool: Quotation
- Parameters: defaults
- Expected result: **~870 quotations across 95 of the 100 documents** (5 documents will show no extracted quotes — could be genuinely quote-less, could be misses; that's fine for the demo and worth mentioning honestly)
- Filename: `SCL_Honi_Soit.ldaca-snapshot`

> Naming note: this is the same filename as Snapshot 2 (Concordance on Honi Soit). Wordflow scopes snapshots per tool, so the two files live in separate per-tool registries and don't collide on load. If you'd prefer distinct filenames for your own bookkeeping (e.g., `SCL_Honi_Soit_concordance` / `SCL_Honi_Soit_quotation`), that's harmless to do.

---

## T-4 days: build the Session-2 research story + capture checkpoints

This is the big prep block. You'll build the full Session-2 workflow yourself in advance, export workspace archives + snapshots at each checkpoint, and host them for participants to load if they fall behind.

### Build the workflow

Open Wordflow in a fresh workspace called `session2-master`. Walk the full A→B→C→D→E chain (script in `runbook.md` Session 2). At each phase boundary, **export the workspace as a portable archive** — five files total, one per phase:

- **At end of A** (data prep complete: imports loaded, renames applied, unused columns dropped, dtypes set, join done → `tweets_with_gender`):
  - File: `Checkpoint_A.zip`
  - This is the most procedurally dense phase for first-time users — 5-7 moves — which is why it gets its own checkpoint.

- **At end of B** (gender-filtered: `tweets_female`, `tweets_male` added, comparative Frequency + iterative Concordance explored):
  - File: `Checkpoint_B.zip`

- **At end of C** (regex `covid|case(s)?|cut(s)?` → aggregated block added; Trends on it with the `cut(s)` gender gap verified):
  - File: `Checkpoint_C.zip`
  - **Verify before saving**: with Trends grouped by matched-term × gender, filtering the `covid`/`case`/`cases` combinations off via the legend leaves only the `cut` / `cuts` lines; switching the chart from line to bar shows male candidates mentioning `cut(s)` more often than female (sharper with the time bin set to weekly). That's the empirical hook of Session 2 — if it doesn't reproduce on your laptop, dig in before the workshop.

- **At end of D** (Topic Modelling on `tweets_female` + `tweets_male` as two corpora, target = 8 / seed = 42 / re-aggregated to 16; 2-3 topics detached as per-gender children):
  - File: `Checkpoint_D.zip`
  - **Verify before saving**: detached topics appear as child blocks under *both* `tweets_female` and `tweets_male` in the graph. If detach produces a single block instead of per-gender children, the topic modelling wasn't run on two corpora — re-run it with both selected.

- **At end of E** (Stack the per-gender topic blocks → unified block → final Trends viewed):
  - File: `Checkpoint_E.zip`

That's **5 workspace archives = 5 checkpoints**, one per phase. Anyone who falls off mid-Session-2 can rejoin from whichever checkpoint matches where you are in the demo.

### Test cross-OS

The workspace-archive portability was recently fixed (May 2026). Before the workshop, **test importing each `Checkpoint_*.zip` on a different OS than the one you exported from** — Mac → Windows, or Linux → Mac, whichever pair you can manage. If anything breaks, file an issue and fall back to snapshots-only recovery for now.

### Publish the Session-2 checkpoints

The five Session-2 workspace archives (A–E) are **workshop-specific** — they live as a tagged release on `milysun/wordflow-workshop`, on this delivery's branch. The five Session-1.5 demo snapshots are handled separately via the `ldaca-analytics-sample-data` repo and don't need uploading here.

To create the release:

```bash
# In your terminal, on this branch:
git checkout intro_workshop_2026-06-03
git tag intro-2026-06-03
git push origin intro-2026-06-03
```

Then on GitHub:

1. Go to `https://github.com/milysun/wordflow-workshop/releases/new`.
2. **Choose a tag**: `intro-2026-06-03`. **Target**: `intro_workshop_2026-06-03`.
3. **Release title**: *Intro to Wordflow — 3 June 2026*.
4. **Description**: list the five archives with one-line descriptions of what each represents (copy from the Build section above).
5. **Attach binaries**: drag in all five `Checkpoint_*.zip` files (`Checkpoint_A.zip` … `Checkpoint_E.zip`).
6. **Publish**.

Verify the download links work in a fresh browser session (logged out, no cache). The link `sih.tools/wordflow → Releases` now resolves to your release; this is what the runbook tells participants to use when they fall behind.

> **Why GitHub Releases?** One URL (`sih.tools/wordflow`) gets people to both the landing page and the release assets, versioned per workshop delivery. No separate Box / OneDrive link to communicate. Each future delivery becomes a new release on its own branch.

---

## T-3 days: rehearse Session 2 against the wall clock

Session 2 is the most ambitious 45 minutes of the day. Practise it twice.

- [ ] **Run 1 — full demo at your fastest comfortable speed.** Stopwatch on. Note where each phase ends.
  - Target: A ≤ 7 min, B ≤ 9 min, C ≤ 10 min, D ≤ 9 min, E ≤ 5 min, total ≤ 40 min with 5 min buffer.
  - If you blow past 45 min: the most likely cut is Phase E (stack + final Trends — describe verbally instead). Phase D's BERTopic run is the next cut (skip the live run, narrate from the saved D checkpoint). Plan in advance which.

- [ ] **Run 2 — practise narrating each step out loud as if to an audience.** Includes the cross-tool moments: the iterative Frequency ↔ Concordance loop in B, the dispersion-select → aggregated block in C-1, the COVID-legend-filter → line→bar comparison on `cut(s)` in C-2 (the empirical hook), the two-corpus Topic Modelling colour-fusion in D, and the Stack → final Trends close in E.

- [ ] **Phase D parameter check.** On the build laptop, run Topic Modelling with **target = 8 topics and seed = 42** with *both* `tweets_female` and `tweets_male` selected. Expect BERTopic to actually produce ~23 topics. Drag the **re-aggregation slider to 16**, confirm the bubbles spread out cleanly with visible colour fusion on shared topics. Detach 2-3 topics and confirm they appear as child blocks under *both* parents. If the slider value or detach behaviour differs from this on the workshop day, narration needs adjusting on the fly.

---

## T-2 days: rehearse Sessions 1 and 3

- [ ] Walk through Session 1.0 (slides 1-6) out loud. Time it. Target ≤ 25 min including 3-min for the parallel Binder sign-in.
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
