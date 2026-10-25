# Wordflow: In-person Intro Workshop, University of Melbourne, 26 October 2026

> **This branch: `melbourne_mdap_workshop_2026-10-26`.** Status: **in preparation** (plan drafted 2026-10-23).
>
> **Monday 26 October 2026, 2:00-5:00 pm AEDT**, Meeting Room M03, Mezzanine, Melbourne Connect, University of Melbourne. Co-hosted by the **Melbourne Data Analytics Platform (MDAP)**, **LDaCA** and the **Sydney Informatics Hub**, with the Sydney Corpus Lab acknowledged as Wordflow's development partner. Registration (MDAP): [rduevents.unimelb.edu.au/event/2814](https://rduevents.unimelb.edu.au/event/2814-point-and-click-text-analytics-an-introduction-to-ldaca), **full at 45**. In person, with possibly a few people joining over Zoom.
>
> **Wordflow version: 0.7.19** (released 2026-10-25 on all platforms: a Project export hot fix, and Topic Modelling says *passage* instead of *segment*). MDAP's pre-workshop email went out at 0.7.15; anyone on an earlier version gets the update prompt when the app starts. 0.7.17 and 0.7.18 change only Topic Modelling (Display options, Search term, the same topics on every run) and add a notice banner for shared servers: everything else on the step sheet is as in 0.7.16.
>
> Earlier deliveries live on their own branches: [`online_workshop_2026-08-28`](../../tree/online_workshop_2026-08-28) (the base of this one: S1 demo-only intro + S2 Annotation hands-on), [`hansard_workshop_2026-09-29`](../../tree/hansard_workshop_2026-09-29) (Wordflow on RAPID-CDL Hansard), [`intro_workshop_2026-06-03`](../../tree/intro_workshop_2026-06-03) (the first 3-hour in-person intro).

---

## What this workshop is

The August online workshop, **re-run in person on the polished 0.7.19**, at the room's pace. August was 90 minutes of recorded demo plus 90 minutes of Annotation hands-on; here the same ground becomes one afternoon where **people do most of the work themselves**.

**The rule for this delivery: show the main steps, let the room do the main steps, and leave time for that.** In August each tool got its full sequence in demo mode: the first step, then the next four, and the room watched. The concepts and most actions haven't changed since, and the August recordings still show every one of those later steps. So here each part shows only **the main steps** (the step sheet's **Try it**), everyone does those, and the rest of each part's time is for finishing them with a helper nearby. Expect that many people won't get further. For anyone who does, the sheet adds two or three one-line ideas per part (**If you finish early**), not instructions; everything else is in the recordings. Nobody should leave having watched step 4 without having done step 1. The projector shows the same steps as a simple flow per part: tool and step only.

Of the 180 minutes, about **40 are talk and demo** and about **130 are hands at the keyboard**; 10 are the break. Part 4 (Annotation) is shorter than in the first draft (25 minutes, not 35) and starts from a checkpoint, so its time goes on coding rather than on building the data. The 30-minute open lab doubles as the buffer: hands-on always runs slower than planned, and nobody should leave mid-exercise.

## North star

> **One thing they leave knowing:** *text data flows through stackable, single-purpose tools, and the meaning of an analysis comes from how you shape your data, not from the tool itself.*

Plus the Annotation extension: *an AI model is just another coder: it earns trust the way a human coder does, through a codebook, a pilot, agreement scores and revision.*

## Data

| Dataset | Role | Size | Why |
|---|---|---|---|
| **ADO: Queensland Election Tweets** (built-in sample) | The guided spine, Parts 1 to 4 | 2,380 tweets (1,646 without retweets), 133 candidates with gender and party | Small, so every step and every Topic Modelling run is quick on any laptop; continuity with August, including the 226 "job" tweets and their verified reference labels for Annotation |
| **RAPID-CDL: Australian Hansard, GST** and **housing** (built-in samples, new since August) | For the open lab and anyone curious: one idea in Part 1 | GST 40,860 paragraphs (about 4.1M words); housing 76,312 paragraphs (about 8.5M words), 1998 to 2026, with a speaker table to join | New and Australian, rich metadata (date, chamber, debate, party, gender after the join), and good for Trends over decades. **Sample before Topic Modelling** (Data Builder Sample, for example 2,000 paragraphs): a full run is too slow on most laptops |
| Your own data | Open lab | | The point of the open lab for anyone who brought some |

## Session structure (2:00-5:00 pm AEDT)

Talk minutes are the facilitator's; everything else is participants at the keyboard. **Try it** is the main steps (4 to 7, the same for everyone); the time after it is for finishing them, with **If you finish early** ideas on the sheet.

| Time | Block | Talk | Hands-on | What happens |
|---|---|---|---|---|
| 2:00-2:12 | **Welcome and setup** | 10 | 2 | MDAP's welcome with housekeeping and safety, Acknowledgement of Country, who we are (MDAP, LDaCA, SIH), why Wordflow, how the afternoon works (show, try, go further). Everyone opens Wordflow and accepts the update while we talk. The one idea: the data block flows between tools |
| 2:12-2:47 | **Part 1 Shape your data** | 6 | 29 | *Try it (to about 2:30):* new Project, import the tweets and Honi Soit (Hansard GST optional), Add the two tweet CSVs and Honi Soit's ZIP (for Part 2's Topic Modelling prep), Data Editor Overview and `created_at` to Date and time, **Join** tweets to candidates, **Filter** out retweets (1,646). Then **clean because the data says so**: a first Frequency cloud shows `https`, `co` and `t` (pieces of `t.co` links, in 1,153 tweets), so Data Editor **Clean text → Remove web links (URLs)** on `text`, and Run again. *Then (about 17 min):* finishing time; ideas: a category, another Clean text option, a look at Hansard GST. **MDAP-Part1** |
| 2:47-3:25 | **Part 2 Look through the lenses** | 8 | 30 | Short show-then-try cycles, one move per tool: **Frequency** (the Part 1 tab; right-click a word to drop it), click a word into **Concordance** and open a row, **Trends** by day and gender. Then **Trends on a category**: `party` to **Category** in the order window (Most rows first, drag Independents last), and a Trends tab with `party` on the axis, grouped by gender, **Stacked bars**. *Then (from about 3:05):* finishing time; ideas: chart types, the Dispersion view, another word. **From 3:17, Topic Modelling prep for Part 3**: everyone starts two runs, in two tabs (multi-tab): the tweets, and Honi Soit (100 news articles) at **Max tokens 128**, so the first-run model download happens during the break. **MDAP-Part2** |
| 3:25-3:35 | Break | | | Also catch-up time; helpers circulate |
| 3:35-4:00 | **Part 3 Topics** | 5 | 20 | *Try it*, the three capabilities new since August: the bubble map and Ungrouped, **read a topic's example texts** (the eye: Most typical passages, Open document for the whole tweet), **name a topic**, **Colour by** `party`; then the Honi Soit run: **Open document** on one article shows its passages in several topics (a tweet is one passage; an article is about six at 128 tokens). *Then (from about 3:47):* finishing time; ideas: Search term, the Topics slider, Colour by gender. **MDAP-Part3** |
| 4:00-4:25 | **Part 4 Coding text with GenAI** | 6 | 19 | Framing (3 min): the AI is another coder; choosing a provider is a research decision. *Try it:* **everyone imports MDAP-Part4** (the 226 job tweets with checked labels and a codebook whose **Task context** says what the data is, what the coding is for and how to decide the hard cases); code page 1 by hand; Compare to the reference (κ, the confusion matrix); connect the shared key, Preview, compare the model with yourself and the reference. *If you finish early:* Run on all 226, a few corrections, a codebook of your own (one is printed on the sheet) |
| 4:25-4:55 | **Open lab** | 0 | 30 | Finish a part, the sheet's ideas, Hansard GST and housing, or your own data; questions one-to-one. This block is the buffer: if the room is behind, it absorbs the overrun |
| 4:55-5:00 | **Close** | 5 | | Feedback, where to get Wordflow and help, the August recordings for every step we didn't show |

**Totals:** about 40 minutes of talk, 130 of hands-on, 10 of break.

### Cut order when late

1. The open lab absorbs the first 15 minutes of overrun: that is what it is for.
2. Part 4: the AI step (provider, Preview) is shown on the shared screen instead of done by everyone; hand-coding and Compare to stay with the room, and need no key.
3. Part 2: Trends on a category is shown on screen only (Frequency, Concordance and Trends over time stay with the room).
4. Never cut a part's hands-on time below 10 minutes, and never cut the close: feedback and where to get help matter more than one more feature.

Talk is the first thing to give up, never hands-on time: if a demo runs long, skip its last move and point at the sheet.

## What's new since August (what returning people will notice)

The four changes worth naming in the room, each met in the flow rather than in a "what's new" slide:

- **Suggestions** (lightbulb, 0.7.12): appear when a result or run looks off and point at the setting that may help. Part 2 (a Concordance Preview with no matches) and Part 3 (Topic Modelling) are where they show.
- **New text cleaning and column tools** in the **Data Editor**: Clean text, Find & replace, Extract text, Combine columns, Split column, Count, Map values, plus Overview. Part 1.
- **Data Builder and Data Editor are separate**: the Data Builder (sidebar, formerly Preprocessing) makes new Data Blocks (Filter, Group, Join, Segment, Aggregate, Sample, Deduplicate, Stack); the Data Editor (the table under the Project graph) edits a block's columns in place, with a live preview and Undo. Part 1.
- **Topic Modelling example texts** (0.7.11): read a topic's most typical passages and open the whole document; name topics (0.7.12); **Colour by** a column with 2 to 8 values; Ungrouped. Part 3.
- **Trends on a category**: a category column on the x-axis, one bar per value in the column's order, which the category window sets (presets, or drag the values). Part 2.

Also changed and used along the way: Workspace is now **Project** and the publish button is **Add to Project** (0.7.8); tabs are on by default; Concordance shows each match in its document again (Match Details, 0.7.16); Topic Modelling's result controls are **Display options**, beside the map on a wide window, with a **Search term** that takes several words at once (0.7.17), and a run gives the same topics every time (0.7.18); date conversion checks the whole column first; Annotation keeps labels if a run stops and sends only unlabelled rows by default.

## Design rationale

- **In person, so hands-on throughout.** August split demo (recorded) from hands-on (not recorded) because the morning was online and reusable. In a room, the recording is already done (the August videos) and the value is people trying things with help at their elbow.
- **The main steps, not the full sequence.** Each part shows its main steps in a few minutes and the room does exactly those with the step sheet. August's demo got through four steps after the basic while some of the room had not done step 1; the recordings already cover those steps, so the room's time goes on doing. The time after Try it is protected: most people need it to finish, and it is where helpers answer "can it do X?". The early-finisher ideas are deliberately small, one line each.
- **Small data for guided steps, big data for exploring.** The tweets keep every guided step fast and identical on every laptop. Hansard is there for anyone ahead or curious, and for the open lab.
- **Checkpoints at each part.** `MDAP-Part1` to `MDAP-Part4`: the Project at the end of each part with its results ready to view (MDAP-Part3 includes both finished Topic Modelling runs), so anyone behind catches up by looking, and can change a setting and Run again; `MDAP-Part4` is where everyone starts Part 4, with no coding done. They also cover a laptop that cannot install the app: the browser option plus a checkpoint.
- **Annotation shortened, not dropped.** The registration page promises it. Part 4 starts from MDAP-Part4, so nobody spends its time filtering, uploading, joining or typing a codebook (those are in the August recording). Coding page 1 by hand and comparing needs no API key, so the core point survives even if the shared key or the network fails.
- **The codebook carries its context.** Since 0.7.15 the codebook has a **Task context**: what the texts are, what the coding is for, and how to decide the hard cases. It is saved with the codebook (unlike the prompt), so it survives the checkpoint and is part of the method people take home. MDAP-Part4's Task context folds in August's v1 prompt and the decision rules from its v2 prompt that match the reference labels; the step sheet prints it in full.
- **Passage, in the app and in our words.** Wordflow 0.7.19 calls Topic Modelling's stretches of text **passages** (issue #441: the **Passages** setting, **Previous passage** / **Next passage**, "tokens per passage"); the Data Builder's **Segment** tool and column names such as `TOPIC_segment_count` keep their names. A passage can be a sentence, a paragraph, several paragraphs packed together, or part of an over-long sentence. On 0.7.18 the buttons still say *segment*.
- **One page for the room.** `docs/melbourne/index.html` carries the steps, the workshop key (stored encoded by `facilitator/set-workshop-key.py`, so it isn't plain text in a public repo) and the checkpoint downloads; sih.tools/ldaca points to it on the day. After the workshop it moves into the landing page.
- **Shared workshop key.** As in August: a fresh OpenRouter key with a hard spend cap, shown when Part 4 reaches the provider step and deleted at 5:00 pm. Own keys welcome.
- **Not recorded** (pending MDAP's view): a hands-on room's screens, questions and stumbles stay off the record. Zoom joiners see the shared screen and follow the same step sheet.

## Open decisions

| Decision | Default in this plan | Who |
|---|---|---|
| Recording | Not recorded | Chao + MDAP |
| Zoom: link, host, who watches the chat | MDAP hosts; a named helper watches the chat | MDAP |
| Floor helpers for 45 people | At least 2 to 3 (MDAP colleagues), briefed on Parts 1 and 4 | MDAP |
| Shared OpenRouter key and spend cap | New key, cap about US$20, created Monday morning | Chao |
| Topic Modelling settings on the tweets | Re-test on 0.7.18 (August's min topic size 7, 40 topics no longer map one-to-one: Max topic size Auto, Ungrouped) | Chao, before Monday |
| Browser option for anyone who cannot install | ARDC BinderHub (Melbourne participants confirmed able to use it); check the Binder pin is 0.7.18 (main was at 0.7.17 on 24 Oct). Wordflow online (`wordflow.ldaca.edu.au`, CILogon sign-in) is a second option if Binder is slow on the day | Chao |

## Folder map

New files for this delivery carry `melbourne` or `2026-10-26` in their names. The August-named files (`*-online.*`, `*-s1*`, `*-s2*`) are the sources being adapted; remove them before participants are linked to this branch.

```
wordflow-workshop/                                 ← branch melbourne_mdap_workshop_2026-10-26
├── README.md                                      ← you are here (canonical plan)
├── facilitator/
│   ├── pre-workshop-checklist-melbourne.md        ← Fri 23 to Mon 26 Oct: who does what, test script, room setup
│   └── runbook-melbourne.md                       ← Chao's script: show lists per part, clock gates, if things break
├── docs/melbourne/                                ← the workshop page (sih.tools/ldaca on the day): the step sheet as a flow of step cards, the workshop key, checkpoint downloads; published to main's docs/
├── participant/
│   └── hands-on-melbourne.md                      ← the step sheet: a chart and Try it steps per part, plus If you finish early ideas
├── slides/
│   └── melbourne-wordflow.html                    ← one deck: welcome, interface, a slide per part, close
├── communications/
│   ├── event-blurb-2026-10-26.md / .html          ← registration copy (sent to MDAP 2026-09)
│   ├── newsletter-blurb-2026-10.md                ← SIH October newsletter
│   └── update-email-melbourne.md                  ← reminder for MDAP to forward: update to the latest, bring a laptop
└── artifacts/
    ├── checkpoints/                               ← v0.7.7 archives from August; to be replaced by A to D from 0.7.18
    ├── online-2026-08-28/tweets_job_reference.csv ← the 226 verified labels Part 4 compares against
    └── promo-2026-10/                             ← newsletter banner
```
