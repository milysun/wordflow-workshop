# Wordflow — Online Workshop, 28 August 2026

> **This branch: `online_workshop_2026-08-28`.** A one-day **online** workshop combining the June intro workshop and the July CAITG winter-school session, on **Wordflow v0.7.x**. Two 1.5-hour sessions with a lunch break:
>
> - **Session 1 (morning, recorded)** — a condensed, demo-only version of the June intro workshop: Wordflow basics, concepts, and a multi-tool workflow. No participant hands-on.
> - **Session 2 (afternoon, NOT recorded)** — a 1.5-hour hands-on on the **Annotation** tool (GenAI text coding), extending the CAITG winter-school session.
>
> The June 3-hour workshop's documentation is kept at the bottom of this file as reference; its materials on this branch (`slides/index.html`, `facilitator/runbook.md`, `participant/hands-on-*.md`) are **v0.5-era sources to condense from**, not deliverables.

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

### Session 1 outline (demo-only, recorded)

| Min | Block |
|---|---|
| 0:00–0:10 | Welcome, Acknowledgement of Country, LDaCA + team, three ways to run Wordflow |
| 0:10–0:22 | Interface tour + the data-block concept (v0.7 UI, incl. the multi-tab system) |
| 0:22–0:42 | Tool tour — Frequency, Concordance, Trends, Topic Modelling, Quotation (~4 min each, from a pre-built workspace with one tab per tool) |
| 0:42–1:15 | The research story, condensed: QLD election tweets — join → filter → comparative frequency ↔ concordance → regex → Trends → topic modelling → stack (demo at full speed, narrated) |
| 1:15–1:25 | Repurpose-the-lens demo (Trends as histogram) |
| 1:25–1:30 | Wrap: what the afternoon holds, setup instructions for the hands-on, lunch |

### Session 2 outline (hands-on, not recorded)

| Min | Block |
|---|---|
| 0:00–0:10 | Welcome back, setup check (app running, sample data imported), catch-up checkpoint for afternoon-only joiners |
| 0:10–0:20 | GenAI as a coder: what to expect, pitfalls, and why we measure agreement (no theory talk precedes this session — unlike CAITG, we owe the room ~10 minutes of framing) |
| 0:20–0:35 | Task setup: Annotation tool, `candidate_info_gender` block, `gender.ai` column, M/F/U codebook |
| 0:35–0:45 | Manual coding + the multi-coder pattern |
| 0:45–0:55 | Connect a model: own API key (prepared before the workshop), provider + model choice |
| 0:55–1:10 | The preview loop: prompt → Preview → Compare To → confusion matrix → revise (the heart of the session) |
| 1:10–1:20 | Run All, review, corrections |
| 1:20–1:30 | Your own data + take-home: local models, ethics approval, feedback, close |

## Design rationale (why this shape)

- **v0.7.x throughout.** New interface and functions; all June-era materials must be checked against v0.7 before reuse (see CLAUDE.md for the verified UI-fact list — notably **Snapshot Mode no longer exists**).
- **Demo-only morning → recordable.** With no participant hands-on there's nothing privacy-sensitive on screen but the facilitator's own demo, no back-and-forth when someone can't follow, and the recording becomes reusable training material. It also compresses 3 hours of June content into 1.5.
- **Hands-on afternoon → deliberately NOT recorded.** Participants' screens, questions, data, and stumbles stay off the record; the session can move at the room's pace.
- **Two sessions, lighter commitment.** People can attend either half: newcomers do the full day; June-workshop alumni can skip the morning and check in just for the new tool. The lunch break is the natural join/leave point — and the afternoon's install/setup window.
- **Checkpoint recovery via workspace archives, not snapshots.** v0.7 removed the frontend Snapshot Mode, but the multi-tab system plus workspace metadata mean **open tabs are saved with the workspace** — so a checkpoint archive restores data blocks *and* the tab layout. Session 2 ships checkpoint files at each major stage; anyone lost re-imports the latest checkpoint and rejoins in under a minute.
- **Online API-key handling.** No shared key on a public short URL this time (it can't be scoped to a room online). The pre-workshop email walks participants through creating their **own OpenRouter key** (free-tier models make this zero-cost); a fallback key can be dropped in the meeting chat at the facilitator's discretion.

## Folder map (this workshop's files)

```
wordflow-workshop/
├── README.md                                ← you are here (canonical structure)
├── slides/
│   ├── online-s1-intro.html                 ← Session 1 deck (recorded morning)
│   └── online-s2-annotation.html            ← Session 2 deck (afternoon hands-on)
├── facilitator/
│   ├── runbook-online-s1.md                 ← Session 1 minute-by-minute
│   ├── runbook-online-s2.md                 ← Session 2 minute-by-minute
│   └── pre-workshop-checklist-online.md     ← checkpoints to build, Zoom/recording setup
├── participant/
│   └── hands-on-annotation-online.md        ← Session 2 step sheet (sent before the day)
└── communications/
    ├── pre-workshop-email-online.md         ← ~1 week before (setup + API key prep)
    └── post-workshop-email-online.md        ← within 24h after (recording link etc.)
```

Everything else in those folders is inherited from the June workshop (v0.5-era) or the CAITG session and serves as source material.

---

---

# Appendix — June 2026: Wordflow 3-Hour Intro Workshop (reference)

Materials for a 3-hour in-person workshop introducing **LDaCA Wordflow** to university researchers (HDR students through senior academics across faculties; HASS is the primary design audience but anyone working with text is welcome).

**⚠ v0.5-era**: the session structure, snapshot-tour mechanics, and any "Snapshot Mode" instructions below do not apply to v0.7.

## Session structure

| Time | Block | Duration | Mode |
|---|---|---|---|
| 1:30 pm – 1:55 pm | **1.0** Intro + UI tour | 25 min | Presentation; participants sign into Binder in parallel |
| 1:55 pm – 2:25 pm | **1.5** Snapshot tour across 5 tools | 30 min | Facilitator-led demo + each participant loads each snapshot |
| 2:25 pm – 2:40 pm | **Break** | 15 min | |
| 2:40 pm – 3:25 pm | **2** Research story | 45 min | Demo at full speed + selective participant follow-along |
| 3:25 pm – 3:40 pm | **Break** | 15 min | |
| 3:40 pm – 3:55 pm | **3.A** Repurpose-the-lens demo | 15 min | Demo; the "wait, you can do that?" moment |
| 3:55 pm – 4:00 pm | **3.B** Lab framing + feedback ask | 5 min | Brief instructions |
| 4:00 pm – 4:25 pm | **3.C** Free hands-on lab | 25 min | Three tracks; helpers circulating |
| 4:25 pm – 4:30 pm | **3.D** Thanks + close | 5 min | |

## Why these design choices

- **Snapshot tour ahead of mechanics (Session 1.5).** Participants touch all 5 analytical tools in 30 minutes and see the *visualisations* before they're asked to *produce* anything. Builds interest through visual variety instead of "configure this importer".
- **One coherent research story in Session 2.** Threading joins → comparative frequency → concordance → trends → topic modelling through a single research question (gender differences in QLD candidate tweets) is more memorable than disconnected exercises. The cross-tool moves (Frequency → click jump → Concordance; Topic Modelling → Add to Workspace → group in Trends) are the things that make Wordflow feel *fluid*.
- **Dual recovery mechanism (snapshots + workspace archives).** Session 2 is a linear chain — one stuck participant 15 min in falls off the rest. Pre-baked checkpoint snapshots and portable workspace archives let anyone rejoin at any major stage. Belt + braces.
- **"Try this" / "follow along" markers in Session 2.** The 18+ step chain is too long to nail every step in 45 min. Hands-on sheets mark the key moves as **try this** and the rest as **follow along** (have a go, no pressure). A checkpoint for every phase (A–E) means anyone who falls behind — or hits a step that won't work — rejoins in 30 seconds, so nobody panics.
- **Session 3.A as conceptual payoff.** Repurposing Trends into a histogram is the demo that lands the lens metaphor.
- **Free lab over structured exercise in Session 3.C.** By 4:00 pm participants are saturated. A loose lab with helpers wins over another guided exercise.

## June folder map

```
facilitator/runbook.md                  ← minute-by-minute, with scripts
facilitator/pre-workshop-checklist.md   ← snapshots + workspace archives to prep
facilitator/common-questions.md         ← anticipated stumbling blocks
facilitator/timing-recovery.md          ← if you fall behind, cut these
participant/welcome.md                  ← printable arrival handout
participant/cheat-sheet.md              ← glossary + UI map (printable)
participant/hands-on-1.md               ← Session 1.5 snapshot tour
participant/hands-on-2.md               ← Session 2 research story
participant/hands-on-3.md               ← Session 3 lens demo + free lab
participant/what-next.md                ← post-workshop reading
slides/index.html                       ← self-contained HTML deck (offline)
communications/pre-workshop-email.md    ← ~1 week before
communications/post-workshop-email.md   ← within 24h after
```

## June tunable parameters

| Knob | Default | Adjust if… |
|---|---|---|
| Session 2 dataset | QLD election tweets (gender metadata; no hashtag filter — dataset is too small to subsample) | Want simpler narrative → use Honi Soit content filter instead |
| Session 2 mode | Demo at full speed; key moves marked "try this", the rest "follow along" | Room is small/confident → full follow-along |
| Checkpoint recovery | Pre-baked snapshots + workspace archive | First delivery → snapshots only |
| Snapshot tour count | 5 (Frequency, Concordance, Trends, Topic, Quotation) | Tight room → 4 (drop Quotation; English-only) |
| Session 3.A demo | Trends → article-size histogram | Have a better example for your audience → swap freely |
| Session 3.C tracks | Continue Session 2 / own data / open exploration | Smaller homogeneous room → one track only |
