# Dr Bhanu Prasad — Personal AI Skills System

This repository is the canonical source for reusable workflows used across ChatGPT Projects, Codex, GitHub repositories, clinical research, medical evidence review, document production, and software engineering.

## Design

The system separates three kinds of context:

1. **Stable operating rules** — `chatgpt/BHANU_AI_OPERATING_SYSTEM.md`
2. **Task-specific skills** — `.agents/skills/<skill-name>/SKILL.md`
3. **Repository-local truth** — each software repository's own `AGENTS.md`, architecture documents, tests, and runbooks

This separation prevents one oversized prompt from mixing medical, research, document, and coding instructions.

## Available skills

| Skill | Use |
|---|---|
| `evidence-first-medical-review` | Current, citation-backed infectious-disease and medical literature synthesis |
| `clinical-case-consultation` | Structured clinical reasoning, differential diagnosis, investigations, treatment, monitoring, and uncertainty |
| `research-protocol-publication` | Protocols, IEC/IRB responses, manuscripts, case reports, grants, and reporting-guideline compliance |
| `robust-repo-change` | Root-cause diagnosis, narrow implementation, regression testing, PR review, CI validation, and merge discipline |
| `artifact-production-qa` | Professional DOCX, PDF, spreadsheet, and slide production with rendering and quality checks |
| `session-worklog` | Compact durable record of goals, decisions, changes, validation, and unresolved risks |

## ChatGPT setup

Create a dedicated ChatGPT Project and add `chatgpt/BHANU_AI_OPERATING_SYSTEM.md` as a project file. Put recurring medical, research, coding, and document chats in that Project so project memory can use the shared file and prior project conversations.

The operating file is intentionally compact. Detailed workflows remain in the skill folders and can be opened through the GitHub connector when needed.

## Codex and repository setup

Codex-compatible tools discover skills under `.agents/skills/`. To copy selected skills into another repository:

```bash
python scripts/sync_skills.py /path/to/target-repo \
  robust-repo-change session-worklog
```

Validate the catalog with:

```bash
python scripts/validate_skills.py
```

Repository-specific rules remain authoritative. A copied skill supplements, but does not override, the target repository's `AGENTS.md` and test requirements.

## Safety boundaries

- Never store patient identifiers, credentials, tokens, private keys, or confidential institutional data in this public repository.
- Medical outputs require current source verification and explicit uncertainty.
- Code completion claims require fresh tests or CI evidence.
- Live trading or production changes require repository-specific risk controls and manual review.
