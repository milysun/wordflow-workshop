# Post-workshop email: online workshop 28 Aug 2026

*Send-ready version (links filled 2026-08-30). Goes to **all 91 registrants**, including the 51 who did not attend: the recordings make the day worth having for them too, and the opt-in question at the end is how we earn the right to email them again.*

**How to send (participant-data rule):** from Eventbrite (**Manage event → Emails to attendees**) if the event still allows it; otherwise from the SIH Training Administration mailbox with every recipient in **BCC**, addresses copied from `private/participants.csv` (filter `event_id = online_workshop_2026-08-28`), and nothing exported anywhere else. Every link below is an absolute https URL; hover-check them in Outlook before sending. The HTML paste source is `post-workshop-email-online.html`.

**Before sending:**

1. **Tag and freeze first.** Plan (decided 2026-08-30): finish the remaining edits, tag the branch tip `online-2026-08-28-final` and push it on Tue 1 Sep evening or Wed 2 Sep morning, then send. At tagging time, switch the GitHub links below from `blob/online_workshop_2026-08-28/` to `blob/online-2026-08-28-final/` so the email points at the frozen copy (branch links keep working either way).
2. **Session 2 recording** paragraph reflects the edit as made: the published video keeps only the slides and the Wordflow interface; participant interactions and the Zoom interface were cut; the opt-out sentence stays so anyone with a concern can ask for a segment to go.
3. **Opt-in mechanism.** The email asks people to **reply "Keep me posted"**. Each reply becomes `promo_opt_in = yes`, `opt_in_date`, `opt_in_source = post_workshop_email` on that person's row in `private/participants.csv`; silence stays blank (not consent). If a sign-up form is adopted instead (decision open; see the 2026-08-30 discussion), swap the link in for the reply instruction before sending.

---

**Subject:** Wordflow workshop: recordings, slides, and whether you'd like to hear from us again

---

Hi all,

Thank you for registering for the LDaCA Wordflow online workshop on Friday 28 August, whether you joined us for the morning tour, the afternoon hands-on, the full day, or couldn't make it in the end. Everything from the day is below, so nobody misses out.

## The recordings

- **Session 1: Wordflow, text analytics without code** (concepts, interface, and the Queensland-election research workflow, 90 min): **https://youtu.be/ExYVSgvYIes**
- **Session 2: Coding text with GenAI, hands-on** (the Annotation tool, 90 min): **https://youtu.be/KcjJViYRYX4**

We had said the afternoon would not be recorded, and the recording was at first kept only for internal use. The session was short and moved quickly through a lot of tasks, so we decided a replay would help anyone wanting a second pass. The published video has been edited down to the slides and the Wordflow interface: participant interactions and the Zoom interface have been removed. If you took part and have any concern about a segment you were involved in, reply to this email and we will remove it.

Both videos are on the Sydney Informatics Hub YouTube channel; share them freely with colleagues who missed the day.

## Materials

- **Slides**: [Session 1](https://github.com/milysun/wordflow-workshop/blob/online_workshop_2026-08-28/slides/online-s1-intro.pdf) and [Session 2](https://github.com/milysun/wordflow-workshop/blob/online_workshop_2026-08-28/slides/online-s2-annotation.pdf) as PDFs (the download button is at the top right of each GitHub page).
- **Session 2 hands-on sheet**: [hands-on-annotation-online.md](https://github.com/milysun/wordflow-workshop/blob/online_workshop_2026-08-28/participant/hands-on-annotation-online.md). Every step from the afternoon, in order, with exact button names. It works as a standalone tutorial alongside the Session 2 recording, so you can do the exercise at your own pace even if you weren't there.
- **Checkpoint workspace files**: [release page](https://github.com/milysun/wordflow-workshop/releases/tag/online-2026-08-28). Five checkpoints (a to e), one per stage of the exercise, plus the human-verified reference coding. Load one via **Data Loader → Workspace manager → Upload workspace** to jump straight to that stage, open tabs and all.
- **Wordflow itself**: download from **https://sih.tools/wordflow**. Documentation and tutorials are built in (Tutorial button, bottom of the sidebar).

## Continuing with the Annotation tool

Three reminders from the close of Session 2, worth reading even if you are meeting the tool through the recording:

1. **Use your own API key**, or go fully local: Add Provider → **Custom** points Wordflow at any OpenAI-compatible local server (Ollama, LM Studio), so your data never leaves your machine. The shared workshop key was deleted at the end of the day.
2. **Check your ethics approval** before coding real research data with an AI model: which models and providers are permitted, and whether data may be sent to an external API at all, is your approval's call.
3. **Keep your methods audit-ready**: save your prompt, codebook, model name, and agreement scores; they belong in your methods section.

## One small ask

If anything in Wordflow confused, surprised, or delighted you, tap the **Feedback** button (bottom-left of the app); it lands directly with the team, and it genuinely shapes what we build next. And if Wordflow ends up in your research, please cite it: the quote icon in the sidebar ("Cite LDaCA Wordflow") has the citation ready to copy.

## Would you like to hear from us again?

We release new Wordflow versions every few weeks and run workshops like this one a few times a year. **If you'd like occasional updates about Wordflow** (new features, and the next workshop when registration opens), **reply to this email with "Keep me posted"**. A handful of emails a year, and every one carries an unsubscribe line.

If you'd rather not, there's nothing to do: we won't add you to any list from today's registration, and this is the last email you'll get from us about the workshop.

## Data acknowledgement

The workshop dataset: Bruns, A.; Angus, D.; Cohen, T.; QUT Digital Observatory (2022). *Queensland Election 2020 on Twitter.* QUT. https://doi.org/10.25912/RDF_1665115527020, with gender metadata contributed by Sydney Corpus Lab. Please cite it if it appears in research outputs.

Thanks again, and reply any time with questions about applying Wordflow to your own corpus.

Dr Chao Sun
Sydney Informatics Hub · chao.sun@sydney.edu.au
