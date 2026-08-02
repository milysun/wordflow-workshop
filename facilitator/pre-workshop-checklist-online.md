# Pre-workshop checklist — online workshop, 28 August 2026

Work top to bottom; the artefact builds (§2–3) are the long poles — start them a week out.

## 1 · Version + known issues (T-7 days)

- [ ] Confirm the shipping Wordflow version (0.7.1 or later 0.7.x) and install it fresh on the presenting machine. The desktop app self-updates — pin/verify the version the morning of, so the room and your screen match.
- [ ] Re-test the **Excel/zip import** bug on that version. If fixed, delete the caveat from: `participant/hands-on-annotation-online.md` §1, `slides/online-s2-annotation.html` (none currently), `runbook-online-s2.md` §0:15, `communications/pre-workshop-email-online.md` (not mentioned — OK).
- [ ] Settings → General → **Enable multi-tab: ON** on the presenting machine.
- [ ] **Retake `slides/images/ui-overview.png` on v0.7** (current file is a v0.5 screenshot — the sidebar shows Annotation, "Help" instead of "Tutorial", and no working-directory footer). Re-aim the numbered-circle overlay in `slides/online-s1-intro.html` (cx/cy pairs) if the layout shifted.

## 2 · Session 1 demo workspaces (T-5 days)

- [ ] **Tour workspace** — one tab per tool, analyses finished, tabs named for the recording:
  - `Frequency` tab: news corpus comparative (Guardian+IA vs Sky+PerthNow), 40 words, stopwords on.
  - `Concordance` tab: Honi Soit, 3-pattern regex, coloured.
  - `Trends` tab: QLD tweets grouped by term/gender/party.
  - `Topic Modeling` tab: news corpus two-sided run (blended vs solid bubbles visible).
  - `Quotation` tab: Honi Soit, sorted by speaker.
- [ ] **Story workspace** — sample data imported, *nothing built* (the research story is built live).
- [ ] **Story backup archives** — build the full story once, exporting a workspace archive at each phase boundary (A–E). These are your Plan B if a live step misbehaves mid-recording. Keep them local; they're not published.

## 3 · Session 2 checkpoint archives (T-5 days)

Build in a clean workspace, exporting after each stage (**Export view → Export Workspace → "Export workspace archive"**), and rename the files:

- [ ] `Checkpoint_0_Data.zip` — workspace + ADO Queensland Election Tweets imported, `candidate_info_gender` added as a block.
- [ ] `Checkpoint_1_Codebook.zip` — plus `gender.ai` column, M/F/U codebook with descriptions, ~5 manual codes.
- [ ] `Checkpoint_2_Preview.zip` — plus a working prompt saved in the Annotation tab. *(Provider/key are NOT in archives — nothing to scrub.)*
- [ ] **Round-trip test each file on a second machine**: Upload workspace → Load → open Annotation → confirm data, tabs, codebook restore; note that block/column selectors need re-picking (that's expected — the sheet says so).
- [ ] Upload the three files to the materials location and put the download links in a text file ready to paste into Zoom chat. ⟨Where: sih.tools/wordflow → Materials, or a GitHub release on this branch⟩

## 4 · AI provider (T-3 days)

- [ ] Your own OpenRouter key works: model list loads, a `:free` Gemma model previews successfully, `gemini-2.5-flash-lite` runs if credited.
- [ ] Confirm at least one **`:free`** model currently listed on OpenRouter handles the task acceptably (free-model lineups change — re-check the week of).
- [ ] Decide the fallback-key policy: if yes, create a **separate throwaway key with a hard spend cap** to paste into chat if several participants' keys fail; revoke it same day. Never on a public URL.

## 5 · Zoom + recording (T-2 days)

- [ ] Schedule ONE meeting covering both sessions (same link, per the email). Waiting room off ⟨or a helper admitting⟩; chat open to everyone; participants can unmute in Session 2.
- [ ] **Recording plan**: cloud-record Session 1 only. **Auto-record OFF** — start manually at the Session 1 title slide, stop at the lunch slide. Before Session 2, confirm recording is off and say so on mic.
- [ ] Test screen share readability: share the app window, bump app zoom (Cmd/Ctrl +), check in the Zoom preview at 720p.
- [ ] Brief helpers ⟨if any⟩: chat triage in S2, the checkpoint drill (Upload workspace → Load → re-select), backup host if you drop.

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
