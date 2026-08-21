# Pre-workshop checklist — online workshop, 28 August 2026

Work top to bottom; the artefact builds (§2–3) are the long poles — start them a week out.

## 1 · Version + release-week timeline

**The week's plan (workshop Friday 28 Aug):**

- **Tue 25 (Alex back)**: helper briefing meeting; Alex triages the workshop-affecting bug issues; target **v0.7.3 bug-fix release Tuesday night**. Decide on #68 (word-count ops): if it ships, the S1 histogram demo can revert to the word-count variant; otherwise the tweets-per-candidate version runs (both are staged).
- **Wed 26**: install v0.7.3 fresh and run the **Wednesday test script** (below). Rebuild the demo workspaces + checkpoint archives on the final version. **Send the pre-workshop email Wednesday night** only after the test passes; if v0.7.3 slips, ship the email anyway (it references "the v0.7 desktop app", not a patch number) and fall back to v0.7.2 with known-bug workarounds.
- **Thu 27**: full rehearsal against the run-of-show panel (both sessions, timed); upload final checkpoint files; T-1 reminder email.
- **Fri 28**: morning-of checks (§7).

**Wednesday test script (everything the materials assume, in order):**

- [ ] Fresh install opens; version correct; multi-tab ON (Settings → General).
- [ ] Sample import → tweets block; Frequency word cloud renders; right-click word → stop words.
- [ ] S2 derivation: Filter regex `^[Rr][Tt]` + negate → Filter contains `job` → **exactly 226 rows**.
- [ ] Annotation: `theme.manual` column + codebook (lowercase codes) + manual codes; `theme.ai`; provider add (throwaway key) → model list → **Preview** → **Compare To** κ + confusion matrix → **Run All** on 226.
- [ ] Ground-truth join: `tweets_job_groundtruth.csv` uploads, joins on `tweet_id` (dtype match), Compare To `theme.verified` gives full-table κ.
- [ ] S1 histogram demo: Expression group-by JSONs from the copy bank → `tweet_count` block → **Trends accepts numeric x-axis + bucketing, line→bar**.
- [ ] Topic Modelling: run on two blocks; note the v0.7.2+ cluster-control wording for the runbook.
- [ ] Checkpoint round-trip on a second machine: Upload workspace → Load → selectors re-pick.
- [ ] Excel/zip import: retest; if fixed, delete the caveat from the hands-on sheet §1 and pre-email.

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

- [ ] `Checkpoint_a_Data.zip`: sample tweets imported → Filter #1 (`^[Rr][Tt]` regex, negated) → Filter #2 (contains `job`) → the **226-row block**, PLUS `tweets_job_groundtruth.csv` (in `artifacts/online-2026-08-28/`; column `theme.verified`) joined on `tweet_id`. **Rebuild the CSV from the RA-verified labels first** (merge `tweets_job_fable_review.csv` corrections; ask Claude).
- [ ] `Checkpoint_b_Codebook.zip`: plus the v1 codebook (three lowercase codes with v1 descriptions), `theme.manual` column with ~8 codes filled, and an empty `theme.ai` column.
- [ ] `Checkpoint_c_V2.zip`: plus the v2 codebook descriptions and v2 prompt saved in the Annotation tab, ready to Run All.
- [ ] **Round-trip test each file on a second machine**: Upload workspace → Load → open Annotation → data, tabs, codebook restore; block/column selectors need re-picking (expected; the sheet says so).
- [ ] **Join test**: join the ground-truth block onto the 226-row block on `tweet_id` (both sides must parse the id with the same dtype), then Compare To `theme.verified` shows a full-table κ.
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

- [ ] **Wed 26 night** (after the test passes): send `communications/pre-workshop-email-online.md` (fill the ⟨placeholders⟩: times, Zoom link, helpers line).
- [ ] **Thu 27**: short reminder — Zoom link, the install task, "morning is recorded / afternoon isn't".
- [ ] T+1 day: `communications/post-workshop-email-online.md` — recording link, slide PDFs (print both decks to PDF via the browser print dialog — they're print-styled), hands-on sheet, checkpoint files.

## 7 · Morning of

- [ ] Wordflow version check (self-updater may have moved overnight — re-pin or re-verify).
- [ ] Tour + Story workspaces load; Tasks section idle; no leftover test workspaces cluttering the Workspace manager on screen.
- [ ] Checkpoint links, hands-on-sheet link, and the API troubleshooting one-liners in a text file ready for chat.
- [ ] Deck files open locally (offline-fine); notes toggled (N) on your second monitor.
- [ ] Do-not-disturb on the presenting machine; close email/Slack; hide the menu-bar clutter — you're recording.
