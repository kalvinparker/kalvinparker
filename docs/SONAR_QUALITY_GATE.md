# SonarQube / SonarCloud Quality Gate — Draft

This document proposes a practical, incremental Quality Gate and rule set for onboarding SonarQube (or SonarCloud) to the `kalvinparker` organization. The intent is to start with quick wins, avoid blocking developer flow, and progressively tighten rules once the team accepts and addresses the initial findings.

## Goals

- Improve code quality and security posture in new code while avoiding large, disruptive changes to legacy code.
- Ensure critical security issues and obvious bugs are caught in PRs.
- Provide actionable guidance and a clear escalation path for exceptions.

## Scope

- Applies to all repositories under `kalvinparker/*` but rollout will be gradual: pilot on one repository for 2–4 weeks before organization-wide enforcement.
- Quality Gate applies to "New Code" by default (Sonar's New Code definition), not to the entire codebase during the initial phase.

## High-level Quality Gate (initial)

The initial gate will fail if any of the following conditions are met within the New Code scope:

1. Blocker or Critical security vulnerabilities found (CWE/OWASP) — FAIL
2. Blocker or Critical reliability bugs (actual code defects) — FAIL
3. New code duplication > 3% — FAIL
4. New code coverage for unit tests decreased (or is below 80% if you prefer an absolute baseline) — FAIL
5. New code maintainability rating falls below B (configurable) — WARN

Notes:
- Coverage is recommended but can be reported separately initially (set to WARN or not applied at first if test harness is missing).
- Maintainability rating thresholds may be tuned per-language.

## Additional rule set (suggested tuning)

Start with Sonar's default 'Sonar way' profile and apply the following customizations:

- Security rules:
  - Keep all Critical & Blocker security rules enabled and set to fail the Quality Gate.
  - Review Medium-level rules and convert noisy ones to WARN or tag them so they appear in the backlog rather than blocking PRs.

- Reliability rules:
  - Enable Nullability and API-contract checks for typed languages.
  - Flag obvious resource leaks and unsafe usages as FAIL for new code.

- Maintainability rules:
  - Enforce function/method complexity thresholds (max 20 cyclomatic complexity per method) but WARN for legacy files.
  - Flag duplicated blocks only if duplication length > 10 lines and duplication density > 3%.

- Code smells and style:
  - Keep as WARN initially; auto-fix via formatters where possible.

- Tests & coverage:
  - Configure coverage collection to calculate 'coverage on new code'. Consider not blocking on coverage until CI harness is reliable.

## Rollout plan (4 phases)

1. Pilot (2–4 weeks)
   - Enable Sonar analysis on one high-activity repo (e.g., `getting-started-todo-app` or `kalvinparker` itself).
   - Use SonarCloud for fast setup (or SonarQube CE if you need to self-host) and use PR analysis only.
   - Apply Quality Gate to New Code only. Do not block merges yet — use PR decoration for visibility.

2. Feedback & tuning (2 weeks)
   - Collect top 20 rule violations and tune/disable noisy rules.
   - Decide thresholds for duplication and complexity based on baseline.

3. Soft enforcement (4 weeks)
   - Change Quality Gate to 'fail' for Critical/Blocker rules in New Code.
   - Start blocking merges on newly introduced Blocker/Critical issues.

4. Organization-wide enforcement
   - Apply the tuned rule set across repositories.
   - Gradually tighten thresholds for maintainability, coverage, and duplication.

## Exceptions & escalation

- Exceptions (temporary) should be raised via PR comments referencing a Sonar issue key and adding a label `sonar-exception` with an expiration date.
- For permanent exceptions (rare), maintain a documented justification in a shared `docs/sonar-exceptions.md` and review quarterly.

## CI integration (GitHub Actions example)

This minimal GH Actions job runs SonarCloud analysis on PRs. Requires `SONAR_TOKEN` saved as a repo secret.

```yaml
name: Sonar Cloud
on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  sonar:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up JDK 17
        uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: '17'

      - name: SonarCloud Scan
        uses: SonarSource/sonarcloud-github-action@master
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
```

For self-hosted SonarQube point the scanner to your server via environment variables and use the community scanner.

## Measurement & metrics

- Track number of new-issues per PR (Goal: 0 critical/blocker per PR).
- Track technical debt ratio over time; set a realistic target (e.g., reduce by 10% Q/Q).
- Keep a weekly digest of top 10 recurring violations.

## Governance

- Sonar admin(s): assign 1–2 platform engineers to manage rules, tokens, and the Sonar instance.
- Review cadence: bi-weekly tuning meetings during pilot, move to monthly after stabilization.

## Appendix: Useful Sonar features

- PR decoration (inline comments)
- Quality Gates (pass/fail per branch)
- Issues widget & weekly report
- Security hotspot review workflow (manual confirmation required before code is marked safe)

---

If you want, I’ll now:
- Implement a SonarCloud GH Action for one repository and open a PR (fast), or
- Create a repository `docs/sonar-exceptions.md` and add templated exception workflow entries.

Pick the next step and I’ll implement it.  
