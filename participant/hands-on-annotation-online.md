# Hands-on: Coding text with GenAI in Wordflow

**LDaCA Online Workshop · Session 2 · 28 August 2026 · 2:00 – 3:30 pm AEST (12:00 – 1:30 pm AWST)**

You'll use Wordflow's **Annotation** tool (new in v0.7) to code a real dataset with an AI model, and, more importantly, to *check* the AI's coding the way you'd check a human coder's: agreement scores, a confusion matrix, and targeted revisions until the numbers hold up.

This sheet mirrors the live session step by step, and works as a standalone tutorial afterwards. Fall behind at any point? Jump to **§10 Checkpoints**; you can rejoin in under a minute.

---

## 0 · Before we start: three things

1. **Wordflow running and updated**: the desktop app from **`sih.tools/wordflow`** (Mac/Windows); if it shows an update notification, accept it (one click). *Windows may show a security warning at install: click **More info**, then **Run anyway**.*
2. **This sheet open** next to Wordflow (a second screen helps).
3. **Model access is provided**: a shared workshop key will be posted in the Zoom chat when we reach §6 (it is deleted at 3:30 pm). Your own OpenRouter / OpenAI / Anthropic / Google key works too, if you prefer.

## 1 · Load the prepared workspace (Checkpoint a)

This morning's data preparation is done for you. Load it in one step:

1. **Data Loader → Workspace manager → Upload workspace** → choose `Checkpoint_a_Data.zip` (link in the Zoom chat) → click **Load** on the new row.
2. You now have a **`Tweets`** block: one row per tweet by a candidate in the 2020 Queensland state election, with the tweet in `text`, `created_at` as a proper date-time, and the candidate's metadata (`party`, `gender`, `full_name`) joined in from the candidate table.

*Prefer to build it yourself later? Data Loader → Import sample data → **ADO — Queensland Election Tweets**; add the tweets and candidate blocks; fix the column types (`created_at` → date-time; `party`, `gender` → category); create `full_name` from `first_name` + `last_name` in **Preprocessing → Create**; join the two on `username`. That is exactly what the checkpoint contains.*

## 2 · Explore first: what is this campaign about?

Before defining any codes, let the data speak.

1. Click the `Tweets` block → open **Frequency**. The word cloud makes it obvious: this campaign is about **jobs**.
2. Optional: click "jobs" in the cloud to jump into **Concordance** and read a few tweets in context. Notice the different ways the word is used; that observation becomes our codebook in §4.

## 3 · Derive the coding dataset (everyone lands on the same 226 rows)

Two filter steps in **Preprocessing → Filter**, each creating a new block:

1. **Drop retweets**: on the `Tweets` block, filter where `text` contains RegEx **`^[Rr][Tt]`**, and tick **negate** (keep everything that does NOT start with rt). This gives the original-tweets block.
2. **Keep the job tweets**: on that new block, filter where `text` contains **`job`** (plain contains, not whole-word, so "jobs" and "job-seeker" count).

Your final block should have **226 rows**. If your number differs, put it in the chat and a helper will jump in (or grab Checkpoint b, §10).

## 4 · Join the reference annotation

The workshop provides **a human-verified reference annotation** for all 226 tweets: coded by a frontier AI model with the same codebook you're about to use, then reviewed tweet-by-tweet by a human coder. Joining them in now means you can measure any coder (human or AI) against them later.

1. Download `tweets_job_reference.csv` from the Zoom chat and add it as a data block (drag & drop, or **Upload files**). It has two columns: `tweet_id` and `theme.reference`.
2. **Preprocessing → Join**: select your 226-row block FIRST (first pick = left table), then the reference block. Join on **`tweet_id`** (left join).
3. The joined block (still 226 rows) now carries `theme.reference` alongside the text. Work in this block from here on.

## 5 · Build the codebook (v1: plain and simple)

The codebook is itself a small data block: one row per code, with a description. The descriptions are what the model actually reads.

1. Open the **Annotation** tool (left sidebar, under **Views**). Under **Selected Data Blocks**, add the joined block. Set **Text Column** to **`text`**.
2. In the **Annotation Column** dropdown, choose **Start new annotation** → name it **`theme.manual`** → **Create**.
3. In the **Codebook** card, click **Create New**, then **Edit** next to **Codes**. **Add code** three times and type exactly (lowercase, to keep everyone's columns comparable):

   | Code | Description |
   |---|---|
   | `promise` | The tweet's main message is jobs being created, protected or supported: announcements, funding, infrastructure or training plans, or claims of jobs already delivered. |
   | `cuts` | The tweet's main message is jobs being cut, lost or at risk: past sackings, warnings that a party will cut jobs, or attacks on an opponent's cuts. |
   | `other` | The word job is used another way: praise like 'did a great job', commentary about job statistics, or anything that fits neither class above. |

4. **Save.**

## 6 · Feel the task (Manual mode, 2 minutes)

Before the AI touches anything, be the coder for a moment: it changes how you read everything after.

1. Leave the **Manual / AI** toggle on **Manual** and click **Start**.
2. Code **about 5 tweets** into `theme.manual` via each row's **Select class** dropdown. Notice the ones that make you hesitate; the AI will hesitate there too.
3. Click **Close**. (In a real team, each coder gets their own column like this, picked under **Annotation Column**.)

## 7 · Connect the AI

1. Create the AI's own column: **Annotation Column → Start new annotation** → **`theme.ai`** → **Create**.
2. Flip the toggle to **AI**, expand **Advanced settings** (the chevron).
3. **+ Add Provider** → **OpenRouter** → paste the **shared key from the Zoom chat** → press Tab to accept the name → **Add Provider**.
4. **Model**: paste the model id from the chat message.
5. **Prompt** (v1, simple): paste into the Prompt field:

   > You are coding tweets posted by candidates during the 2020 Queensland state election. Read each tweet and assign the code that best describes how it uses the word job or jobs.

## 8 · Preview, measure against the reference annotation, revise

1. Click **Preview**. The model codes the visible page (10 rows; raise **Rows per page** for a bigger sample). Predictions are display-only; nothing is written to your data yet.
2. Click **Compare To** and tick **`theme.reference`**: the human-verified reference annotation. A **Cohen's Kappa** badge (e.g. `κ 0.74`) appears; **hover it** for the **confusion matrix**.
3. Optionally also tick **`theme.manual`**: how does the AI agree with *you*, and how do you agree with the reference? Disagreement is data, not failure.
4. Click **Filter any difference** (the filter icon by the column header) and read the disagreements. Mixed tweets ("jobs, not cuts!") and campaign vote-lists ("For Health. For Jobs.") are the usual suspects. Is the model wrong, or was the codebook silent about these cases?
5. **Revise**: update the codebook descriptions to v2 (Edit the codebook, extend each description), and the prompt:

   | Code | v2 description (v1 plus the new rules) |
   |---|---|
   | `promise` | …as v1, plus: Concrete spending or program announcements framed as job-creating (including via #qldjobs) count as promise. Cutting or slashing prices, costs or taxes is not cutting jobs. If a tweet both promises jobs and attacks cuts, code promise only when the promise leads the message. |
   | `cuts` | …as v1, plus: Includes 'jobs, not cuts' slogans whose differentiating message is the threat of cuts, and non-partisan warnings of job losses such as industry decline or climate impacts. |
   | `other` | …as v1, plus: Includes campaign value lists where 'For Jobs' is one item among many, idioms such as 'top job', sarcasm about an opponent's job promises, and posts where jobs appear only as a hashtag with no substantive message. |

   > Prompt v2: You are coding tweets posted by candidates during the 2020 Queensland state election. Read each tweet and assign the code that best describes how it uses the word job or jobs. Code the tweet's central message, not passing mentions. If a tweet fits two classes, choose the one carrying the main emphasis. If you cannot tell, use other.

6. **Update Preview** → watch κ move. That loop (codebook → pilot → agreement → revise) is the method; everything else is buttons.

## 9 · Run All: coding at scale

1. Click **Run All**: all 226 tweets, about a minute. (In **Advanced settings → Run All processing**: **Reprocess all rows** replaces the column; **Fill missing only** keeps existing labels.)
2. The **Annotation Review** table opens: **Compare To `theme.reference`** now gives a full-table κ over all 226 rows: your headline number. Expect roughly two-thirds `promise`, one-sixth `cuts`, one-sixth `other`.
3. Fix any wrong rows via a **Correction** column (it suggests `theme.ai.correction`), and note **Use as example**: your corrections can feed back into the AI as worked examples.
4. Your coded column is ordinary data now: filter on it, chart `theme.ai` by party in **Trends**, or export CSV from the **Export** view.

## 10 · Checkpoints: if you fall behind

Three checkpoint workspaces are posted in the Zoom chat. Load one: **Data Loader → Workspace manager → Upload workspace** → choose the ZIP → click **Load** on the new row → re-select the block/columns in the Annotation tool (selections aren't stored in the file; everything else is).

| Checkpoint | Restores the state after… |
|---|---|
| **a** | §1: the prepared `Tweets` block (column types fixed, candidate metadata joined) |
| **b** | §5: the 226-row block with `theme.reference` joined, the v1 codebook, and the `theme.manual` column |
| **c** | §8: `theme.ai` column, v2 codebook and v2 prompt in place, ready to Run All |

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
