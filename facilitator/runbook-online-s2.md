# Runbook — Online workshop Session 2 (90 min, hands-on, NOT recorded)

> **Rewritten 2026-08-27** to the current design: the jobs theme-coding task on the 226-tweet block, Title-case `Promise` / `Cuts` / `Other` codebook, a preview → compare → correct loop and an examples run, all measured against a **human-verified reference annotation**, a **shared workshop key**, checkpoint workspace archives a/b/c/d as rescues (**a** = the Tweets block everyone builds first; **d** = the v2 codebook block). **Prompts are not saved in checkpoints or codebook blocks**: after any load, participants must paste the v1/v2 prompt again; brief the helpers, the responsible-AI slide before the tool, and the showcase segment. Wall-clock rows and every chat snippet: `facilitator/run-of-show-online.html`. Participant steps: `participant/hands-on-annotation-online.md` (its § numbers are used below).

**Coding text with GenAI: the Annotation tool · Friday 28 August 2026 · 2:00 – 3:30 pm AEST (12:00 – 1:30 pm AWST) · Zoom**

Deck: `slides/online-s2-annotation.html`, 9 slides, done by ~14:12, then live Wordflow. Helpers (co-hosts): Gordon, Georgie, Xinwei, Alex, Seb; breakout rooms Help-1/2/3 pre-created. Online pacing rule: after every "now you do it" step, wait a beat longer than feels natural and ask for a ✅ reaction rather than "everyone good?" silence.

**Setup before start** (full list in `pre-workshop-checklist-online.md`): recording **OFF** and auto-record disabled; checkpoint ZIPs a/b/c + `tweets_job_reference.csv` uploaded, links in the panel's fields; the shared key created at 12:35 with a spend cap, tested (model list loads, one Preview succeeds), pasted into the panel; room model `google/gemini-2.5-flash-lite`, fallback model in the panel; your own Wordflow on a clean workspace, multi-tab ON, cursor kit on; full MBP screen shared.

---

## 14:00 · Welcome back + the checks (slides 1–3, 5 min)

Say the recording status first: *"Unlike this morning, this session is **not** recorded: ask anything, break anything."* Welcome afternoon-only joiners; one-breath orientation (sidebar = tools, middle = the tool, right = your data and graph). Checks: app running **and updated** (accept the update notification; quit and reopen if none showed), sheet open (chat the link), that's it: model access comes from us in a few minutes. Introduce the helpers and the breakout plan (*"stuck: message a helper or raise a hand; they'll pull you into a room"*). Post the S2 welcome snippet.

## 14:05 · Framing: GenAI as a coder, and choosing a provider (slides 4–6, 7 min)

- **Slide 4, the idea (2 min):** the promise (thousands of texts against *your* categories, minutes, no training data) vs the pitfalls (confidently wrong; inconsistent on edge cases; biased where language is biased; drifts on vague prompts; never unsure unless allowed). Land: *"today isn't 'trust the AI', it's how to check it."*
- **Slide 5, the method (2 min):** treat it like a new coder: codebook → pilot → measure agreement against a reference (a human-verified annotation coded to the same codebook, or another coder) → revise → document. Slowly: *"a coder earns trust through agreement, human or machine."*
- **Slide 6, responsible AI (~2 min, unhurried, before anyone touches the tool; a reminder, not a course):** say the sentence explicitly: *"today we use shared OpenRouter access so everyone can do the exercise; that is convenience, not an endorsement of OpenRouter or any commercial AI service for research."* Four cards, one breath each: ethics approval plus institutional, journal and funder rules decide providers and whether data may leave at all; local models keep data on your machine but don't make a model fair (it can still key on a name or an ethnicity), so de-identify regardless and consider synthetic data while developing; fit includes methodology (reflexive, interpretive analysis has no model that fits); and you remain accountable for everything the AI did on your behalf. Verbal aside only, not on the slide (over half the room is external): USyd people can go deeper in SIH's GenAI training series. Also why the key dies at 3:30.
- **Slide 7 (roadmap) 30 s, slide 8 (checkpoints) 45 s:** *"whenever you fall behind: chat link → Upload workspace → Load → re-select the block. Under a minute."* Then live Wordflow for the rest; keep the sheet's § numbers in your mouth.

## 14:12 · STEP 1 · Build the Tweets block from scratch (sheet §1, 9 min, brisk)

This is the morning's data prep replayed at speed: continuity for the morning people, and the afternoon-only joiners need to have done it once rather than inherit a mystery ZIP. Narrate each move in one line; don't teach.

1. **Data Loader → Create workspace.**
2. **Import sample data → ADO — Queensland Election Tweets → Import selected**; add **both** blocks: the candidate tweets and the candidate info (metadata).
3. Column types via the column menu: tweets `created_at` → date-time; candidate `party`, `gender` → category. (*"Types decide what tools can do with a column: dates give you Trends, categories give you groups."*)
4. **Preprocessing → Create** on the candidate block: `full_name` = first_name + " " + last_name, Apply as **Update**.
5. **Preprocessing → Join**: tweets **FIRST** (left), candidate block second, on `username`, left join → rename the result **`Tweets`**.

Rescue, said out loud and posted in chat: *"lost anywhere here? Load Checkpoint a: it is exactly this result."* Helpers pull stragglers into a room while the rest continue. ✅-check on a block called `Tweets`.

## 14:21 · Explore, then derive the block (sheet §2–3, 7 min)

Click `Tweets` → **Frequency**: the word cloud says **jobs**, with **cuts** close behind: *"the campaign's language about jobs is our theme; normally you'd read and iterate here, we've pre-baked the codebook for time."* Optional 20-second click on "jobs" into Concordance. Then **Preprocessing → Filter #1** on `Tweets`: `text` contains RegEx `^[Rr][Tt]`, **negate** → the originals block. **Filter #2** on that block: `text` contains `job` (plain contains, so "jobs" and "job-seeker" count). Say **226** out loud; ✅-check on 226. Anyone else's number: helper + breakout; Checkpoint b (`Jobs_with_ref`, after the next step) catches them up.

## 14:28 · Join the reference annotation (sheet §4, 4 min)

Chat the `tweets_job_reference.csv` link. Add it as a block (drag & drop or Upload files). **Preprocessing → Join**: the 226-row block **FIRST** (first pick = left), then the reference block, on `tweet_id`, left join; rename the result **`Jobs_with_ref`** (Checkpoint b is exactly this). Say what the column is: *"`theme.reference`: all 226 tweets coded by a frontier model with the codebook you're about to see, then reviewed tweet-by-tweet by a human coder. Not gospel; a reference you can measure any coder against, human or AI."* ✅-check.

## 14:32 · Codebook v1 (sheet §5, 4 min)

**Annotation** tool → add `Jobs_with_ref` → Text Column `text` → **Annotation Column → Start new annotation → `job.manual`**. **Codebook → Create New → Edit**: three codes, Title-case exactly as written, paste the v1 descriptions from the copy bank (chat them too). *"The descriptions are what the model will read; write them as instructions to a new research assistant."*

## 14:36 · Be the coder first: a page by hand, then κ against the reference (sheet §6, 6 min)

**Manual → Start**: everyone codes the **first page** (10 tweets) into `job.manual`. *"Notice where you hesitate; the model will hesitate there too."* Then the reveal: **Compare To → tick `theme.reference`** → κ badge for the coded rows, hover for the confusion matrix. Read one disagreement aloud and ask: who's right? Land: *"often nobody: the codebook was silent. That's what we fix in a few minutes. And this is exactly how a team measures coder against coder: one column each, Compare To."* Close. Say the catch-up line: *"Checkpoint c is exactly this state: v1 codebook plus a hand-coded first and last page; if you missed anything so far, load it now, before the AI."* The AI column itself is created in the next step.

## 14:42 · Connect the model: the danger zone, go slow (sheet §7, 8 min)

Post the key + model snippet. **Start new annotation → `job.AI`**. Toggle **AI** → **Advanced settings**, and name what's in there: *"example, prompt, and inference settings: the prompt the model reads, how many of your examples it may see per class, and whether Run All reprocesses or only fills gaps."* **+ Add Provider → OpenRouter** → paste key → Tab → **Add Provider** → **Model**: `google/gemini-2.5-flash-lite`. Frame the model honestly: *"an older, small, cheap model, chosen on purpose. Don't expect perfection; starting cheap is how you find a task's boundaries before paying for a bigger model."* Paste the **v1 prompt**. Say: *"the key is shared, temporary, and deleted at 3:30."* Helpers sweep chat; breakout for stragglers; **unreachable** and **fallback-model** snippets ready.

## 14:50 · Preview, compare, correct (sheet §8, 10 min, protect these)

**Preview** page 1; page forward through two or three pages to show the feel; **come back to page 1**, where everyone's manual codes live. **Compare To → tick `job.manual` and `theme.reference`**: two κ badges. Explain κ in one breath (*"agreement corrected for chance: 1 perfect, 0 what guessing gets"*), hover for the **confusion matrix** (*"which codes get confused with which"*). **Filter any difference** (the mask): only the disagreements remain; read two aloud and ask who's right. Then **Correction**: *"you could make a new column; in this scenario reuse `job.manual`: a correction is a human coding, and one column of human decisions is what we'll feed back as examples in a minute."* Correct a couple of rows.

## 15:00 · Run All: coding at scale (sheet §9, 5 min)

**Run All** into `job.AI` (~1 min; name **Reprocess all rows** vs **Fill missing only**). **Annotation Review → Compare To `theme.reference`** = the full-table κ. Rehearsal: **0.843**; say the day's number, whatever it is, and that variation is normal. *"The AI didn't just do the job; it did the whole corpus, and you have the numbers to judge it."*

## 15:05 · Feed examples back, measure again (sheet §10, 8 min)

The second lever, with the first result kept intact: **Start new annotation → `job.AI.example`** (*"never overwrite a result you may want to compare against"*). In **Advanced settings**, set **`job.manual`** as the examples (**Use as example**; mention **Max examples per class**). **Run All** into the new column → **Compare To**: tick `theme.reference` **and `job.AI`**, so the two runs sit side by side. Rehearsal: **0.728**, *lower* than 0.843. While it's up, show the review-table tools once: **Filter any difference** between `job.AI.example` and `job.AI` (*"exactly where the examples changed the model's mind"*), the **display option** that shows the compared columns' values in the table, and the **exists / does not exist** filter (*"rows with or without a value: how you find the rows a model skipped or mis-coded, and what Fill missing only would target"*). Land it without drama: *"examples don't guarantee improvement; they can pull the model toward your particular hesitations. That is why every change gets measured, never assumed."* Hover both confusion matrices to show where the behaviour moved. (If the day's numbers go the other way, the lesson is the same: measure.)

## 15:13 · Revise the codebook: v2 (sheet §11, 6 min)

The third lever. Chat the Checkpoint d link first (*"if you're behind, load d: it holds the v2 codebook block"*). On screen: block menu → **Clone** the v1 codebook block → rename **`Job_with_ref_codebook_v2`** → edit the descriptions to v2 (or simply select the block from Checkpoint d). Annotation tool: **Codebook → `Job_with_ref_codebook_v2`**, **Start new annotation → `job.AI_v2`**, **paste the v2 prompt** (say it: *"the prompt lives only in this field; it is not in the codebook and not in any checkpoint"*). **Run All → Compare To `theme.reference` + `job.AI`**. Rehearsal: the *first* v2 draft scored **0.66** (vs 0.843 plain, 0.728 examples) because it decided vote-lists and 'jobs, not cuts' slogans the opposite way to the reference; the aligned v2 (Thu night rewrite) scored **0.805** on flash-lite, and **0.867** on GLM 5.3 flash (whose v1 was 0.809; GLM is slower, so the room stays on flash-lite). Whatever the day's number, land the three-part lesson: *"a revised codebook must make the same decisions as your reference, or better rule-following lowers κ (0.66); codebook and model interact: the sharper v2 helped the stronger model (0.81 → 0.87) and cost the small one a little (0.84 → 0.81), because longer instructions ask more of a small model; and models differ: the same misaligned v2 scored 0.53 on DeepSeek v4 flash, 0.69 on GLM 5.3 flash. You only know any of this by measuring."* Then: *"three measured runs: plain, examples, revised codebook. Now you can say which lever did what, instead of guessing."*

## 15:19 · Showcase: same tool, cleverer questions (demo only, 3 min; first cut if late)

One codebook, not three: **A** sentiment toward the LNP (aspect, not sentence), Preview only, from the copy bank. Name **B** (place outside Queensland) and **C** (more than two people) in one breath; they're in the sheet's appendix. Land: *"classic NLP problems, now one codebook away; the checking workflow you just did is what makes them trustworthy."*

## 15:22 · Take it home + close on time (slide 9, 8 min)

Slide 9, top to bottom: the shared key is gone at 3:30, so real research means your own key or a **local model** (Add Provider → Custom: Ollama, LM Studio); **ethics approval** decides models and providers; keep the loop and document prompt, codebook, model, κ; **no AI required**: a team of human coders each in their own column, Compare To gives percent agreement, Cohen's κ or Krippendorff's α across multiple reference columns; Wordflow is under active development: **Feedback** button, one-click updates, cite via the sidebar's quote icon. Thank the helpers. Follow-up email tomorrow: Session 1 recording, materials, checkpoints. **Close at 15:30.**

## 15:30 · Immediately after

**Delete the OpenRouter key** (openrouter.ai → Keys → `workshop-2026-08-28`), then clear it from the panel field. Stop Zoom; save the chat log; export your S2 workspace archive as the reference copy.

---

## If things break

| Symptom | Do |
|---|---|
| Someone can't complete the §1 build | Load Checkpoint a (exactly the §1 result). If even that fails: sample import → tweets block alone; nothing in §2–9 needs the metadata. |
| Someone's filter count isn't 226 | Helper + breakout; or load Checkpoint b (`Jobs_with_ref`: the 226 rows with the reference joined). |
| Anyone behind at 14:42, before the AI | Load Checkpoint c (v1 codebook + hand-coded first and last pages); they continue with the model like everyone else. |
| Provider add fails / model list empty | Re-paste the key (no trailing space); Tab before Add Provider; last resort: they watch the shared screen and use Checkpoint c later at home with their own key. |
| openrouter.ai unreachable on their network | Post the unreachable snippet: code manually, watch the AI steps, repeat later on another network or with a local model. |
| Room model returns 429s / errors | Post the fallback-model snippet; everyone swaps the model id, nothing else changes. Both models were tested Thursday. |
| Run All slow for the room | Keep talking through Annotation Review on your own screen; the numbers arrive as you speak. |
| Way behind at 15:00 | Cut in order: showcase → v2 run (point at Checkpoint d + appendix for home) → examples run. Run All + take-home are the non-negotiables. |
| Someone loads a checkpoint and the AI does nothing / errors | The prompt is empty: prompts are not in the codebook block nor in checkpoints. Paste v1 or v2 from the chat. Helpers: this is the #1 thing to check after any checkpoint load. |
| Someone pastes the key in public chat elsewhere | It has a spend cap and dies at 15:30; delete early if abused. |
