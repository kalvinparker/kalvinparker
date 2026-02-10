#!/usr/bin/env python3
"""Generate an aggregated 'Recent changes' section for the README.

This script reads `.github/scripts/repos.txt` for a list of repos (owner/repo per line),
queries the GitHub API for the latest commit on the default branch, and replaces the
Recent changes section in README.md with an aggregated list.
"""
import os
import re
import requests
from datetime import datetime

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
README = os.path.join(ROOT, 'README.md')
REPOS_FILE = os.path.join(ROOT, '.github', 'scripts', 'repos.txt')
GITHUB_API = 'https://api.github.com'

def load_repos(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = [l.strip() for l in f if l.strip() and not l.startswith('#')]
    return lines

def get_latest_commit(owner_repo, token):
    headers = {'Authorization': f'token {token}'} if token else {}
    owner, repo = owner_repo.split('/')
    try:
        # get default branch
        url_repo = f'{GITHUB_API}/repos/{owner}/{repo}'
        print(f"REQUEST: GET {url_repo}")
        r = requests.get(url_repo, headers=headers)
        print(f"RESPONSE: {r.status_code} {r.reason} for {owner_repo}")
        if r.status_code != 200:
            try:
                print(f"  body: {r.text[:400]}")
            except Exception:
                pass
            return None
        data = r.json()
        branch = data.get('default_branch', 'main')
        # get latest commit on default branch
        url_commit = f'{GITHUB_API}/repos/{owner}/{repo}/commits/{branch}'
        print(f"REQUEST: GET {url_commit}")
        r2 = requests.get(url_commit, headers=headers)
        print(f"RESPONSE: {r2.status_code} {r2.reason} for commit {owner_repo}@{branch}")
        if r2.status_code != 200:
            try:
                print(f"  body: {r2.text[:400]}")
            except Exception:
                pass
            return None
        c = r2.json()
        sha = c.get('sha', '')[:7]
        date = c.get('commit', {}).get('committer', {}).get('date', '')
        message = c.get('commit', {}).get('message', '').split('\n')[0]
        return {'repo': owner_repo, 'sha': sha, 'date': date, 'message': message}
    except Exception as ex:
        print(f"ERROR: Exception while fetching {owner_repo}: {ex}")
        return None

def render_section(entries):
    lines = []
    lines.append('## Recent changes (aggregate across workspace)')
    lines.append('')
    lines.append('Summary of the most recent commits across active repositories:')
    lines.append('')
    for e in entries:
        if e is None:
            continue
        dt = e['date']
        try:
            dtf = datetime.fromisoformat(dt.replace('Z', '+00:00')).strftime('%Y-%m-%d')
        except Exception:
            dtf = dt
        lines.append(f"- {dtf} — {e['repo']} — {e['sha']} — {e['message']}")
    lines.append('')
    lines.append('Note: these entries are pulled from the repositories listed in `.github/scripts/repos.txt`.')
    lines.append('')
    return '\n'.join(lines)

def replace_section(readme_path, new_section):
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # find the "## Recent changes" heading and replace until the following '---' divider
    pattern = re.compile(r"## Recent changes[\s\S]*?\n---", re.M)
    if not pattern.search(content):
        # fallback: append section before final '---' if exists, else at end
        if '---' in content:
            content = content.replace('---', new_section + '\n---', 1)
        else:
            content = content + '\n' + new_section
    else:
        content = pattern.sub(new_section + '\n---', content, count=1)
    # Collapse any repeated '---' dividers into a single one to avoid accumulative runs
    content = re.sub(r'(?:\n---\s*){2,}', '\n---\n', content)
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"WROTE: {readme_path} (new section written)")

def main():
    token = os.environ.get('GITHUB_TOKEN')
    repos = load_repos(REPOS_FILE)
    entries = []
    for r in repos:
        try:
            entries.append(get_latest_commit(r, token))
        except Exception:
            entries.append(None)
    section = render_section(entries)
    replace_section(README, section)

if __name__ == '__main__':
    main()
