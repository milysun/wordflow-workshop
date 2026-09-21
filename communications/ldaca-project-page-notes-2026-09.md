# Notes for the LDaCA website project page on Wordflow (reply to Bridey)

*Draft reply, 2026-09-21 (v2, softened after Chao's review), for Chao to send. Bridey (LDaCA comms) already has a description of Wordflow and asked for notes under three headings: the problem, learnings and outcomes beyond the app, and anything else to highlight. Written as notes she can shape, not finished web copy. Numbers are as of 21 September 2026; the Zenodo DOI for v0.7.7 was confirmed by Chao on 2026-09-21.*

*Terminology: the UI's "Workspace" is being renamed **"Project"** in the release after v0.7.7. The web page will take a while to build, so these notes already say "project". Word-choice rule applied: "coding" is qualitative coding; the other thing is "programming".*

---

**Subject:** Re: Wordflow project page: notes

Hi Bridey,

Thanks for taking this on, and no rush from our side. Here are some notes under your three headings. They're deliberately more than you'll need, so take what fits the page and cut the rest. Monika, please add or correct anything from the Sydney Corpus Lab side.

## 1. The problem Wordflow addresses

- **Most HASS research runs on text, and most text analysis tools expect you to program.** Interviews, archives, newspapers, parliamentary records, social media, survey comments: the questions researchers ask of them (what's said, by whom, how often, in what context, how it changes over time) have well-worn computational answers, but those answers have mostly lived in Python and R. If you don't have that background, you stay with manual reading, hit a ceiling, or hand the job to someone else.
- **Our own earlier answer had its limits.** LDaCA's text analytics tools (formerly the Australian Text Analytics Platform, ATAP) started life as a collection of Jupyter notebooks. They did their job, but each tool was maintained on its own, the experience was patchy from one to the next, and a notebook is still a page of code to someone who doesn't program. Wordflow is that collection rebuilt as a single point-and-click app.
- **A newer pressure: generative AI used badly.** Researchers are already pasting text into chat interfaces, and in our consulting work we keep seeing the same three problems: results nobody can reproduce (no record of which prompt or model), costs nobody can predict, and answers that come back as prose rather than data, so they can't be counted, checked or analysed further. Wordflow's Annotation tool, released in 2026, was built with those three problems in mind.
- **And the question underneath: where does the analysis run?** A national project can't host every researcher's analysis on shared servers forever, and plenty of data can't leave a researcher's own machine anyway. Wordflow had to work both as a hosted service and as something researchers own and run themselves.

## 2. Learnings and outcomes beyond the app

- **One codebase, four ways in.** The same app is available as a try-it-now launch on ARDC's BinderHub (institutional sign-in, nothing to install), a persistent LDaCA-hosted web service, a one-line Python install, and signed desktop apps for Mac and Windows that work offline. It looks and behaves the same in all four. The lesson we'd pass on to other projects: shared national infrastructure only has to carry the work that genuinely needs sharing. Sensitive or heavy work moves onto researchers' own hardware at no cost to the project, and the extra effort on our side was a one-off release pipeline.
- **The project is the methods section.** Every result in Wordflow is a data block that can feed the next tool, and the visual project graph doubles as a record of how you got there. Projects export as portable archives, so an analysis can be handed to a collaborator, a supervisor or a reviewer and reopened intact. Point-and-click and reproducible turned out to go together quite happily.
- **AI as one more coder.** The Annotation tool treats a model the way a research team treats a new human coder: it gets the codebook, codes a sample, has its agreement with the researcher measured (Cohen's kappa, a confusion matrix), the codebook gets revised, and only then does it code the whole corpus. Every label sits beside the text it came from and is data for the other tools. Local models are supported, so confidential text needn't leave the machine. Our premise, said out loud in every training session: AI doesn't replace critical thinking, and no model deserves blind trust. Workshop participants have run this whole cycle themselves in 90 minutes, and seen with their own eyes that adding examples to a prompt can make agreement worse, not better. That's exactly the kind of check we want people to run.
- **Multilingual from the start.** Language-appropriate tokenisation for English, European languages, Chinese, Japanese, Korean and more. Through the install and desktop channels, this has carried the tool to communities LDaCA's hosted infrastructure was never funded to serve.
- **What we've learnt from teaching it.** Since June 2026 we've run a three-hour in-person introduction at the University of Sydney (44 registrations, 23 in the room), a hands-on session at the CAITG winter school, and a one-day online workshop in August (91 registrants from 19 countries, 40 attended; both sessions recorded and public). A few things now shape every delivery: one research question threaded through every tool rather than disconnected exercises; checkpoint project files so anyone who falls behind rejoins in under a minute; and the honest admission that hands-on blocks always run slower than planned, so we build in a buffer. A feedback form ships inside every copy of the app and has returned 57 responses so far, which go straight into the development queue.
- **Released properly.** Public releases on the Python Package Index, each archived with a DOI on Zenodo, open source under an open licence, versioned public documentation. Current release v0.7.7 (September 2026), https://doi.org/10.5281/zenodo.22266622.

## 3. Other things worth highlighting

- **A data science team and a corpus linguistics lab, working together.** Wordflow is developed at the University of Sydney by the Sydney Informatics Hub together with the Sydney Corpus Lab, as part of LDaCA. That pairing is why the tools speak corpus linguistics (concordance, dispersion, comparative frequency) rather than generic "text mining".
- **Part of the LDaCA ecosystem.** LDaCA curates national text collections; Wordflow is one place where those collections, alongside researchers' own data, can be analysed by the people the collections are for. The latest release can connect to LDaCA collections directly from its Data Loader through the LDaCA API. It's working with some public collections now, and we're continuing to test it, including on collections with access controls, so we'd describe it as a growing connection rather than a finished one.
- **Coming up:** a three-session in-person series at the University of Sydney with the RAPID-CDL project on 29–30 September (qualitative transcripts; the Proceedings of Federal Parliament; analysing parliamentary discourse at scale with Wordflow), an in-person introduction at the University of Melbourne with the Melbourne Data Analytics Platform on 26 October, five accepted presentations and a poster at eResearch Australasia 2026 in Melbourne (26–30 October), and a webinar in ARDC's HASS&I Research Data Commons series on 26 November.
- **Where to point people:** https://sih.tools/wordflow (installers, browser launch, screenshots, workshop recordings and materials) and the source code at https://github.com/Australian-Text-Analytics-Platform/LDaCa_Text_Analytics_Tools.
- **A one-liner, if it helps:** *Wordflow puts corpus-scale text analysis, including responsible AI-assisted coding, into a point-and-click workspace that researchers can run anywhere, from a browser tab on ARDC infrastructure to their own laptop.*

Happy to look over the page whenever it's ready.

Cheers,
Chao

---

## Before sending

- Version: the page can name v0.7.7 and its DOI, or just say "the latest release" if a bug-fix release (v0.7.8) lands before the page goes live; v0.7.7 shipped in a hurry and is known to be buggy

- Monika is happy with the Sydney Corpus Lab wording and the "working together" framing
- "Project" (not "Workspace") is used throughout, matching the post-v0.7.7 UI; the one-liner's "point-and-click workspace" is the ordinary English word, not the UI term, so it stays
- Workshop numbers are from `private/attendance_report_2026-08-28.md` and the eResearch A5 abstract; feedback count 57 from Qualtrics on 2026-09-21; no participant names or emails are included here
