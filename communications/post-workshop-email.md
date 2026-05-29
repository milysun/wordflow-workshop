# Post-workshop email

*Send within 24 hours of the workshop. Copy the body below; attach or link the captured snapshots.*

---

**Subject:** Wordflow workshop — links, snapshots, and what's next

---

Hi all,

Thanks for spending three hours with Wordflow yesterday. Some of you asked for resources and follow-up; here's everything in one place.

## The files from today

**Session-1.5 demo snapshots** (the five we toured the tools with) — these ship with the LDaCA sample-data catalogue, so they import alongside the sample datasets in Wordflow. **No separate download needed.** In **Data Loader → Import sample data**, the modal's **Demo Snapshots** tab lets you select and import them any time.

**Session-2 checkpoints** (the QLD election tweet workflow, one workspace archive per phase) — these are workshop-specific. Download from **sih.tools/wordflow → Releases** → the *Intro to Wordflow — 3 June 2026* release:

- `Checkpoint_A.zip` — after join + dtype.
- `Checkpoint_B.zip` — after gender filter + iterative Freq ↔ Concordance.
- `Checkpoint_C.zip` — after the regex aggregation + Trends with the `cut(s)` gender gap.
- `Checkpoint_D.zip` — after Topic Modelling on two corpora + detach into per-gender child blocks.
- `Checkpoint_E.zip` — after Stack + final Trends.

**How to use them:**
- **Demo snapshots**: in the matching tool, click the folder icon → Load snapshot. The five we used are already in your snapshot list once you've imported demo snapshots in Wordflow.
- **Workspace archives** (`Checkpoint_*.zip`): in **Data Loader → Import workspace archive →** pick the file. You'll have a full reproduction of the workflow up to that checkpoint.

## Documentation

- **Tutorial home**: [link to docs index] — start here, pick the tool you saw today.
- **Tool-by-tool tutorials**: linked from the home page; each tool has a 5–10 minute walkthrough.
- **In-app help**: every `?` icon next to a control opens the relevant tutorial section directly.

## Sample data — and how to cite it

All three datasets are publicly available and ship as part of the sample-data catalogue (**Data Loader → Import sample data** in the app — the **Datasets** tab of the modal). They were supplied by LDaCA partner organisations. **Please cite if used in published research.**

- **2025 Australian Federal Election — NewsTalk & Reddit** *(the `newstalk_stories` corpus you saw in Tools 1 + 4, plus the AusReddit data)*. Supplied by The Digital Observatory at Queensland University of Technology (formerly the *Australian Digital Observatory*, an ARDC-funded platform). Links: [newstalk.digitalobservatory.net.au](https://newstalk.digitalobservatory.net.au/), [ausreddit.digitalobservatory.net.au](https://ausreddit.digitalobservatory.net.au/), [digitalobservatory.net.au](https://www.digitalobservatory.net.au/).
- **Queensland Election 2020 on Twitter** *(candidate tweets with gender metadata, Session 2)*. Collected by QUT Digital Observatory with Prof. Axel Bruns, Prof. Daniel Angus, and Tegan Cohen. Gender metadata by [Sydney Corpus Lab](https://sydneycorpuslab.com/). **Cite as**: Bruns, A.; Angus, D.; Cohen, T.; QUT Digital Observatory (2022). *Queensland Election 2020 on Twitter.* Queensland University of Technology. [doi.org/10.25912/RDF_1665115527020](https://doi.org/10.25912/RDF_1665115527020).
- **Honi Soit Corpus** *(student newspaper, English, 100 articles, ~60,000 words — Tools 2 + 5)*. Compiled by [Sydney Corpus Lab](https://sydneycorpuslab.com/) (February 2024), using constructed-week sampling of [Honi Soit](https://honisoit.com/category/news/) news articles from January 2021 to December 2022. Used with permission from the Honi Soit editorial team.

## Installing Wordflow on your own machine

Three options:

1. **Cloud (Binder)** — same URL as today's workshop. Free, no install. Caveat: don't upload sensitive data.
2. **Desktop app (Mac / Windows)** — native installer, runs everything locally. Recommended for serious work. Downloads: [link].
3. **Python (`pip install ldaca-wordflow`)** — for Python users, gives you CLI access. Requires Python 3.14+ and around 500 MB of disk.

## Where to get help

- **In-app `?` icons** — fastest answer for "what does this control do?"
- **Documentation site** — fastest answer for "how do I do X?"
- **GitHub issues** — best place to report bugs. The maintainers actually read them.
- **LDaCA community Slack / mailing list** — [link if available].
- **Me, by email** — for follow-up questions specific to your research project.

## One question for you

Reply with **one sentence** answering this:

> *What would have made the workshop more useful for you?*

Even a brief reply helps me design the next one. No need to be polite; the most useful replies are the most direct.

## Thank you

You were a great group. I hope to see what you build.

[FACILITATOR NAME]
[INSTITUTION] · [EMAIL]
