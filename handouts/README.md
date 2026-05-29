# Handouts — print/PDF build

Turns the participant Markdown docs into print-ready, self-contained HTML you
can save as PDF. **Zero install** — uses only the Python that ships with macOS.

## Build

```bash
python3 handouts/build.py
```

Then open each generated `.html` in a browser and **File → Print → Save as PDF**
(choose A4, default margins, "Background graphics" on so the accent colours and
code/table shading print).

## Outputs

| File | What it is | How it's used |
|---|---|---|
| `welcome-cheatsheet.html` | Welcome card + cheat sheet | **Print double-sided**, one sheet per attendee for the day |
| `hands-on.html` | Sessions 1.5 / 2 / 3 step sheets | Save as `hands-on.pdf`, attach to the **GitHub Release** so anyone who falls behind can read the steps |
| `participant-pack.html` | Everything (welcome + cheat sheet + all hands-on + what-next) | Save as `participant-pack.pdf`, link from the **post-workshop email** |

## Notes

- The generated `*.html` / `*.pdf` are **not committed** (see `.gitignore`) —
  regenerate from the Markdown whenever the source changes.
- `build.py` converts the Markdown subset these docs use (headings, bold/italic/
  code, nested lists, blockquotes, fenced code, pipe tables, rules, emoji, links).
  External URLs are printed in full after the link text so they're usable on paper.
- If the cheat-sheet's ASCII UI map is too wide for the page, reduce the `pre`
  `font-size` in the `CSS` block of `build.py`.
