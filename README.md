# Wordflow — ARDC HASS&I RDC Webinar, 26 November 2026

> **This branch: `ardc_hassi_webinar_2026-11-26`.** Status: **delivered on Thursday 26 November 2026; this branch is now frozen** as the record of what was presented (branched 2026-09-20 from `melbourne_mdap_workshop_2026-10-26`).
>
> **Delivered:** a 30-minute talk followed by Q&A, 2–3 pm AEDT. **197 registered**; ARDC has not yet reported attendance, but about **60 people** were on Zoom at any one time. It was well received and drew many questions. Slides as delivered (21 slides, from the PPTX inserted into ARDC's deck): **[PPTX with both screen recordings embedded, and PDF](https://github.com/milysun/wordflow-workshop/releases/tag/ardc-webinar-2026-11-26)** (GitHub release `ardc-webinar-2026-11-26`), and the PDF on this branch: [slides/ardc-webinar-wordflow.pdf](slides/ardc-webinar-wordflow.pdf). The PDF shows only placeholder frames for the two videos on slides 6 and 9: the 5 min 51 s tour (1.3× speed) and the 2 min 32 s Code Designer → AI coding demo. ARDC will publish the recording on its YouTube channel; it is to be linked from the Workshops and talks section of the landing page on `main` once it is up.
>
> A **one-hour online webinar** in the ARDC **HASS&I Research Data Commons** webinar series, focus area **LDaCA**, on **Thursday 26 November 2026, 2 pm AEDT**. ARDC runs the session (MC, registration, recording on ARDC YouTube, closing survey, resource page); we supply 1–2 presenters and about **45–50 minutes** of content. Presenter: Chao Sun, alone (ARDC's opening slides also name Prof. Monika Bednarek, by mistake: she takes no part; Chao corrects that slide); MC: Mary Filsell (ARDC).
>
> **Shape: decided 2026-11-01. A 30–40 minute information talk**, followed by Q&A. It is condensed from the **eResearch Australasia 2026** talks and poster, which are kept outside this repo in `../e-Research26/`. No live demo; muted recordings are narrated live. It has five purposes: introduce Wordflow; the advantages and how it serves more researchers (four ways to run it, GenAI coding done properly); connections to ARDC-funded work (LDaCA collections, ADO, RAPID-CDL, BinderHub, Nectar); FAIR, tagged through the talk and gathered at the end of the third part; and outreach and training (usage, workshops). Since 2026-11-16 the order follows the three promises on ARDC's opening slides: **see** (what Wordflow is, a recorded tour), **learn** (a checked way to use AI for qualitative coding), **explore** (where it runs, your own computer included; data sources; FAIR), then outreach and the close. ARDC's MC gives the Acknowledgement of Country and introduces the presenter, so the deck does not repeat them. Indigenous data stays off the slides; a prepared answer is kept for questions (untested, no claims, an invitation). Slide-by-slide plan: `slides/ardc-webinar-outline.md`.
>
> **ARDC timeline** (from the partner form): session description to Kit Greenhill by **1 October 2026** → content built and demo material tested → **rehearsal with the ARDC outreach team on Thursday 19 November** (bring the deck; agree how our slides go into ARDC's Google Slides deck and test the recordings) → log in 30 minutes early on the day → ARDC publishes the recording and a resource page afterwards.
>
> **Deliverables on this branch:** `communications/ardc-hassi-webinar-description-2026-11-26.md` (the filled form text, done 2026-09-20); the webinar deck (a Slides artifact, linked from `slides/ardc-webinar-outline.md`; it goes into the "Add your slides/content" slot of ARDC's Google Slides deck, in our own style); a short run-sheet to follow. The Melbourne (26 Oct) and August files below are inherited sources, not this webinar's deliverables, and are to be cleared out if participants are ever linked here.
>
> The rest of this README is inherited from the **28 August online workshop** and does not describe this webinar.

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
