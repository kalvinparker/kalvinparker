# SonarQube Exception Procedure and Template

Use this document when requesting an exception for a Sonar issue that you believe should not block a PR or be remediated immediately. Exceptions are temporary by default and require a clear justification and an owner who will resolve the underlying issue before the expiration date.

## When to request an exception

- The Sonar rule flags a false positive.
- The fix for the issue requires a larger refactor that cannot be completed in the current sprint.
- The remediation has unacceptable risk (e.g., changes production behavior) and requires staged rollout.

Exceptions must NOT be used to permanently ignore valid security or critical reliability issues.

## How to request an exception (process)

1. Create a GitHub Issue in this repository with the `sonar-exception-request` label (or open a PR comment referencing the Sonar issue key).
2. Fill the template below (copy into the issue body). Include a link to the Sonar issue, affected files, and proposed remediation plan.
3. Assign the issue to the owning engineer and add at least one reviewer from the platform/security team.
4. The platform/security team reviews within 3 business days. If approved, the reviewer will add the label `sonar-exception-approved` and include an expiration date.
5. Automation will add a reminder 7 days before expiration. If expired, the exception label is removed and the issue is re-opened (or flagged for remediation).

## Exception request template

Copy this into a new GitHub Issue when requesting an exception and fill in values.

---
Title: Sonar Exception Request — [SHORT SUMMARY]

Repository: [repo/name]

Sonar Issue Key: [e.g., sonar:XXXXX]

Affected files / paths:
- path/to/file1
- path/to/file2

Severity (Sonar): [BLOCKER | CRITICAL | MAJOR | MINOR]

Why this is an exception (reason):
- Brief justification — is it a false positive or requires major refactor? Be specific.

Proposed mitigation or plan to remediate:
- What will be done, by whom, and an estimated timeline. If the plan is to refactor, include milestones.

Owner (person/team): @username or team-name

Requested expiration date (YYYY-MM-DD): YYYY-MM-DD

Risk if exception is granted:
- Any security, stability, or operational risk while exception is active.

Alternative approaches considered:
- List alternatives and why they weren't chosen.

Approval (for reviewer use):
- Approver: @username
- Approval date: YYYY-MM-DD
- Expiration date set: YYYY-MM-DD

---

## Approval policy

- Only organization admins or designated Sonar admins can mark an exception as approved.
- Approvals for `BLOCKER` or `CRITICAL` severity require a second sign-off from a security lead.

## Automation suggestions (nice-to-have)

- A GitHub Action or scheduled workflow that:
  - Adds `sonar-exception-request` label when the issue is created from a template.
  - Notifies the `#devops` or `#security` Slack channel with issue details.
  - Adds a reminder 7 days before expiration and on expiration.
  - Automatically removes the `sonar-exception-approved` label when expired and re-opens the issue.

## Example

- Title: Sonar Exception Request — Temporary allow JSON parsing complexity in `parser.js`
- Sonar Issue Key: sonar:12345
- Affected files: src/parser.js
- Severity: MAJOR
- Reason: Fix requires replacing a historical parsing module across multiple services; planned refactor in Q1.
- Proposed plan: Owner @alice will land a phased refactor across 3 PRs in the next 6 weeks; temporary exception until 2025-12-15.
- Owner: @alice

## Review cadence

- Platform/security team reviews sonar-exception issues weekly and audits active exceptions monthly.

## Where to store long-term exceptions

- Permanent exceptions are strongly discouraged. If a permanent exception is considered, document it in `docs/sonar-exceptions-archive.md` with a business justification and sign-off.
