# Wordflow — In-person Intro Workshop, University of Melbourne, 26 October 2026

> **This branch: `melbourne_mdap_workshop_2026-10-26`.** Status: **planning** (branched 2026-09-20 from `online_workshop_2026-08-28`).
>
> A single **in-person** session at the **University of Melbourne**, co-hosted by the **Melbourne Data Analytics Platform (MDAP)**, **LDaCA** and the **Sydney Informatics Hub** (with the Sydney Corpus Lab acknowledged as Wordflow's development partner), introducing **Wordflow (latest v0.7 release)** to researchers. **Monday 26 October 2026**, **3 hours** (decided 2026-09-20; start time TBC; MDAP to say if 3 h is too long). Same shape as the June intro workshop.
>
> Working plan (tools not yet fixed; a sketch to be replaced by a proper session table):
>
> | Approx. | Block | Notes |
> |---|---|---|
> | 0:00–0:20 | Welcome, concepts, interface tour | Participants open the app in parallel |
> | 0:20–1:30 | **Part 1** Simplified June intro: a multi-tool research workflow (import → prepare → Frequency / Concordance / Trends / Topic Modelling → export), demo + follow-along | Includes a 10-min break; checkpoint archives for anyone who falls behind |
> | 1:30–1:45 | Break | |
> | 1:45–2:30 | **Part 2** The **Annotation** tool (GenAI text coding): codebook → pilot → agreement → revise | Drawn from the August Session 2 hands-on, cut down |
> | 2:30–3:00 | Open lab, questions, own data; wrap-up | **The buffer.** Hands-on sessions always run slower than planned; this block absorbs the overrun, and if the room is behind it becomes an optional stay-on session |
>
> Pacing rule for this delivery: plan every hands-on block for the slowest third of the room, and treat the final 30 minutes as optional so nobody leaves mid-exercise.
>
> **Sources on this branch.** The August online materials (`slides/online-s1-intro.html` = condensed June intro on v0.7; `slides/online-s2-annotation.html` + `participant/hands-on-annotation-online.md` = Annotation hands-on; `artifacts/checkpoints/` = v0.7.7 checkpoint archives) are kept here as the starting point and will be replaced by this workshop's own files. **Remove the August-only files before the pre-workshop email links participants to this branch.** The June 3-hour in-person structure is on [`intro_workshop_2026-06-03`](../../tree/intro_workshop_2026-06-03) (v0.5-era: check every UI claim against the v0.7 list in CLAUDE.md).
>
> The rest of this README still describes the **28 August online workshop** and is to be rewritten as the Melbourne plan firms up. General blurb: [communications/event-blurb-2026-10-26.md](communications/event-blurb-2026-10-26.md).

---

## North star

Refined from June (wording tightened 2026-08-21; the idea is unchanged):

> **One thing they leave knowing:** *text data flows through stackable, single-purpose tools, and the meaning of an analysis comes from how you shape your data, not from the tool itself.*

Plus the afternoon's extension: *an AI model is just another coder — it earns trust the same way a human coder does: codebook, pilot, agreement scores, revision.*

## Session structure

| Time (AEST) | Time (AWST) | Session | Duration | Mode |
|---|---|---|---|---|
| 11:00 am – 12:30 pm | 9:00 – 10:30 am | **1** Wordflow: concepts, interface, and a real multi-tool workflow | 90 min | Presentation + live demo. **No hands-on. Recorded.** |
| 12:30 – 2:00 pm | 10:30 am – 12:00 pm | **Lunch break** | 90 min | Also the install/setup window for Session 2 |
| 2:00 – 3:30 pm | 12:00 – 1:30 pm | **2** Hands-on: coding text with GenAI (Annotation tool) | 90 min | Participant hands-on. **Not recorded.** |

*Times chosen for a nation-wide audience: WA participants (2 h behind AEST) get Session 1 in early working hours rather than before 9 am, and Session 2 over their midday.*

### Session 1 outline (demo-only, recorded) — revised 2026-08-24

A **full-capability tour in eight per-tool chapters**, built live in one workspace from empty to export, cut for reuse as tutorial chapters. The on-screen stance is exploratory: no defined research question, no conclusions promised. Privately, the jobs/cuts campaign language recurs across chapters as connective tissue (and happens to be the afternoon's Annotation theme), and gender serves as a convenient binary split; neither is announced as a claim. Click-level steps: `facilitator/demo-checklist-s1.md`.

| Min | Chapter |
|---|---|
| 0:00–0:12 | Slides: welcome, Acknowledgement of Country, team/LDaCA, three ways to run it, demo roadmap + dataset slide (exploratory stance) |
| 0:12–0:21 | Ch 1 Getting around: hints, workspace, sample import, drag-and-drop, graph/data views |
| 0:21–0:34 | Ch 2 Preparing data: dtypes, Create, Join, Filter (+ chat pause) |
| 0:34–0:44 | Ch 3 Frequency: Honi Soit single + tweets F/M comparative → click into Concordance |
| 0:44–0:56 | Ch 4 Concordance: tweets jobs/cuts + Honi Soit dispersion (+ chat pause) |
| 0:56–1:04 | Ch 5 Trends (background jobs kicked off first: Honi Soit topic model + Quotation Run All) |
| 1:04–1:16 | Ch 6 Topic Modelling: live F/M run, bubbles, job topics → Trends |
| 1:16–1:22 | Ch 7 Quotation (from the background run) · Ch 8 Export & workspace archives |
| 1:22–1:30 | Recap → bridge to the afternoon, takeaways, lunch/setup slide |

### Session 2 outline (hands-on, not recorded)

| Min | Block |
|---|---|
| 0:00–0:05 | Welcome back, setup check (app running and updated), orientation for afternoon-only joiners |
| 0:05–0:12 | Framing: GenAI as a coder (codebook → pilot → agreement → revise → document), then responsible AI: choosing a provider is a research decision (ethics approval, data privacy, local vs commercial models, cost) |
| 0:12–0:32 | Build the `Tweets` block from scratch, briskly (workspace, sample data, column types, `full_name`, join with candidate metadata; Checkpoint a = the rescue), explore (jobs, cuts), derive the 226 non-retweet "job" tweets (Filter ×2), join the reference annotation |
| 0:32–0:36 | Codebook v1 (`Promise` / `Cuts` / `Other`) |
| 0:36–0:42 | Be the coder first: annotate the first page by hand into `job.manual`, then Compare To the reference annotation: κ + confusion matrix on your own coding |
| 0:42–0:50 | Connect a model (shared workshop key, deleted at 3:30 pm; own keys welcome); a small, cheap model on purpose |
| 0:50–1:00 | Preview a few pages, back to page 1: Compare To `job.manual` and the reference → κ + confusion matrix, the mask, corrections (reuse `job.manual`) |
| 1:00–1:05 | Run All into `job.AI`; headline κ against the reference (rehearsal 0.84) |
| 1:05–1:13 | Feed `job.manual` back as examples into `job.AI.example`; Run All; κ again (rehearsal 0.73): examples don't guarantee improvement |
| 1:13–1:19 | Revised codebook v2 (`Job_with_ref_codebook_v2`, Checkpoint d) into `job.AI_v2`; κ again: three measured runs |
| 1:19–1:21 | Demo: same v2 on a stronger model (GLM 5.3 flash); the hands-on ends |
| 1:21–1:24 | After coding: the coded block is data; filter per code, Frequency, Trends by party, Concordance, Topic Modelling |
| 1:24–1:25 | Showcase in one breath (Checkpoint e) |
| 1:25–1:30 | Take-home: your own data, local models, ethics, manual multi-coder use, feedback, close |

## Design rationale (why this shape)

- **v0.7.x throughout.** New interface and functions; all June-era materials must be checked against v0.7 before reuse (see CLAUDE.md for the verified UI-fact list — notably **Snapshot Mode no longer exists**).
- **Demo-only morning → recordable.** With no participant hands-on there's nothing privacy-sensitive on screen but the facilitator's own demo, no back-and-forth when someone can't follow, and the recording becomes reusable training material. It also compresses 3 hours of June content into 1.5.
- **Hands-on afternoon → deliberately NOT recorded.** Participants' screens, questions, data, and stumbles stay off the record; the session can move at the room's pace.
- **Two sessions, lighter commitment.** People can attend either half: newcomers do the full day; June-workshop alumni can skip the morning and check in just for the new tool. The lunch break is the natural join/leave point — and the afternoon's install/setup window.
- **Checkpoint recovery via workspace archives, not snapshots.** v0.7 removed the frontend Snapshot Mode, but the multi-tab system plus workspace metadata mean **open tabs are saved with the workspace** — so a checkpoint archive restores data blocks *and* the tab layout. Session 2 ships checkpoint files at each major stage; anyone lost re-imports the latest checkpoint and rejoins in under a minute.
- **Shared workshop key, not participant keys.** A fresh OpenRouter key with a hard spend cap is created on the day, posted in the Zoom chat when the hands-on reaches the provider step, and deleted at 3:30 pm; participants with their own OpenRouter / OpenAI / Anthropic / Google keys can use those instead. Free-tier models are not used: their per-account rate limits cannot serve a room sharing one account.

## Folder map (this workshop's files)

```
wordflow-workshop/                           ← branch online_workshop_2026-08-28
├── README.md                                ← you are here (canonical structure)
├── slides/
│   ├── online-s1-intro.html                 ← Session 1 deck (recorded morning)
│   ├── online-s2-annotation.html            ← Session 2 deck (afternoon hands-on)
│   ├── online-s1-intro.pdf / online-s2-annotation.pdf ← shareable PDF exports (post-workshop)
│   └── images/                              ← logos, v0.7 UI screenshot, team photos
├── participant/
│   └── hands-on-annotation-online.md        ← Session 2 step sheet (linked from the pre-workshop email)
├── facilitator/
│   ├── demo-checklist-s1.md                 ← Session 1 click-by-click demo checklist
│   ├── runbook-online-s1.md                 ← Session 1 spoken script + timing
│   ├── runbook-online-s2.md                 ← Session 2 minute-by-minute
│   ├── run-of-show-online.html              ← presenter panel (private screen; chat snippets)
│   ├── pre-workshop-checklist-online.md     ← release-week timeline, test script, checkpoints
│   └── stress-test-openrouter.py            ← shared-account concurrency test
├── communications/
│   ├── pre-workshop-email-online.md / .html ← sent Thu 27 Aug (HTML = paste source)
│   ├── post-workshop-email-online.md        ← within 24 h after
│   ├── promo-blurbs-online.md / .html       ← Eventbrite / newsletter / social copy
│   └── images/                              ← banners
└── artifacts/online-2026-08-28/             ← the 226 "job" tweets: model coding, human review, verified labels
```
