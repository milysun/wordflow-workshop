# Pre-workshop checklist — online workshop, 28 August 2026

Work top to bottom; the artefact builds (§2–3) are the long poles — start them a week out.

## 1 · Version + known issues (T-7 days)

- [ ] Base release is **v0.7.2** (Tauri, published 2026-08-19). Install it fresh on the presenting machine; only bug-fix updates expected before the day. The desktop app self-updates, so re-verify the version the morning of. Note: **Windows installer is unsigned** (SmartScreen warning; More info → Run anyway); macOS is signed and notarized.
- [ ] Re-test the **Excel/zip import** bug on that version. If fixed, delete the caveat from: `participant/hands-on-annotation-online.md` §1, `slides/online-s2-annotation.html` (none currently), `runbook-online-s2.md` §0:15, `communications/pre-workshop-email-online.md` (not mentioned — OK).
- [ ] Settings → General → **Enable multi-tab: ON** on the presenting machine.
- [x] ~~Retake the UI screenshot~~ DONE 2026-08-21: slide 7 now uses `slides/images/ui-overview-v07.png` (v0.7.2 capture from Chao) with re-aimed circles and a rewritten legend.

## 2 · Session 1 demo workspaces (T-5 days)

- [ ] **Tour workspace** — one tab per tool, analyses finished, tabs named for the recording:
  - `Frequency` tab: news corpus comparative (Guardian+IA vs Sky+PerthNow), 40 words, stopwords on.
  - `Concordance` tab: Honi Soit, 3-pattern regex, coloured.
  - `Trends` tab: QLD tweets grouped by term/gender/party.
  - `Topic Modelling` tab: news corpus two-sided run (blended vs solid bubbles visible).
  - `Quotation` tab: Honi Soit, sorted by speaker.
- [ ] **Story workspace** — sample data imported, *nothing built* (the research story is built live).
- [ ] **Story backup archives** — build the full story once, exporting a workspace archive at each phase boundary (A–E). These are your Plan B if a live step misbehaves mid-recording. Keep them local; they're not published.

## 3 · Session 2 checkpoint archives (T-5 days)

Build in a clean workspace on v0.7.2, exporting after each stage (**Export view → Export Workspace → "Export workspace archive"**), and rename the files. Class names everywhere are lowercase: `promise` / `cuts` / `other`.

- [ ] `Checkpoint_a_Data.zip`: sample tweets imported → Filter #1 (`^[Rr][Tt]` regex, negated) → Filter #2 (contains `job`) → the **226-row block**, PLUS `tweets_job_groundtruth.csv` (in `artifacts/online-2026-08-28/`) loaded as a block, ready to join on `tweet_id`.
- [ ] `Checkpoint_b_Codebook.zip`: plus the v1 codebook (three lowercase codes with v1 descriptions), `theme.manual` column with ~8 codes filled, and an empty `theme.ai` column.
- [ ] `Checkpoint_c_V2.zip`: plus the v2 codebook descriptions and v2 prompt saved in the Annotation tab, ready to Run All.
- [ ] **Round-trip test each file on a second machine**: Upload workspace → Load → open Annotation → data, tabs, codebook restore; block/column selectors need re-picking (expected; the sheet says so).
- [ ] **Join test**: join the ground-truth block onto the 226-row block on `tweet_id` (both sides must parse the id with the same dtype), then Compare To `theme.fable` shows a full-table κ.
- [ ] Upload the three ZIPs + `tweets_job_groundtruth.csv` to the materials location; paste the links into the run-of-show panel's Checkpoint field.

## 4 · AI provider (T-3 days)

- [ ] The **shared session key is the primary path** (decided): create it fresh on the day (12:35 step in the run-of-show) with a hard spend cap, named `workshop-2026-08-28`, and **delete it at 15:30**. Budget sanity check: ~50 participants × 226 tweets × a few preview pages on flash-lite is still only a few dollars; set the cap accordingly (e.g. US$20).
- [ ] Rehearse the full flow on a throwaway key beforehand: model list loads, `google/gemini-2.5-flash-lite` previews and Run-Alls the 226-row block cleanly, and note the run time.
- [ ] Confirm at least one `:free` model currently on OpenRouter handles the v1 task acceptably (fallback if the shared key rate-limits under 50 concurrent users; free models have their own per-account limits, so they are the backup, not the plan).

## 5 · Zoom + recording (T-2 days)

- [ ] Schedule ONE meeting covering both sessions (same link, per the email). Waiting room off ⟨or a helper admitting⟩; chat open to everyone; participants can unmute in Session 2.
- [ ] **Recording plan**: cloud-record Session 1 only. **Auto-record OFF** — start manually at the Session 1 title slide, stop at the lunch slide. Before Session 2, confirm recording is off and say so on mic.
- [ ] Test screen share readability: share the app window, bump app zoom (Cmd/Ctrl +), check in the Zoom preview at 720p.
- [ ] **Helpers (all co-hosts)**: morning = Alex + Seb (chat inquiries, roll); afternoon = Gordon, Georgie, Xinwei, Alex, Seb (roll, chat triage, resend links/key/prompts, breakout rooms, escalate via Teams/mobile if the majority is struggling). Pre-create breakout rooms **Help-1/2/3**.
- [ ] **Helper briefing meeting (Tue/Wed before)**: walk the run-of-show panel top to bottom; share the hands-on sheet and the panel file itself (it holds every chat snippet); agree the escalation signal ("majority struggling" = you stop and repeat on screen); collect their known-pitfall suggestions.

## 6 · Communications

- [ ] T-7 days: send `communications/pre-workshop-email-online.md` (fill the ⟨placeholders⟩: times, Zoom link, helpers line).
- [ ] T-1 day: short reminder — Zoom link, the two setup tasks, "morning is recorded / afternoon isn't".
- [ ] T+1 day: `communications/post-workshop-email-online.md` — recording link, slide PDFs (print both decks to PDF via the browser print dialog — they're print-styled), hands-on sheet, checkpoint files.

## 7 · Morning of

- [ ] Wordflow version check (self-updater may have moved overnight — re-pin or re-verify).
- [ ] Tour + Story workspaces load; Tasks section idle; no leftover test workspaces cluttering the Workspace manager on screen.
- [ ] Checkpoint links, hands-on-sheet link, and the API troubleshooting one-liners in a text file ready for chat.
- [ ] Deck files open locally (offline-fine); notes toggled (N) on your second monitor.
- [ ] Do-not-disturb on the presenting machine; close email/Slack; hide the menu-bar clutter — you're recording.
