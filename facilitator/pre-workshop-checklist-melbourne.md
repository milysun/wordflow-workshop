# Pre-workshop checklist: Melbourne, Monday 26 October 2026

> Chao-only. The plan it serves is in `README.md`. Workshop: **Mon 26 Oct, 2:00-5:00 pm AEDT, Meeting Room M03, Mezzanine, Melbourne Connect**; 45 registered (full), a few possibly on Zoom; Wordflow **0.7.16**. Prep window: **Fri 23 to Mon 26** (the weekend). Chao is in Melbourne that week for eResearch (26-30 Oct, MCG).

## 1 · Friday 23 Oct: unblock the people side

- [ ] **Reminder email to MDAP** to forward today or Saturday: `communications/update-email-melbourne.md` (update to the latest version, bring laptop and charger, browser option). Fill or delete the Zoom paragraph.
- [ ] **Ask MDAP** (one message, five questions):
  1. **Zoom**: who hosts, the link, and who in the room watches the chat? (Default: MDAP hosts; one helper owns the chat.)
  2. **Helpers**: can 2 to 3 MDAP colleagues help on the floor for 45 people? 30-minute briefing before 2 pm (§5).
  3. **Recording**: plan is *not recorded* (hands-on room). OK with them?
  4. **Room**: projector input (HDMI or USB-C), a microphone if Zoom joiners need to hear, power boards for 45 laptops, access from 1:15 pm for setup.
  5. **Network**: everyone on eduroam with their own laptop (planned); guest Wi-Fi for anyone without eduroam? Any filtering of `openrouter.ai`?
- [ ] Confirm with MDAP that registrant data stays with them (we do not take the list; no opt-in question this time, consistent with August).

## 2 · Saturday 24 Oct: test 0.7.16 end to end, pin the TBCs

Run the whole flow on the **desktop app, 0.7.16**, from an empty data folder (a fresh-install state shows the first-run hints the room will see). If possible repeat Parts 1 and 3 on a **Windows** laptop: most of the room will not have Apple silicon, and Topic Modelling on Windows still uses the processor.

- [ ] **Part 1**: new Project; import the QLD tweets and **Hansard GST**; time the Hansard import (decides whether everyone starts it in Part 1). Data Editor Overview; `created_at` to date-and-time through the conversion window; Combine columns `full_name` on candidates; Join tweets (left) to candidates on `username`; Filter out retweets: **1,646 rows**; Map values `party` into sides (prepare the mapping list for the Explore card).
- [ ] **Part 2**: Frequency with women and men candidates' tweets; the exact mode names for the comparison; right-click a word into stop words; click a word into Concordance; **Match Details** (0.7.16) opens at the match; `job(s)?|cut(s)?` Run, then Add to Project; Trends by day and gender, then by matched word. Note one place a **suggestion** reliably appears (a Concordance Preview with no matches is the documented one) for the demo.
- [ ] **Part 3: Topic Modelling settings for the tweets, re-tested on 0.7.16.** August used min topic size 7, 40 topics, a recorded seed and found 5 "job" topics; 0.7.12 changed the clustering (Max topic size Auto, Ungrouped), so those numbers no longer carry over. Find settings that give a readable map in **under 2 minutes on a mid-range Windows laptop**, record Seed, Topics, Max topic size and Max tokens (the 0.7.16 Max tokens suggestion may fire on tweets: decide whether to accept it on screen). Time the first run including the model download.
- [ ] **Part 3 examples**: the eye opens example texts; Most typical; Open document; name a topic; find a topic that reads well when named (a "jobs" or "health" topic); Add to Project for one topic, then Trends.
- [ ] **Hansard Explore cards**: Sample GST to 2,000 paragraphs (Seed 0) and time Topic Modelling on it; Trends of GST paragraphs by year and chamber; Join the speaker table on `speaker_detail_id` for party and gender. Write what works into the Explore cards.
- [ ] **Part 4**: as August's sheet, on 0.7.16 labels: the 226 job tweets (Filter `job` on the no-retweet block), upload `artifacts/online-2026-08-28/tweets_job_reference.csv` and join on `tweet_id`, codebook v1 with **Task context** (new in 0.7.15; decide whether to use it), code page 1 by hand, Compare To the reference, provider via Settings → Servers, Preview, Compare To, Run. **Which rows to annotate** now defaults to only rows without a label: check it does not trip the hand-coded-then-AI flow.
- [ ] **Browser option**: launch ARDC BinderHub from sih.tools/wordflow; check it runs **0.7.16** (the 0.7.16 Binder launch was still pending a human check on 23 Oct) and that a checkpoint loads in it.

## 3 · Sunday 25 Oct: build the materials and the checkpoints

- [ ] **Checkpoints A to D** from one clean 0.7.16 run-through, exported as Project archives, then round-trip each on a second machine (import, open, re-pick the tool inputs: those are not saved):
  - **A**, end of Part 1: tweets and candidates imported, types set, `full_name`, the joined block, the no-retweet block.
  - **B**, end of Part 2: plus the `job(s)?|cut(s)?` Concordance block and the Trends tab.
  - **C**, end of Part 3: plus the Topic Modelling tab (settings from §2) and one named topic added to the Project.
  - **D**, Part 4 start: plus the 226 job tweets joined to the reference labels and the v1 codebook block. The prompt and model are not saved in a Project: the sheet says to re-select them.
  - Replace the v0.7.7 archives in `artifacts/checkpoints/` (they hold August's flow). Host the zips where the room can download them in one click (a GitHub release on this repo, as August did) and make a short link or QR code.
- [ ] **Participant step sheet** `participant/hands-on-melbourne.md`: Together steps and an Explore card per part, checkpoints linked, plain 0.7.16 labels. Share it in the room by QR code and short link.
- [ ] **Deck** `slides/melbourne-wordflow.html`: welcome and housekeeping (Melbourne Connect: toilets, emergency, Acknowledgement of Country for Wurundjeri Woi-wurrung land, to confirm with MDAP), who we are, why Wordflow, interface, one idea, a title slide per part with its Explore card, Part 4 framing, close. Reuse the September deck's current-version interface slide and the August slides' structure.
- [ ] **Runbook** with clock gates and the cut order (README), printed or on the second screen.
- [ ] Remove the August-only files from this branch before its link goes to participants (`*-online.*`, `*-s1*`, `*-s2*`, the August checkpoint archives, `artifacts/snapshots/`).

## 4 · AI provider: the shared key

- [ ] **Network**: participants use their own laptops on eduroam (Chao, 2026-10-23), so requests are not funnelled through one shared address and August's rate-limit picture holds (paid models: no OpenRouter platform request cap while the balance is positive). No extra stress test planned.
- [ ] **If errors appear on the day** (429s or timeouts in the Tasks panel): ask the room to lower **Requests at once** (Advanced settings, default 10) to 3 and Run again; labels already returned are kept. Everyone Previews first anyway, so the full Run is never the first call.
- [ ] Room model and fallback: re-check `google/gemini-2.5-flash-lite` (August's room model) and the fallback `z-ai/glm-5.3-flash` are still listed and priced; 0.7.15 shows a one-line description under each model, so check what the room will read there.
- [ ] **Monday morning**: create the key `workshop-2026-10-26` with a hard cap (about US$20), test it once from the hotel network, put it in the runbook. **Delete it at 5:00 pm.**
- [ ] If `openrouter.ai` is blocked on the venue network: Part 4 still runs by hand (be the coder first, Compare To the reference), and the AI steps are shown on the shared screen from a phone hotspot.

## 5 · Monday 26 Oct

- [ ] **Morning**: Wordflow on the presenting laptop is 0.7.16 (the updater may have moved; no newer version expected). Empty data folder or a clean Project list for the on-screen Part 1. Deck opens offline. Checkpoint link and QR tested on a phone.
- [ ] **1:15 pm, room setup**: projector and screen readable from the back (Wordflow zoomed: Cmd and + twice); Zoom running and sharing the whole screen if anyone joins online; mic check; Wi-Fi joined; **warm the Topic Modelling model cache** by running Part 3 once on the venue network (the first run downloads the model). Power boards out. QR code for the step sheet on screen as people arrive.
- [ ] **1:30 pm, helper briefing** (15 minutes): the plan in one page; the three known pitfalls: (1) the Join's first pick is the left table; (2) after loading a checkpoint, re-pick the tool's Data Block and columns; (3) in Part 4 the prompt and model are not saved, re-select them. The escalation signal: if a third of the room is stuck on the same step, stop and show it on screen.
- [ ] **During**: one helper owns the Zoom chat; the others own a section of the room each. Checkpoint link posted in the Zoom chat at each part.
- [ ] **5:00 pm**: delete the shared key. Ask MDAP for attendance numbers (aggregate only) for the SIH training report.

## 6 · After

- [ ] Post-workshop email via MDAP within a day: step sheet, slide PDF, checkpoints, the August recordings, sih.tools/wordflow, Feedback in the app.
- [ ] Merge anything fixed on this branch into a final tag `melbourne-2026-10-26-final`, as with August and September.
