# Wordflow — 3-Hour Intro Workshop

Materials for a 3-hour in-person workshop introducing **LDaCA Wordflow** to university researchers (HDR students through senior academics across faculties; HASS is the primary design audience but anyone working with text is welcome).

These files are **local working drafts** — they live outside the repo's tracked content. Adapt freely.

---

## North star

> **One thing they leave knowing:** *text data flows through stackable, single-purpose tools — and the meaning of an analysis is shaped by how you shape your data, not by the tool itself.*

Three concrete outcomes for every participant:

1. They can open Wordflow, find the main UI components, and load both a snapshot and a workspace archive without being told twice.
2. They have *seen* a real multi-tool research workflow play out — joins, filters, comparative frequency, concordance with dispersion, trends, topic modelling — even if they didn't follow every step.
3. They left the room with a "wait, you can do that?" moment from the lens-repurpose demo, and at least one of: a saved snapshot, a portable workspace archive, or an idea about their own corpus.

If they leave with those three, the workshop succeeded.

---

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

---

## Why these design choices

In case you want to adapt later:

- **Snapshot tour ahead of mechanics (Session 1.5).** Participants touch all 5 analytical tools in 30 minutes and see the *visualisations* before they're asked to *produce* anything. Builds interest through visual variety instead of "configure this importer".
- **One coherent research story in Session 2.** Threading joins → comparative frequency → concordance → trends → topic modelling through a single research question (gender differences in QLD candidate tweets) is more memorable than disconnected exercises. The cross-tool moves (Frequency → left-click jump → Concordance; detach topics → group in Trends) are the things that make Wordflow feel *fluid*.
- **Dual recovery mechanism (snapshots + workspace archives).** Session 2 is a linear chain — one stuck participant 15 min in falls off the rest. Pre-baked checkpoint snapshots and portable workspace archives let anyone rejoin at any major stage. Belt + braces.
- **"Watch" / "try this" markers in Session 2.** The 18+ step chain is too long for full follow-along in 45 min. Hands-on sheets mark each move as **try this** (key learning) or **watch only** (advanced/optional). Mode A facilitators can ignore the markers; less-confident participants use them as an explicit permission to put the keyboard down.
- **Session 3.A as conceptual payoff.** Repurposing Trends into a histogram is the demo that lands the lens metaphor. It takes 15 min and is the single moment most likely to be quoted afterwards.
- **Free lab over structured exercise in Session 3.C.** By 4:00 pm participants are saturated. A loose lab with helpers wins over another guided exercise — they consolidate by exploring at their own pace.

---

## Folder map

```
workshop/
├── README.md                       ← you are here
├── facilitator/
│   ├── runbook.md                  ← minute-by-minute, with scripts
│   ├── pre-workshop-checklist.md   ← snapshots + workspace archives to prep
│   ├── common-questions.md         ← anticipated stumbling blocks
│   └── timing-recovery.md          ← if you fall behind, cut these
├── participant/
│   ├── welcome.md                  ← printable arrival handout
│   ├── cheat-sheet.md              ← glossary + UI map (printable)
│   ├── hands-on-1.md               ← Session 1.5 snapshot tour
│   ├── hands-on-2.md               ← Session 2 research story (try-this/watch-only marked)
│   ├── hands-on-3.md               ← Session 3 lens demo + free lab
│   └── what-next.md                ← post-workshop reading
├── slides/
│   └── index.html                  ← self-contained HTML deck (offline)
└── communications/
    ├── pre-workshop-email.md       ← ~1 week before
    └── post-workshop-email.md      ← within 24h after
```

---

## How to use these materials

**A week before the workshop**

1. Read `facilitator/pre-workshop-checklist.md` — the five Session-1.5 demo snapshots ship with the LDaCA sample data and just need to be verified. You do need to **build and upload the five Session-2 workspace archives (A → E, one per phase)** as a GitHub Release on this branch.
2. Send `communications/pre-workshop-email.md` (lightly tailored).
3. Print `participant/welcome.md` + `participant/cheat-sheet.md` (double-sided) per attendee.

**Day of**

1. Open `facilitator/runbook.md` on your second monitor / printout — that's your script.
2. Open `slides/index.html` on the projector (any browser, offline-fine).
3. Have `facilitator/common-questions.md` accessible during breaks.
4. Have the URLs / download links for the demo snapshots + Session-2 workspace archive ready to drop in chat.

**After**

1. Send `communications/post-workshop-email.md` with the snapshots, the workspace archive, and links.

---

## Tunable parameters

| Knob | Default | Adjust if… |
|---|---|---|
| Session 2 dataset | QLD election tweets (gender metadata; no hashtag filter — dataset is too small to subsample) | Want simpler narrative → use Honi Soit content filter instead |
| Session 2 mode | Demo at full speed + selective follow-along (3-4 "try this" moves) | Room is small/confident → full follow-along (and bump Session 2 to 60 min from somewhere else) |
| Checkpoint recovery | Pre-baked snapshots + workspace archive | First delivery → snapshots only; add archives next iteration |
| Snapshot tour count | 5 (Frequency, Concordance, Trends, Topic, Quotation) | Tight room → 4 (drop Quotation; it's English-only with narrower appeal) |
| Session 3.A demo | Trends → article-size histogram | Have a better "lens repurpose" example for your audience → swap freely |
| Session 3.C tracks | Continue Session 2 / own data / open exploration | Smaller homogeneous room → one track only |
