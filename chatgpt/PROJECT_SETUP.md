# ChatGPT Project setup

## Why Projects

Long procedural instructions should not depend on ordinary account memory. ChatGPT Projects provide a shared context layer using project instructions, project files, and conversations within that project.

## Recommended structure

### 1. Clinical and Infectious Diseases

Add these files:

- `BHANU_AI_OPERATING_SYSTEM.md`
- `.agents/skills/evidence-first-medical-review/SKILL.md`
- `.agents/skills/clinical-case-consultation/SKILL.md`
- `.agents/skills/session-worklog/SKILL.md`

Move clinical case discussions, guideline reviews, transplant/ICU infection work, antimicrobial dosing, and AMSP work into this Project.

### 2. Research and Publications

Add these files:

- `BHANU_AI_OPERATING_SYSTEM.md`
- `.agents/skills/research-protocol-publication/SKILL.md`
- `.agents/skills/evidence-first-medical-review/SKILL.md`
- `.agents/skills/artifact-production-qa/SKILL.md`
- `.agents/skills/session-worklog/SKILL.md`

Move protocols, IEC/IRB revisions, manuscripts, case reports, grants, questionnaires, and publication work into this Project.

### 3. Software, GitHub, and Trading Bot

Add these files:

- `BHANU_AI_OPERATING_SYSTEM.md`
- `.agents/skills/robust-repo-change/SKILL.md`
- `.agents/skills/session-worklog/SKILL.md`

Connect the relevant GitHub repository. Keep repository-specific architecture and validation in that repository's `AGENTS.md` and tests.

### 4. Documents and Administration

Add these files:

- `BHANU_AI_OPERATING_SYSTEM.md`
- `.agents/skills/artifact-production-qa/SKILL.md`
- `.agents/skills/session-worklog/SKILL.md`

Use for letters, health bulletins, workshop schedules, Word documents, spreadsheets, PDFs, and presentations.

## Project instructions

Use the first sections of `BHANU_AI_OPERATING_SYSTEM.md` as Project instructions. Keep the complete file uploaded as project knowledge so task-specific routing remains available.

## Continuing work in another chat

At the end of substantial work, create a `session-worklog` entry and save it to the Project. The next chat should read the latest worklog and authoritative artifact rather than relying on a full transcript replay.

## Updating the common source

1. Edit and validate this GitHub repository through a PR.
2. After merge, replace the corresponding Project file when the workflow materially changes.
3. Do not upload patient-identifiable or confidential institutional material into this public repository.
