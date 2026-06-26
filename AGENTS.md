# AGENTS.md

## Repository purpose

This repository stores reusable, evidence-backed Agent Skills and ChatGPT Project instructions for Dr Bhanu Prasad's recurring workflows. It must remain compact, auditable, platform-compatible, and free of confidential data.

## Operating rules

1. Read this file, `README.md`, and `skills-manifest.json` before editing skills.
2. Keep one skill focused on one recurring task family.
3. Put activation criteria in YAML `description`; put procedural details in the body.
4. Prefer progressive disclosure: keep `SKILL.md` concise and place large references or scripts beside it only when necessary.
5. Do not copy third-party skill text verbatim. Adapt concepts and document provenance in `THIRD_PARTY_SOURCES.md`.
6. Never add patient identifiers, clinical records, access tokens, API secrets, institutional confidential material, or proprietary documents.
7. Do not weaken source verification, medical uncertainty, software validation, or live-trading safeguards.
8. For code changes, use a branch and PR. Keep the diff narrow and run the validator before claiming completion.

## Required validation

```bash
python scripts/validate_skills.py
python -m compileall -q scripts
```

When `scripts/sync_skills.py` changes, also run a temporary-directory smoke test that copies at least one skill and confirms its `SKILL.md` exists.

## Skill requirements

Every `.agents/skills/<name>/SKILL.md` must contain:

- YAML frontmatter with `name` and `description`
- a name matching the containing directory
- sections for purpose, workflow, validation, and failure/uncertainty handling
- no raw secrets or personally identifiable patient information

## Review standard

Before merge, verify:

- the skill triggers only for its intended task family
- instructions are specific enough to execute and concise enough to load on demand
- outputs demand evidence rather than unsupported confidence
- required tools and limitations are explicit
- any adapted external concept is listed in `THIRD_PARTY_SOURCES.md`
