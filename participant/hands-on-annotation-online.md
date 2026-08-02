# Hands-on — Coding text with GenAI in Wordflow

**LDaCA Online Workshop · Session 2 · 28 August 2026 · 1:30 – 3:00 pm**

You'll use Wordflow's **Annotation** tool (new in v0.7) to code a real dataset with an AI model — and, more importantly, to *check* the AI's coding the way you'd check a human coder's: agreement scores, a confusion matrix, and targeted corrections.

This sheet mirrors the live session step by step, and works as a standalone tutorial afterwards. Fall behind at any point? Jump to **§10 Checkpoints** — you can rejoin in under a minute.

---

## 0 · Before we start — three things

1. **Wordflow running** — the v0.7.x desktop app from **`sih.tools/wordflow`** (Mac/Windows), or *Launch in Binder* on the same page (needs an Australian university AAF sign-in; don't upload sensitive data there).
2. **Your API key at hand** — from the pre-workshop email: an **openrouter.ai** key (free account; free models available), or an OpenAI / Anthropic / Google key you already have.
3. **This sheet open** next to Wordflow — a second screen helps.

No key? Do everything below anyway — you'll be able to run steps 1–6 and 8 fully, and watch the AI runs on the shared screen; your key can go in any time later.

## 1 · Workspace and data

1. In the **Data Loader**, click **Create workspace** and give it a name.
2. Click **Import sample data**. In the dialog, tick **ADO — Queensland Election Tweets** → **Import selected**. Wait for the **✓ Imported** chip.
3. Add **`candidate_info_gender`** as a data block and click it: one row per candidate — `party`, `electorate`, `first_name`, `last_name`, `username`, and a human-coded **`gender`** column. That last column is our ground truth; today the AI competes with it.
4. **Or bring your own data**: drag & drop a file, or use **Upload files**. CSV and plain-text files work. *(Known issue in 0.7.x: Excel spreadsheets and zip archives fail to import — export to CSV first.)*

## 2 · Open the Annotation tool

1. In the left sidebar under **Views**, click **Annotation**.
2. Under **Selected Data Blocks**, add **`candidate_info_gender`** (the **Add data block** button, or double-click the block's node in the graph).
3. Set **Text Column** to **`first_name`** — that's what the model will read.
4. In the **Annotation Column** dropdown, choose **Start new annotation**. Name the column **`gender.ai`** → **Create**.
   *(The `.ai` suffix is just a naming habit — it keeps AI-coded columns obvious next to human ones.)*

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

## 5 · Connect your AI model

1. Flip the toggle to **AI**, then expand the settings via the chevron (**Advanced settings**).
2. Under **Provider**, click **+ Add Provider**:
   - **Provider**: `OpenRouter` (or OpenAI / Anthropic / Google if that's the key you brought)
   - **API Key**: paste your key. It's write-only — Wordflow never displays it again.
   - **Name**: press Tab to accept the suggestion → **Add Provider**
3. Under **Model**, search the live list and pick one:
   - a **free** Gemma model — search "gemma", choose one tagged `:free` (zero cost), or
   - `google/gemini-2.5-flash-lite` / `google/gemini-2.5-flash` if your account has credit, or
   - any model you like — the field also accepts a typed model id.

## 6 · Preview before you run

1. The **Prompt** field shows a default prompt greyed out — press **Tab** to start from it, or write your own. Say what the text is (Australian election candidates' first names) and what to do when unsure (use `U`).
2. Click **Preview**. The model codes the visible page (10 rows; raise **Rows per page** up to 100 for a bigger sample). The `gender.ai (preview)` column shows predictions — **nothing is written to your data yet**. This is your pilot study.
3. Now check it like you'd check a coder. Click **Compare To** and tick the human-coded **`gender`** column. Metric: **Cohen's Kappa** (default; Percent Agreement and Krippendorff's Alpha are there too).
4. A score badge (e.g. `κ 0.81`) appears in the column header. **Hover the badge** — that's the **confusion matrix**. Where do the disagreements pile up? (Usually `U` vs everything.)
5. Click the **Filter any difference** button (filter icon by the column header) to see *only* the rows where the model and the human disagree. Read them. Is the model wrong, or is the human coding debatable? Both happen.
6. Revise your prompt or codebook descriptions → **Update Preview** → watch the score move. **This loop is the skill** — codebook → pilot → agreement → revise.
7. Optional, few-shot: set a **Correction** column, correct a few rows, then click **Use as example** — your corrections become worked examples sent with every request.

## 7 · Run All

1. Click **Run All**. Progress appears above the results and in the sidebar **Tasks** list (**Stop** cancels).
2. In **Advanced settings → Run All processing**, note the two modes:
   - **Reprocess all rows** (default) — replaces the whole annotation column.
   - **Fill missing only** — keeps existing labels (e.g. your manual codes) and codes only the empty rows.
3. When it finishes, the **Annotation Review** table opens: same **Compare To**, confusion matrix, and disagreement filters — now over the whole dataset. Correct any rows the model got wrong via a **Correction** column (it suggests `gender.ai.correction`).
4. Your annotations live in the data block itself — filter on `gender.ai`, feed it into Frequency or Trends, or export it from the **Export** view as CSV.

## 8 · Now do it with your own data

Load your own CSV (any text column works) and think of a *harder* coding problem than names — stance, sentiment, topic, whether a text contains a policy claim. Write the codebook, preview on a page, check agreement against your own manual codes, revise, run. No data of your own? Try to beat your κ on the names task, or code the tweets block's `text` column for topic.

## 9 · Before you use this in real research

- **You already have the real-research setup** — your own key, your own account. To keep data fully on your machine, use a **local model**: in **Add Provider** choose **Custom** and point it at any local server that speaks the OpenAI Chat Completions API (e.g. Ollama, LM Studio).
- **Check your ethics approval.** Which AI models and providers you may use — and whether your data is allowed to be sent to an external API at all — is governed by your approval, not by what the tool can do.
- **Keep your methods audit-ready**: save your prompt, codebook, model name, and agreement scores. They belong in your methods section.

## 10 · Checkpoints — if you fall behind

Checkpoint files are workspace archives posted in the Zoom chat (also in the follow-up email):

| File | Restores the state after… |
|---|---|
| `Checkpoint_0_Data.zip` | §1 — workspace with the sample data imported |
| `Checkpoint_1_Codebook.zip` | §3–4 — annotation column, codebook, some manual codes |
| `Checkpoint_2_Preview.zip` | §6 — a working prompt + codebook ready to Preview |

To load one:

1. **Data Loader → Workspace manager → Upload workspace** → choose the downloaded `.zip`.
2. Click **Load** on the newly listed workspace.
3. Back in **Annotation**: if a selector shows empty, re-select the data block / columns — the data, tabs, and results are all restored; only the tool's current selections aren't stored in the file.

Your provider and API key are untouched — they live on your machine, never inside workspace files (which is also why checkpoint files are safe to share).

---

*Data: Bruns, A.; Angus, D.; Cohen, T.; QUT Digital Observatory (2022). Queensland Election 2020 on Twitter. QUT. doi.org/10.25912/RDF_1665115527020. Gender metadata by Sydney Corpus Lab. Please cite if used in research.*
