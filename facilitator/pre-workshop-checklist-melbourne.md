# Pre-workshop checklist: Melbourne, Monday 26 October 2026

> Chao-only. The plan it serves is in `README.md`. Workshop: **Mon 26 Oct, 2:00-5:00 pm AEDT, Meeting Room M03, Mezzanine, Melbourne Connect**; 45 registered (full), a few possibly on Zoom; Wordflow **0.7.18** (built 24 Oct; release CI running that afternoon). Prep window: **Fri 23 to Mon 26** (the weekend). Chao is in Melbourne that week for eResearch (26-30 Oct, MCG).

## 1 · Friday 23 Oct: unblock the people side

- [ ] **Reminder email to MDAP** to forward today or Saturday: `communications/update-email-melbourne.md` (update to the latest version, bring laptop and charger, browser option). Fill or delete the Zoom paragraph.
- [ ] **Ask MDAP** (one message, five questions):
  1. **Zoom**: who hosts, the link, and who in the room watches the chat? (Default: MDAP hosts; one helper owns the chat.)
  2. **Helpers**: can 2 to 3 MDAP colleagues help on the floor for 45 people? 30-minute briefing before 2 pm (§5).
  3. **Recording**: plan is *not recorded* (hands-on room). OK with them?
  4. **Room**: projector input (HDMI or USB-C), a microphone if Zoom joiners need to hear, power boards for 45 laptops, access from 1:15 pm for setup.
  5. **Network**: everyone on eduroam with their own laptop (planned); guest Wi-Fi for anyone without eduroam? Any filtering of `openrouter.ai`?
- [ ] Confirm with MDAP that registrant data stays with them (we do not take the list; no opt-in question this time, consistent with August).

## 2 · Saturday 24 Oct: test 0.7.18 end to end, pin the TBCs

- [ ] **0.7.18 is released and offered**: the CI on `v0.7` passes, the release is promoted to Latest, and a 0.7.16 install offers the update at start. If it is not out by Sunday evening, run Monday on **0.7.17**: the step sheet's labels are the same (0.7.18 only greys the Search term example, makes topics repeatable on corpora over about 8,000 segments, speeds up the end of a run and adds the shared-server notice), and the tweets are far below 8,000 segments.

Run the whole flow on the **desktop app, 0.7.18**, from an empty data folder (a fresh-install state shows the first-run hints the room will see). If possible repeat Parts 1 and 3 on a **Windows** laptop: most of the room will not have Apple silicon, and Topic Modelling on Windows still uses the processor.

- [ ] **Part 1 Try it, timed as a participant would do it (target 10 minutes)**: new Project; import the QLD tweets (time the Hansard GST import too); Add both files; Overview; `created_at` to Date and time; Join tweets (left) to candidates on `username`; Filter out retweets: **1,646 rows**; Frequency on `Tweets_original` shows `https`, `co`, `t` near the top; Clean text → Remove web links (URLs), the same column, Apply; Frequency **Run** again and they are gone (check whether the open Frequency tab needs Run or refreshes itself, and fix the sheet's step 7 to match). Then the three early-finisher ideas once each, as written on the sheet.
- [ ] **Part 2 Try it (target 4 minutes per tool)**: Frequency on `Tweets_original`, right-click a word into stop words; click a word into Concordance, click a row (Row Details at the match); Trends `created_at` Daily by `gender`; `party` → Category, Most rows first, drag `N/A (Independent)` to the end, Convert; new Trends tab, `party` on the axis, group `gender`, Stacked bars (bars in the dragged order). The early-finisher ideas once each (chart types, Dispersion view, another word). Note one place a **suggestion** reliably appears (a Concordance Preview with no matches is the documented one) for the demo.
- [ ] **Part 3: Topic Modelling settings for the tweets, re-tested on 0.7.18.** August used min topic size 7, 40 topics, a recorded seed and found 5 "job" topics; 0.7.12 changed the clustering (Max topic size Auto, Ungrouped), so those numbers no longer carry over. Find settings that give a readable map in **under 2 minutes on a mid-range Windows laptop**, record Seed, Topics, Max topic size and Max tokens (the 0.7.16 Max tokens suggestion may fire on tweets: decide whether to accept it on screen). Time the first run including the model download. On the projector (window zoomed Cmd and + twice), note whether **Display options** sit beside the map or below it, so the demo matches what the room sees; **Search term** `job` should light up the job topics.
- [ ] **Side task and Part 3 step 5** (128 tokens on Honi Soit verified by Chao, 2026-10-25): time importing Honi Soit (Add ZIP → Texts as one Data Block (100)) and its run alongside the tweets run on a mid-range Windows laptop; check the lightbulb offers **Use 128 tokens**; pick an article whose Open document shows passages in two or three topics for the demo.
- [ ] **Part 3 Try it**: the eye opens example texts; Most typical; Open document; name a topic; find one that reads well when named (a "jobs" or "health" topic) for the demo; **Colour by** `party` (7 parties in the tweets, within its 2-to-8 limit; check it is offered on the category `party` and how the legend reads on the projector). The early-finisher ideas once each (Search term `job`, the Topics slider, Colour by gender).
- [ ] **Hansard for the open lab**: Sample GST to 2,000 paragraphs (Seed 0) and time Topic Modelling on it; Trends of GST paragraphs by year and chamber; Join the speaker table on `speaker_detail_id` for party and gender. Check the open lab ideas on the sheet work as written.
- [ ] **Part 4, from Checkpoint D as the room will do it**: import D, Annotation, add `Jobs_with_ref` and the `Codebook` block (check the **Code column** picks itself, or add "pick `code`" to the sheet), read the Task context in Edit, `job.manual`, code page 1, Compare to `theme.reference`, `job.AI`, provider, Preview, Compare to. **Run all 226 with the new Task context** and record κ against `theme.reference`: August's 0.84 was with the one-sentence v1 prompt. If the Task context scores clearly lower, cut its decision rules back to the data description and purpose, and fix the sheet's printed copy to match. **Which rows to annotate** defaults to only rows without a label: check it does not trip the hand-coded-then-AI flow.
- [ ] **Browser option**: launch ARDC BinderHub from sih.tools/wordflow; check it runs **0.7.18** (the master repo's Binder pin was 0.7.17 on 24 Oct: bump it once 0.7.18 is on PyPI, then launch once to build the image before Monday) and that a checkpoint loads in it. Wordflow online (`wordflow.ldaca.edu.au`, CILogon sign-in) is the second browser option.

## 3 · Sunday 25 Oct: build the materials and the checkpoints

- [ ] **Checkpoints A to D** from one clean 0.7.18 run-through, exported as Project archives, then round-trip each on a second machine, ideally one still on 0.7.16 or 0.7.17 for anyone who skipped the update (import, open, re-pick the tool inputs: those are not saved):
  - **A**, end of Part 1 Try it: tweets and candidates added, `created_at` as Date and time, `Tweets` (joined), `Tweets_original` (1,646 rows) with web links removed from `text`, and the Frequency tab. Block names as in `participant/hands-on-melbourne.md`. Nothing from the early-finisher ideas.
  - **B**, end of Part 2 Try it: plus `party` as a category (Most rows first, Independents last), the Concordance tab and both Trends tabs (by day; by party).
  - **C**, end of Part 3: plus the Topic Modelling tab (settings from §2) with one named topic, coloured by party, and the Honi Soit block with its 128-token run.
  - **D is where everyone starts Part 4**, so it is the one that must not fail: C plus `Jobs` (226), the reference block, `Jobs_with_ref` and a codebook block named **`Codebook`** with the three v1 codes and the **Task context** exactly as printed in the step sheet (saved with the codebook, so it survives the archive). No annotation columns. The model is not saved: the sheet says to pick it. Time the import on a mid-range Windows laptop.
  - Replace the v0.7.7 archives in `artifacts/checkpoints/` (they hold August's flow). Host the zips where the room can download them in one click (a GitHub release on this repo, as August did) and make a short link or QR code.
- [ ] **Participant step sheet** `participant/hands-on-melbourne.md` (drafted 2026-10-23 from verified 0.7.16 labels; restructured 2026-10-24/25 into a chart, Try it and If you finish early per part, Part 4 from Checkpoint D with a full Task context, Part 3 labels for 0.7.17): walk it during the Saturday test and fix anything that reads wrong; fill the checkpoint links; share it in the room by QR code and short link.
- [ ] **Deck** `slides/melbourne-wordflow.html` (drafted 2026-10-23, 20 slides): fill the orange placeholders (toilets, campus security number from MDAP; step-sheet short link and QR); confirm the Acknowledgement of Country wording with MDAP; replace the interface screenshot with a 0.7.18 one taken during the Saturday test.
- [ ] **Runbook** `facilitator/runbook-melbourne.md` (drafted 2026-10-24): fill its ⟨orange⟩ gaps from the Saturday test (Topic Modelling settings, the topic to name, whether Frequency refreshes after cleaning); print it or put it on the second screen.
- [ ] Remove the August-only files from this branch before its link goes to participants (`*-online.*`, `*-s1*`, `*-s2*`, the August checkpoint archives, `artifacts/snapshots/`).

## 4 · AI provider: the shared key

- [ ] **Network**: participants use their own laptops on eduroam (Chao, 2026-10-23), so requests are not funnelled through one shared address and August's rate-limit picture holds (paid models: no OpenRouter platform request cap while the balance is positive). No extra stress test planned.
- [ ] **If errors appear on the day** (429s or timeouts in the Tasks panel): ask the room to lower **Requests at once** (Advanced settings, default 10) to 3 and Run again; labels already returned are kept. Everyone Previews first anyway, so the full Run is never the first call.
- [ ] Room model and fallback: re-check `google/gemini-2.5-flash-lite` (August's room model) and the fallback `z-ai/glm-5.3-flash` are still listed and priced; 0.7.15 shows a one-line description under each model, so check what the room will read there.
- [ ] **Monday morning**: create the key `workshop-2026-10-26` with a hard cap (about US$20), test it once from the hotel network, put it in the runbook. **Delete it at 5:00 pm.**
- [ ] If `openrouter.ai` is blocked on the venue network: Part 4 still runs by hand (be the coder first, Compare To the reference), and the AI steps are shown on the shared screen from a phone hotspot.

## 5 · Monday 26 Oct

- [ ] **Morning**: Wordflow on the presenting laptop is 0.7.18 (or 0.7.17 if 0.7.18 did not ship: see §2). Empty data folder or a clean Project list for the on-screen Part 1. Deck opens offline. Checkpoint link and QR tested on a phone.
- [ ] **1:15 pm, room setup**: projector and screen readable from the back (Wordflow zoomed: Cmd and + twice); Zoom running and sharing the whole screen if anyone joins online; mic check; Wi-Fi joined; **warm the Topic Modelling model cache** by running Part 3 once on the venue network (the first run downloads the model). Power boards out. QR code for the step sheet on screen as people arrive.
- [ ] **1:30 pm, helper briefing** (15 minutes): the plan in one page; the rule (show the main steps, the room does the main steps; most people will need the whole time for them, so help people finish rather than pushing extras); the known pitfalls: (1) the Join's first pick is the left table; (2) after loading a checkpoint, re-pick the tool's Data Block and columns; (3) Part 4 starts with everyone importing Checkpoint D: help anyone whose import or **Open** stalls first, and point out that their own Project is still in the **Project manager** for the open lab; (4) the model is not saved in D, pick it. The escalation signal: if a third of the room is stuck on the same step, stop and show it on screen.
- [ ] **During**: one helper owns the Zoom chat; the others own a section of the room each. Checkpoint link posted in the Zoom chat at each part.
- [ ] **5:00 pm**: delete the shared key. Ask MDAP for attendance numbers (aggregate only) for the SIH training report.

## 6 · After

- [ ] Post-workshop email via MDAP within a day: step sheet, slide PDF, checkpoints, the August recordings, sih.tools/wordflow, Feedback in the app.
- [ ] Merge anything fixed on this branch into a final tag `melbourne-2026-10-26-final`, as with August and September.
