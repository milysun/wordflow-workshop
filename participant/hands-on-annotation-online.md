# Hands-on: Coding text with GenAI in Wordflow

**LDaCA Online Workshop · Session 2 · 28 August 2026 · 2:00 – 3:30 pm AEST (12:00 – 1:30 pm AWST)**

You'll use Wordflow's **Annotation** tool (new in v0.7) to code a real dataset with an AI model, and, more importantly, to *check* the AI's coding the way you'd check a human coder's: agreement scores, a confusion matrix, and targeted revisions until the numbers hold up.

This sheet mirrors the live session step by step, and works as a standalone tutorial afterwards. Fall behind at any point? Jump to **§10 Checkpoints**; you can rejoin in under a minute.

---

## 0 · Before we start: three things

1. **Wordflow running**: the latest v0.7 desktop app from **`sih.tools/wordflow`** (Mac/Windows). *Windows may show a security warning: click **More info**, then **Run anyway**.*
2. **This sheet open** next to Wordflow (a second screen helps).
3. **Model access is provided**: a shared workshop key will be posted in the Zoom chat when we reach §6 (it is deleted at 3:30 pm). Your own OpenRouter / OpenAI / Anthropic / Google key works too, if you prefer.

## 1 · Workspace and data

1. In the **Data Loader**, click **Create workspace** and give it a name.
2. Click **Import sample data**. In the dialog, tick **ADO — Queensland Election Tweets** → **Import selected**. Wait for the **✓ Imported** chip.
3. Add the **candidate tweets** file as a data block: one row per tweet from candidates in the 2020 Queensland state election, with the tweet in the `text` column.

## 2 · Explore first: what is this campaign about?

Before defining any codes, let the data speak.

1. Click the tweets block → open **Frequency**. The word cloud makes it obvious: this campaign is about **jobs**.
2. Optional: click "jobs" in the cloud to jump into **Concordance** and read a few tweets in context. Notice the different ways the word is used; that observation becomes our codebook in §4.

## 3 · Derive the coding dataset (everyone lands on the same 226 rows)

Two filter steps in **Preprocessing → Filter**, each creating a new block:

1. **Drop retweets**: on the tweets block, filter where `text` contains RegEx **`^[Rr][Tt]`**, and tick **negate** (keep everything that does NOT start with rt). This gives the original-tweets block.
2. **Keep the job tweets**: on that new block, filter where `text` contains **`job`** (plain contains, not whole-word, so "jobs" and "job-seeker" count).

Your final block should have **226 rows**. If your number differs, put it in the chat and a helper will jump in (or grab Checkpoint a, §10).

## 4 · Build the codebook (v1: plain and simple)

The codebook is itself a small data block: one row per code, with a description. The descriptions are what the model actually reads.

1. Open the **Annotation** tool (left sidebar, under **Views**). Under **Selected Data Blocks**, add the 226-row block. Set **Text Column** to **`text`**.
2. In the **Annotation Column** dropdown, choose **Start new annotation** → name it **`theme.manual`** → **Create**.
3. In the **Codebook** card, click **Create New**, then **Edit** next to **Codes**. **Add code** three times and type exactly (lowercase, to keep everyone's columns comparable):

   | Code | Description |
   |---|---|
   | `promise` | The tweet's main message is jobs being created, protected or supported: announcements, funding, infrastructure or training plans, or claims of jobs already delivered. |
   | `cuts` | The tweet's main message is jobs being cut, lost or at risk: past sackings, warnings that a party will cut jobs, or attacks on an opponent's cuts. |
   | `other` | The word job is used another way: praise like 'did a great job', commentary about job statistics, or anything that fits neither class above. |

4. **Save.**

## 5 · Be the coder first (Manual mode)

1. Leave the **Manual / AI** toggle on **Manual** and click **Start**.
2. Each row has a **Select class** dropdown: code **about 8 tweets** into `theme.manual`. These become the standard the AI has to match.
3. Click **Close** when done.

## 6 · Connect the AI

1. Create the AI's own column: **Annotation Column → Start new annotation** → **`theme.ai`** → **Create**. (Your codes stay safe in `theme.manual`.)
2. Flip the toggle to **AI**, expand **Advanced settings** (the chevron).
3. **+ Add Provider** → **OpenRouter** → paste the **shared key from the Zoom chat** → press Tab to accept the name → **Add Provider**.
4. **Model**: paste the model id from the chat message.
5. **Prompt** (v1, simple): paste into the Prompt field:

   > You are coding tweets posted by candidates during the 2020 Queensland state election. Read each tweet and assign the code that best describes how it uses the word job or jobs.

## 7 · Preview, measure, revise (this is the skill)

1. Click **Preview**. The model codes the visible page (10 rows; raise **Rows per page** for a bigger sample). Predictions are display-only; nothing is written to your data yet.
2. Click **Compare To** and tick **`theme.manual`**. A **Cohen's Kappa** badge (e.g. `κ 0.74`) appears; **hover it** for the **confusion matrix** against your own codes.
3. Click **Filter any difference** (the filter icon by the column header) and read the disagreements. Mixed tweets ("jobs, not cuts!") and campaign vote-lists ("For Health. For Jobs.") are the usual suspects. Is the model wrong, or was the codebook silent about these cases?
4. **Revise**: update the codebook descriptions to v2 (Edit the codebook, extend each description), and the prompt:

   | Code | v2 description (v1 plus the new rules) |
   |---|---|
   | `promise` | …as v1, plus: Concrete spending or program announcements framed as job-creating (including via #qldjobs) count as promise. Cutting or slashing prices, costs or taxes is not cutting jobs. If a tweet both promises jobs and attacks cuts, code promise only when the promise leads the message. |
   | `cuts` | …as v1, plus: Includes 'jobs, not cuts' slogans whose differentiating message is the threat of cuts, and non-partisan warnings of job losses such as industry decline or climate impacts. |
   | `other` | …as v1, plus: Includes campaign value lists where 'For Jobs' is one item among many, idioms such as 'top job', sarcasm about an opponent's job promises, and posts where jobs appear only as a hashtag with no substantive message. |

   > Prompt v2: You are coding tweets posted by candidates during the 2020 Queensland state election. Read each tweet and assign the code that best describes how it uses the word job or jobs. Code the tweet's central message, not passing mentions. If a tweet fits two classes, choose the one carrying the main emphasis. If you cannot tell, use other.

5. **Update Preview** → watch κ move. That loop (codebook → pilot → agreement → revise) is the method; everything else is buttons.

## 8 · Run All: coding at scale

1. Click **Run All**: all 226 tweets, about a minute. (In **Advanced settings → Run All processing**: **Reprocess all rows** replaces the column; **Fill missing only** keeps existing labels.)
2. The **Annotation Review** table opens: same **Compare To**, confusion matrix and disagreement filters, now over everything. Expect roughly two-thirds `promise`, one-sixth `cuts`, one-sixth `other`.
3. Fix any wrong rows via a **Correction** column (it suggests `theme.ai.correction`), and note **Use as example**: your corrections can feed back into the AI as worked examples.
4. Your coded column is ordinary data now: filter on it, chart `theme.ai` by party in **Trends**, or export CSV from the **Export** view.

## 9 · Optional: compare against a full reference coding

The workshop provides a reference coding of all 226 tweets (`tweets_job_groundtruth.csv`, in the chat and the follow-up email): tweet ids plus a `theme.fable` column produced by a frontier model with the same v1 codebook.

1. Add it as a data block, then **Preprocessing → Join**: your 226-row block first (left), join on `tweet_id`.
2. In the Annotation Review, **Compare To → `theme.fable`**: now your κ is computed over all 226 rows, not just the ones you hand-coded.

## 10 · Checkpoints: if you fall behind

Three checkpoint workspaces are posted in the Zoom chat. Load one: **Data Loader → Workspace manager → Upload workspace** → choose the ZIP → click **Load** on the new row → re-select the block/columns in the Annotation tool (selections aren't stored in the file; everything else is).

| Checkpoint | Restores the state after… |
|---|---|
| **a** | §3: the 226-row block, plus the reference coding block ready to join |
| **b** | §4–6: v1 codebook, `theme.manual` + `theme.ai` columns ready |
| **c** | §7: the v2 codebook and prompt in place, ready to Run All |

Your provider and API key live on your machine, never inside workspace files, so loading a checkpoint doesn't touch them.

## 11 · Before you use this in real research

- **The shared workshop key is deleted at 3:30 pm today.** For your research: your own API key (the setup is identical), or a **local model**: in **Add Provider** choose **Custom** and point it at any local server that speaks the OpenAI Chat Completions API (e.g. Ollama, LM Studio), so your data never leaves your machine.
- **Check your ethics approval.** Which AI models and providers you may use, and whether your data is allowed to be sent to an external API at all, is governed by your approval, not by what the tool can do.
- **Keep your methods audit-ready**: save your prompt, codebook, model name, and agreement scores. They belong in your methods section.

---

## Appendix · Same tool, cleverer questions (replay at home)

Three more codebooks for the same 226 tweets, shown as demos in the session. Each is one small codebook away; the checking workflow from §7 is what makes them trustworthy.

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
