#!/usr/bin/env python3
"""Check every internal link in the book.

Walks the markdown files, resolves relative links, image paths and in-file
heading anchors, and reports the ones that do not exist. External links
(http, mailto) are not checked.

Usage: python tools/check_links.py [root]

Exits non-zero when something is broken, so CI fails on a dead link.
"""

import re
import sys
from pathlib import Path

SKIP_DIRS = {".git", ".claude", "workshops", "node_modules"}
LINK = re.compile(r"\]\(([^)\s]+)\)")
HEADING = re.compile(r"^#{1,6} (.+)$", re.M)
FENCE = re.compile(r"^```.*?^```", re.M | re.S)
COMMENT = re.compile(r"<!--.*?-->", re.S)


def readable(path: Path) -> str:
    """File contents without fenced code blocks or HTML comments.

    A link inside a code sample is an example, and a link inside a comment is
    parked on purpose — neither should fail the build.
    """
    text = path.read_text(encoding="utf-8")
    text = COMMENT.sub("", text)
    return FENCE.sub("", text)


def slug(heading: str) -> str:
    """Turn a heading into the anchor GitHub generates for it."""
    text = heading.strip().lower()
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)  # links keep their text
    text = re.sub(r"[`*_]", "", text)  # inline formatting is ignored
    text = re.sub(r"[^a-z0-9 -]", "", text)  # other punctuation is dropped
    return text.replace(" ", "-")


def markdown_files(root: Path) -> list[Path]:
    return sorted(
        p for p in root.rglob("*.md")
        if not SKIP_DIRS & set(p.relative_to(root).parts)
    )


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    files = markdown_files(root)
    sources = {f: readable(f) for f in files}
    anchors = {
        f.resolve(): {slug(h) for h in HEADING.findall(text)}
        for f, text in sources.items()
    }

    failures = []
    for f in files:
        here = f.relative_to(root)
        for match in LINK.finditer(sources[f]):
            target = match.group(1)
            if target.startswith(("http://", "https://", "mailto:", "#!")):
                continue
            path, _, anchor = target.partition("#")
            resolved = (f.parent / path).resolve() if path else f.resolve()

            if path and not resolved.exists():
                failures.append(f"MISSING FILE    {here} -> {target}")
                continue
            if anchor and resolved.suffix == ".md":
                known = anchors.get(resolved)
                if known is None:  # outside the checked tree
                    continue
                if anchor not in known:
                    failures.append(f"MISSING ANCHOR  {here} -> {target}")

    for failure in failures:
        print(failure)
    print(f"checked {len(files)} markdown files, {len(failures)} broken link(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
