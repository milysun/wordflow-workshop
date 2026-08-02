# Runbook — Online workshop Session 1 (90 min, recorded)

**Wordflow: concepts, interface, and a real multi-tool workflow · Friday 28 August 2026 · 11:00 am – 12:30 pm AEST (9:00 – 10:30 am AWST) · Zoom**

Deck: `slides/online-s1-intro.html` (27 slides). This session is **all demo, no participant hands-on** — which means you control the clock completely. It is **recorded**: narrate for the future viewer as much as for the live room (say what you're clicking, read short bits of screen text aloud, don't rely on cursor-pointing alone).

**Setup before start** (full list in `pre-workshop-checklist-online.md`): Wordflow v0.7.x desktop with **multi-tab ON** (Settings → General → Enable multi-tab); the pre-built **Tour** workspace loaded (one tab per tool, analyses finished); the **Story** workspace data imported but the workflow NOT yet built (you build it live); Zoom screen share tested at a readable zoom level; deck on second monitor.

Timestamps below are minutes from start.

---

## 0:00 – 0:03 · Title + Acknowledgement (slides 1–2)

**START THE RECORDING before you speak.** Greet; let the join-trickle settle for ~a minute. Acknowledgement of Country — same care as in person.

## 0:03 – 0:06 · How today works (slide 3)

Say the recording sentence verbatim and early: *"This morning session is being recorded and shared afterwards — the afternoon hands-on will not be."* Then the contract for the morning: *"No hands-on before lunch — you don't need Wordflow installed to get everything from this session. Watch, and put questions in the chat; I'll take them at section breaks."* Preview the afternoon and its two lunch-time setup tasks (install + API key — both in the pre-workshop email). June-workshop alumni: *"you'll recognise the shape of this morning; v0.7 has a new interface, and this afternoon's tool is entirely new."*

## 0:06 – 0:10 · Who built this + why (slides 4–5)

Attribution chain (team → USyd → LDaCA → ARDC/NCRIS), then the why-slide. Say the north-star sentence slowly — it structures the whole day.

## 0:10 – 0:13 · Three ways to run it (slide 6)

Desktop (recommended, what the afternoon assumes), Binder (AAF only), Python. One breath each. *"Everything is at sih.tools/wordflow."*

## 0:13 – 0:22 · Interface tour (slides 7–8, mostly live)

Switch to the live app (Tour workspace). Walk the 7 things: **Views** sidebar (point at Annotation — *"this afternoon's star"*), tool interface, workspace graph, Data Viewer (*"not just a viewer — column and block management live here"*), quick-select, **Help**, **Feedback**. Then slide 8 — the data-block concept, and plant the tabs line: *"analyses run in tabs, tabs are saved with the workspace — remember that for this afternoon's checkpoints."*

**Chat-question break #1** (~1 min).

## 0:22 – 0:42 · Tool tour (slides 9–14, live from the Tour workspace)

~4 min per tool, one pre-built tab each. Don't build anything; interpret what's on screen.

1. **Frequency** — news corpus comparative. Cloud↔List toggle; **right-click a word** → it lands in the Stop words filter and vanishes. Flash a download icon (PNG/CSV).
2. **Concordance** — Honi Soit, 3-pattern regex, coloured; show Dispersion view.
3. **Trends** — QLD tweets; same period grouped three ways; legend-as-filter.
4. **Topic Modeling** — news corpus two-sided; bubble colour blending vs solid; hover for top words.
5. **Quotation** — Honi Soit; sort by speaker; say "English-only" honestly.

Timing check at 0:42: if late, trim Quotation to 2 min (it has the narrowest appeal).

**Chat-question break #2** (~1 min).

## 0:42 – 1:15 · The research story, live build (slides 15–21)

Land the question on slide 16, restate the watching contract (*"full speed, narrated, recorded — nobody needs to memorise clicks"*), then build in the **Story** workspace. Condensed from the June session-2 script; phase boundaries are your chat-question points.

- **A · Load, prepare, join (~5 min).** Data Loader → add `qldelection2020_candidate_tweets` + `candidate_info_gender`. Rename the long block via its **menu icon** → `tweets`. Show one column-menu delete; align `username` dtypes. **Preprocessing → Join** — select `tweets` FIRST (first pick = left table), left join on `username` → `tweets_with_gender`. Landing line: *"data prep is part of the analysis — the join is a research decision."*
- **B · Filter + Frequency ↔ Concordance loop (~7 min).** Filter `gender='F'` / `'M'`. Both → Frequency comparative (40 words, stopwords on). Do the loop honestly 2–3 times: click a word → Concordance → read → back → next word. Converge on `covid`, `case(s)`, `cut(s)`. *"The regex in the next phase grew straight out of this loop."*
- **C · Regex → Add to Workspace → Trends (~8 min).** Concordance Regex mode: `covid|case(s)?|cut(s)?`. Glance at Dispersion, then **Table view → Add to Workspace** (table = one row per hit; Dispersion aggregates per document — wrong shape for Trends). Trends on the matched block, group term × gender; legend the COVID lines off; **switch line → bar** — male candidates mention `cut(s)` more. Weekly bin sharpens it. Let the chart land before you name it; don't oversell (*"suggestive, not definitive — but real, from raw tweets in twenty minutes"*).
- **D · Topic Modeling on two corpora (~7 min).** Select both gender blocks → Topic Modeling, target 8, seed 42, Run. While it runs (~60–90 s): point at the sidebar **Tasks** progress, and take a chat question — this is your built-in buffer. ~23 topics → re-aggregate to 16, bubbles spread. Colour story: solid = gender-dominant, blended = shared. Select 2–3 topics → **Add to Workspace** → per-gender child blocks.
- **E · Stack → final Trends (~4 min).** **Preprocessing → Stack** the per-gender topic blocks → unified block. Trends: weekly, group by topic (or gender × topic). Landing: *"Four analysis tools, one workflow — and the workspace graph behind me is the whole method, captured as a picture."*

## 1:15 – 1:25 · Repurpose the lens (slides 22–23)

- **Through the tool (~4 min):** back in Trends — legend filtering, click / click + Shift-click a range → **Add to Workspace**. One breath: same move on Topic Modeling bubbles and Concordance dispersion markers.
- **Into the tool (~6 min), the quotable one:** Honi Soit block → **Preprocessing → Create** → word-count column. Trends: x-axis = word count (not the date), 100 intervals, line → bar. *"Trends is drawing a histogram. The tool didn't change — the data did."*

## 1:25 – 1:30 · Landing + takeaways + lunch (slides 24–26)

Slide 24 slowly — say it twice. Slide 25: three takeaways, land the name reveal on #3. Slide 26 (lunch): walk the two setup tasks once out loud; repeat that the afternoon is not recorded and keyboards are required; *"no key? come anyway."* Flash slide 27 (data acknowledgements) and note it ships in the follow-up email.

**STOP THE RECORDING.** Leave slide 26 on screen through lunch for late lookers. Keep the Zoom meeting open (same link for both sessions).

---

## If things break

| Symptom | Do |
|---|---|
| Topic Modeling run stalls mid-demo | Switch to the Tour workspace's finished Topic Modeling tab and narrate from there; the Story build resumes at Phase E via the pre-built backup workspace |
| Any live-build step misbehaves | Backup workspace archives for phases A–E are in the materials folder (see checklist) — load the next one and keep the narrative moving; the recording matters more than the liveness |
| Screen share lags / font too small | Zoom → share the app window only (not the desktop); bump the app zoom (Cmd/Ctrl +) — check readability in the Zoom preview, not on your monitor |
| Way behind at 0:42 | The tour is done — protect the research story. Cut slide-22 (repurpose-through) and keep the histogram; takeaways can compress to 1 min |
| Way behind at 1:15 | Skip straight to the histogram demo (the quotable one), then slides 24–26. Never skip slide 26 — the afternoon depends on it |
