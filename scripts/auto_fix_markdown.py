#!/usr/bin/env python3
"""
Simple automated markdown fixer.
- Remove trailing spaces
- Ensure first line is H1 (if not present, promote first heading or insert H1 from filename)
- Add fenced-code language hints when the first line inside a fence looks like a shell command (heuristic)
- Add language hint `json` when block content starts with '{' on first non-empty line

Usage: python scripts/auto_fix_markdown.py <path1> [<path2> ...]
It will modify files in place and print a summary.
"""
import sys
import re
from pathlib import Path

SHELL_COMMAND_RE = re.compile(r"^\$ |^sudo |^curl |^wget |^apt |^dnf |^yum |^pip |^python |^npm |^git ", re.IGNORECASE)


def fix_file(path: Path) -> bool:
    text = path.read_text(encoding='utf-8')
    orig = text

    # Remove trailing spaces (but keep two spaces at line-end for deliberate breaks)
    lines = text.splitlines()
    new_lines = []
    for ln in lines:
        if ln.endswith('  '):
            new_lines.append(ln)
        else:
            new_lines.append(ln.rstrip())

    text = '\n'.join(new_lines) + ("\n" if lines and lines[-1] == '' or not text.endswith('\n') else '')

    # Ensure first non-empty line is an H1
    lines = text.splitlines()
    first_non_empty_idx = None
    for i, ln in enumerate(lines):
        if ln.strip() != '':
            first_non_empty_idx = i
            break
    if first_non_empty_idx is None:
        return False

    if not re.match(r'^# ', lines[first_non_empty_idx]):
        # If there is a heading later promote it
        promoted = False
        for j in range(first_non_empty_idx, min(first_non_empty_idx+10, len(lines))):
            if re.match(r'^(#{1,6})\s+', lines[j]):
                # promote by inserting H1 above
                title_text = re.sub(r'^#{1,6}\s+', '', lines[j]).strip()
                lines.insert(first_non_empty_idx, f"# {title_text}")
                promoted = True
                break
        if not promoted:
            # use filename as title
            title = path.stem.replace('-', ' ').replace('_', ' ').title()
            lines.insert(first_non_empty_idx, f"# {title}")

    # Fix fenced code blocks: add language hints heuristically
    out_lines = []
    in_fence = False
    fence_delim = None
    fence_content = []
    fence_start_idx = None
    for i, ln in enumerate(lines):
        if not in_fence:
            m = re.match(r'^(?P<fence>```+)(?P<lang>\S*)\s*$', ln)
            if m:
                in_fence = True
                fence_delim = m.group('fence')
                lang = m.group('lang')
                fence_content = []
                fence_start_idx = len(out_lines)
                out_lines.append(ln)  # placeholder
            else:
                out_lines.append(ln)
        else:
            if ln.strip() == fence_delim:
                # analyze fence_content
                first_nonempty = ''
                for c in fence_content:
                    if c.strip():
                        first_nonempty = c.strip()
                        break
                chosen_lang = None
                if first_nonempty.startswith('{'):
                    chosen_lang = 'json'
                elif SHELL_COMMAND_RE.search(first_nonempty) or first_nonempty.startswith('$'):
                    chosen_lang = 'bash'
                elif first_nonempty.startswith('<') and first_nonempty.endswith('>'):
                    chosen_lang = 'xml'
                # if the fence opener had no lang, replace opener with lang
                opener = out_lines[fence_start_idx]
                if re.match(r'^(?P<fence>```+)$', opener):
                    if chosen_lang:
                        out_lines[fence_start_idx] = opener + chosen_lang
                in_fence = False
                fence_delim = None
                out_lines.append(ln)
            else:
                fence_content.append(ln)
                out_lines.append(ln)

    new_text = '\n'.join(out_lines) + ('\n' if not ''.join(out_lines).endswith('\n') else '')

    if new_text != orig:
        path.write_text(new_text, encoding='utf-8')
        return True
    return False


if __name__ == '__main__':
    # If no args are provided, default to processing the current directory
    # This makes the script safe to invoke from npm or CI without explicit paths.
    args = sys.argv[1:]
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
