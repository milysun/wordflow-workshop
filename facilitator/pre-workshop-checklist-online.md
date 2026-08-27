# Pre-workshop checklist — online workshop, 28 August 2026

Work top to bottom; the artefact builds (§2–3) are the long poles — start them a week out.

## 1 · Version + release-week timeline

**The week's plan (workshop Friday 28 Aug):**

- **Tue 25 (Alex back)**: helper briefing meeting; Alex triages the workshop-affecting bug issues; target **v0.7.3 bug-fix release Tuesday night**. Decide on #68 (word-count ops); note the histogram demo is now optional F.2 in the S1 plan (2026-08-24), so this only matters if time miraculously allows it.
- **Wed 26**: install v0.7.3 fresh and run the **Wednesday test script** (below). Rebuild the demo workspaces + checkpoint archives on the final version. **Send the pre-workshop email Wednesday night** only after the test passes; if v0.7.3 slips, ship the email anyway (it references "the v0.7 desktop app", not a patch number) and fall back to v0.7.2 with known-bug workarounds.
- **Thu 27** *(actual: v0.7.3 still unreleased Thursday morning, Alex fixing)*: **pre-workshop email goes out by lunchtime** via Eventbrite (final text in `communications/pre-workshop-email-online.md`; it hedges with "latest v0.7" + "accept the in-app update prompt if offered tomorrow"); full rehearsal against the run-of-show panel (both sessions, timed); build checkpoint files on whatever version is current tonight, and if v0.7.3 lands late, re-run the checkpoint round-trip on it before bed.
- **Fri 28**: morning-of checks (§7).

**Wednesday test script (everything the materials assume, in order):**

- [ ] Fresh install opens; version correct; multi-tab ON (Settings → General).
- [ ] Sample import → tweets block; Frequency word cloud renders; right-click word → stop words.
- [ ] S2 derivation: Filter regex `^[Rr][Tt]` + negate → Filter contains `job` → **exactly 226 rows**.
- [ ] Annotation: `theme.manual` column + codebook (lowercase codes) + manual codes; `theme.ai`; provider add (throwaway key) → model list → **Preview** → **Compare To** κ + confusion matrix → **Run All** on 226.
- [ ] Reference join: `tweets_job_reference.csv` uploads, joins on `tweet_id` (dtype match), Compare To `theme.reference` gives full-table κ.
- [ ] Checkpoint round-trip on a second machine: Upload workspace → Load → selectors re-pick.
- [ ] Excel/zip import: retest; if fixed, delete the caveat from the hands-on sheet §1 and pre-email.

**Wednesday TBC hunt for the S1 demo (pins every TBC in `demo-checklist-s1.md` / `runbook-online-s1.md`; write the answers into the checklist):**

- [ ] **Topic Modelling on tweets_F + tweets_M with min topic size 7, topics 40**: find and RECORD the seed that reproduces the **5 "job" topics** via the word text-filter. Time the run.
- [ ] Topic Modelling controls: exact v0.7.2/3 labels for sampling, segmentation methods, min topic size, topic-count **re-aggregation**; does bubble **lasso** selection exist (v0.7.1 had multi-click only)? If no lasso, strike 6.5's lasso line.
- [ ] **Honi Soit Topic Modelling**: pick parameters, time the run (feeds the Ch5 background-kickoff timing).
- [ ] **Quotation Run All on Honi Soit**: time it. If > ~20 min, the kickoff moves from Ch5 (11:56) to Ch3 (11:34). Record the output column names after Add to Workspace.
- [ ] Concordance: exact name of the extraction column on an Add-to-Workspace block; does the review table have a filter as well as sort?
- [ ] String dtype label: still "Utf8View" in v0.7.3, or renamed? Prepare the one-sentence explainer either way.
- [ ] "Ways to add a block to a tool": confirm the full list (quick-select · double-click graph node · in-tool selector?) for Ch3.1.
- [ ] Workspace creation: exact button wording for Ch1.3; graph-view node markers ("red dots") wording for Ch2.6.
- [ ] Frequency comparative: exact mode names (side-by-side vs juxtaposed/overuse) for Ch3.7.
- [ ] S1 histogram demo (optional F.2 only): Expression group-by JSONs from the copy bank → `tweet_count` block → Trends numeric x-axis + bucketing, line→bar.

## 2 · Session 1 demo prep (T-5 days) — full-capability tour, built live from empty

*(Replaces the old Tour + Story workspace pair: the 2026-08-24 plan builds ONE workspace on camera, from creating it in Ch1 through Export in Ch8. See `demo-checklist-s1.md`.)*

- [ ] **Fresh-state check**: app opens with no workspace; contextual hints ON; multi-tab ON.
- [ ] **Demo CSV** chosen and staged in an easy folder for the Ch1 drag-and-drop (any small, uncontroversial CSV; not the S2 reference file).
- [ ] **Section backup archives** — build the full demo once end-to-end (this is also the rehearsal), exporting a workspace archive at each chapter boundary (Ch2, Ch4, Ch5, Ch6, Ch8 at minimum). Plan B if a live step misbehaves mid-recording; the Ch6/Ch8 archives also carry the finished Honi Soit Topic Modelling + Quotation results in their tabs (fallback if the background jobs aren't done when reached). Keep them local; not published.
- [ ] Write the pinned TBC values (seed, timings, control labels — from the Wednesday hunt above) into `demo-checklist-s1.md` before the Thursday rehearsal.

## 3 · Session 2 checkpoint archives (T-5 days)

Build in a clean workspace on v0.7.2, exporting after each stage (**Export view → Export Workspace → "Export workspace archive"**), and rename the files. Class names everywhere are lowercase: `promise` / `cuts` / `other`.

- [ ] `Checkpoint_a_Data.zip`: sample tweets imported → Filter #1 (`^[Rr][Tt]` regex, negated) → Filter #2 (contains `job`) → the **226-row block**, PLUS `tweets_job_reference.csv` (in `artifacts/online-2026-08-28/`; column `theme.reference`) joined on `tweet_id`. Built 2026-08-27 from Kelvin's review (Fable coding with 22 overrides); Xinwei's second pass may adjust it further.
- [ ] `Checkpoint_b_Codebook.zip`: plus the v1 codebook (three lowercase codes with v1 descriptions), `theme.manual` column with ~8 codes filled, and an empty `theme.ai` column.
- [ ] `Checkpoint_c_V2.zip`: plus the v2 codebook descriptions and v2 prompt saved in the Annotation tab, ready to Run All.
- [ ] **Round-trip test each file on a second machine**: Upload workspace → Load → open Annotation → data, tabs, codebook restore; block/column selectors need re-picking (expected; the sheet says so).
- [ ] **Join test**: join the reference block onto the 226-row block on `tweet_id` (both sides must parse the id with the same dtype), then Compare To `theme.reference` shows a full-table κ.
- [ ] Upload the three ZIPs + `tweets_job_reference.csv` to the materials location; paste the links into the run-of-show panel's Checkpoint field.

## 4 · AI provider (T-3 days)

- [ ] The **shared session key is the primary path** (decided): create it fresh on the day (12:35 step in the run-of-show) with a hard spend cap, named `workshop-2026-08-28`, and **delete it at 15:30**. Budget sanity check: ~50 participants × 226 tweets × a few preview pages on flash-lite is still only a few dollars; set the cap accordingly (e.g. US$20).
- [ ] Rehearse the full flow on a throwaway key beforehand: model list loads, `google/gemini-2.5-flash-lite` previews and Run-Alls the 226-row block cleanly, and note the run time.
- [ ] **Know the rate-limit facts (verified against OpenRouter docs, 2026-08-21):**
  - Limits are **per account, not per key**. Extra keys on the same account add zero capacity.
  - `:free` models: **20 requests/minute per account across all free models combined**, and 1,000/day (the $10 lifetime purchase unlocks 1,000/day, up from 50; it does NOT raise the 20 RPM). One shared account × a whole room means **free models are unusable as the room path AND unusable as the fallback**. Spreading people across different free models does not help; the cap is account-wide.
  - **Paid models (no `:free` suffix): no OpenRouter platform request cap** while the balance is positive; the real ceilings are upstream-provider capacity and Cloudflare's per-IP abuse protection. Participants call from their own home/office IPs, so the per-IP layer is naturally spread; the shared thing is only the account.
  - Cost sanity: 70 people × 226 tweets on flash-lite ≈ 16k tiny requests ≈ **under US$2**. The $10 already on the account covers the day; the US$20 key cap stands.
- [ ] **Fallback is a second PAID model on a different upstream** (e.g. `openai/gpt-5-nano`), pre-tested on the v1 task. If the room model starts returning 429/errors mid-session (upstream congestion), everyone switches the Model dropdown; nothing else changes. Put its id in the panel's fallback-model field.
- [ ] **Stress test (Wednesday, with the real account)**: run `facilitator/stress-test-openrouter.py` with ~50 concurrent requests × a few hundred total against the room model, from one machine. Watch for 429s, Cloudflare 403s, and latency. Costs cents. If the account itself gets throttled at one-machine concurrency, escalate: the room's load will be gentler per-IP but heavier in total.

## 5 · Zoom + recording (T-2 days)

- [ ] Schedule ONE meeting covering both sessions (same link, per the email). Waiting room off ⟨or a helper admitting⟩; chat open to everyone; participants can unmute in Session 2.
- [ ] **Recording plan**: cloud-record Session 1 only. **Auto-record OFF** — start manually at the Session 1 title slide, stop at the lunch slide. Before Session 2, confirm recording is off and say so on mic.
- [ ] **Screen-share setup (decided 2026-08-24)**: Wordflow full screen + deck on the MBP built-in display; panel and everything else on the external screen; Zoom shares the **entire MBP screen** so cursor/click effects reach the feed. Bump app zoom (Cmd/Ctrl +) for readability.
- [ ] **Cursor visibility kit**: macOS Accessibility → Display → Pointer: size up, coloured fill; install a click-effect app (**Mouzz**, free, or Presentify/Mouseposé). In a test meeting, **cloud-record 30 s** and check the downloaded .mp4: note its actual resolution (screen share records near the shared display's effective resolution; the 720p/1080p caps are for webcams), and confirm the enlarged pointer, click ripple, and (if used) Ctrl+scroll zoom are visible. Consider a "More Space" display scaling on the MBP for more recorded pixels, balanced against on-screen text size. Fallback if effects misbehave: window share still carries the enlarged pointer, but loses ripples and screen zoom.
- [ ] **Helpers (all co-hosts)**: morning = Alex + Seb (chat inquiries, roll); afternoon = Gordon, Georgie, Xinwei, Alex, Seb (roll, chat triage, resend links/key/prompts, breakout rooms, escalate via Teams/mobile if the majority is struggling). Pre-create breakout rooms **Help-1/2/3**.
- [ ] **Helper briefing meeting (Tue/Wed before)**: walk the run-of-show panel top to bottom; share the hands-on sheet and the panel file itself (it holds every chat snippet); agree the escalation signal ("majority struggling" = you stop and repeat on screen); collect their known-pitfall suggestions.

## 6 · Communications

- [ ] **Wed 26 night** (after the test passes): send `communications/pre-workshop-email-online.md` (fill the ⟨placeholders⟩: times, Zoom link, helpers line).
- [ ] **Thu 27**: short reminder — Zoom link, the install task, "morning is recorded / afternoon isn't".
- [ ] T+1 day: `communications/post-workshop-email-online.md` — recording link, slide PDFs (print both decks to PDF via the browser print dialog — they're print-styled), hands-on sheet, checkpoint files.

## 7 · Morning of

- [ ] Wordflow version check (self-updater may have moved overnight — re-pin or re-verify).
- [ ] Tour + Story workspaces load; Tasks section idle; no leftover test workspaces cluttering the Workspace manager on screen.
- [ ] Checkpoint links, hands-on-sheet link, and the API troubleshooting one-liners in a text file ready for chat.
- [ ] Deck files open locally (offline-fine); notes toggled (N) on your second monitor.
- [ ] Do-not-disturb on the presenting machine; close email/Slack; hide the menu-bar clutter — you're recording.
