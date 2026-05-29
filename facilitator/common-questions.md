# Common Questions and Stumbling Blocks

What participants will ask, what tends to break, and what to say.

Use as a pre-read; keep open during the workshop.

---

## During setup (Session 1.0 → 1.5)

### "I can't open the link."
- Check spelling; the workshop URL is on the whiteboard.
- If Binder-based: ask them to refresh after 30 seconds (cold-start takes 10–60s on first hit).
- If still failing → seat them next to a working neighbour to pair.

### "What browser should I use?"
- Chrome, Edge, Firefox, Safari — any current desktop browser is fine. Mobile browsers won't work well; warn them.

### "Do I need to install anything?"
- No, not for the workshop — Binder runs Wordflow in your browser. If you want the desktop app for later (or as a backup today if Binder is slow), the link is on **sih.tools/wordflow**.

### "What is Binder / what is this loading?"
- *"A cloud computer that runs Wordflow for you. First time someone opens it today it takes a minute to start; after that everyone gets it fast."*

### "How do I find the feedback button?"
- A small **square speech-bubble** icon labelled **Feedback** at the bottom of the left sidebar (next to Tutorial). Mention this often during the workshop — it's the easiest channel for them to report friction.

---

## During the snapshot tour (Session 1.5)

### "I see no data blocks / snapshots."
- They skipped the setup step. Walk them through **Data Loader → Import sample data**, then select all three in the **Datasets** tab and all five in the **Demo Snapshots** tab, then **Import selected**.

### "Snapshot Mode is greyed out / I can't find it."
- The toggle is the **pencil icon next to the "VIEWS" title** in the left sidebar. (Not the top menu.) Click it to switch on or off.

### "Why can't I change anything?"
- Snapshot Mode is on. That's intentional during the snapshot tour. They'll turn it off at the start of Session 2.

### "I want to keep exploring this tool."
- Park it: *"Come back in the free lab. We have to keep moving to see all five."*

### "Will my own data look like this?"
- *"Yes — these snapshots were made from real corpora. You can produce the same outputs on your own data once you've imported it. We'll do exactly that in Session 2."*

---

## During Session 2 (the research story)

### "I lost track / my screen doesn't match yours."
- **Default response**: *"That's fine — go to sih.tools/wordflow → Releases. Download whichever Checkpoint (A–E) matches where I am, then in Wordflow: Data Loader → Import workspace archive → pick the file. You'll be back in sync in 30 seconds."*
- Don't try to talk individual participants back into sync mid-demo. The checkpoints exist for this.

### "I'm not sure if this move was 'try this' or 'watch only'."
- Their hands-on-2 sheet labels each move. *"If you missed it, watch this one and try in the free lab."*

### "The join produced too many / too few rows."
- They probably picked the wrong join type or the wrong key column. Pause briefly, point at your projected screen, continue. They can reload checkpoint A if needed.

### "Dtype warning — what do I do?"
- *"Accept the normalisation. Wordflow is just standardising column types — making sure all dates are dates, all numbers are numbers. It's plumbing; it'll save you trouble later."*

### "I clicked a word in Frequency but nothing happened."
- Was Concordance tool unlocked / available? If not, the jump silently fails. Try again after switching tool sidebar focus.
- Was there a stale Concordance result still loaded? Sometimes the jump appends rather than replacing.

### "The regex returned zero matches / too many."
- For zero: check the search mode is set to **Regex**, not Text. Check the parentheses-OR syntax `(a|b|c)`.
- For too many: the regex matches as substrings by default; add `\b` word boundaries: `\b(cases|covid|lnp\w*)\b`.
- During the demo, pre-test your regex. Don't improvise.

### "BERTopic is taking forever."
- 30-90 seconds is normal on tweets. The Task Centre shows progress.
- If it's much longer: the corpus may be too large. Topic Modelling has a built-in sampling step — make sure it's enabled.

### "I added a block by accident / I have too many branches."
- *"Doesn't matter — ignore the wrong branches. They don't change anything else. Or open the block's menu icon → Delete."*

---

## During Session 3.A (lens repurpose demo)

### "Wait — Trends doesn't have to be over time?"
- *"Exactly. That's the point. Any numeric column can be the x-axis. Date is the most common, but it's not the only option."*

### "Where did the word-count column come from?"
- *"I made it. Preprocessing → Create column → expression for tokens-per-row. Wordflow let me synthesise a new column from existing data."*

### "Can I do this with my own data?"
- *"Yes — that's the whole idea. Any tool, on any column you've made, with any grouping. We'll explore in the free lab next."*

---

## During Session 3.C (free lab)

### "Can I upload a Word document / PDF?"
- Not directly. Wordflow accepts CSV, TSV, Excel, or Parquet. If they have docs, ask: *"Can you get just the text into a CSV with one row per document?"*
- Quick tools: spreadsheet copy-paste for small corpora; Pandoc for batch conversion; ATAP has separate ingestion tools for serious work.

### "My CSV won't load."
- Common causes: weird encoding (recommend UTF-8 save from Excel); first row not headers; line breaks inside cells unescaped. Open in a text editor and inspect.
- If urgent and small: have them save as Parquet or XLSX from another tool.

### "How do I save my work?"
- *"Wordflow auto-saves your workspace on every change. Close the tab and come back — it's still there. To take it off the cloud: Data Loader → Export workspace archive. For a single result: camera icon → Save snapshot."*

### "Can I install this on my own laptop?"
- Yes — desktop app (Mac/Win) or `pip install ldaca-wordflow`. Desktop installer is on **sih.tools/wordflow**.
- Caveat: install size is hundreds of MB (includes ML models). Warn them.

### "Does it work offline?"
- The local install yes; the Binder/cloud version no.

### "Can I use it on my phone / tablet?"
- Technically yes, but the UI is laid out for laptop / desktop screens. Not recommended.

---

## Conceptual / "why" questions

### "Is this AI?"
- *"Some tools use AI under the hood — Topic Modelling uses BERTopic, which uses a small language model to group texts. Most other tools — Concordance, Frequency, Trends — are deterministic statistics. What matters is whether the output is interpretable, and we aim for yes."*

### "Will my data leave my computer?"
- **Crucial question — answer carefully.** Depends on deployment:
  - **Local install**: no, everything stays on your machine.
  - **Binder/cloud**: data is uploaded to the cloud server during your session and deleted when the session ends. **Do not upload sensitive or unpublished research data to the workshop's cloud instance.**
  - Pre-workshop email covers this.

### "Is this for quantitative or qualitative researchers?"
- *"Both. Concordance and Quotation are close-reading tools — they preserve context. Frequency, Trends, Topic Modelling are distant-reading / quantitative. The same workspace can hold both."*

### "How big a corpus can it handle?"
- *"Millions of rows for filtering and frequency. Topic Modelling has a sampling step for very large corpora. If you have a corpus that doesn't fit, ask us."*

### "How does it compare to Voyant / AntConc / NLTK / spaCy?"
- *"Voyant is browser-based and fast, but you can't chain operations. AntConc is desktop, single-corpus, no derived corpora. NLTK and spaCy are libraries — you write Python. Wordflow is for researchers who want the graphical chaining without writing code. Each has its strengths."*

### "Can my workspace archive be shared with someone using a different OS?"
- *"The portability fix landed recently and we've tested across [your tested OS pair]. Cross-OS is the design intent and should work, but if you hit an issue — please tap the feedback button."*

### "Can I cite Wordflow in a paper?"
- Yes — citation info is on the docs site. Note it in the post-workshop email.

---

## When you don't know the answer

*"Good question — let me check during the break / I'll get back to you after."* Then write it on the whiteboard so you don't forget. Honesty is fine. Faking confidence loses the room.
