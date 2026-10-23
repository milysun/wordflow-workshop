# Hands-on: Point-and-click text analytics with Wordflow

**University of Melbourne · Monday 26 October 2026 · 2:00-5:00 pm · Meeting Room M03, Mezzanine, Melbourne Connect**
*Hosted by the Melbourne Data Analytics Platform, LDaCA and the Sydney Informatics Hub*

Each part has two halves. **Together** is what we do on screen, step by step: follow along here. **Explore** is your time: try the suggestions, try the Hansard data, or try your own. Fall behind at any point? Load the part's **checkpoint** (the table at the end) and carry on.

Names in **bold** are the exact words on Wordflow's buttons and menus.

---

## 0 · Before we start

1. **Open Wordflow** and accept the **update** it offers. No prompt? **Help → Check for Updates**. Not installed? `sih.tools/wordflow`: the desktop app for Mac or Windows, or **Launch in Binder** to run it in your browser.
2. **Keep this sheet open** beside Wordflow.
3. Stuck? Put your hand up: a helper will come to you.

Lightbulb **suggestions** may pop up as you work: they appear when a result looks off and point at the setting that may help. Read them, or click **Dismiss**.

---

## Part 1 · Shape your data (2:15)

### Together

**A new Project, and the data**

1. In the **Data Loader**, under **Create Project**, type a name (for example `Melbourne`) and click **Create Project**.
2. Click **Import sample data**. Tick the **Queensland Election Tweets** collection and the **RAPID-CDL: Australian Hansard, GST** collection, then **Import selected**. The tweets arrive in seconds; Hansard is bigger, so carry on while it downloads.
3. Importing brings in **files**, not yet data. In the file list, open `sample_data` → `ADO` → `twitter`. Click **Add** beside `qldelection2020_candidate_tweets.csv`, then **Add to Project**. Do the same for `candidate_info_gender.csv`. Both now appear in the **Project Graph** and the **Data Blocks** list: 2,380 tweets, and 133 candidates with their party and gender.

**Look before you change anything: the Data Editor**

4. Click the tweets block. The table below the graph is the **Data Editor**. Click **Overview**: rows, columns, how many documents, empties, duplicates, and how long the texts are.
5. The column `created_at` holds dates written as text. Click the small type symbol at the left of its header and choose **Date and time**. The window shows what the values become and checks the whole column first: click **Convert**.
6. On the candidates block, make `gender` and `party` categories: type symbol → **Category** → **Convert**. Categories give you value lists in filters and colours in charts.
7. Still on candidates: **Add column** → **Combine columns…**. Template: `{first_name} {last_name}` (type `{` to pick a column). **New column name**: `full_name`. Check the preview line, then **Apply**. Every edit in the Data Editor can be reversed with **Undo**.

**Make new blocks: the Data Builder**

8. Open **Data Builder** in the sidebar, then the **Join** tab. **Add Data Block**: pick the **tweets first** (the first one is the left table), then the candidates. Set **Left column** and **Right column** to `username`; **Join type** stays **Left**. **New Data Block name**: `Tweets`. Click **Add to Project**. Check: 2,380 rows, now with `party`, `gender` and `full_name` on every tweet.
9. **Filter** tab. **Add Data Block**: `Tweets`. **Add condition**: column `text`, **starts with**, `RT`, and tick **negate** (keep the tweets that do *not* start with RT, so retweets drop out). **New Data Block name**: `Tweets_original`. **Add to Project**. Check: **1,646 rows**.

Look at the Project Graph: every step you took is a block, and the arrows are your method.

### Explore (from about 2:35)

- **Clean text**, **Find & replace**, **Count words, characters, or matches…**: try them on a copy of `text` (**Add column** → **Copy column…** first). The preview shows the change before **Apply**; **Undo** takes it back.
- **Map values…** on the candidates' `party`: give each of the ten parties a side (Labor and Greens, LNP and One Nation and Katter, Others…). **Fill the rest** keeps anything you don't type.
- **Hansard**: in the file list, `sample_data` → `RAPID-CDL` → `hansard_au_gst`. **Add** `Hansard_AU_gst_metadata.parquet` (40,860 paragraphs) and `speaker_detail.parquet`. **Join** the paragraphs (first) to the speakers on `speaker_detail_id`: now every paragraph has the speaker's name, party and gender.

*Behind? Load **Checkpoint A**.*

---

## Part 2 · Look through the lenses (2:45)

### Together

**Two corpora to compare**

1. **Data Builder** → **Filter**, on `Tweets_original`: **Add condition** → `gender` → tick **F** only → name `Tweets_F` → **Add to Project** (721 tweets). Again with **M** → `Tweets_M` (925 tweets).

**Frequency: who says what**

2. Open **Frequency**. **Add Data Block**: `Tweets_F`, then `Tweets_M`. **Text column**: `text`. **Tokeniser model**: pick the one under **Recommended**. **Run**.
3. Look at **Cloud view** and **List view**, and the **Juxtorpus** cloud that sets the two side by side. **Keyword Analysis** says which words are used more by one group than the other.
4. Campaign noise (handles, names) crowding the cloud? **Right-click** a word to drop it into the **Stop words filter**. Or switch stop words on and **Select language** → English.

**Concordance: read it in context**

5. **Click** a word in the cloud, for example `jobs`. A new **Concordance** tab opens, named after the word, with a preview already run.
6. **Click a row**: the tweet opens with the match in bold. **Next row** steps through them.
7. Start a fresh Concordance tab (**+**), **Add Data Block** `Tweets_original`. **Search word or phrase**: `job(s)?|cut(s)?` and tick **Use regular expression**. **Run** (Preview checks only one page). **Show metadata**: tick `full_name`, `party` and `gender`.
8. **Add to Project** → name `Tweets_jobcut` → **Add to Project**. Each match is now a row, with the matched word in `CONC_matched_text`.

**Trends: when**

9. Open **Trends**. **Add Data Block** `Tweets_original`. **Time, number or category column**: `created_at`, **Daily**. **Add group**: `gender`. **Run**. Try **Chart**: **Bars**, **Stacked bars**, and **Normalise to 100%**.

### Explore (from about 3:05)

- Swap `gender` for `party`: one click, a different study.
- Trends on `Tweets_jobcut`, grouped by `CONC_matched_text` (tick **Ignore capitals**): when did the talk turn to cuts?
- Concordance's **Dispersion view**: where in each text the matches fall. Click a mark: **Match Details**, with **Previous match** and **Next match**.
- **Hansard**: Trends on the GST paragraphs, `date` **Yearly**, grouped by `chamber`. The peak is no surprise: the GST began on 1 July 2000.

### Before the break: start a Topic Modelling run

10. Open **Topic Modelling**. **Add Data Block** `Tweets_original`, **Text column** `text`. Leave the settings as they are and click **Run**. If a lightbulb says your texts are short, click its **Use … tokens** button first. The first run downloads a model: watch it in **Tasks** over the break.

*Behind? Load **Checkpoint B**.*

---

## Part 3 · Topics (3:35)

### Together

1. The **topic map**: each bubble is a topic, sized by how many tweets it holds. Hover a bubble to see its words. Grey **Ungrouped** holds the texts that fit no topic.
2. **Find topics**: type `job*` to light up the topics that use the word.
3. **Read the texts, not just the words.** In the topic list, click the eye (**Show examples**). **Most typical** shows the texts closest to the heart of the topic first; the **Top 10%** badge says how typical each one is. **Open document** shows a whole text.
4. **Name a topic** you can now describe: the pencil (**Rename**), or double-click the topic's title. The name follows the topic everywhere.
5. Select that topic in the list, then **Add to Project** (in **Result settings**) → **One row per document** → **Add to Project**. Only the selected topics are included.
6. **Trends** on the new block, by `party`: who talks about this topic, and when?

### Explore (from about 3:45)

- **Topics** in **Result settings**: fewer, broader topics, or more, narrower ones. Names stay with their topics.
- **Colour by** `party`.
- **Random** examples instead of **Most typical**: does the topic still hold?
- **Hansard**: first **Data Builder** → **Sample** → **Random sample**, **Fraction / Count** `2000`, **Random seed** `0` → **Add to Project**. Then Topic Modelling on the sample. (All 40,860 paragraphs would take a long time on a laptop.)

*Behind? Load **Checkpoint C**.*

---

## Part 4 · Coding text with GenAI (4:00)

An AI model is just another coder. It earns trust the way a human coder does: a codebook, a pilot, agreement scores, and revision. We code by hand first, then check the model against ourselves and against labels our team has checked.

### Together

**The 226 job tweets, with checked labels**

1. **Data Builder** → **Filter** on `Tweets_original`: `text` **contains** `job` (leave **case sensitive** unticked) → name `Jobs` → **Add to Project**. Check: **226 rows**.
2. Download the checked labels, [`tweets_job_reference.csv`](https://github.com/milysun/wordflow-workshop/releases/download/online-2026-08-28/tweets_job_reference.csv), and drop it into the **Data Loader**'s file list (or use **Upload files**). **Add** → **Add to Project**.
3. **Join**: `Jobs` first, then the reference block, both on `tweet_id`, **Left** → name `Jobs_with_ref` → **Add to Project**. It now carries `theme.reference`.

*Short on time? **Checkpoint D** has `Jobs_with_ref` and the codebook ready: skip to step 7.*

**A codebook**

4. Open **Annotation**. **Add Data Block** `Jobs_with_ref`; **Text column** `text`.
5. **Annotation column** → **Start new annotation** → **Column name** `job.manual` → **Create**.
6. **Codebook** → **Create new**, then **Edit** beside **Codes**. **Task context (optional)**: `Tweets posted by candidates during the 2020 Queensland state election. Each code describes how the tweet uses the word job or jobs.` Then **Add code** three times, typed exactly (the codes must match the reference letter for letter), and **Save**:

   | Code | Description |
   |---|---|
   | `Promise` | The tweet's main message is jobs being created, protected or supported: announcements, funding, infrastructure or training plans, or claims of jobs already delivered. |
   | `Cuts` | The tweet's main message is jobs being cut, lost or at risk: past sackings, warnings that a party will cut jobs, or attacks on an opponent's cuts. |
   | `Other` | The word job is used another way: praise like 'did a great job', commentary about job statistics, or anything that fits neither class above. |

**Be the coder first**

7. Leave the switch on **Manual** and click **Start**. Code the first page yourself, with each row's **Select code** list. Notice the tweets that make you hesitate.
8. **Compare to** → tick `theme.reference`. A **Cohen's Kappa** score appears in your column's header: 1 is perfect agreement, 0 is what chance would get. **Hover** it for the confusion matrix: which codes you mixed up. Where you differ, was it you, the reference, or a codebook that didn't say? Click **Close**.

**Then the model**

9. **Annotation column** → **Start new annotation** → `job.AI` → **Create**. Flip the switch to **AI**.
10. **Provider** → **Add provider** → **OpenRouter**, paste the **workshop key** shown on screen → **Add provider**. **Model**: `google/gemini-2.5-flash-lite`, a small, inexpensive model, chosen on purpose.
11. **Preview**: the model codes one page; nothing is saved yet. Look at two or three pages, then go back to **page 1**, where your own codes are.
12. **Compare to** → tick `job.manual` and `theme.reference`: how far the model agrees with **you**, and with the checked labels. Hover each score.
13. **If time:** **Run** codes all 226 into `job.AI` in about a minute. **Compare to** `theme.reference` gives the headline score. In August this model scored about **0.84**; yours will differ a little.

### Explore

- Disagree with the model? Use **Correction:** to choose a column for your corrections (**Create new…** makes one) and correct a few rows; **Use as example** feeds them back to the model. Run into a new column and compare again: examples don't always help, which is why you measure.
- A codebook of your own on the same 226 tweets: sentiment toward one party, or whether a tweet mentions a place outside Queensland. Code a page by hand first.

*Behind? Load **Checkpoint D**.*

---

## Open lab (4:35)

Try Wordflow on what interests you, with us beside you.

- **Your own data**: a spreadsheet, a folder of text files, or a ZIP. Drop it into the **Data Loader**, then **Add**.
- **Hansard GST or housing** (housing is in the same **Import sample data** list):
  - **Trends**: how often "negative gearing" or "first home buyers" comes up, year by year, by chamber or by party.
  - **Frequency**: one party's words against another's (**Filter** on `party` after the speaker join).
  - **Concordance**: every "housing affordability", in context.
  - **Topic Modelling** on a sample: what the housing debates are about.

---

## Checkpoints: if you fall behind

A checkpoint is a whole Project saved as a ZIP. To load one: **Data Loader** → **Project manager** → **Import Project** → choose the ZIP → click **Open** on its row. Then pick the tool's Data Block and columns again (those choices are not saved in the file; everything else is).

| Checkpoint | After |
|---|---|
| ⟨**A** link⟩ | Part 1: `Tweets` and `Tweets_original` built |
| ⟨**B** link⟩ | Part 2: plus `Tweets_F`, `Tweets_M`, `Tweets_jobcut` and the analysis tabs |
| ⟨**C** link⟩ | Part 3: plus a finished Topic Modelling tab and one named topic added to the Project |
| ⟨**D** link⟩ | Part 4: plus `Jobs_with_ref` (226 tweets with `theme.reference`) and the codebook |

Your AI provider and key stay on your computer, never inside a Project file, so checkpoints are safe to share and loading one never touches your key.

---

## Before you use this in your own research

- **The workshop key is deleted at 5:00 pm today.** For your research, use your own key (the steps are the same), or a **local model**: in **Add provider**, choose **Custom** and point it at a local server such as Ollama or LM Studio, so your data never leaves your computer.
- **Check your ethics approval** and your institution's rules on AI use: they decide which models you may use and whether your data may be sent to an external service. De-identify regardless. You remain responsible for everything the AI does on your behalf.
- **Keep your method on record**: codebook, task context, model, examples and agreement scores belong in your methods section.

**Keep going:** `sih.tools/wordflow` for downloads and documentation; in the app, **Help** and **Feedback**. The full August workshop is on video: *Wordflow from zero* ([youtu.be/ExYVSgvYIes](https://youtu.be/ExYVSgvYIes)) and *Coding text with GenAI* ([youtu.be/KcjJViYRYX4](https://youtu.be/KcjJViYRYX4)), recorded on an earlier version, where Workspace is now Project and Preprocessing is now the Data Builder.

---

*Data: Bruns, A.; Angus, D.; Cohen, T.; QUT Digital Observatory (2022). Queensland Election 2020 on Twitter. QUT. doi.org/10.25912/RDF_1665115527020. Hames, S., & Alpert, E. (2026). Proceedings of Australian Federal Parliament: An Analytical Database (Version 2026-09-21). Zenodo. doi.org/10.5281/zenodo.22868754 (RAPID-CDL). Please cite if you use them in research.*
