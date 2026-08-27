# Runbook — Online workshop Session 2 (90 min, hands-on, NOT recorded)

> **⚠ Superseded (2026-08-20):** Session 2 was redesigned around the jobs theme-coding task (226-tweet block via two filters, lowercase promise/cuts/other codebook, v1→v2 revision arc, shared session key, showcase segment). The live source of truth is `facilitator/run-of-show-online.html` plus `participant/hands-on-annotation-online.md`; this file awaits the review-pass rewrite. The break-glass table at the bottom remains largely valid.

**Coding text with GenAI: the Annotation tool · Friday 28 August 2026 · 2:00 – 3:30 pm AEST (12:00 – 1:30 pm AWST) · Zoom**

Deck: `slides/online-s2-annotation.html` (7 slides — done by minute ~15, then live). Participant sheet: `participant/hands-on-annotation-online.md` (drop the link in chat at the start; it mirrors every step). This is the CAITG 45-minute session grown to 90: same spine, but you own the theory framing (no preceding speaker), participants bring **their own API keys**, and recovery runs on **checkpoint workspace archives** instead of a facilitator sprint.

**Setup before start** (full list in `pre-workshop-checklist-online.md`): recording **OFF** — verify, and disable auto-record for this meeting; checkpoint files uploaded and their links ready to paste; your own OpenRouter key working; a clean workspace on your machine; helpers briefed on the checkpoint drill ⟨if any⟩.

Online pacing rule: after every "now you do it" step, give a beat longer than feels natural, and ask for a ✅ reaction in Zoom rather than "everyone good?" silence.

---

## 0:00 – 0:05 · Welcome back + the three checks (slides 1–2)

Say the recording status out loud first: *"Unlike this morning, this session is **not** being recorded — ask anything, break anything."* Welcome afternoon-only joiners explicitly; one-breath orientation for them (sidebar = tools, middle = the tool, right = your data + graph). Run the three checks (app running / key at hand / sheet open — link in chat). Anyone without app or key: follow the shared screen, everything up to the AI runs still works on their machine later.

## 0:05 – 0:15 · Framing: GenAI as a coder (slides 3–4)

Your condensed theory segment — the winter school had a whole talk here; you have ten minutes, and they're load-bearing.

- **Slide 3 (~5 min):** the promise (thousands of texts against *your* categories, minutes, no training data) vs the pitfalls (confidently wrong; inconsistent on edge cases; biased where language is biased; drifts on vague prompts; never unsure unless you allow it). Land: *"today is not 'trust the AI' — it's how to check it."*
- **Slide 4 (~5 min):** the method — treat it like a new coder: codebook → pilot → agreement (κ) → revise → document. Say slowly: *"a coder earns trust through agreement — human or machine."* This loop is the agenda; point at it.

Show slide 5 (roadmap) for 30 seconds, slide 6 (checkpoints) for 60 — *"if you fall behind at any point: chat link, Upload workspace, Load, re-select the block. Under a minute, and you're back with us."* Then live Wordflow for the rest.

## 0:15 – 0:25 · Workspace + data (live, everyone follows)

1. **Data Loader → Create workspace**, any name.
2. **Import sample data** → tick **ADO — Queensland Election Tweets** → **Import selected**. (Flat list in v0.7 — no tabs in this dialog.) Wait for the **"✓ Imported"** chip.
3. Add **`candidate_info_gender`** as a data block; click it — walk the columns in the Data Viewer: `party, electorate, first_name, last_name, username`, and human-coded `gender`. *"One row per candidate. The gender column is our reference annotation — coded by people. Today the AI competes with them."*
4. Mention own-data upload for later (drag & drop, CSV/plain text; **Excel and zip import are broken in 0.7.x — export to CSV first** ⟨re-verify against the shipping version before the day⟩).

**✅-check + Checkpoint 0** (`Checkpoint_0_Data.zip`) into chat: *"anyone stuck on import — this file is the workspace you just saw me build."*

## 0:25 – 0:40 · Annotation column + codebook + manual coding (live, everyone follows)

1. Sidebar → **Annotation**. Add `candidate_info_gender` under **Selected Data Blocks**; **Text Column = `first_name`** — *"that's all the model gets to read."*
2. **Annotation Column → Start new annotation** → name it **`gender.ai`** → **Create**. (The `.ai` suffix is our naming habit, not the tool's.)
3. **Codebook → Create New**, then **Edit**: add **M / F / U** with one-sentence descriptions. Teaching point, verbatim from CAITG (it worked): *"The description field is your codebook definition — the model reads it word for word. Write it like instructions to a new RA. Vague codebook, vague coder — human or machine."* Give the room 3 minutes to write their own descriptions; read one or two from chat volunteers.
4. **Manual mode → Start**: code 3–4 rows on screen; ask everyone to do ~5. Point out the multi-coder pattern (one column per coder, continue via the Annotation Column dropdown). **Close**.

**✅-check + Checkpoint 1** (`Checkpoint_1_Codebook.zip`).

## 0:40 – 0:50 · Provider + model (live — the online danger zone)

The step that loses people online: no helpers at shoulders, so go slow and use chat aggressively.

1. Toggle **AI** → expand **Advanced settings** (chevron).
2. **+ Add Provider** → **OpenRouter** → paste **your own key** → Tab to accept the name → **Add Provider**. Remind: keys are write-only here — *"Wordflow never shows your key again after you save it."*
3. **Model**: search the live list. Suggest for the room: a `:free` Gemma model (search "gemma", pick one tagged `:free` — zero cost) or `google/gemini-2.5-flash-lite` if they added credit. Any provider's key works (OpenAI / Anthropic / Google via their own provider entries).
4. Troubleshoot via chat: model list won't load → free-type the exact model id; key rejected → check for clipped characters when pasting.

This is a genuine 10 minutes — don't compress it. Anyone whose key won't cooperate: *"watch the next section on my screen; Preview needs nothing saved, you can wire your key up after the session with the sheet."*

## 0:50 – 1:10 · The preview loop (live — the heart, protect these 20 minutes)

1. **Prompt** field: Tab to take the default, then edit — add context (Australian election candidates' first names) and an escape hatch (unsure → `U`).
2. **Preview** — codes the visible page (10 rows; **Rows per page** up to 100 for a steadier sample). Predictions are display-only: *"nothing has touched your data — this is the pilot study from slide 4."*
3. **Compare To** → tick **`gender`** → **Cohen's Kappa** (default; Percent Agreement and Krippendorff's Alpha are one click away). Badge appears → **hover it → the confusion matrix.** Tie back: *"step 3 of the loop — agreement, measured, in one hover."*
4. **Filter any difference** (filter icon by the column header) → read 2–3 disagreements aloud; ask the room in chat: model wrong, or human coding debatable? (`U` boundary cases will surface — that's the point.)
5. Revise prompt or codebook description → **Update Preview** → watch κ move. One full loop on screen, then **5 quiet minutes for the room to loop on their own** — this is the skill being trained. Collect κ values in chat; celebrate the spread (*"different codebooks, different coders — same as a human team"*).

**✅-check + Checkpoint 2** (`Checkpoint_2_Preview.zip` — includes a working prompt + codebook; after loading, re-select block/column if selectors are empty).

## 1:10 – 1:20 · Run All + review (live)

1. **Run All**. While it runs: **Advanced settings → Run All processing** — **Reprocess all rows** (default) vs **Fill missing only** (*"keeps your manual codes, fills the gaps"*); Temperature 0 = deterministic. Progress in the banner + sidebar **Tasks**; **Stop** exists.
2. **Annotation Review**: Compare To / matrix / filters, now full-table. Set a **Correction** column (accepts the suggested `gender.ai.correction`), correct one row, mention **Use as example** (corrections become few-shot examples).
3. Close the loop: the coded column is ordinary data — filter on it, chart it in Trends (morning attendees will feel the click), export CSV from the **Export** view.

## 1:20 – 1:30 · Your own data + take it home (slide 7)

~5 min free play or guided restart: own CSV + a harder coding problem (stance, topic, policy claims) — or improve κ on the names task, or code the tweets block's `text` column for topic. Then slide 7, plainly, in order: own key was the real-research setup all along; **local models** via Add Provider → Custom (Ollama, LM Studio); **ethics approval decides which models/providers — check before real data**; keep the loop and document it (prompt, codebook, model, κ → methods section); Feedback button + citation. Point to the follow-up email (Session 1 recording, materials, checkpoints). Thank the room; end on time.

---

## If things break

| Symptom | Do |
|---|---|
| Someone lost mid-exercise | Checkpoint link + slide-6 drill: Upload workspace → Load → re-select block/column. Do the first one together on screen so the room sees it once |
| Participant's model list won't load | Free-type the exact model id (the field accepts typed names); check the key pasted whole |
| Key rejected / no key | They follow on your screen; the sheet works standalone afterwards. Fallback shared key in chat only at your discretion — never on a public URL |
| Provider error strip in Preview | **Retry** button; if it's a 429, switch them to a `:free` model |
| Run All "completed with N failed batches" | Blank rows remain — rerun with **Fill missing only** |
| Zoom crashes / you drop out | Helpers hold the room ⟨name a backup host⟩; on rejoin, resume from your last checkpoint file — you eat your own dog food |
| Way behind at 1:10 | Skip Run All — the preview loop already carried the payload. Never skip the ethics close |
