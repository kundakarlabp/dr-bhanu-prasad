---
name: github-connected-fast-coding
description: Perform efficient repository diagnosis, implementation, validation, pull-request review, and squash merge from ordinary ChatGPT chats using the connected GitHub application without repeatedly rediscovering access or reading the whole repository.
---

# GitHub-Connected Fast Coding

## Purpose

Reduce tool calls, duplicated repository exploration, and context waste when ordinary ChatGPT chats are used for code work without a local clone, IDE, coding VM, or dedicated coding agent.

## Workflow

### 1. Confirm access once

Use the connected GitHub application as the normal repository interface. Check the repository and permission state once, then proceed. Do not repeatedly compare connector, PAT, clone, or alternative access methods after read/write access is confirmed.

Never request that a user paste a personal access token into chat when the connected GitHub application already provides the required permission.

### 2. Load compact repository context

Read only:

1. repository `AGENTS.md`
2. compact repository map or equivalent architecture file
3. task-specific skill router
4. exact files ranked for the reported error, symbol, or enhancement

Prefer repository-generated context reports containing paths, symbol signatures, ownership, related tests, and validation commands. Avoid reading the whole repository or repeatedly reopening unchanged files.

### 3. Use precise retrieval

Search in this order:

1. exact error or log event
2. exact class, function, configuration key, command, or test name
3. owning module and direct callers
4. related regression tests
5. recent commits or PRs touching the same path

Fetch complete implementation bodies only after the owning files have been identified. Preserve repository-local architecture and source-of-truth boundaries.

### 4. Diagnose before editing

- Reproduce the exact failure through a deterministic test, fixture replay, CI failure, or safe harness.
- Form falsifiable root-cause hypotheses.
- Identify affected files and files that must remain untouched.
- Distinguish the underlying defect from notification noise or secondary symptoms.
- Do not create broad refactors, duplicate owners, hidden fallbacks, or exception suppression.

### 5. Implement through a narrow branch

- Create a branch from current `main`.
- Add or update regression coverage where practical.
- Make the smallest owner-consistent correction.
- Review the complete diff before opening the PR.
- Keep unrelated optimization, refactoring, and formatting out of the same PR.

### 6. Validate efficiently

Use repository-provided changed-file-to-test planning when available. Run focused checks first for rapid feedback, then the complete required suite before merge.

Completion evidence should include:

- compilation/build success
- focused regression tests
- architecture and safety checks
- complete required suite
- final-head GitHub Actions result
- resolved valid review threads

### 7. PR and squash merge

Write a focused PR containing root cause, changed files, untouched areas, runtime impact, validation evidence, and residual risk. Address technically valid review comments and rerun CI after the final change.

Squash merge only when the user explicitly requested implementation and merge, the PR head is unchanged, all required checks pass, and valid review threads are resolved. Otherwise leave the PR open.

## Efficiency rules

- Reuse already fetched repository facts within the task.
- Do not repeatedly verify the same permission, branch, file, or CI result.
- Batch independent reads and searches when the tool supports it.
- Prefer compact symbol/signature maps over complete file dumps for orientation.
- Use exact paths and current blob SHAs for writes.
- Treat GitHub Actions as independent final validation, not as a substitute for root-cause analysis.
- Record durable decisions in a compact worklog after substantial work.

## Validation

Before declaring completion, verify the actual merged PR state and merge commit. Confirm that final CI corresponds to the final PR head, not an earlier commit. Report any unavailable execution or deployment step explicitly.

## Failure and uncertainty handling

When repository access, code-search indexing, branch state, CI logs, or the failure itself cannot be verified, do not improvise. State the exact missing evidence and perform the narrowest next retrieval action. Never turn intended work into completed work or claim deployment when only repository code was merged.
