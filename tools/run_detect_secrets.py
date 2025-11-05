#!/usr/bin/env python3
import sys
import json
from detect_secrets.core.scan import scan

def run(path, out):
    result = scan(paths=[path])
    # Serialize a compact report
    report = {}
    for filename, secrets in result.items():
        report[filename] = [ { 'type': s.type(), 'line_number': s.line_number, 'secret': s.secret[:40] } for s in secrets ]
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: run_detect_secrets.py <path> <out.json>')
        sys.exit(2)
    run(sys.argv[1], sys.argv[2])
