# Wordflow: In-person Intro Workshop, University of Melbourne, 26 October 2026

> **This branch: `melbourne_mdap_workshop_2026-10-26`.** Status: **in preparation** (plan drafted 2026-10-23).
>
> **Monday 26 October 2026, 2:00-5:00 pm AEDT**, Meeting Room M03, Mezzanine, Melbourne Connect, University of Melbourne. Co-hosted by the **Melbourne Data Analytics Platform (MDAP)**, **LDaCA** and the **Sydney Informatics Hub**, with the Sydney Corpus Lab acknowledged as Wordflow's development partner. Registration (MDAP): [rduevents.unimelb.edu.au/event/2814](https://rduevents.unimelb.edu.au/event/2814-point-and-click-text-analytics-an-introduction-to-ldaca), **full at 45**. In person, with possibly a few people joining over Zoom.
>
> **Wordflow version: 0.7.16** (released 2026-10-23). MDAP's pre-workshop email went out at 0.7.15; anyone on 0.7.15 or earlier gets the update prompt when the app starts.
>
> Earlier deliveries live on their own branches: [`online_workshop_2026-08-28`](../../tree/online_workshop_2026-08-28) (the base of this one: S1 demo-only intro + S2 Annotation hands-on), [`hansard_workshop_2026-09-29`](../../tree/hansard_workshop_2026-09-29) (Wordflow on RAPID-CDL Hansard), [`intro_workshop_2026-06-03`](../../tree/intro_workshop_2026-06-03) (the first 3-hour in-person intro).

---

## What this workshop is

The August online workshop, **re-run in person on the polished 0.7.16**, at the room's pace. August was 90 minutes of recorded demo plus 90 minutes of Annotation hands-on; here the same ground becomes one afternoon where **people do most of the work themselves**.

**The rule for this delivery: talk less than half the time.** Every block is *show briefly, do it together, then explore*. Of the 170 working minutes, about 60 are talk and demo and about 110 are hands at the keyboard, guided or free. The last 25 minutes are an open lab that doubles as the buffer: hands-on always runs slower than planned, and nobody should leave mid-exercise.

## North star

> **One thing they leave knowing:** *text data flows through stackable, single-purpose tools, and the meaning of an analysis comes from how you shape your data, not from the tool itself.*

Plus the Annotation extension: *an AI model is just another coder: it earns trust the way a human coder does, through a codebook, a pilot, agreement scores and revision.*

## Data

| Dataset | Role | Size | Why |
|---|---|---|---|
| **ADO: Queensland Election Tweets** (built-in sample) | The guided spine, Parts 1 to 4 | 2,380 tweets (1,646 without retweets), 133 candidates with gender and party | Small, so every step and every Topic Modelling run is quick on any laptop; continuity with August, including the 226 "job" tweets and their verified reference labels for Annotation |
| **RAPID-CDL: Australian Hansard, GST** and **housing** (built-in samples, new since August) | The explore playground: optional in each Explore block, central in the open lab | GST 40,860 paragraphs (about 4.1M words); housing 76,312 paragraphs (about 8.5M words), 1998 to 2026, with a speaker table to join | New and Australian, rich metadata (date, chamber, debate, party, gender after the join), and good for Trends over decades. **Sample before Topic Modelling** (Data Builder Sample, for example 2,000 paragraphs): a full run is too slow on most laptops |
| Your own data | Open lab | | The point of the open lab for anyone who brought some |

## Session structure (2:00-5:00 pm AEDT)

Talk minutes are the facilitator's; everything else is participants at the keyboard.

| Time | Block | Talk | Hands-on | What happens |
|---|---|---|---|---|
| 2:00-2:15 | **Welcome and setup** | 12 | 3 | Housekeeping, Acknowledgement of Country, who we are (MDAP, LDaCA, SIH), why Wordflow, how the afternoon works. Everyone opens Wordflow and accepts the update to 0.7.16 while we talk. The interface and the one idea: the data block flows between tools |
| 2:15-2:45 | **Part 1 Shape your data** | 8 | 22 | *Together:* new Project, import the tweets (and start the Hansard import, which takes a while), Data Editor Overview, set the date column's type, combine candidates' first and last names, Join tweets to candidates, Filter out retweets. *Explore:* the Data Editor's column tools (Clean text, Count words, Map values to group parties into sides), or the same steps on Hansard GST joined to its speaker table. **Checkpoint A** |
| 2:45-3:25 | **Part 2 Look through the lenses** | 12 | 28 | *Together:* Frequency comparing women and men candidates (right-click a word to drop it), click a word into Concordance, read a match in context (Match Details, new in 0.7.16), search `job(s)?|cut(s)?` and Add to Project, Trends by day and by gender. *Explore:* a lens card per tool, on the tweets or on Hansard (for example GST mentions by year and chamber). Before the break: **start a Topic Modelling run** so the first-run model download happens during the break. **Checkpoint B** |
| 3:25-3:35 | Break | | | Also catch-up time; helpers circulate |
| 3:35-4:00 | **Part 3 Topics** | 7 | 18 | The run started before the break: the bubble map, **read a topic's example texts** (the eye: Most typical, Open document), **name a topic**, Ungrouped, a suggestion if one shows. Add a topic to the Project and send it to Trends. *Explore:* Topics, Max topic size, Colour by party. **Checkpoint C** |
| 4:00-4:35 | **Part 4 Coding text with GenAI** | 10 | 25 | Framing: the AI is another coder, and choosing a provider is a research decision. *Together:* the 226 "job" tweets, codebook v1 (`Promise` / `Cuts` / `Other`), **be the coder first**: code page 1 by hand, Compare To the reference labels (κ and the confusion matrix). Connect the shared workshop key; Preview; compare the model with yourself and with the reference. *If time:* Run on all 226 and read the headline κ. **Checkpoint D** |
| 4:35-5:00 | **Open lab and close** | 5 | 20 | Explore cards on Hansard GST and housing, or your own data; questions one-to-one. 4:55: feedback, where to get Wordflow and help, recordings of the August sessions. This block is the buffer: if the room is behind, it absorbs the overrun |

**Totals:** about 54 minutes of talk, 116 of hands-on, 10 of break.

### Cut order when late

1. Part 4's full Run (Preview and Compare To still make the point).
2. Part 3's Explore (keep the example texts and naming a topic: they are the new feature people will use most).
3. Part 2's Trends by matched word (keep Trends by gender).
4. The open lab shrinks, but never below 10 minutes of close: feedback and where to get help matter more than one more feature.

Never cut the Explore part of Part 1 or Part 2 to make up time: that is the point of this delivery.

## What's new since August (what returning people will notice)

The four changes worth naming in the room, each met in the flow rather than in a "what's new" slide:

- **Suggestions** (lightbulb, 0.7.12): appear when a result or run looks off and point at the setting that may help. Part 2 (a Concordance Preview with no matches) and Part 3 (Topic Modelling) are where they show.
- **New text cleaning and column tools** in the **Data Editor**: Clean text, Find & replace, Extract text, Combine columns, Split column, Count, Map values, plus Overview. Part 1.
- **Data Builder and Data Editor are separate**: the Data Builder (sidebar, formerly Preprocessing) makes new Data Blocks (Filter, Group, Join, Segment, Aggregate, Sample, Deduplicate, Stack); the Data Editor (the table under the Project graph) edits a block's columns in place, with a live preview and Undo. Part 1.
- **Topic Modelling example texts** (0.7.11): read a topic's most typical segments and open the whole document; name topics (0.7.12); Ungrouped. Part 3.

Also changed and used along the way: Workspace is now **Project** and the publish button is **Add to Project** (0.7.8); tabs are on by default; Concordance shows each match in its document again (Match Details, 0.7.16); date conversion checks the whole column first; Annotation keeps labels if a run stops and sends only unlabelled rows by default.

## Design rationale

- **In person, so hands-on throughout.** August split demo (recorded) from hands-on (not recorded) because the morning was online and reusable. In a room, the recording is already done (the August videos) and the value is people trying things with help at their elbow.
- **Show, do, explore.** Each block shows a step in a few minutes, the room does it together with the step sheet, then explores with a card of suggestions. The Explore time is protected: it is where people find out whether the tool fits their own work.
- **Small data for guided steps, big data for exploring.** The tweets keep every guided step fast and identical on every laptop. Hansard is there for anyone ahead or curious, and for the open lab.
- **Checkpoints at each part.** A Project archive per part (A to D, exported from 0.7.16) lets anyone who fell behind import it and rejoin in under a minute. They also cover a laptop that cannot install the app: the browser option plus a checkpoint.
- **Annotation shortened, not dropped.** The registration page promises it. Coding page 1 by hand and comparing needs no API key, so the core point survives even if the shared key or the network fails.
- **Shared workshop key.** As in August: a fresh OpenRouter key with a hard spend cap, shown when Part 4 reaches the provider step and deleted at 5:00 pm. Own keys welcome.
- **Not recorded** (pending MDAP's view): a hands-on room's screens, questions and stumbles stay off the record. Zoom joiners see the shared screen and follow the same step sheet.

## Open decisions

| Decision | Default in this plan | Who |
|---|---|---|
| Recording | Not recorded | Chao + MDAP |
| Zoom: link, host, who watches the chat | MDAP hosts; a named helper watches the chat | MDAP |
| Floor helpers for 45 people | At least 2 to 3 (MDAP colleagues), briefed on Parts 1 and 4 | MDAP |
| Shared OpenRouter key and spend cap | New key, cap about US$20, created Monday morning | Chao |
| Topic Modelling settings on the tweets | Re-test on 0.7.16 (August's min topic size 7, 40 topics no longer map one-to-one: Max topic size Auto, Ungrouped) | Chao, before Monday |
| Browser option for anyone who cannot install | ARDC BinderHub (Melbourne participants confirmed able to use it); check the Binder pin is 0.7.16 | Chao |

## Folder map

New files for this delivery carry `melbourne` or `2026-10-26` in their names. The August-named files (`*-online.*`, `*-s1*`, `*-s2*`) are the sources being adapted; remove them before participants are linked to this branch.

```
wordflow-workshop/                                 ← branch melbourne_mdap_workshop_2026-10-26
├── README.md                                      ← you are here (canonical plan)
├── facilitator/
│   ├── pre-workshop-checklist-melbourne.md        ← Fri 23 to Mon 26 Oct: who does what, test script, room setup
│   └── (to come) runbook-melbourne.md, run-of-show-melbourne.html
├── participant/
│   └── (to come) hands-on-melbourne.md            ← the step sheet: Together steps + Explore cards per part
├── slides/
│   └── (to come) melbourne-wordflow.html          ← one deck: welcome, interface, a title slide per part, close
├── communications/
│   ├── event-blurb-2026-10-26.md / .html          ← registration copy (sent to MDAP 2026-09)
│   ├── newsletter-blurb-2026-10.md                ← SIH October newsletter
│   └── update-email-melbourne.md                  ← reminder for MDAP to forward: update to 0.7.16, bring a laptop
└── artifacts/
    ├── checkpoints/                               ← v0.7.7 archives from August; to be replaced by A to D from 0.7.16
    ├── online-2026-08-28/tweets_job_reference.csv ← the 226 verified labels Part 4 compares against
    └── promo-2026-10/                             ← newsletter banner
```
