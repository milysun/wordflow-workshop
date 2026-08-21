# S1 demo checklist — every click, in order (recorded session)

> Companion to `run-of-show-online.html` (timing) and `runbook-online-s1.md` (spoken script).
> This file is only the ACTIONS: what to click, in what order, and what the screen should show
> before you move on. Tick as you go; if a SEE line doesn't match, fix it before continuing,
> since the recording keeps everything.

## The six mistakes that would hurt the recording (read this box before starting)

1. **Recording**: START at the title slide, STOP after the lunch slide. Nothing else matters if this is wrong.
2. **Join order**: in Preprocessing → Join, pick `tweets` FIRST. First pick = left table. Wrong order = candidates without tweets instead of tweets without gender.
3. **Dtype check BEFORE the join**: `username` must have the same dtype on both blocks. Do the check on camera (it's a teaching point) but do it, or the join misbehaves.
4. **Table view BEFORE Add to Workspace** in phase C. Dispersion aggregates per document, which is the wrong shape for Trends. If you forget: delete the block via its menu icon, switch view, redo.
5. **Topic Modelling seed = 42.** Any other seed and your rehearsed topic story (counts, colours) won't reproduce.
6. **Rename the tweets block FIRST** (step A2), before anything derives from it, so every downstream block and the final workspace-graph shot read cleanly.

---

## 0 · Pre-flight (before the recording starts)

- [ ] Wordflow final release open (v0.7.3 if shipped, else v0.7.2).
- [ ] **Settings → General → Enable multi-tab = ON.**
- [ ] **Tour** workspace loaded: 5 finished tabs, in sidebar tool order: Frequency (news comparative), Concordance (Honi Soit 3-pattern regex), Trends (QLD tweets), Topic Modelling (news two-sided), Quotation (Honi Soit).
- [ ] **Story** workspace: QLD sample data imported (`qldelection2020_candidate_tweets` + `candidate_info_gender` blocks present), **nothing built**, no extra tabs.
- [ ] Phase backup archives (A–E) reachable in a folder you can find without hunting.
- [ ] Deck on second monitor, run-of-show panel on the private screen, DND on, notifications off.
- [ ] Zoom: share the **app window**, not the desktop. Check readability in the Zoom preview.

**▶ START THE RECORDING at the title slide, before you speak.**

---

## 1 · Interface tour (Tour workspace) · ~0:13

Point at, in order (the "7 things", matching the welded screenshot on slide 7):

- [ ] 1 **Views** sidebar; pause on **Annotation** ("this afternoon's star").
- [ ] 2 Tool interface (whatever tab is active).
- [ ] 3 Workspace graph; double-click one node → it lands in the active tool. Undo that selection.
- [ ] 4 Data Viewer; open one block's **menu icon** and one **column menu** to show management lives here (don't change anything).
- [ ] 5 Quick-select.
- [ ] 6 **Help** (sidebar footer).
- [ ] 7 **Feedback** (sidebar footer).
- [ ] Plant the tabs line: rename a tab by **clicking the already-active tab a second time**, then say "tabs are saved with the workspace" (afternoon checkpoints depend on this).

## 2 · Tool tour (Tour workspace, pre-built tabs; interpret, don't build) · ~0:22

- [ ] **Frequency** (news comparative): toggle Cloud ↔ List · **right-click a word** → it joins "Stop words filter (N)" and vanishes · flash a download icon (image = PNG, table = CSV).
- [ ] **Concordance** (Honi Soit): show the 3 coloured regex patterns · switch to **Dispersion** view · back to list.
- [ ] **Trends** (QLD): same period grouped three ways · click legend entries to filter lines off/on.
- [ ] **Topic Modelling** (news two-sided): hover a bubble → top words · point at one solid vs one blended bubble.
- [ ] **Quotation** (Honi Soit): sort by speaker · say "English-only" honestly.
- [ ] Timing gate: at 0:42 on the clock, phase A must be starting. Late? Quotation was the cut.

## 3 · Research story (SWITCH to the Story workspace) · 0:42–1:15

### A · Load, prepare, join (~5 min)

- [ ] A1 Data Loader: both blocks present (`qldelection2020_candidate_tweets`, `candidate_info_gender`). If not: **Import sample data** → `ADO — Queensland Election Tweets` → **Import selected**.
- [ ] A2 **Rename first**: tweets block **menu icon** → Rename → `tweets`. (Menu icon, never right-click.)
- [ ] A3 One column delete via the **column menu** (pick a column you rehearsed; narrate that block/column management lives in the Data Viewer).
- [ ] A4 ⚠ Check `username` dtype on BOTH blocks; align (cast) if they differ. SEE: same dtype both sides.
- [ ] A5 Preprocessing → **Join**: select `tweets` **FIRST**, then `candidate_info_gender` · key = `username` both sides · **left** join · Apply result as **Create new Data Block** → name `tweets_with_gender`.
      SEE: row count = the tweets count (unchanged), with gender columns appended.
- [ ] A6 Preprocessing → **Create** on `tweets_with_gender`: `full_name` = [first_name chip] + `" "` (typed literal, with the space) + [last_name chip].
      SEE: preview shows real full names, one per row. Say the landing line ("no code, just terms").

### B · Filter + Frequency ↔ Concordance loop (~7 min)

- [ ] B1 Preprocessing → **Filter** on `tweets_with_gender`: `gender = F` → new block (name it `tweets_F`).
- [ ] B2 Repeat: `gender = M` → `tweets_M`.
- [ ] B3 Frequency: select **both** blocks → comparative · 40 words · stopwords on.
- [ ] B4 The loop, honestly, 2–3 rounds: **click a word** → Concordance opens on it → read 2–3 lines aloud → back to Frequency → next word.
- [ ] B5 End the loop ON `covid` / `case(s)` / `cut(s)`: these seed the phase-C regex. Say so.

### C · Regex → Add to Workspace → Trends (~8 min)

- [ ] C1 Concordance on `tweets_with_gender`, **Regex** mode: `covid|case(s)?|cut(s)?`.
      SEE: three patterns, three colours.
- [ ] C2 Glance at Dispersion (one breath).
- [ ] C3 ⚠ Switch to **Table view** (one row per hit) → **Add to Workspace**.
      SEE: new matched block in the Data Viewer, gender column still aboard.
- [ ] C4 Trends on the matched block: group by term × gender · legend the COVID lines OFF · **switch line → bar** · weekly bin.
      SEE: male candidates ahead on `cut(s)`. Let it land; "suggestive, not definitive".

### D · Topic Modelling, two corpora (~7 min)

- [ ] D1 Select `tweets_F` + `tweets_M` → Topic Modelling · target **8** · seed **42** · Run.
- [ ] D2 While it runs (~60–90 s): point at sidebar **Tasks** progress, take one chat question (built-in buffer).
- [ ] D3 SEE: ~23 topics. **Re-aggregate to 16** → bubbles spread.
- [ ] D4 Colour story: point at one solid (gender-dominant) and one blended (shared) bubble; hover for top words.
- [ ] D5 Select 2–3 topics: **click each bubble** (multi-click only; no drag, no shift-range on bubbles) → **Add to Workspace**.
      SEE: per-gender child blocks appear.

### E · Stack → final Trends (~4 min)

- [ ] E1 Preprocessing → **Stack**: the per-gender topic blocks → one unified block.
- [ ] E2 Trends on it: weekly · group by topic (or gender × topic).
- [ ] E3 Finish on the **workspace graph**: "the graph is the method." (This is the recording's money shot; make sure the block names read cleanly.)

## 4 · Repurpose the lens · 1:15–1:25

- [ ] L1 Through the tool: back in Trends → legend filtering · **click** one point, then **click + Shift-click** a range → **Add to Workspace**. One breath: same move exists on Topic Modelling bubbles and Concordance dispersion markers.
- [ ] L2 Into the tool: select the `tweets` block → Preprocessing → **Expression** · context = **group by** · paste the two rows (also in the panel's copy bank):

      {"expression": {"op": "column", "name": "username"}}

      {"expression": {"op": "count", "operand": {"op": "column", "name": "username"}}, "alias": "tweet_count"}

- [ ] L3 Apply result as **Create new Data Block**. SEE: one row per candidate with `tweet_count`.
- [ ] L4 Trends on the new block: x-axis = `tweet_count`, bucketed · line → bar.
      SEE: a histogram: most candidates tweet a little, a few constantly. Landing line twice: "The tool didn't change; the data did."

## 5 · Wrap · 1:25–1:30

- [ ] Slides: landing (say it twice) → takeaways → lunch slide (walk both setup tasks aloud; afternoon not recorded; keyboards required).
- [ ] Flash the data-acknowledgements slide; it ships in the follow-up email.

**■ STOP THE RECORDING.** Confirm it has stopped before the install clinic starts.

- [ ] Install clinic (12:30, ~15 min, off the record): Windows SmartScreen "More info → Run anyway"; macOS first-open Open confirmation. Leave the lunch slide on screen; keep the Zoom meeting open.

---

## If a step breaks mid-recording

| Symptom | Do |
|---|---|
| Any phase-A–E build step misbehaves | Load the NEXT phase's backup archive (Data Loader → Workspace manager → Upload workspace → Load; re-select blocks/columns in the tool) and keep the narrative moving. The recording matters more than the liveness. |
| Topic Modelling stalls | Switch to the Tour workspace's finished Topic Modelling tab and narrate there; resume the Story at phase E from the backup. |
| You said something wrong | Correct it on camera in one sentence and move on. Don't restart the recording. |
