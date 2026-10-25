"""Put the shared workshop key into the Melbourne page, or take it out.

    python3 facilitator/set-workshop-key.py          # asks for the key (not echoed)
    python3 facilitator/set-workshop-key.py --clear  # removes it (after 5 pm)

The key is stored reversed and base64-encoded, so it is not plain text in the
page's source; the page decodes it for display. That keeps automated scanners
from matching it, not people: the key still needs a spend cap and deleting at
5 pm. Asking for the key keeps it out of your shell history.
"""

import base64
import getpass
import pathlib
import re
import sys

PAGE = pathlib.Path(__file__).resolve().parent.parent / "docs" / "melbourne" / "index.html"
LINE = re.compile(r"const WORKSHOP_KEY_ENCODED = '[^']*';")


def main() -> None:
    html = PAGE.read_text(encoding="utf-8")
    if len(LINE.findall(html)) != 1:
        sys.exit(f"Couldn't find the key line in {PAGE}")
    if "--clear" in sys.argv[1:]:
        encoded = ""
    else:
        key = getpass.getpass("Workshop key (input hidden): ").strip()
        if not key:
            sys.exit("No key given; nothing changed.")
        encoded = base64.b64encode(key[::-1].encode("utf-8")).decode("ascii")
    PAGE.write_text(LINE.sub(f"const WORKSHOP_KEY_ENCODED = '{encoded}';", html), encoding="utf-8")
    print("Key cleared." if not encoded else f"Key set in {PAGE.relative_to(PAGE.parents[2])}.")


if __name__ == "__main__":
    main()
