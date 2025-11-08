# Hi — I'm Kalvin 👋

[![profile-badge](https://img.shields.io/badge/Status-Security%20Hardened-brightgreen)]()
[![readme sync](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/kalvinparker/kalvinparker/main/kalvinparker/.github/last-sync.json)](https://github.com/kalvinparker/kalvinparker/actions)

Welcome! I'm a security-minded engineer focused on Governance, DevSecOps, infrastructure as code, and reliable CI/CD.

- 🔭 I’m currently working on: Automating README snapshot sync across repositories and ELK Stack hardening
- 🌱 Learning of the day: <!-- START_LEARNING -->GitHub Actions security, PAT scopes, and secret-scanning mitigation<!-- END_LEARNING -->
- ⚡ Most used tool this week: <!-- START_TOOL -->PowerShell, gh, docker<!-- END_TOOL -->

## Skills & Tools

![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)
![PowerShell](https://img.shields.io/badge/-PowerShell-012456?logo=powershell&logoColor=white)
![Docker](https://img.shields.io/badge/-Docker-2496ED?logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/-GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)
![Git](https://img.shields.io/badge/-Git-F05032?logo=git&logoColor=white)
![Node.js](https://img.shields.io/badge/-Node.js-43853D?logo=node.js&logoColor=white)
![npm](https://img.shields.io/badge/-npm-CB3837?logo=npm&logoColor=white)
![Elastic](https://img.shields.io/badge/-Elastic-005571?logo=elastic&logoColor=white)
![Terraform](https://img.shields.io/badge/-Terraform-7B42BC?logo=terraform&logoColor=white)
![Trivy](https://img.shields.io/badge/-Trivy-0A0A0A?logo=aquasecurity&logoColor=white)
![detect-secrets](https://img.shields.io/badge/-detect--secrets-2B7A78?logo=python&logoColor=white)
![git-filter-repo](https://img.shields.io/badge/-git--filter--repo-4B6F9C?logo=git&logoColor=white)
![GitHub CLI](https://img.shields.io/badge/-gh%20cli-000000?logo=github&logoColor=white)

Core focus areas: DevSecOps, Infrastructure-as-Code, CI/CD automation, container security, and observability.

## Weekly time graph

![Time graph](./assets/timegraph.svg)

## Recent changes (aggregate across workspace)

Summary of the most recent commits across active repositories:

- 2025-11-05 — kalvinparker/ELK-Stack — 59ba1eb — chore: add .secrets.baseline and detect_secrets_ELK-Stack.out files
- 2025-11-05 — kalvinparker/getting-started-todo-app — a7a15a4 — chore: add initial .markdownlint.json configuration for markdown linting
- 2025-11-05 — kalvinparker/mywebsite — 15948a0 — Add .secrets.baseline and detect_secrets_mywebsite.out files for secret detection configuration
- 2025-11-08 — kalvinparker/secure-gemini — 4f49657 — ci: add GHCR debug login step (fix duplicate)
- 2024-09-21 — kalvinparker/KSyP.tech — 8c51a43 — Update fundamental-secuurity-concepts.md
- 2025-11-08 — kalvinparker/kalvinparker — 1cfaa7d — chore: update CHANGES.md and README snapshot

### Recent workspace-wide updates (Nov 2025)

- CI & Actions reliability: Fixed a failing composite local action (`.github/actions/set-topics`) by adding an explicit `shell: bash`, ensuring `actions/checkout` runs before the action, and switching `npm ci` to `npm install --silent` for runners without lockfiles. This stabilized the `ci.yml` workflow across repositories.
- README automation: Added a generator and scheduled/dispatchable workflow to keep a synchronized 'Recent changes' summary across repos (generates `CHANGES.md`/README snapshots).
- Sonar pilot: Created a SonarCloud pilot project (`Sonarcube`) and programmatically created a custom Quality Gate (id: 136670, name: `kalvinparker_default_gate`). Attachment to the project requires an organization admin (attach attempt returned a 403 due to token/org permission mismatch).
- Enforce new-code checks in CI: Added `.github/workflows/enforce-new-code.yml` and `scripts/enforce_sonar_new_code.sh` to enforce these New Code conditions on PRs (coverage >= 80%, duplication <= 3%, ratings A for maintainability/reliability/security, 100% Security Hotspots Reviewed, and no new bugs/vulnerabilities). This acts as a fallback if the custom Quality Gate cannot be attached automatically.
- Secure-gemini sensitive blob: Prepared an `expunge_blob.ps1` helper and support-request template to remove a sensitive tracked blob (SHA: `23ef0d0af42e0a296096c22121ad99a52f00d237`) from `secure-gemini` history. Remote purge is pending coordination with repository admins and/or GitHub support due to push-protection.

Next actions:

- Ask a SonarCloud organization admin to attach Quality Gate id `136670` to the project `kalvinparker_Sonarcube` (PowerShell/curl helpers are available under `Sonarcube/` for admins).
- Run the markdown auto-fixer in a feature branch to address outstanding markdownlint errors and re-enable stricter lint rules.
- Coordinate the remote expunge for `secure-gemini` so the rewritten release branch can be pushed.

If you'd like, I can open a PR with the auto-fixes for markdown, wire the enforcement workflow to branch protection, or prepare the support request text for GitHub to assist with the blob purge.

Note: these entries are pulled from the repositories listed in `.github/scripts/repos.txt`.

---

*This README is partially generated by GitHub Actions. See `.github/workflows/` for automation.*

---

## **I**n **O**ther **N**ews

* **🛡️ Security policy:** Review our security policy, including reporting instructions and support expectations — see [SECURITY.md](SECURITY.md).
* **📜 Project log:** Discover recent updates, features, and improvements for this repository — see [CHANGES.md](CHANGES.md).
* **⚖️ License details:** Find the official license and terms for using this project — see [LICENSE](LICENSE).

---

---

---

---

---

---
