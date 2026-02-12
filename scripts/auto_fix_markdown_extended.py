#!/usr/bin/env python3
"""
Extended automated markdown fixer (safe fixes):
- Ensure first non-empty line is H1 (MD041)
- Remove trailing punctuation from headings (MD026)
- Remove spaces inside emphasis markers (MD037)
- Normalize list marker spacing to single space (MD030)

Usage: python scripts/auto_fix_markdown_extended.py [path...]
"""
from pathlib import Path
import re
import sys

HEADING_RE = re.compile(r'^(?P<prefix>#{1,6}\s*)(?P<text>.*?)(?P<trail>\s*[.:;!?]+\s*)?$')
EMPHASIS_RE = re.compile(r'(\*\*|__)(\s+)([^\s].*?)(\1)')
LIST_RE = re.compile(r'^([ \t]*)([-*+]|\d+\.)\s{2,}(.*)$')


def fix_file(path: Path) -> bool:
    text = path.read_text(encoding='utf-8')
    orig = text
    lines = text.splitlines()

    # Ensure first non-empty line is H1
    first_non_empty_idx = None
    for i, ln in enumerate(lines):
        if ln.strip() != '':
            first_non_empty_idx = i
            break
    if first_non_empty_idx is None:
        return False
    if not re.match(r'^# ', lines[first_non_empty_idx]):
        # find next heading to promote or insert filename-based H1
        promoted = False
        for j in range(first_non_empty_idx, min(first_non_empty_idx+10, len(lines))):
            if re.match(r'^(#{1,6})\s+', lines[j]):
                title_text = re.sub(r'^#{1,6}\s+', '', lines[j]).strip()
                lines.insert(first_non_empty_idx, f"# {title_text}")
                promoted = True
                break
        if not promoted:
            title = path.stem.replace('-', ' ').replace('_', ' ').title()
            lines.insert(first_non_empty_idx, f"# {title}")

    out = []
    for ln in lines:
        # Fix heading trailing punctuation
        m = HEADING_RE.match(ln)
        if m and ln.lstrip().startswith('#'):
            prefix = m.group('prefix')
            text = m.group('text') or ''
            # strip trailing punctuation characters from heading text
            text = re.sub(r'[\s.:;!?]+$', '', text)
            new_ln = f"{prefix}{text}"
            ln = new_ln

        # Fix emphasis spaces like "** text **" -> "**text**"
        ln = re.sub(r'\*\*\s+([^\*].*?)\s+\*\*', r'**\1**', ln)
        ln = re.sub(r'__\s+([^_].*?)\s+__', r'__\1__', ln)

        # Normalize list marker spacing to single space
        lm = LIST_RE.match(ln)
        if lm:
            indent = lm.group(1)
            marker = lm.group(2)
            rest = lm.group(3)
            ln = f"{indent}{marker} {rest}"

        out.append(ln)

    new_text = '\n'.join(out) + ('\n' if not ''.join(out).endswith('\n') else '')
    if new_text != orig:
        path.write_text(new_text, encoding='utf-8')
        return True
    return False


def main(argv):
    args = argv[1:]
    if not args:
        args = ['.']
    targets = []
    for a in args:
        p = Path(a)
        if p.is_dir():
            targets.extend(list(p.rglob('*.md')))
        elif p.is_file():
            targets.append(p)
    changed = []
    for t in sorted(set(targets)):
        try:
            if fix_file(t):
                changed.append(str(t))
        except Exception as e:
            print(f'Error processing {t}: {e}')
    if changed:
        print('Modified files:')
        for c in changed:
            print(' -', c)
    else:
        print('No changes made.')


if __name__ == '__main__':
    main(sys.argv)
