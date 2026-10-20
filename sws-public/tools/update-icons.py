#!/usr/bin/env python3
"""Refresh the app icons embedded in dashboard.html.

  python update-icons.py <folder holding the app repos> [path/to/dashboard.html]

For each app listed in APPS, this reads the favicon the app declares in its own <head> (or, for the few that
keep it as a file, the file), shrinks bitmaps to 48 px, and rewrites everything between the ICONS markers in
dashboard.html. The rest of the page is left byte for byte as it was. Apps with no page of their own (the
script repos, which are only links to GitHub) get no icon, and the dashboard simply shows none.

Needs Pillow, for the bitmap icons only:  pip install pillow
"""
import base64
import io
import re
import sys
import urllib.parse
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    Image = None

MAX_PX = 48
START, END = "/* ICONS:START */", "/* ICONS:END */"
# the app's page when it is not <id>/index.html
PAGES = {
    "time-pilot": "time-pilot/static/index.html",
    "ntfy-reminders": "ntfy-reminders/standalone/ntfy-client-demo.html",
}
# apps that are only a link to a GitHub repo
NO_PAGE = {"motd-stats", "debian-harden", "powershell-automate"}


def b64(raw):
    return base64.b64encode(raw).decode("ascii")


def icon_links(page_html):
    """Every <link rel="icon"> in <head>, as dicts. Apple touch icons are left out."""
    head = page_html.split("</head>")[0]
    out = []
    for tag in re.findall(r"<link\b[^>]*>", head, re.I):
        attrs = dict((k.lower(), v) for k, v in re.findall(r'([\w-]+)="([^"]*)"', tag))
        rel = attrs.get("rel", "").lower()
        if "icon" in rel and "apple" not in rel and "mask" not in rel and attrs.get("href"):
            out.append({"href": attrs["href"], "type": attrs.get("type", "").lower(), "sizes": attrs.get("sizes", "").lower()})
    return out


def pick(cands):
    """An SVG if there is one (it is the smallest and sharpest), otherwise the largest declared bitmap."""
    for c in cands:
        if "svg" in c["type"] or c["href"].startswith("data:image/svg"):
            return c

    def px(c):
        m = re.match(r"(\d+)x", c["sizes"])
        return int(m.group(1)) if m else 0
    return max(cands, key=px)


def load(href, page):
    """(mime, bytes) for a data: URI or a file next to the page."""
    if href.startswith("data:"):
        head, body = href.split(",", 1)
        raw = base64.b64decode(body) if ";base64" in head else urllib.parse.unquote_to_bytes(body)
        return head[5:].split(";")[0], raw
    for p in (page.parent / href, page.parent / href.lstrip("/"), page.parent / Path(href).name):
        if p.is_file():
            ext = p.suffix.lower()
            return {".svg": "image/svg+xml", ".png": "image/png", ".ico": "image/x-icon"}.get(ext, "image/png"), p.read_bytes()
    raise FileNotFoundError(f"{href} (declared by {page})")


def encode(mime, raw):
    if "svg" in mime:
        return "data:image/svg+xml;base64," + b64(raw)
    if Image is None:
        sys.exit("Pillow is needed to shrink the bitmap icons:  pip install pillow")
    img = Image.open(io.BytesIO(raw)).convert("RGBA")
    if max(img.size) > MAX_PX:
        scale = MAX_PX / max(img.size)
        img = img.resize((max(1, round(img.width * scale)), max(1, round(img.height * scale))), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, "PNG", optimize=True)
    return "data:image/png;base64," + b64(buf.getvalue())


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    root = Path(sys.argv[1])
    dash = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).resolve().parent.parent / "dashboard.html"
    raw = dash.read_bytes()
    text = raw.decode("utf-8")
    if text.count(START) != 1 or text.count(END) != 1:
        sys.exit(f"{dash} needs exactly one {START} and one {END}")

    apps_block = text[text.index("var APPS = ["):]
    apps_block = apps_block[:apps_block.index("\n  ];")]
    ids = re.findall(r"\{ id: '([a-z0-9-]+)'", apps_block)

    lines, report = [], []
    for app in ids:
        if app in NO_PAGE:
            report.append((app, "no page", 0))
            continue
        page = root / PAGES.get(app, f"{app}/index.html")
        if not page.is_file():
            sys.exit(f"missing page for {app}: {page}")
        cands = icon_links(page.read_text(encoding="utf-8", errors="replace"))
        if not cands:
            report.append((app, "NO ICON DECLARED", 0))
            continue
        mime, data = load(pick(cands)["href"], page)
        uri = encode(mime, data)
        lines.append(f"    '{app}': '{uri}',")
        report.append((app, mime.split("/")[1], len(uri)))

    block = START + "\n  var ICONS = {\n" + "\n".join(lines) + "\n  };\n  " + END
    i, j = text.index(START), text.index(END) + len(END)
    dash.write_bytes((text[:i] + block + text[j:]).encode("utf-8"))

    for app, kind, size in report:
        print(f"  {app:22s} {kind:14s} {size:>7} chars")
    print(f"{len(lines)} icons, {sum(r[2] for r in report) // 1024} KB, written to {dash}")


if __name__ == "__main__":
    main()
