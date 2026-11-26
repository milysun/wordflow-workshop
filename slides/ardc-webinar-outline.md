# ARDC HASS&I webinar: talk outline (draft 2, 2026-11-16)

> **Delivered 26 November 2026.** This outline is the plan as of draft 2 and was not updated for the last changes to the deck. The slides as delivered are `slides/ardc-webinar-wordflow.pdf` (21 slides) and the GitHub release https://github.com/milysun/wordflow-workshop/releases/tag/ardc-webinar-2026-11-26 (PPTX with both recordings embedded, and PDF).

**Thursday 26 November 2026, 2 pm AEDT** · ARDC HASS&I Research Data Commons webinar series, focus area LDaCA · Presenter: Chao Sun, alone (ARDC's opening slides also name Prof. Monika Bednarek, by mistake: she takes no part) · MC: Mary Filsell (ARDC) · Rehearsal with ARDC: Thursday 19 November

**Deck (draft 2, 2026-11-16):** Slides artifact https://claude.ai/artifact/MrBBzuk3Qh2hW6kMVYMzQU (22 slides, eResearch visual style, speaker notes carry timings; exports to .pptx or PDF). Its built files are not in this repo. Draft 2 reorders the parts to follow ARDC's opening slides, turns slide 2 into a roadmap, adds the AI Code Designer (Wordflow 0.7.21) to slide 8, and refreshes the figures to 16 November. Slide 3 keeps the heading and cards Chao reviewed on 15 November.

**Shape (Chao, 2026-11-01):** an information talk of **30 to 40 minutes**, condensed from the eResearch Australasia 2026 talks and poster, with Q&A after. No live demo: short muted recordings, narrated live. The ARDC form promised 45 to 50 minutes of content; a shorter talk leaves 10 to 20 minutes for questions, so tell Kit.

**Five purposes, and where each sits:**

1. **Introduce Wordflow** (Part 1)
2. **The advantages, and how it serves more researchers** (Part 2: GenAI coding done properly; Part 3: four ways to run it)
3. **The connection to other ARDC-funded work:** LDaCA collections, ADO, RAPID-CDL, the ARDC BinderHub, Nectar (Part 3, slides 15 and 16)
4. **FAIR:** tagged as it comes up, gathered on slide 17 at the end of Part 3
5. **Outreach and training:** usage, workshops, the feedback loop (Part 4)

**ARDC's frame (their Google Slides deck; PDF export received 2026-11-16).** ARDC's MC opens with eight slides before ours: title and presenters, Acknowledgement of Country, recording notice (questions go in the Zoom chat and are taken at the end), code of conduct, the series, the session title, **"How today will help you do better research"**, and "Who's in the room?" (a chat prompt: where are you, and what is your relationship to text analytics?). Our slides go into the "Add your slides/content" slot. After ours come ARDC's "Key Information", next session, ARDC Connect and contact slides. We keep our own visual style (Chao, 2026-11-16).

The three promises on ARDC's slide 7 now set the order of the talk:

| ARDC's promise | Our part |
|---|---|
| **See** corpus-scale analysis, like frequencies and topic modelling, without programming | Part 1, slides 3 to 6 |
| **Learn** about a responsible, verifiable way to use AI for qualitative coding | Part 2, slides 7 to 10 |
| **Explore** options for reproducible, shareable analysis of sensitive data, kept safely on your own computer | Part 3, slides 11 to 17 |

Because the MC gives the Acknowledgement of Country and introduces the presenter, the deck no longer has its own Acknowledgement and "who we are" slide: one spoken sentence on slide 1 and one breath on slide 2 cover them.

**Audience:** HASS and Indigenous studies researchers, plus librarians, research support staff and trainers. Most do not program and many have not seen Wordflow. The eResearch talks spoke to infrastructure and support staff, so this talk cuts the mechanism detail (BinderHub files, the app-or-service test) and keeps what a researcher would act on.

**Running thread: FAIR, tagged as it comes up.** Rather than one FAIR slide bolted on at the end, put a small F / A / I / R tag in the corner of each slide where a principle is at work (Project graph = R, four ways in = A, DOIs = F, and so on). The FAIR slide at the end of Part 3 then gathers what the audience has already seen. This puts ARDC's main concern through the whole talk without extra minutes.

---

## Slide by slide (about 31 and a half minutes of content; room to run to 38)

| # | Slide | Time | Cum. | Beat | Source |
|---|---|---|---|---|---|
| | **Part 1: See. What Wordflow is** | | | | |
| 1 | Title | 0:30 | 0:30 | Take over from the MC; no second introduction. One spoken sentence acknowledging the Country you join from, a word on one or two chat answers, then on. | new |
| 2 | Today: see, learn, explore | 0:45 | 1:15 | ARDC's three promises as the roadmap, in their words and their order. Who we are in one breath, spoken: SIH with the Sydney Corpus Lab, for LDaCA, an ARDC co-investment enabled by NCRIS. | ARDC opening slide 7 |
| 3 | The gap | 1:30 | 2:45 | Most HASS research runs on text; most text analysis tools expect you to program. Cards (as reviewed 15 Nov): the barrier first (learn Python or R), then what it leaves people with (read by hand, or ask a chat AI). Keep the PhD story for Part 2. | page notes §1, A4 s2 |
| 4 | Wordflow in one picture | 1:30 | 4:15 | The hero Topics screenshot. Four lines from the poster: bring your text; analyse without programming; GenAI for qualitative coding; tools that work together. Open source, free. | poster panel, `hero-topics-2026-10-26.png` |
| 5 | The central idea: data blocks and the Project graph `R` | 1:30 | 5:45 | Every result becomes a Data Block another tool can analyse. The Project graph is the methods section, drawn: a record and a recipe of the method. The north star, said once. | poster, A1 s4, README north star |
| 6 | Recorded tour (2:30 to 3:00) | 3:00 | 8:45 | QLD 2020 election tweets: import sample data, join candidate gender, Frequency (male vs female) → click a word → Concordance → Trends by party → Topic Modelling with named topics. Narrate live. Give Frequency and Topic Modelling the clearest screen time (ARDC's first promise names them). **Needs recording on 0.7.21**; the Melbourne Parts 1 to 3 Try-it steps are the script. | Melbourne step sheet |
| | **Part 2: Learn. GenAI for qualitative coding, done properly** | | | | |
| 7 | Where chat falls short | 1:15 | 10:00 | Opens Part 2. The PhD student and the Reddit posts (anonymous). Four problems in one breath each: a question without knowing the data, paying to re-read it, unverifiable, irreproducible. | A4 s2 + s3 merged |
| 8 | The method stays; AI joins it as a new coder | 2:00 | 12:00 | Code by hand → codebook (one line: the **AI Code Designer**, new in 0.7.21, can suggest a first draft from a brief and a sample of texts; the researcher checks and edits every code) → trial the AI on a sample → agreement and the failed cases → refine → **the gate** (AI–human agreement comparable to human–human; the researcher decides) → scale up. This audience knows coding, so skip A4's "what coding is" slides. | A4 s5 + s8 merged |
| 9 | Recorded demo (2:45 clip) | 3:00 | 15:00 | Code by hand · trial the AI · scale up, narrated over the existing clip. Codes land in a column beside the text and feed every other tool. The clip predates the AI Code Designer; if it is recorded again on 0.7.21, give the designer about 15 seconds. | A4 s9 recording |
| 10 | Your choice of model, your accountability | 1:30 | 16:30 | Commercial, local (data stays on the machine) or institutional, same codebook and checks. Ethics approval still governs. The researcher answers for the results; no model deserves blind trust. Prompt, model, settings and codebook are saved with the Project `R`. | A4 s13 + s14 + s11 merged |
| | **Part 3: Explore. Your options, the ARDC ecosystem, FAIR** | | | | |
| 11 | One tool, many kinds of researcher | 1:00 | 17:30 | Opens Part 3. The seven need cards (new ideas, teaching, private data, big corpus, no budget, not a programmer, hot desking). Sweep, don't read. Land on the question: how does a small team serve all of them? | A3 s2 (swap "not a coder" for "not a programmer") |
| 12 | Four ways to run it `A` | 2:00 | 19:30 | ARDC BinderHub (institutional sign-in, nothing to install), hosted app wordflow.ldaca.edu.au (resume anywhere), desktop app (sensitive data stays local, offline), `uvx ldaca-wordflow`. One codebase, one interface: a Project downloaded from one opens in any other `I`. | A3 s3, poster band |
| 13 | Why this lets us serve more | 1:00 | 20:30 | Heavy and private work moves to the researcher's own device, so shared national infrastructure serves more people with the same resources. Said as our reasoning, not a rule. | A3 s4 |
| 14 | Any language | 0:45 | 21:15 | Chinese, Japanese and Korean tokenisers beside English and European languages; the Japanese fake-news corpus as the image. Through the desktop and PyPI it reaches researchers abroad at no cost to national hosting. Do not claim Indigenous-language support (see below). | poster, `jp-cloud-card.png` |
| 15 | Where the data comes from | 2:00 | 23:15 | The ecosystem diagram from the poster. **LDaCA collections:** 0.7.21 has *Import LDaCA collections* in the Data Loader, with an LDaCA access token from the Data Portal for collections with access conditions (call it a growing connection; see open items). **ADO:** QLD election tweets (DOI on screen). **RAPID-CDL:** Hansard GST and housing samples; the Hansard workshop series in September. **Sydney Corpus Lab:** Honi Soit, candidate gender. Researchers' own data beside all of these. | poster ecosystem panel, page notes §3 |
| 16 | Where it runs: national infrastructure, repurposed | 1:15 | 24:30 | The ARDC BinderHub, built for notebooks, used as an on-demand web host: one private copy per launch, AAF or Tuakiri sign-in, nothing held between sessions, a pinned launch link per release `R`. The hosted app on Nectar. LADAL's nine R Shiny tools now launch the same way: the pattern travels within LDaCA. | A2 s6, s9, s12, s15 condensed |
| 17 | What makes it FAIR | 2:00 | 26:30 | Gather the tags; this closes ARDC's third promise (reproducible, shareable). Two levels: **the software is FAIR** (PyPI, a Zenodo DOI per release plus the concept DOI, open source, public versioned documentation) and **it helps researchers make their analyses FAIR** (open formats in and out, a portable Project archive, the Project graph as provenance, a pinned launch link per release, codebook and AI run settings saved). | poster FAIR panel, BRAINSTORM FAIR table |
| | **Part 4: Outreach and training, close** | | | | |
| 18 | Reach so far | 1:15 | 27:45 | Stat tiles: desktop downloads, releases, workshop registrants, app launches, countries reached online, feedback received, recording views. **Refresh all figures in the week of the webinar** (last set: 16 Nov; sources below). Users from education, linguistics, social science, psychology, political science. | A3 s5, poster reach panel |
| 19 | Taking it to researchers: workshops | 2:00 | 29:45 | A timeline of deliveries: USyd intro (3 Jun), CAITG Winter School (30 Jul), online (28 Aug, 19 countries, recorded), Hansard series with RAPID-CDL (29–30 Sep), University of Melbourne with MDAP and SIH (26 Oct). What every delivery now does: one research question threaded through every tool, checkpoint Projects so nobody falls behind for long, a recorded demo plus an unrecorded hands-on, nothing to install (BinderHub or desktop). Workshop photos. | A2 s12 notes, A5, page notes §2, `workshop-ws*.jpg` |
| 20 | The loop back to development, and what's next | 1:00 | 30:45 | A feedback form inside every copy of the app; 100+ pieces of feedback go straight into the development queue, and the release cadence shows it. Next: modules for particular kinds of data (interviews, parliamentary records, social media), and taking demos to school seminars and centres. Say "planned" unless a case has happened. Ask: invite us. | A3 s5 notes, A5 |
| 21 | Try it, work with us | 0:45 | 31:30 | QR to the landing page (all four ways in), concept DOI 10.5281/zenodo.20408328, contact. The ask: research communities, data custodians and trainers who want to try it with their people. ARDC's "Key Information" slide follows ours: Chao fills it in with the link, DOI and contact. | poster bottom strip, A3 s7 |
| 22 | Thank you |  |  | Acknowledgements (ARDC, Nectar, LDaCA/NCRIS, SIH, SCL, ADO, RAPID-CDL). Leave up through Q&A. | A2 s17, A4 s16 |

**If it runs long, cut in this order:** slide 14 (any language) into one line on slide 12 (−0:45); slide 11 (many kinds of researcher) into one spoken sentence on slide 12 (−1:00); the tour on slide 6 down to 2:00 (−1:00); slide 20 (the feedback loop) into slide 19 (−1:00). Never cut slides 5, 8 or 17.

**If there is room (up to 38 minutes):** slide 19 gets the Annotation hands-on finding (participants ran the whole loop in 90 minutes and saw that adding examples can lower agreement); slide 16 plays the 94-second Binder launch clip (on the slide, click to play).

---

## Figures on slide 18: where each comes from

Last refreshed **16 November 2026**; refresh again in the week of the webinar and change the date line on the slide.

| Tile | 27 Oct | 16 Nov | Source |
|---|---|---|---|
| Desktop downloads | 451 (450+) | 538 (530+): 289 Windows, 249 macOS | GitHub release assets: the sum of `download_count` over every `.msi` and `.dmg`, from `gh api --paginate "repos/Australian-Text-Analytics-Platform/ldaca-wordflow/releases?per_page=100"`. A lower bound: GitHub resets a count when an asset is replaced. |
| Releases since May 2026 | 39 | 41 | Published GitHub releases since 1 May 2026, pre-releases left out. |
| App launches | 10+ a day | 302 in 33 days (300+; about 9 a day) | Update checks: the sum of `download_count` over the `latest*.json` assets of releases from v0.7.14 (14 October). Approximate, and older builds do not report. The tile now shows the total, because the daily average has dipped below ten. |
| Recording views | 276 | 299 (162 + 137) | YouTube: the AI Annotator session (`KcjJViYRYX4`) and the full walkthrough (`ExYVSgvYIes`). |
| Workshop registrants | 225 | not recounted | Registers; unchanged unless a workshop has run since Melbourne. |
| Countries, one online workshop | 19 | unchanged | 28 August attendance report. |
| Feedback | 100+ | not recounted | The in-app feedback form's responses. |

- **DOIs:** the slide used to say "39 releases, each with a DOI". Zenodo holds 26 records under the concept DOI, starting at v0.5.5-rc1 (27 May 2026), so every release since June has a DOI but the earlier May builds do not. The tile now says "releases since May 2026" and the footnote says "Every release since June has its own DOI". Two Zenodo oddities to tidy when convenient: one record is labelled v8.0.0 (28 September) and v0.7.7 appears three times.
- **Not on the slide:** PyPI shows 4,171 downloads without mirrors from 18 May to 14 November (pypistats.org); the figure includes automated installs, so use it with care.

---

## Getting our slides into ARDC's Google Slides deck

Agree the route with ARDC at the 19 November rehearsal, and test the recordings through Zoom there.

1. **Import, editable (first choice).** From the deck page, Share › Export gives a .pptx (and, where it is offered, a direct send to Google Slides). Upload the .pptx to Google Drive and open it with Google Slides. In ARDC's deck: File › Import slides, pick that file, select all, keep **"Keep original theme" ticked**, import, then move the slides into the "Add your slides/content" slot. Both decks are 16:9 and DM Sans is a Google font, so the look should hold; check every slide after import, since rounded cards, pills and shadows can shift. This needs edit access to ARDC's deck, or ARDC does the import from our converted file.
2. **Images, exact (fallback for any slide that converts badly).** Export the deck as PDF, turn the pages into 1920×1080 PNGs, and set each as a slide background or full-slide image. Exact, but not editable, and the notes have to be pasted in.
3. **Do not merge (fallback for the whole deck).** ARDC shares its opening slides, Chao shares our deck from the browser for the talk, and ARDC shares again for the close. The recordings play as they do now.

**Recordings.** Google Slides plays video only from Google Drive or YouTube, and a video inside an imported .pptx usually does not survive the conversion. So upload each MP4 to Google Drive, then on its slide: Insert › Video › Google Drive, and under Format options › Video playback choose "Play (on click)" and mute. Three slides carry a recording: 6 (tour, to be made), 9 (annotation demo) and 16 (Binder launch, optional). The Drive files must be shared with whoever runs the slides on the day ("anyone with the link can view" is the simple way); allow a few minutes after upload for Drive to process them; whoever shares the screen should tick Zoom's "Optimize for video clip". Keep the MP4s on the laptop as a last resort.

**ARDC's "Key Information" slide** (after ours): Chao edits it directly in ARDC's deck. Put on it the landing page link, the concept DOI 10.5281/zenodo.20408328, the contact address, and the two workshop recordings.

---

## Q&A prep: Indigenous data (not on the slides)

The series is HASS *and Indigenous*, and the ARDC form lists "researchers and custodians working with sensitive or access-restricted text, including Indigenous data" under who should attend, so expect the question. Chao has not tried Wordflow on Indigenous data and makes no promise, so the slides leave it out and this is the answer, if asked.

**A possible answer (spoken, about a minute):**

> We haven't worked with Indigenous data or with Indigenous communities, so I can't make any claims there. The CARE principles (Collective benefit, Authority to control, Responsibility, Ethics) are about governance and relationships, and software can't meet them on its own. Some design choices might matter to people who govern that kind of data: the desktop app keeps the text on the researcher's own computer and works offline; local AI models mean text needn't go to a commercial service; and LDaCA collections with access conditions are imported with the researcher's own LDaCA access token. But that's untested for this purpose. If you work with Indigenous communities or custodians and see a possible use, we'd like to learn what would be needed, led by them.

**Follow-ups to expect:**

- *"Does it handle Indigenous languages?"* Untested. Text written in the Latin alphabet will load and count, but we have no language-specific tokenisers or stop-word lists, and we haven't checked whether word splitting suits any of these languages. Don't promise support.
- *"Can access restrictions travel with the data into Wordflow?"* Collection access is checked when you import with your own LDaCA token. After import the data sits in your Project, and as far as we know Wordflow doesn't carry the conditions forward or enforce them (confirm with Alex). The researcher stays bound by the access agreement. Only give this answer once the end-to-end check below holds.

**Keep consistent with this answer:**

- **Drop "FAIR and CARE aligned".** The A3 lightning deck (slide 6) said "Open, FAIR and CARE aligned". Don't repeat it on any slide here.
- **Say "your text stays on your computer", not "nothing leaves".** The desktop app does check for updates over the network (which is how launches are counted).
- **Check the token claim.** Confirm that the LDaCA token import respects collection access conditions end to end in 0.7.21.
- **Optional:** run the answer past LDaCA's access and Indigenous data governance colleagues, who may have a pointer to LDaCA's own work you could give instead.

---

## Open items before the 19 November rehearsal

- [ ] **Recordings:** the slide 6 tour on 0.7.21 (2:30 to 3:00, muted). The August recordings predate the Project and Data Builder renames, so don't reuse them. The deck still reuses the eResearch annotation clip (2:45) and Binder clip (94 s); check neither contradicts 0.7.21. If the annotation clip is recorded again, add about 15 seconds of the AI Code Designer.
- [ ] **Google Slides:** agree the route with ARDC (section above) and test video playback through Zoom at the rehearsal.
- [ ] **ARDC's deck, edited by Chao directly:** on the opening slide change "WordFlow" to "Wordflow" (their slide 6 has it right) and remove Prof. Monika Bednarek's name (listing her was ARDC's misunderstanding); fill in the "Key Information" slide (section above).
- [ ] **Numbers:** refresh in the week of the webinar (table above). Recount the feedback responses. Also reconcile two counts that disagree: the poster says "7 workshops: 5 in person, 2 online", but A3 slide 5 says "6 since April, five in person and one online" (225 registrants). Decide whether the April user-testing session counts, and confirm the Melbourne attendance figure.
- [ ] **LDaCA collections:** which collections import cleanly today, and whether access-controlled ones work. Slide 15's wording depends on this ("growing connection" is the safe default).
- [ ] **Training plan status:** has any seminar or centre delivery happened since June (A5's engagement model)? If yes, slide 20 can name it.
- [ ] **Photo consent** for the two workshop photos on slide 19, since the webinar is recorded.
- [ ] **Timing:** tell ARDC the content is 30 to 40 minutes, so they can plan the rest of the hour as Q&A.
- [ ] **Word choice:** say "without programming". Never "without writing code" or "code-free" (A3 slide 2 and the poster pitch use these). "Code" means qualitative coding here.
