#!/usr/bin/env python3
"""Build print-ready HTML handouts from the participant Markdown docs.

Zero dependencies — uses only the Python standard library (macOS ships
/usr/bin/python3). To produce PDFs:

    python3 handouts/build.py
    # then open the generated .html files in a browser and
    # File > Print > Save as PDF.

Outputs (into handouts/):
    welcome-cheatsheet.html  — print double-sided for the day (1 sheet)
    hands-on.html            — Sessions 1.5/2/3 steps; PDF for the GitHub Release
    participant-pack.html    — everything; PDF linked from the post-workshop email

The converter handles the Markdown subset these docs actually use: ATX
headings, bold/italic/inline-code, links, ordered+unordered (nested) lists,
blockquotes, fenced code blocks, pipe tables, horizontal rules and emoji.
"""

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent      # wordflow-workshop/
PART = ROOT / "participant"
OUT = Path(__file__).resolve().parent              # handouts/

# ---------------------------------------------------------------- inline ----

_CODE_TOKEN = "\x00CODE{}\x00"


def _inline(text: str) -> str:
    """Convert inline Markdown in a single logical line to HTML."""
    # 1. pull out `code spans` so their contents aren't touched by other rules
    spans: list[str] = []

    def _stash(m: re.Match) -> str:
        spans.append(html.escape(m.group(1)))
        return _CODE_TOKEN.format(len(spans) - 1)

    text = re.sub(r"`([^`]+)`", _stash, text)

    # 2. escape everything else
    text = html.escape(text)

    # 3. links [text](url)
    text = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: f'<a href="{html.escape(m.group(2), quote=True)}">{m.group(1)}</a>',
        text,
    )

    # 4. bold then italic (bold first so ** isn't eaten by * rule)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\w)_([^_]+)_(?!\w)", r"<em>\1</em>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)

    # 5. restore code spans
    for i, s in enumerate(spans):
        text = text.replace(_CODE_TOKEN.format(i), f"<code>{s}</code>")
    return text


# ----------------------------------------------------------------- lists ----


def _indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _render_list(lines: list[str], i: int) -> tuple[str, int]:
    """Render a (possibly nested) list starting at lines[i]. Returns (html, next_i)."""
    out: list[str] = []
    base = _indent(lines[i])
    ordered = bool(re.match(r"\s*\d+\.\s", lines[i]))
    out.append("<ol>" if ordered else "<ul>")
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            # blank line: peek — if next non-blank is a deeper/equal list item, keep going
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and re.match(r"\s*([-*]|\d+\.)\s", lines[j]) and _indent(lines[j]) >= base:
                i = j
                continue
            break
        m = re.match(r"(\s*)([-*]|\d+\.)\s+(.*)", line)
        if not m:
            break
        ind = len(m.group(1))
        if ind < base:
            break
        if ind > base:
            inner, i = _render_list(lines, i)
            # attach nested list to the previous <li>
            if out and out[-1].endswith("</li>"):
                out[-1] = out[-1][: -len("</li>")] + inner + "</li>"
            else:
                out.append(inner)
            continue
        out.append(f"<li>{_inline(m.group(3))}</li>")
        i += 1
    out.append("</ol>" if ordered else "</ul>")
    return "".join(out), i


# ----------------------------------------------------------------- table ----


def _render_table(lines: list[str], i: int) -> tuple[str, int]:
    def cells(row: str) -> list[str]:
        row = row.strip()
        if row.startswith("|"):
            row = row[1:]
        if row.endswith("|"):
            row = row[:-1]
        return [c.strip() for c in row.split("|")]

    header = cells(lines[i])
    i += 2  # skip header + delimiter row
    out = ["<table><thead><tr>"]
    out += [f"<th>{_inline(c)}</th>" for c in header]
    out.append("</tr></thead><tbody>")
    while i < len(lines) and "|" in lines[i] and lines[i].strip():
        out.append("<tr>" + "".join(f"<td>{_inline(c)}</td>" for c in cells(lines[i])) + "</tr>")
        i += 1
    out.append("</tbody></table>")
    return "".join(out), i


# ---------------------------------------------------------------- blocks ----

_TABLE_DELIM = re.compile(r"^\s*\|?[\s:|-]*-[\s:|-]*\|?\s*$")


def md_to_html(md: str) -> str:
    lines = md.split("\n")
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        # fenced code block
        if stripped.startswith("```"):
            i += 1
            buf = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(html.escape(lines[i]))
                i += 1
            i += 1  # closing fence
            out.append("<pre><code>" + "\n".join(buf) + "</code></pre>")
            continue

        # horizontal rule
        if re.match(r"^\s*([-*_])\1\1+\s*$", line):
            out.append("<hr>")
            i += 1
            continue

        # heading
        h = re.match(r"^(#{1,6})\s+(.*)", line)
        if h:
            lvl = len(h.group(1))
            out.append(f"<h{lvl}>{_inline(h.group(2))}</h{lvl}>")
            i += 1
            continue

        # table (header row followed by a delimiter row)
        if "|" in line and i + 1 < len(lines) and _TABLE_DELIM.match(lines[i + 1]):
            block, i = _render_table(lines, i)
            out.append(block)
            continue

        # blockquote
        if stripped.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            inner = md_to_html("\n".join(buf))
            out.append(f"<blockquote>{inner}</blockquote>")
            continue

        # list
        if re.match(r"^\s*([-*]|\d+\.)\s+", line):
            block, i = _render_list(lines, i)
            out.append(block)
            continue

        # paragraph (gather consecutive plain lines)
        buf = []
        while i < len(lines) and lines[i].strip() and not re.match(
            r"^\s*(#{1,6}\s|>|```|([-*]|\d+\.)\s|([-*_])\3\3)", lines[i]
        ):
            if "|" in lines[i] and i + 1 < len(lines) and _TABLE_DELIM.match(lines[i + 1]):
                break
            buf.append(lines[i].strip())
            i += 1
        out.append(f"<p>{_inline(' '.join(buf))}</p>")
    return "\n".join(out)


# ------------------------------------------------------------------ page ----

CSS = """
:root { --ink:#1d1b18; --muted:#6b6760; --accent:#c8423e; --soft:#f4eee3; --line:#e3ddd0; }
@page { size: A4; margin: 16mm 15mm; }
* { box-sizing: border-box; }
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
       color: var(--ink); font-size: 10.5pt; line-height: 1.46; margin: 0; }
.doc { max-width: 720px; margin: 0 auto; padding: 4mm 0; }
.doc + .doc { page-break-before: always; }
h1 { font-size: 19pt; color: var(--accent); margin: 0 0 .3em; }
h2 { font-size: 14pt; color: var(--accent); margin: 1.1em 0 .35em; border-bottom: 1px solid var(--line); padding-bottom: .15em; page-break-after: avoid; }
h3 { font-size: 11.5pt; margin: .9em 0 .3em; page-break-after: avoid; }
p { margin: .4em 0; }
ul, ol { margin: .35em 0 .55em; padding-left: 1.5em; }
li { margin: .18em 0; page-break-inside: avoid; }
li > ul, li > ol { margin: .2em 0 .25em; }
code { font-family: "SF Mono", Menlo, Consolas, monospace; font-size: .88em;
       background: var(--soft); padding: .05em .35em; border-radius: 4px; }
pre { background: var(--soft); border: 1px solid var(--line); border-radius: 6px;
      padding: .7em .9em; overflow: auto; font-size: 8.2pt; line-height: 1.4;
      page-break-inside: avoid; }
pre code { background: none; padding: 0; font-size: inherit; }
blockquote { margin: .55em 0; padding: .35em .9em; border-left: 3px solid var(--accent);
             background: #faf6ee; color: var(--muted); page-break-inside: avoid; }
blockquote p { margin: .2em 0; }
table { border-collapse: collapse; width: 100%; margin: .6em 0; font-size: 9.6pt;
        page-break-inside: avoid; }
th, td { border: 1px solid var(--line); padding: .35em .55em; text-align: left; vertical-align: top; }
th { background: var(--soft); }
hr { border: none; border-top: 1px solid var(--line); margin: 1.1em 0; }
a { color: var(--accent); text-decoration: none; }
a[href^="http"]::after { content: " (" attr(href) ")"; font-size: .82em; color: var(--muted); word-break: break-all; }
strong { font-weight: 700; }
/* Two-column glossary (cheat sheet, page 1) — keeps the whole glossary on one side */
.cols2 { column-count: 2; column-gap: 11mm; }
.cols2 h3 { margin-top: .55em; break-after: avoid; }
.cols2 h3, .cols2 p, .cols2 ul, .cols2 li { break-inside: avoid; }
"""

TEMPLATE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>{title}</title>
<style>{css}</style>
</head><body>
{body}
</body></html>
"""


def render_doc(name: str, md: str) -> str:
    """Render a participant doc to HTML. The cheat sheet's glossary (everything
    between the 'Page 1' heading and 'Page 2') is wrapped in a two-column block so
    it fits a single printed side; the UI map on Page 2 stays full-width."""
    if name != "cheat-sheet.md" or "\n## Page 2" not in md:
        return md_to_html(md)
    page1, rest = md.split("\n## Page 2", 1)
    page2 = "## Page 2" + rest
    m = re.search(r"(?m)^## Page 1[^\n]*$", page1)
    if not m:
        return md_to_html(md)
    head, glossary = page1[: m.end()], page1[m.end():]
    return (md_to_html(head)
            + '<div class="cols2">' + md_to_html(glossary) + "</div>"
            + md_to_html(page2))


def build_page(out_name: str, title: str, sources: list[str]) -> None:
    docs = []
    for name in sources:
        md = (PART / name).read_text(encoding="utf-8")
        docs.append(f'<div class="doc">{render_doc(name, md)}</div>')
    page = TEMPLATE.format(title=title, css=CSS, body="\n".join(docs))
    (OUT / out_name).write_text(page, encoding="utf-8")
    print(f"  wrote {out_name}  ({len(sources)} doc(s))")


def main() -> None:
    print("Building handouts ->", OUT)
    build_page("welcome-cheatsheet.html", "Wordflow Workshop — Welcome & Cheat Sheet",
               ["welcome.md", "cheat-sheet.md"])
    build_page("hands-on.html", "Wordflow Workshop — Hands-on",
               ["hands-on-1.md", "hands-on-2.md", "hands-on-3.md"])
    build_page("participant-pack.html", "Wordflow Workshop — Participant Pack",
               ["welcome.md", "cheat-sheet.md", "hands-on-1.md", "hands-on-2.md",
                "hands-on-3.md", "what-next.md"])
    print("Done. Open the .html files and File > Print > Save as PDF.")


if __name__ == "__main__":
    main()
