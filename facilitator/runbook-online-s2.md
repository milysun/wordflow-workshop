# Runbook — Online workshop Session 2 (90 min, hands-on, NOT recorded)

> **Rewritten 2026-08-27** to the current design: the jobs theme-coding task on the 226-tweet block, lowercase `promise` / `cuts` / `other` codebook with a v1 → v2 revision arc measured against a **human-verified reference annotation**, a **shared workshop key**, checkpoint workspace archives a/b/c (everyone loads **a** at the start), the responsible-AI slide before the tool, and the showcase segment. Wall-clock rows and every chat snippet: `facilitator/run-of-show-online.html`. Participant steps: `participant/hands-on-annotation-online.md` (its § numbers are used below).

**Coding text with GenAI: the Annotation tool · Friday 28 August 2026 · 2:00 – 3:30 pm AEST (12:00 – 1:30 pm AWST) · Zoom**

Deck: `slides/online-s2-annotation.html`, 9 slides, done by ~14:12, then live Wordflow. Helpers (co-hosts): Gordon, Georgie, Xinwei, Alex, Seb; breakout rooms Help-1/2/3 pre-created. Online pacing rule: after every "now you do it" step, wait a beat longer than feels natural and ask for a ✅ reaction rather than "everyone good?" silence.

**Setup before start** (full list in `pre-workshop-checklist-online.md`): recording **OFF** and auto-record disabled; checkpoint ZIPs a/b/c + `tweets_job_reference.csv` uploaded, links in the panel's fields; the shared key created at 12:35 with a spend cap, tested (model list loads, one Preview succeeds), pasted into the panel; room model `google/gemini-2.5-flash-lite`, fallback model in the panel; your own Wordflow on a clean workspace, multi-tab ON, cursor kit on; full MBP screen shared.

---

## 14:00 · Welcome back + the checks (slides 1–3, 5 min)

Say the recording status first: *"Unlike this morning, this session is **not** recorded: ask anything, break anything."* Welcome afternoon-only joiners; one-breath orientation (sidebar = tools, middle = the tool, right = your data and graph). Checks: app running **and updated** (accept the update notification; quit and reopen if none showed), sheet open (chat the link), that's it: model access comes from us in a few minutes. Introduce the helpers and the breakout plan (*"stuck: message a helper or raise a hand; they'll pull you into a room"*). Post the S2 welcome snippet.

## 14:05 · Framing: GenAI as a coder, and choosing a provider (slides 4–6, 7 min)

- **Slide 4, the idea (2 min):** the promise (thousands of texts against *your* categories, minutes, no training data) vs the pitfalls (confidently wrong; inconsistent on edge cases; biased where language is biased; drifts on vague prompts; never unsure unless allowed). Land: *"today isn't 'trust the AI', it's how to check it."*
- **Slide 5, the method (2 min):** treat it like a new coder: codebook → pilot → measure agreement against a reference (a human-verified annotation coded to the same codebook, or another coder) → revise → document. Slowly: *"a coder earns trust through agreement, human or machine."*
- **Slide 6, responsible AI (~2 min, unhurried, before anyone touches the tool):** say the sentence explicitly: *"today we use shared OpenRouter access so everyone can do the exercise; that is convenience, not an endorsement of OpenRouter or any commercial AI service for research."* Ethics approval decides providers and whether data may leave at all; privacy (local models keep everything on your machine); fit for the question; cost and accountability. Also why the key dies at 3:30.
- **Slide 7 (roadmap) 30 s, slide 8 (checkpoints) 45 s:** *"whenever you fall behind: chat link → Upload workspace → Load → re-select the block. Under a minute."* Then live Wordflow for the rest; keep the sheet's § numbers in your mouth.

## 14:12 · STEP 1 · Load Checkpoint a: the prepared Tweets block (sheet §1, 8 min)

Chat the checkpoint link (panel snippet). Everyone: **Data Loader → Workspace manager → Upload workspace → Checkpoint_a_Data.zip → Load.** SEE: a block called **`Tweets`**. Say what is inside and why: *"this morning's data preparation, done for you: tweets plus candidate metadata joined on username, `created_at` as a real date-time, `party` and `gender` as categories, `full_name` built from first and last name. Loading it is also the rescue move for later."* Fallback for anyone whose upload fails: sample import → tweets block (metadata optional today). ✅-check before moving on.

## 14:20 · Identify the theme, derive the block (sheet §2–3, 8 min)

Click `Tweets` → **Frequency**: the word cloud says **jobs**; that's the theme (*"normally you'd read and iterate here; we've pre-baked the codebook for time"*). Then **Preprocessing → Filter #1** on `Tweets`: `text` contains RegEx `^[Rr][Tt]`, **negate** → the originals block. **Filter #2** on that block: `text` contains `job` (plain contains, so "jobs" and "job-seeker" count). Say **226** out loud; ✅-check on 226. Anyone else's number: helper + breakout; Checkpoint b carries this block onward.

## 14:28 · Join the reference annotation (sheet §4, 4 min)

Chat the `tweets_job_reference.csv` link. Add it as a block (drag & drop or Upload files). **Preprocessing → Join**: the 226-row block **FIRST** (first pick = left), then the reference block, on `tweet_id`, left join. Say what the column is: *"`theme.reference`: all 226 tweets coded by a frontier model with the codebook you're about to see, then reviewed tweet-by-tweet by a human coder. Not gospel; a reference you can measure any coder against, human or AI."* ✅-check.

## 14:32 · Codebook v1 + feel the task (sheet §5–6, 7 min)

**Annotation** tool → add the joined block → Text Column `text` → **Annotation Column → Start new annotation → `theme.manual`**. **Codebook → Create New → Edit**: three codes, lowercase, paste the v1 descriptions from the copy bank (chat them too). Then **Manual → Start**: everyone codes ~5 tweets. *"Notice where you hesitate; the model will hesitate there too. In a team, each coder gets their own column exactly like this."* Close. Then **Start new annotation → `theme.ai`** so the AI has its own column.

## 14:39 · Connect the model: the danger zone, go slow (sheet §7, 8 min)

Post the key + model snippet. On screen, slowly: toggle **AI** → **Advanced settings** → **+ Add Provider → OpenRouter** → paste key → Tab → **Add Provider** → **Model**: paste the id. Say: *"the key is shared, temporary, and deleted at 3:30; on your own data you'd use your own key or a local model."* Helpers sweep chat; breakout for stragglers; **OpenRouter unreachable** snippet ready for anyone whose network blocks it (they code manually and watch). If the room model starts erroring, post the **switch to fallback model** snippet.

## 14:47 · The preview loop: v1 works, the reference makes it better (sheet §8, 15 min, protect these)

Paste the **v1 prompt**. **Preview** (page of 10; display-only). **Compare To → tick `theme.reference`** (and optionally `theme.manual`: *"how do YOU agree with the reference?"*). κ badge; **hover** for the confusion matrix. **Filter any difference**; read two or three disagreements aloud: the mixed "jobs, not cuts!" slogans and the "For Health. For Jobs." vote-lists will be the ones. Ask the room: model wrong, or codebook silent? Then **the revision**: Edit codebook → paste the **v2 descriptions**; paste the **v2 prompt**; **Update Preview**; watch κ move. Land it: *"codebook → pilot → agreement → revise. That loop is the method; everything else is buttons."* Mention that the reference itself came out of this loop: a human reviewer overrode the model on 22 of 226 tweets, mostly on exactly these two rules.

## 15:02 · Run All: trustworthy coding at scale (sheet §9, 8 min)

**Run All** on all 226 (~1 min; name **Reprocess all rows** vs **Fill missing only**). **Annotation Review** → **Compare To `theme.reference`** = the full-table κ, the headline number. Expected shape: roughly three-quarters `promise`, the rest split between `cuts` and `other`. Correct one row via the **Correction** column (`theme.ai.correction`) and point at **Use as example**: corrections feed back as worked examples. *"The AI didn't just do the job; it did the whole corpus, and you have the numbers to trust it."* Then one breath on afterlife: the coded column is ordinary data (filter on it, Trends by `party`, Export CSV).

## 15:10 · Showcase: same tool, cleverer questions (demo only, 12 min)

*"Watch, don't follow."* Three quick codebooks on the same 226 tweets, Preview only, all in the copy bank: **A** sentiment toward the LNP (aspect, not sentence); **B** mentions a place outside Queensland (the model knows geography); **C** more than two people mentioned (counting and names). Land: *"classic NLP problems, now one codebook away; the checking workflow you just did is what makes them trustworthy."* Take chat questions while previews run.

## 15:22 · Take it home + close on time (slide 9, 8 min)

Slide 9, top to bottom: the shared key is gone at 3:30, so real research means your own key or a **local model** (Add Provider → Custom: Ollama, LM Studio); **ethics approval** decides models and providers; keep the loop and document prompt, codebook, model, κ; **no AI required**: a team of human coders each in their own column, Compare To gives percent agreement, Cohen's κ or Krippendorff's α across multiple reference columns; Wordflow is under active development: **Feedback** button, one-click updates, cite via the sidebar's quote icon. Thank the helpers. Follow-up email tomorrow: Session 1 recording, materials, checkpoints. **Close at 15:30.**

## 15:30 · Immediately after

**Delete the OpenRouter key** (openrouter.ai → Keys → `workshop-2026-08-28`), then clear it from the panel field. Stop Zoom; save the chat log; export your S2 workspace archive as the reference copy.

---

## If things break

| Symptom | Do |
|---|---|
| Checkpoint a won't load for someone | Sample import → tweets block; they proceed without metadata (nothing in §2–9 needs it). |
| Someone's filter count isn't 226 | Helper + breakout; or load Checkpoint b (block + reference join + v1 codebook). |
| Provider add fails / model list empty | Re-paste the key (no trailing space); Tab before Add Provider; last resort: they watch the shared screen and use Checkpoint c later at home with their own key. |
| openrouter.ai unreachable on their network | Post the unreachable snippet: code manually, watch the AI steps, repeat later on another network or with a local model. |
| Room model returns 429s / errors | Post the fallback-model snippet; everyone swaps the model id, nothing else changes. Both models were tested Thursday. |
| Run All slow for the room | Keep talking through Annotation Review on your own screen; the numbers arrive as you speak. |
| Way behind at 15:02 | Skip the showcase (it's demo-only); Run All + take-home are the non-negotiables. |
| Someone pastes the key in public chat elsewhere | It has a spend cap and dies at 15:30; delete early if abused. |
