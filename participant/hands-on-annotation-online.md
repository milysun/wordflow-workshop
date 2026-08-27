# Hands-on: Coding text with GenAI in Wordflow

**LDaCA Online Workshop · Session 2 · 28 August 2026 · 2:00 – 3:30 pm AEST (12:00 – 1:30 pm AWST)**

You'll use Wordflow's **Annotation** tool (new in v0.7) to code a real dataset with an AI model, and, more importantly, to *check* the AI's coding the way you'd check a human coder's: agreement scores, a confusion matrix, and targeted revisions until the numbers hold up.

This sheet mirrors the live session step by step, and works as a standalone tutorial afterwards. Fall behind at any point? Jump to **§12 Checkpoints**; you can rejoin in under a minute.

---

## 0 · Before we start: three things

1. **Wordflow running and updated**: the desktop app from **`sih.tools/wordflow`** (Mac/Windows); if it shows an update notification, accept it (one click). *Windows may show a security warning at install: click **More info**, then **Run anyway**.*
2. **This sheet open** next to Wordflow (a second screen helps).
3. **Model access is provided**: a shared workshop key will be posted in the Zoom chat when we reach §6 (it is deleted at 3:30 pm). Your own OpenRouter / OpenAI / Anthropic / Google key works too, if you prefer.

## 1 · Build the Tweets block (brief; this is the morning's data prep)

1. In the **Data Loader**, click **Create workspace** and give it a name.
2. Click **Import sample data**. In the dialog, tick **ADO — Queensland Election Tweets** → **Import selected**. Wait for the **✓ Imported** chip, then add **both** files as data blocks: the **candidate tweets** (one row per tweet, text in `text`) and the **candidate info** (one row per candidate: `party`, `gender`, `first_name`, `last_name`, `username`).
3. Fix the column types (open the column's menu in the Data view → change type): tweets `created_at` → **date-time**; candidate `party` and `gender` → **category**.
4. **Preprocessing → Create** on the candidate block: new column `full_name` = `first_name` + `" "` + `last_name` (Apply result as **Update**).
5. **Preprocessing → Join**: select the tweets block **FIRST** (first pick = left table), then the candidate block; join on **`username`** (left join). Rename the result **`Tweets`** (block menu → Rename).

*Lost anywhere in this step? Load **Checkpoint a** (§10): it contains exactly this result, and nothing more.*

## 2 · Explore first: what is this campaign about?

Before defining any codes, let the data speak.

1. Click the `Tweets` block → open **Frequency**. In the word cloud, **jobs** dominates, and **cuts** is not far behind: the campaign's language about jobs is our theme.
2. Optional: click "jobs" in the cloud to jump into **Concordance** and read a few tweets in context. Notice the different ways the word is used (creating jobs, cutting jobs, "did a great job"); that observation becomes our codebook in §5.

## 3 · Derive the coding dataset (everyone lands on the same 226 rows)

Two filter steps in **Preprocessing → Filter**, each creating a new block:

1. **Drop retweets**: on the `Tweets` block, filter where `text` contains RegEx **`^[Rr][Tt]`**, and tick **negate** (keep everything that does NOT start with rt). This gives the original-tweets block.
2. **Keep the job tweets**: on that new block, filter where `text` contains **`job`** (plain contains, not whole-word, so "jobs" and "job-seeker" count).

Your final block should have **226 rows**. If your number differs, put it in the chat and a helper will jump in (or grab Checkpoint b, §12).

## 4 · Join the reference annotation

The workshop provides **a human-verified reference annotation** for all 226 tweets: coded by a frontier AI model with the same codebook you're about to use, then reviewed tweet-by-tweet by a human coder. Joining them in now means you can measure any coder (human or AI) against them later.

1. Download `tweets_job_reference.csv` from the Zoom chat and add it as a data block (drag & drop, or **Upload files**). It has two columns: `tweet_id` and `theme.reference`.
2. **Preprocessing → Join**: select your 226-row block FIRST (first pick = left table), then the reference block. Join on **`tweet_id`** (left join).
3. The joined block (still 226 rows) now carries `theme.reference` alongside the text. Rename it **`Jobs_with_ref`** (block menu → Rename) and work in this block from here on.

## 5 · Build the codebook (v1: plain and simple)

The codebook is itself a small data block: one row per code, with a description. The descriptions are what the model actually reads.

1. Open the **Annotation** tool (left sidebar, under **Views**). Under **Selected Data Blocks**, add **`Jobs_with_ref`**. Set **Text Column** to **`text`**.
2. In the **Annotation Column** dropdown, choose **Start new annotation** → name it **`job.manual`** → **Create**.
3. In the **Codebook** card, click **Create New**, then **Edit** next to **Codes**. **Add code** three times and type exactly (Title-case, exactly as written: codes must match the reference file letter for letter):

   | Code | Description |
   |---|---|
   | `Promise` | The tweet's main message is jobs being created, protected or supported: announcements, funding, infrastructure or training plans, or claims of jobs already delivered. |
   | `Cuts` | The tweet's main message is jobs being cut, lost or at risk: past sackings, warnings that a party will cut jobs, or attacks on an opponent's cuts. |
   | `Other` | The word job is used another way: praise like 'did a great job', commentary about job statistics, or anything that fits neither class above. |

4. **Save.**

## 6 · Be the coder first: annotate a page by hand, then measure yourself

Before the AI touches anything, code the first page yourself. It changes how you read everything after, and it shows you the measuring tools on your own work first.

1. Leave the **Manual / AI** toggle on **Manual** and click **Start**.
2. Code the **first page** (10 tweets) into `job.manual` via each row's **Select class** dropdown. Notice the ones that make you hesitate; the AI will hesitate there too.
3. Now measure yourself: click **Compare To** and tick **`theme.reference`**. A **Cohen's Kappa** badge appears for the rows you coded; **hover it** for the confusion matrix. Where you and the reference disagree, who is right? Often the honest answer is "the codebook didn't say", which is exactly what §8 fixes.
4. Click **Close**. In a real team, each coder gets their own column like this (picked under **Annotation Column**), and the same Compare To measures coder against coder.

## 7 · Connect the AI

1. Create the AI's own column: **Annotation Column → Start new annotation** → **`job.AI`** → **Create**. (Your `job.manual` stays as it is.)
2. Flip the toggle to **AI** and expand **Advanced settings** (the chevron): this panel holds the **example, prompt, and inference settings**: the prompt, how many examples per class the model may see, and how Run All treats existing rows.
3. **+ Add Provider** → **OpenRouter** → paste the **shared key from the Zoom chat** → press Tab to accept the name → **Add Provider**.
4. **Model**: paste the model id from the chat message (`google/gemini-2.5-flash-lite`). This is an older, small, cheap model, chosen on purpose: don't expect perfection. Starting with a cheap model is good practice: find the task's boundaries first, and pay for a bigger model only if the numbers say you need to.
5. **Prompt** (v1, simple): paste into the Prompt field:

   > You are coding tweets posted by candidates during the 2020 Queensland state election. Read each tweet and assign the code that best describes how it uses the word job or jobs.

## 8 · Preview, compare, correct

1. Click **Preview**. The model codes the visible page (10 rows; **Rows per page** changes the sample). Predictions are display-only; nothing is written to your data yet. Page forward through two or three pages to get a feel, then **come back to page 1**, where your own codes live.
2. Click **Compare To** and tick **`job.manual`** and **`theme.reference`**. A **Cohen's Kappa** badge appears for each: how far the AI agrees with *you*, and with the reference. κ is agreement corrected for chance: 1 is perfect, 0 is what guessing would get. **Hover** a badge for its **confusion matrix**: which codes get confused with which.
3. Click **Filter any difference** (the mask icon by the column header) to see only the rows where the AI disagrees with your choice. Read them. Is the model wrong, were you, or was the codebook silent?
4. **Correction**: choose a column to hold your corrections. You could create a new one (`job.AI.correction` is suggested), but in this exercise **reuse `job.manual`**: a correction is a human coding, and keeping every human decision in one column makes it reusable as examples in §10. Correct a few rows.

## 9 · Run All: coding at scale

1. Click **Run All**: all 226 tweets, about a minute. (In **Advanced settings → Run All processing**: **Reprocess all rows** replaces the column; **Fill missing only** keeps existing labels.)
2. The **Annotation Review** table opens: **Compare To `theme.reference`** now gives a full-table κ over all 226 rows: your headline number. In rehearsal this model scored about **κ 0.84** against the reference; yours will differ a little, and that is normal for these models.
3. Your coded column is ordinary data now: filter on it, chart `job.AI` by `party` in **Trends**, or export CSV from the **Export** view.

## 10 · Feed your own codes back as examples, and measure again

Few-shot examples are the other lever besides the codebook. Try it, but keep the first result:

1. **Do not overwrite `job.AI`.** Create a fresh column: **Annotation Column → Start new annotation** → **`job.AI.example`**.
2. In **Advanced settings**, set your **`job.manual`** codes as the examples (the **Use as example** control; **Max examples per class** limits how many the model sees).
3. **Run All** again into the new column, then **Compare To**: tick **`theme.reference`** and **`job.AI`**, so the two runs sit side by side.
4. Three review-table tools worth knowing here: **Filter any difference** between `job.AI.example` and `job.AI` shows exactly where the examples changed the model's mind; the **display option** shows the compared columns' values next to the prediction; and the **exists / does not exist** filter selects rows with or without a value in a column, which is how you find rows a model skipped or gave an invalid code, and what **Fill missing only** would target.
5. Compare the two κ values. In rehearsal the examples run scored **κ 0.73**, *lower* than the plain run's 0.84. Examples don't guarantee improvement: they can pull the model toward your particular hesitations. This is why you measure every change instead of assuming it helped. Hover both confusion matrices to see where the behaviour moved.

## 11 · Revise the codebook: v2

The third lever is the codebook itself. The §8 disagreements point at cases v1 was silent about: mixed "jobs, not cuts!" slogans, campaign vote-lists ("For Health. For Jobs."), hashtag-only mentions, and "cutting prices" that is not cutting jobs. One rule of the game: the revised codebook must make the *same* decisions on those cases as the reference annotation does, otherwise a better-followed codebook scores a *lower* κ. (Our first draft of v2 got this wrong and dropped from 0.84 to 0.66.)

1. Duplicate your v1 codebook block (block menu → **Clone**), rename the copy **`Job_with_ref_codebook_v2`**, and edit its descriptions to v2 (below). Short on time? **Checkpoint d** contains exactly this block.

   | Code | v2 description (aligned with the reference annotation's decisions) |
   |---|---|
   | `Promise` | The tweet's main subject is jobs being created, protected or supported: announcements, funding, infrastructure, training or economic-recovery plans, claims of jobs already delivered, and campaign messaging that puts jobs forward as a commitment. This includes campaign value lists where 'For Jobs' appears among other items, 'jobs, not cuts' slogans and vote calls where the author's own pro-jobs stance leads, recovery messaging tagged #qldjobs, and tweets whose subject is a job-creation promise even when reporting or mocking an opponent's promise. |
   | `Cuts` | The tweet's main subject is jobs being cut, lost or at risk: past sackings, warnings that a party or policy will cut jobs, attacks that spell out an opponent's cuts (who cuts what, how many), and non-partisan warnings of job losses such as industry decline or climate impacts. A bare 'jobs, not cuts' slogan is not enough: the tweet must make the threat of cuts its message. Cutting or slashing prices, costs, taxes or bills is not cutting jobs. |
   | `Other` | The word job is used another way, or the post carries no substantive jobs message: praise like 'did a great job' or 'top job', commentary or news links about job statistics, and posts where jobs appear only as a hashtag on content with no jobs message (a photo op, a greeting, a thank-you). |

2. In the Annotation tool, pick **`Job_with_ref_codebook_v2`** as the **Codebook**, create a fresh column **`job.AI_v2`**, and paste the v2 prompt:

   > You are coding tweets posted by candidates during the 2020 Queensland state election. Read each tweet and assign the code that best describes what it says about jobs. Code the tweet's main subject, not passing mentions. Campaign slogans and vote lists count as the author's own commitment. If a tweet both promises jobs and attacks cuts, choose Promise unless the cuts are spelled out as the main message. If the word job is not about employment, or the post has no real jobs message, use Other.

3. **Run All** → **Compare To `theme.reference`** and **`job.AI`**. Did the sharper codebook move κ? Either way you now have three measured runs (plain, examples, revised codebook) and can say which lever did what.

## 12 · Checkpoints: if you fall behind

Four checkpoint workspaces are posted in the Zoom chat. Load one: **Data Loader → Workspace manager → Upload workspace** → choose the ZIP → click **Load** on the new row → re-select the block/columns in the Annotation tool (selections aren't stored in the file; everything else is).

| Checkpoint | Restores the state after… |
|---|---|
| **a** | §1: the `Tweets` block (column types fixed, `full_name`, candidate metadata joined) |
| **b** | §4: the 226-row `Jobs_with_ref` block with `theme.reference` joined |
| **c** | §6: v1 codebook in place, `job.manual` coded for the first page (1–10) and the last page (221–226); everything ready to connect the AI |
| **d** | §11 step 1: the v2 codebook block `Job_with_ref_codebook_v2` added, ready for the v2 run |

Your provider and API key live on your machine, never inside workspace files, so loading a checkpoint doesn't touch them. **Prompts are not saved anywhere but the Prompt field**: they are not part of the codebook block and not restored by a checkpoint. After loading any checkpoint and choosing the model, paste the prompt again (v1 or v2, from the chat / this sheet).

## 13 · Before you use this in real research

- **The shared workshop key is deleted at 3:30 pm today.** For your research: your own API key (the setup is identical), or a **local model**: in **Add Provider** choose **Custom** and point it at any local server that speaks the OpenAI Chat Completions API (e.g. Ollama, LM Studio), so your data never leaves your machine.
- **Check your ethics approval, and the rules around it.** Which AI models and providers you may use, and whether your data may be sent to an external API at all, is governed by your ethics approval plus your institution's, journal's and funder's AI-use rules, not by what the tool can do. A local model keeps data on your machine but does not make a model fair: de-identify regardless. You remain accountable for everything the AI did on your behalf.
- **Keep your methods audit-ready**: save your prompt, codebook, model name, examples used, and agreement scores. They belong in your methods section.

---

## Appendix · Same tool, cleverer questions (replay at home)

Three more codebooks for the same 226 tweets, shown as demos in the session. Each is one small codebook away; the checking workflow from §8–11 is what makes them trustworthy.

**A · Sentiment toward the LNP** (aspect, not sentence)
Prompt: *For each tweet, judge the sentiment expressed toward the LNP (Liberal National Party) or its leader Deb Frecklington specifically, not the overall tone of the tweet. If neither is mentioned or referenced, use none.*

| Code | Description |
|---|---|
| `neg` | The tweet criticises, attacks or blames the LNP or its leader. |
| `pos` | The tweet praises or supports the LNP or its leader. |
| `neu` | The LNP or its leader is mentioned without a clear positive or negative judgement. |
| `none` | The tweet does not mention or refer to the LNP or its leader. |

**B · Mentions a place outside Queensland?**
Prompt: *Decide whether the tweet mentions any real place located outside Queensland, interstate or overseas. Queensland towns, regions, electorates and roads do not count.*

| Code | Description |
|---|---|
| `yes` | The tweet mentions at least one real place outside Queensland, for example another Australian state or city, or another country. |
| `no` | All places mentioned are in Queensland, or no places are mentioned at all. |

**C · More than two people mentioned?**
Prompt: *Count the distinct individual people the tweet refers to, by name or @handle. Groups, parties and organisations do not count as people.*

| Code | Description |
|---|---|
| `yes` | The tweet refers to more than two distinct individual people. |
| `no` | The tweet refers to two or fewer distinct individual people. |

---

*Data: Bruns, A.; Angus, D.; Cohen, T.; QUT Digital Observatory (2022). Queensland Election 2020 on Twitter. QUT. doi.org/10.25912/RDF_1665115527020. Please cite if used in research.*
