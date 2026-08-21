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
