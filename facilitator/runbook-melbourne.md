# Runbook: Melbourne in-person workshop (3 hours, hands-on, not recorded)

**Point-and-click text analytics: an introduction to LDaCA Wordflow · Monday 26 October 2026 · 2:00-5:00 pm AEDT · Meeting Room M03, Mezzanine, Melbourne Connect**

> Drafted 2026-10-24 from `README.md` (canonical plan and timings) and `participant/hands-on-melbourne.md` (the step sheet: "P1.3" below means Part 1, Try it step 3). Deck: `slides/melbourne-wordflow.html`, 19 slides (N toggles the speaker notes). Setup, helper briefing and the shared key: `pre-workshop-checklist-melbourne.md` §4-5. Settings found in the Saturday test go in the ⟨orange⟩ gaps.

**The rule for the afternoon: show the main steps, the room does the main steps, and give them the time.** Each demo stops at the part's last Try it step, exactly as on the projector's flow. Anything after that is *"it's in the August recordings"*, even when it's tempting. Expect many people to need all the time to finish Try it; the sheet's *If you finish early* ideas are one line each, for the few who don't. The room's time is the point: about 40 minutes of you in 180.

**Pacing in the room:** after each Try it, ask *"hands up when you've got [the visible result]"* and move on when about two-thirds are up; helpers take the rest. If a third of the room is stuck on the same step, stop and show that one step on screen. Zoom joiners: one helper owns the chat and posts each checkpoint link as you name it.

---

## 2:00 · Welcome (slides 1-10, 10 min)

Slide 2 is up from 1:45 as people arrive: helpers walk the room checking that Wordflow opens and has updated (the Display options in Topic Modelling are the visible sign of 0.7.17 or later; nobody needs to open it now).

- **MDAP opens** with their welcome, housekeeping and safety (toilets, exits, evacuation); they're the host, so there's no slide for it. Then **slide 3, Acknowledgement of Country**, unless MDAP gives it in their welcome.
- **Slide 4, how this works (1 min):** *"In August I demoed every tool's whole sequence, and the recordings still show all of it. Today I show you the first move, you do that move, and the rest of the time is yours to finish it, with a helper beside you. Done early? The sheet has a few ideas."* Checkpoints in one sentence.
- **Slides 5-6, who and why (2 min together):** thank MDAP and the helpers. The north-star sentence, slowly.
- **Slides 7-8, interface and the one idea (2 min):** switch to the live app for slide 7 if it's quicker than the screenshot. *"The data block is what flows between the tools."*
- **Slides 9-10, data and the afternoon (2 min):** tweets together, Hansard to explore. Point at the times.

## 2:12 · Part 1 · Shape your data (slide 11; show 6 min, the room to 2:47)

**Show, stopping after P1.7:**

1. **Create Project** `Melbourne`; **Import sample data**: tick the tweets and Honi Soit, and Hansard GST (*"Hansard is big; let it download in the background, it's for later"*).
2. `sample_data` → `ADO` → `twitter`: **Add** both CSVs → **Add to Project**. *"Importing brings files; Add makes them data."* Then `SCL` → **Add** `Honi_Soit.zip` → **Texts as one Data Block (100)**: *"a ZIP of text files becomes one block, a row per article. We'll use it before the break."*
3. Tweets block → **Overview** (rows, empties, duplicates, lengths: *"look before you change anything"*). `created_at` type symbol → **Date and time** → **Convert**. *"Types decide what tools can do with a column."*
4. **Data Builder → Join**: tweets **first**, then candidates, `username` both sides → `Tweets`. Say out loud: *"the first one you add is the left table."*
5. **Filter**: `text` starts with `RT`, **negate** → `Tweets_Original`, **1,646**.
6. **Frequency** on `Tweets_Original`, Recommended tokeniser, **Run**. Point at `https`, `co`, `t`: *"nobody wrote these. They're the pieces of t.co links, in 1,153 of these 1,646 tweets. The data tells you what to clean."*
7. Click `Tweets_Original` in the graph → **Clean text** → **Remove web links (URLs)**, `text`, **The same column**, show the preview, **Apply**. Back in Frequency, **Run** ⟨or: refreshes by itself, from the Saturday test⟩: gone. *"Undo is always there."*

Then: *"Your turn: steps 1 to 7. Hands up when your cloud has no https in it."* **2:30:** *"Keep going at your own pace; if you're done, the sheet has three ideas."* Helpers go to whoever is still on the Join or the Filter.

**2:45:** *"MDAP-Part1 is on the page, if you want a clean start for Part 2."* (Zoom chat helper posts it.)

## 2:47 · Part 2 · Look through the lenses (slide 12; short cycles to about 3:05, finishing time to 3:17, Topic Modelling prep to 3:25)

Each cycle: about 2 minutes on screen, then about 3 for the room. Don't wait for everyone between cycles; helpers catch up the stragglers.

- **Cycle 1, Frequency and Concordance (P2.1-2):** the Part 1 Frequency tab. Cloud and List view; right-click a handle to drop it. Click `jobs`: a Concordance tab named `jobs` opens, previewed. Click a row: Row Details, the match in bold, **Next row**. *"Every number you see in a cloud, you can read."*
- **Cycle 2, Trends over time (P2.3):** `Tweets_Original`, `created_at`, **Daily**, **Add group** `gender`, **Run**. Ask what the peaks might be (polling day was 31 October).
- **Cycle 3, a category in your order (P2.4-5):** `party` type symbol → **Category**. The window: each party with its count. **Most rows first**, then drag `N/A (Independent)` to the end: *"the order is yours: it's how every table, legend and chart will show this column."* **Convert**. New Trends tab, `party` on the axis, group `gender`, **Run**, **Stacked bars**. *"Labor wrote three tweets in four. And most of the Greens' tweets were by women."*

**About 3:05:** finishing time. Helpers go to whoever hasn't got the party bars yet.

**3:17, out loud:** *"Before the break, Topic Modelling prep for Part 3: steps 6 and 7 on your sheet, two runs in two tabs."* Show both on screen, about 3 minutes: (6) `Tweets_Original`, `text`, settings ⟨as tested: Topics, Max topic size, Max tokens, Seed⟩, **Run**; if the lightbulb offers smaller Max tokens, ⟨accept / don't, from the Saturday test⟩. *"The first run downloads a model: watch Tasks."* (7) Honi Soit, added in Part 1: in Topic Modelling, **+** for a new tab: *"tabs: one tool, two analyses side by side, each with its own settings."* Text column `document`, **Use 128 tokens**, **Run**. *"Longer texts, read in passages: after the break, one article holding several themes."* Target: both running by 3:22.

## 3:25 · Break (slide 13, 10 min)

Open slide 13 as the break starts: it shows the clock plus 10 minutes. Check the Tasks panel on your screen: two runs, tweets and Honi Soit. Helpers sit with anyone behind: MDAP-Part3 has both runs finished.

## 3:35 · Part 3 · Topics (slide 14; show 5 min, the room to 4:00)

*"Three things here are new since August: reading a topic's texts, naming topics, and colouring the map by your own columns."*

**Show, stopping after P3.5:**

1. The map: hover a bubble for its words; grey **Ungrouped**: *"texts that fit no topic: it doesn't force them."*
2. The eye, **Show examples**: **Most typical** first, the **Top N%** badge; **Open document** for the whole tweet. *"Don't name a topic from its words. Read it."* Then a word in the list that says nothing (a handle, `amp`): **Display options** → stop words switch on → pencil, **Edit stop words** → add it → **Save**. *"It only changes the words shown, not the topics: no need to run again."*
3. Name the topic you just read: pencil or double-click. ⟨the topic that reads well, from the Saturday test⟩.
4. **Colour by** `party` in **Display options** (beside the map on a wide window, below on a narrow one). *"Solid: mostly one party. Pale: shared. Labor wrote most tweets, so look for the bubbles that aren't Labor's."*
5. The Honi Soit tab (anyone without it: MDAP-Part3 has it, finished): one topic, **Show examples**, **Open document**. *"Wordflow reads text in passages: here up to 128 tokens, a few paragraphs. A tweet is one passage; an article is six or so. This topic's passages are tinted; the grey ones belong to other topics. One article, several themes."* **Next passage** to step through.

Hands up when everyone has named a topic. **3:47:** finishing time; early finishers have the sheet's ideas (Search term, the Topics slider).

## 4:00 · Part 4 · Coding text with GenAI (slides 15-16; framing 3 min, show 3 min, room to about 4:22)

**Slide 15 (3 min):** *"An AI model is just another coder. It earns trust the way a human coder does: a codebook, a pilot, agreement scores, and revision."* Choosing a provider is a research decision: ethics, data leaving the machine, local or commercial, cost. *"Today: a workshop key on a small, inexpensive model, on purpose. It's deleted at 5."*

**Slide 16, show (P4.1-4):**

1. **Import MDAP-Part4**, **Open**. *"Everyone starts from the same Project, so the time goes on coding. Your own Project is still in the Project manager for the open lab."*
2. Annotation, tab **A-1**: `Tweets_job_with_reference`, `text` and `Codebook_Job` are already selected (the checkpoint saved them). **Edit**: read the **Task context** aloud. Step 3 picks the empty `Job_Manual`. *"This is the brief you'd give a new research assistant: what the texts are, what we want to find out, how to decide the hard cases. It's saved with the codebook, so it's part of your method."*
3. `Job_Manual`, **Manual**, **Start**: code two rows aloud, hesitating honestly.
4. **Compare to** `theme.reference`: κ in the header, hover for the confusion matrix.

*"Your turn: steps 1 to 4. Code your whole first page."* **When most of the room has a κ (about 4:12),** go to P4.5-6 (the key is on the workshop page, sih.tools/ldaca, with a Copy button; show it on screen too): **Annotation column** → `Job_AI`, AI switch, **Add provider**, OpenRouter, key, then a model: type to find one of the five the key allows (Gemini 2.5 Flash Lite, Gemini 2.5 Flash, Gemma 4 26B A4B (not the "(free)" one), Qwen3.6 35B A3B, Qwen3.8 27B; the page lists them), **Preview**, back to page 1, **Compare to** both columns. *"How far does it agree with you? With the checked labels? Where it disagrees, who's right, or was the codebook silent?"*

If most of the room has no κ by 4:15: do P4.5-6 on screen only (cut order 2) and keep the room on hand-coding and Compare to.

## 4:25 · Open lab (slide 17, 30 min)

*"The rest of the time is yours: finish a part, try the sheet's ideas, Hansard, or your own data."* Walk the room with the helpers. Same rule: if several people hit the same thing, show it on screen. Anyone still in Annotation can Run all 226 here.

## 4:55 · Close (slides 18-19, 5 min)

Slide 18: the spotlight line, slowly. Slide 19: sih.tools/wordflow; *"every step I didn't show is in the August videos"*; the in-app **Feedback** button, now, before people pack up; the key dies at 5. Thank MDAP, the helpers, and the room.

**5:00:** delete the shared key at OpenRouter, then `python3 facilitator/set-workshop-key.py --clear` and publish the page again. Ask MDAP for the attendance count (aggregate only).

---

## Timing gates

| Gate | Must be happening | If late (README cut order) |
|---|---|---|
| 2:30 | Most of the room past the Filter | If most are still on the Join: show Join and Filter once more on screen, point at MDAP-Part1 |
| 2:47 | Part 2 starts | Part 1 ends regardless; MDAP-Part1 on the page |
| 3:00 | Cycle 3 (category) starting | Show the category Trends on screen only (cut order 3) |
| 3:22 | Both Topic Modelling runs started | Not negotiable: the model downloads over the break. If short of time, step 6 only; MDAP-Part3 has both runs finished |
| 3:35 | Part 3 | Break stays 10 minutes |
| 4:00 | Part 4 | Part 3 ends; everyone imports MDAP-Part4 |
| 4:12-4:15 | Key on screen | AI step on screen only (cut order 2) |
| 4:25 | Open lab | The open lab absorbs up to 15 minutes of overrun (cut order 1) |
| 4:55 | Close | Hard stop: feedback and where to get help |

## If things break

| Symptom | Do |
|---|---|
| Labels on someone's screen don't match the sheet (Result settings, Find topics) | They're on 0.7.16 or earlier: **Help → Check for Updates**, or carry on (only Part 3 labels differ) |
| Frequency still shows `https` after cleaning | Cleaned the wrong block (`Tweets` instead of `Tweets_Original`), or the tab needs **Run** again |
| `party` not offered on the Trends axis or in Colour by | It's still text: type symbol → **Category** → **Convert** (P2.4) |
| Topic Modelling run very slow or failed after the break | MDAP-Part3 has both runs finished; carry on from it |
| Hansard import still downloading at 2:30 | Fine: it's only for the open lab. Large downloads on venue Wi-Fi can be slow |
| MDAP-Part4 won't import or **Open** stalls | Helper first; the import is a single ZIP, so a USB stick with the four MDAP checkpoint ZIPs is the fallback |
| Annotation errors (429, timeouts) in Tasks | **Advanced settings → Requests at once** to 3, **Preview** again |
| `openrouter.ai` blocked on the venue network | Part 4 by hand only (P4.1-4); AI steps on the shared screen from a phone hotspot |
| Laptop can't install Wordflow | Binder (or Wordflow online) from sih.tools/wordflow, then the latest checkpoint |
| Projector text too small | Cmd and + twice in Wordflow; Display options move below the map at that width |
