# Hands-on — Coding text with GenAI in Wordflow

**CAITG Winter School · 30 July 2026 · 45 minutes**

You'll use Wordflow's new **Annotation** tool (v0.7) to code a real dataset with an AI model — and, more importantly, to *check* the AI's coding the way you'd check a human coder's: agreement scores, a confusion matrix, and targeted corrections.

Ask for help any time. If a step doesn't work, put your hand up and keep reading — the next step rarely depends on the previous one being perfect.

---

## 0 · Get Wordflow running — `sih.tools/wordflow`

Pick one:

- **Desktop app (recommended)** — download the v0.7.1 installer for Mac or Windows from the page. Everything runs on your own machine.
- **Binder (browser)** — click *Launch in Binder*. Needs an **AAF sign-in** (Australian university credentials), so it's not available to international participants. Don't upload sensitive data to it.

---

## 1 · Workspace and data

1. In the **Data Loader**, click **Create workspace** and give it a name.
2. Click **Import sample data**. On the **Datasets** tab, select **ADO — Queensland Election Tweets** → **Import selected**.
3. You now have two files available: the candidate tweets, and **`candidate_info_gender`** — one row per candidate, with `party`, `electorate`, `first_name`, `last_name`, `username`, and a human-coded `gender` column.
4. **Or bring your own data**: drag & drop a file, or use the upload button. CSV and plain-text files work. *(Known issue in 0.7.1: Excel spreadsheets and zip archives fail to import — export to CSV first.)*

**Three ways to hand a data block to a tool** — use whichever feels natural:

- Inside a tool: **Add data block** (searchable list) or **Add preset**.
- In the workspace graph: click a node and use its **+** button (or double-click the node).
- In the left sidebar, under **Data Blocks**: the add button on a block.

## 2 · Open the Annotation tool

1. In the left sidebar under **Views**, click **Annotation**.
2. Under **Annotation Data Block → Selected Data Blocks**, add the **`candidate_info_gender`** block.
3. Set **Text Column** to **`first_name`** — that's what the model will read.
4. In the **Annotation Column** dropdown, choose **Start new annotation**. Name the column **`gender.ai`** → **Create**.
   *(The `.ai` suffix is just a naming habit — it keeps AI-coded columns obvious next to human ones.)*
5. Optional: click **Show metadata** in the results header later to display `last_name`, `party`, etc. alongside — context for judging the coding.

## 3 · Build a codebook

The codebook is itself a small data block: one row per code, with a description. The descriptions are what the model actually reads — write them like instructions to a new research assistant.

1. In the **Codebook** card, click **Create New** — this makes an empty `..._codebook` block and selects it.
2. Next to **Codes**, click **Edit**. In the **Edit codebook** dialog, **Add code** three times:

   | Code | Description (suggestion — write your own) |
   |---|---|
   | `M` | The first name is typically used for men in Australia. |
   | `F` | The first name is typically used for women in Australia. |
   | `U` | The name is ambiguous, initials only, unisex, or you cannot tell. |

3. **Save.**

## 4 · Code a few rows yourself (Manual mode)

Before the AI touches anything, be the coder for a minute.

1. Leave the **Manual / AI** toggle on **Manual** and click **Start**.
2. Each row has a **Select class** dropdown — code 5–10 rows into `gender.ai`.
3. This is exactly how a human coding team works in Wordflow: each coder gets their own column (`gender.chao`, `gender.sam`, …) and picks it under **Annotation Column** to continue their work.
4. Click **Close** when done.

## 5 · Connect an AI model

1. Flip the toggle to **AI**, then expand the settings via the chevron (**Advanced settings**).
2. Under **Provider**, click **+ Add Provider**:
   - **Provider**: `OpenRouter`
   - **API Key**: copy today's temporary key from **`sih.tools/api`**
   - **Name**: press Tab to accept the suggestion → **Add Provider**
3. Under **Model**, search and pick one — good choices today:
   - `google/gemini-2.5-flash`
   - `google/gemini-2.5-flash-lite`
   - or a free `gemma` model (search "gemma", pick one tagged `:free`)

*The key on `sih.tools/api` is shared and dies after today. For real research, use your own key or a local model — see step 9.*

## 6 · Preview before you run

1. The **Prompt** field shows a default prompt greyed out — press **Tab** to start from it, or write your own. Say what the text is (Australian election candidates' first names) and what to do when unsure (use `U`).
2. Click **Preview**. The model codes the visible page (10 rows; raise **Rows per page** up to 100 for a bigger sample). The `gender.ai (preview)` column shows predictions — **nothing is written to your data yet**.
3. Now check it like you'd check a coder. Click **Compare To** and tick the human-coded **`gender`** column. Pick a metric: **Percent Agreement**, **Cohen's Kappa** (default), or **Krippendorff's Alpha**.
4. A score badge (e.g. `κ 0.81`) appears in the column header. **Hover the badge** — that's the **confusion matrix**. Where do the disagreements pile up? (Usually `U` vs everything.)
5. Click the **Filter any difference** button (filter icon by the column header) to see *only* the rows where the model and the human disagree. Read them. Is the model wrong, or is the human coding debatable? Both happen.
6. Revise your prompt or codebook descriptions → **Update Preview** → watch the score move. This loop *is* the skill.
7. Optional, few-shot: set a **Correction** column, correct a few rows, then click **Use as example** — your corrections become worked examples sent with every request.

## 7 · Run All

1. Click **Run All**. Progress appears above the results and in the sidebar **Tasks** list (**Stop** cancels).
2. In **Advanced settings → Run All processing**, note the two modes:
   - **Reprocess all rows** (default) — replaces the whole annotation column.
   - **Fill missing only** — keeps existing labels (e.g. your manual codes) and codes only the empty rows.
3. When it finishes, the **Annotation Review** table opens: same **Compare To**, confusion matrix, and disagreement filters — now over the whole dataset. Correct any rows the model got wrong via a **Correction** column.
4. Your annotations live in the data block itself — filter on `gender.ai`, feed it into Frequency or Trends, or export it from the **Export** view as CSV.

## 8 · Now do it with your own data

Load your own CSV (any text column works) and think of a *harder* coding problem than names — stance, sentiment, topic, whether a tweet contains a policy claim. Write the codebook, preview on a page, check agreement against your own manual codes, revise, run.

## 9 · Before you use this in real research

- **The workshop API key stops working today.** Get your own key (OpenRouter or another provider), or run a **local model** — in **Add Provider** choose **Custom** and point it at any local server that speaks the OpenAI Chat Completions API (e.g. Ollama, LM Studio).
- **Check your ethics approval.** Which AI models and providers you may use — and whether your data is allowed to be sent to an external API at all — is governed by your approval, not by what the tool can do.
- **Keep your methods audit-ready**: save your prompt, codebook, model name, and agreement scores. They belong in your methods section.

---

*Data: Bruns, A.; Angus, D.; Cohen, T.; QUT Digital Observatory (2022). Queensland Election 2020 on Twitter. QUT. doi.org/10.25912/RDF_1665115527020. Gender metadata by Sydney Corpus Lab. Please cite if used in research.*
