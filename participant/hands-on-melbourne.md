# Hands-on: Point-and-click text analytics with Wordflow

**University of Melbourne · Monday 26 October 2026 · 2:00-5:00 pm · Meeting Room M03, Mezzanine, Melbourne Connect**
*Hosted by the Melbourne Data Analytics Platform, LDaCA and the Sydney Informatics Hub*

Each part starts with a few minutes on screen, then it's your turn.

- **Try it** is the basic move with each tool: a few steps, the same for everyone.
- **Go further** is a menu for the rest of the time. Pick anything, in any order, on the tweets, on the Hansard data, or on your own. Nobody is expected to finish it.

Fall behind at any point? Load the part's **checkpoint** (the table at the end) and carry on. Names in **bold** are the exact words on Wordflow's buttons and menus.

---

## 0 · Before we start

1. **Open Wordflow** and accept the **update** it offers. No prompt? **Help → Check for Updates**. Not installed? `sih.tools/wordflow`: the desktop app for Mac or Windows, or **Launch in Binder** to run it in your browser.
2. **Keep this sheet open** beside Wordflow.
3. Stuck? Put your hand up: a helper will come to you.

Lightbulb **suggestions** may pop up as you work: they appear when a result looks off and point at the setting that may help. Read them, or click **Dismiss**.

---

## Part 1 · Shape your data (2:12)

### Try it

1. **A Project and the data.** In the **Data Loader**, under **Create Project**, type a name (for example `Melbourne`) and click **Create Project**. Click **Import sample data**, tick **Queensland Election Tweets** (and **RAPID-CDL: Australian Hansard, GST** if you'd like it for later: it's bigger, so let it download while you work), then **Import selected**.
2. **Files into Data Blocks.** Importing brings in files, not yet data. In the file list, open `sample_data` → `ADO` → `twitter`. Click **Add** beside `qldelection2020_candidate_tweets.csv`, then **Add to Project**. Do the same for `candidate_info_gender.csv`. Both appear in the **Project Graph**: 2,380 tweets, and 133 candidates with their party and gender.
3. **Look, then fix one thing.** Click the tweets block: the table under the graph is the **Data Editor**. Click **Overview** for a summary. The column `created_at` holds dates written as text: click the small type symbol at the left of its header, choose **Date and time**, then **Convert**. Trends needs real dates in Part 2.
4. **Join.** Open **Data Builder** in the sidebar, then **Join**. **Add Data Block**: the **tweets first** (the first one is the left table), then the candidates. Set **Left column** and **Right column** to `username`. **New Data Block name**: `Tweets`. Click **Add to Project**. Every tweet now carries its candidate's `party` and `gender`.
5. **Filter.** The **Filter** tab. **Add Data Block** `Tweets`, **Add condition**: `text`, **starts with**, `RT`, and tick **negate** (keep the tweets that do *not* start with RT, so retweets drop out). **New Data Block name**: `Tweets_original`. **Add to Project**. Check: **1,646 rows**.

**Clean the text, because the data tells you to**

6. **A first look.** Open **Frequency** in the sidebar. **Add Data Block** `Tweets_original`, **Text column** `text`, and under **Tokeniser model** pick the one under **Recommended**. **Run**. Among the biggest words: `https`, `co` and `t`. Nobody wrote them: they're the pieces of web links (`https://t.co/…`), which 1,153 of the 1,646 tweets carry.
7. **Clean them out.** Click `Tweets_original` in the Project Graph. In the **Data Editor**, **Clean text** → **Remove web links (URLs)**. **Column**: `text`; **Save result to**: **The same column**. The preview shows the links gone: **Apply**. Back in **Frequency**, **Run** again: `https`, `co` and `t` have left the cloud. Changed your mind? **Undo** in the Data Editor.

Look at the Project Graph: every step you took is a block, and the arrows are your method.

### Go further (from about 2:30)

- **Categories**: on `Tweets_original`, the type symbol on `gender` → **Category** → **Convert**. Categories give you tick lists in Filter and colours in charts.
- **Two corpora to compare in Part 2**: **Filter** `Tweets_original` on `gender` (tick **F** if it's a Category, or **equals** `F` if not) into `Tweets_F` (721 tweets), and the same with `M` into `Tweets_M` (925).
- **More cleaning** on a copy of `text` (**Add column** → **Copy column…** first): **Clean text** → **Remove punctuation and symbols**, or **lowercase**; **Find & replace**; **Count words, characters, or matches…** for each tweet's length. The preview shows the change before **Apply**; **Undo** takes it back.
- **Combine columns…** (under **Add column**) on the candidates: template `{first_name} {last_name}` (type `{` to pick a column), **New column name** `full_name`.
- **Map values…** on `party`: give each party a side (Labor and Greens, LNP and One Nation and Katter, Others…). **Fill the rest** keeps anything you don't type.
- **Hansard**: in the file list, `sample_data` → `RAPID-CDL` → `hansard_au_gst`. **Add** `Hansard_AU_gst_metadata.parquet` (40,860 paragraphs) and `speaker_detail.parquet`. **Join** the paragraphs (first) to the speakers on `speaker_detail_id`: now every paragraph has the speaker's name, party and gender.

*Behind? Load **Checkpoint A**.*

---

## Part 2 · Look through the lenses (2:47)

Three tools, one move each, and Trends twice: over time, then across categories. Each is shown for a couple of minutes, then it's your turn.

### Try it

1. **Frequency: which words.** Your Frequency tab from Part 1 is still open, with clean text. Look at the **Cloud view** and the **List view**. Campaign noise (handles, names) crowding the cloud? **Right-click** a word to drop it.
2. **Concordance: in context.** **Click** a word in the cloud, for example `jobs`. A new **Concordance** tab opens, named after the word, with its matches already shown. **Click a row**: the tweet opens with the match in bold. **Next row** steps through them.
3. **Trends over time.** Open **Trends**. **Add Data Block** `Tweets_original`. **Time, number or category column**: `created_at`, **Daily**. **Add group**: `gender`. **Run**.
4. **A category in your own order.** Trends can also put a category along the bottom, one bar per value. On `Tweets_original` in the **Data Editor**, click the type symbol on `party` → **Category**. The window shows each party with its number of tweets: choose **Most rows first**, then **drag** `N/A (Independent)` to the end (or drag the parties into any order that suits your question). **Convert**.
5. **Trends across parties.** A new Trends tab (**+**), **Add Data Block** `Tweets_original`, **Time, number or category column**: `party`, **Add group**: `gender`, **Run**. One bar per party, in your order. **Chart** → **Stacked bars**. Labor wrote three tweets in four; most of the Greens' were by women.

### Go further (from about 3:05)

- **Women and men compared**: Frequency with two blocks, `Tweets_F` then `Tweets_M` (from Part 1's Go further). The **Juxtorpus** cloud sets them side by side, and **Keyword Analysis** says which words one group uses more than the other.
- **Stop words**: switch them on and **Select language** → English.
- **Your own search**: a new Concordance tab (**+**), **Add Data Block** `Tweets_original`, **Search word or phrase** `job(s)?|cut(s)?`, tick **Use regular expression**, **Run**. **Show metadata** adds `party` and `gender` beside each match. **Add to Project** turns the matches into a block (`Tweets_jobcut`), with the matched word in `CONC_matched_text`.
- Trends on `Tweets_jobcut`, grouped by `CONC_matched_text` (tick **Ignore capitals**): when did the talk turn to cuts?
- Concordance's **Dispersion view**: where in each text the matches fall. Click a mark: **Match Details**, with **Previous match** and **Next match**.
- Trends over time: **Chart** → **Bars**, **Stacked bars**, **Normalise to 100%**. Swap the group `gender` for `party`: one click, a different study.
- A different party order: choose **Category** on `party` again and drag; **Run** the party Trends again and the bars follow.
- **Hansard**: Trends on the GST paragraphs, `date` **Yearly**, grouped by `chamber`. The peak is no surprise: the GST began on 1 July 2000.

### Before the break (3:22): start a Topic Modelling run

6. Open **Topic Modelling**. **Add Data Block** `Tweets_original`, **Text column** `text`. Leave the settings as they are and click **Run**. If a lightbulb says your texts are short, click its **Use … tokens** button first. The first run downloads a model: it carries on over the break, in **Tasks**.

*Behind? Load **Checkpoint B**.*

---

## Part 3 · Topics (3:35)

Three things here are new since August: reading a topic's texts, naming topics, and colouring the map by your own columns.

### Try it

1. **The topic map.** Each bubble is a topic, sized by how many tweets it holds. Hover a bubble to see its words. Grey **Ungrouped** holds the texts that fit no topic.
2. **Read the texts, not just the words.** In the topic list, click the eye (**Show examples**). **Most typical** shows the passages closest to the heart of the topic first. **Open document** shows the whole tweet a passage comes from.
3. **Name a topic** you can now describe: the pencil (**Rename**), or double-click the topic's title. The name follows the topic everywhere.
4. **Colour by** `party` (in **Display options**, beside or below the map): a bubble's colour is solid when its tweets come mostly from one party and pale when they're spread across parties. Labor wrote three tweets in four, so look for the bubbles that aren't Labor's.

### Go further (from about 3:47)

- **Search term** (in **Display options**): type `job` to light up the topics that use it, *jobs* included. `job, health` gives each term its own colour.
- The **Topics** slider in **Display options**: fewer, broader topics, or more, narrower ones. Names stay with their topics.
- **Random** examples instead of **Most typical**: does the topic still hold?
- **Follow a topic over time**: select it in the list, then **Add to Project** (in **Display options**) → **One row per document** → **Add to Project**. Only the selected topics are included. Then **Trends** on the new block, by `party`.
- **Colour by** `gender` instead; **Words per topic** for a longer list of each topic's words.
- **Hansard**: first **Data Builder** → **Sample** → **Random sample**, **Fraction / Count** `2000`, **Random seed** `0` → **Add to Project**. Then Topic Modelling on the sample. (All 40,860 paragraphs would take a long time on a laptop.)

*Behind? Load **Checkpoint C**.*

---

## Part 4 · Coding text with GenAI (4:00)

An AI model is just another coder. It earns trust the way a human coder does: a codebook, a pilot, agreement scores, and revision. We code by hand first, then check the model against ourselves and against labels our team has checked.

Everyone starts this part from **Checkpoint D**, so the time goes on coding rather than setup. It holds the 226 tweets that mention jobs, the labels our team checked for them (`theme.reference`), and this codebook:

> **Task context**: Tweets posted by candidates around the 2020 Queensland state election (polling day 31 October 2020). Retweets are left out, and only tweets containing "job" or "jobs" are included: 226 tweets. We are studying how candidates talked about employment: as a promise of jobs created or protected, or as a warning about jobs cut or lost. Code each tweet's main message about jobs, not passing mentions. Campaign slogans and lists of values ("For jobs. For health.") count as the candidate's own commitment. If a tweet both promises jobs and attacks cuts, choose Promise unless the cuts are spelled out as its main message. Cutting prices, costs or taxes is not cutting jobs. If "job" is not about employment ("did a great job"), or the tweet has no real jobs message, choose Other.

| Code | Description |
|---|---|
| `Promise` | The tweet's main message is jobs being created, protected or supported: announcements, funding, infrastructure or training plans, or claims of jobs already delivered. |
| `Cuts` | The tweet's main message is jobs being cut, lost or at risk: past sackings, warnings that a party will cut jobs, or attacks on an opponent's cuts. |
| `Other` | The word job is used another way: praise like 'did a great job', commentary about job statistics, or anything that fits neither class above. |

The **Task context** tells the model, and any human coder, what the texts are, why we are coding them, and how to decide the hard cases. It is saved with the codebook, so it travels with the Project and belongs in your methods section.

### Try it

1. **Load Checkpoint D**: **Data Loader** → **Project manager** → **Import Project** → choose the ZIP → click **Open** on its row.
2. Open **Annotation**. **Add Data Block** `Jobs_with_ref`; **Text column** `text`. Under **Codebook**, **Add Data Block** → `Codebook`. Click **Edit** beside **Codes**: the codes and the **Task context** above are there. Close the window.
3. **Be the coder first.** **Annotation column** → **Start new annotation** → **Column name** `job.manual` → **Create**. With the switch on **Manual**, click **Start** and code the first page yourself, with each row's **Select code** list. Notice the tweets that make you hesitate.
4. **Compare to** → tick `theme.reference`. A **Cohen's Kappa** score appears in your column's header: 1 is perfect agreement, 0 is what chance would get. **Hover** it for the confusion matrix: which codes you mixed up. Click **Close**.
5. **Then the model.** **Start new annotation** → `job.AI` → **Create**, and flip the switch to **AI**. **Provider** → **Add provider** → **OpenRouter**, paste the **workshop key** shown on screen → **Add provider**. **Model**: `google/gemini-2.5-flash-lite`, a small, inexpensive model, chosen on purpose.
6. **Preview**: the model codes one page; nothing is saved yet. Go back to **page 1**, where your own codes are, and **Compare to** `job.manual` and `theme.reference`: how far does the model agree with **you**, and with the checked labels?

### Go further

- **Run** codes all 226 into `job.AI` in about a minute. **Compare to** `theme.reference` gives the headline score. In August this model scored about **0.84** with a one-sentence instruction instead of this Task context; yours will differ a little.
- Disagree with the model? **Correction:** → **Create new…** makes a column for your corrections. Correct a few rows and tick **Use as example** to feed them back to the model. Run into a new column and compare again: examples don't always help, which is why you measure.
- **A codebook of your own** on the same tweets: **Codebook** → **Create new**, then **Edit**. Write the **Task context** first (what the texts are, what you want to find out, how to decide the hard cases), then **Add code** for each code, and **Save**. Code a page by hand before any model sees it. One to try, sentiment toward the LNP:
  > **Task context**: Tweets posted by candidates around the 2020 Queensland state election that mention jobs. The Liberal National Party (LNP), led by Deb Frecklington, was in opposition. We want to know how candidates positioned themselves against the LNP. Judge the sentiment toward the LNP or its leader specifically, not the tweet's overall tone. If neither is mentioned or referred to, choose none.

  Codes: `neg` (criticises, attacks or blames the LNP or its leader), `pos` (praises or supports them), `neu` (mentions them without a clear judgement), `none` (doesn't mention or refer to them).
- **Build the 226 yourself**, as Checkpoint D was made: **Filter** `Tweets_original` on `text` **contains** `job` (226 rows); download [`tweets_job_reference.csv`](https://github.com/milysun/wordflow-workshop/releases/download/online-2026-08-28/tweets_job_reference.csv), drop it into the **Data Loader** and **Add** it; **Join** the two on `tweet_id`.

The August recording *Coding text with GenAI* (link at the end) walks through all of these.

---

## Open lab (4:25)

Try Wordflow on what interests you, with us beside you. Anything from a Go further list is fair game too.

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
| ⟨**A** link⟩ | Part 1: tweets and candidates, `created_at` as dates, `Tweets`, `Tweets_original` with the web links removed, and the Frequency tab |
| ⟨**B** link⟩ | Part 2: plus `party` as a category in order, the Concordance tab and both Trends tabs |
| ⟨**C** link⟩ | Part 3: plus a finished Topic Modelling tab with one named topic, coloured by party |
| ⟨**D** link⟩ | Part 4's starting point, for everyone: plus `Jobs_with_ref` (226 tweets with `theme.reference`) and `Codebook` |

Your AI provider and key stay on your computer, never inside a Project file, so checkpoints are safe to share and loading one never touches your key.

---

## Before you use this in your own research

- **The workshop key is deleted at 5:00 pm today.** For your research, use your own key (the steps are the same), or a **local model**: in **Add provider**, choose **Custom** and point it at a local server such as Ollama or LM Studio, so your data never leaves your computer.
- **Check your ethics approval** and your institution's rules on AI use: they decide which models you may use and whether your data may be sent to an external service. De-identify regardless. You remain responsible for everything the AI does on your behalf.
- **Keep your method on record**: codebook, task context, model, examples and agreement scores belong in your methods section.

**Keep going:** `sih.tools/wordflow` for downloads and documentation; in the app, **Help** and **Feedback**. Every tool in today's Go further lists is shown step by step in the August workshop videos: *Wordflow from zero* ([youtu.be/ExYVSgvYIes](https://youtu.be/ExYVSgvYIes)) and *Coding text with GenAI* ([youtu.be/KcjJViYRYX4](https://youtu.be/KcjJViYRYX4)). They were recorded on an earlier version: Workspace is now Project, Preprocessing is now the Data Builder, and Topic Modelling's settings have moved, but the steps are the same.

---

*Data: Bruns, A.; Angus, D.; Cohen, T.; QUT Digital Observatory (2022). Queensland Election 2020 on Twitter. QUT. doi.org/10.25912/RDF_1665115527020. Hames, S., & Alpert, E. (2026). Proceedings of Australian Federal Parliament: An Analytical Database (Version 2026-09-21). Zenodo. doi.org/10.5281/zenodo.22868754 (RAPID-CDL). Please cite if you use them in research.*
