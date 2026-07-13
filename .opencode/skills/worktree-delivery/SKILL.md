---
name: worktree-delivery
description: Deliver one implementation task safely using an isolated Git worktree, scoped edits, verification, commit, push, and an evidence-based completion report.
compatibility: opencode
metadata:
  owner: engineering-os
  version: "1.0"
---

# Worktree delivery

## Before editing

1. Read the task and optional review artifact.
2. Run `git status --short`, `git branch --show-current`, and
   `git worktree list`.
3. Fetch the base branch when a remote exists.
4. If the task worktree exists, inspect and reuse it.
5. Otherwise create the task branch and worktree from the stated base branch.
6. Enter the worktree and confirm `pwd`, branch, and clean status.
7. Run baseline verification if defined.

## Implementation

- Modify only allowed paths.
- Use project conventions and the smallest correct design.
- Add tests for changed behavior.
- On a correction pass, address the review findings without unrelated cleanup.
- Stop when scope or requirements are contradictory.

## Completion

1. Run all final verification commands.
2. Run `git diff --check`.
3. Inspect `git diff` and `git status --short`.
4. Stage explicit intended files.
5. Commit with a conventional commit message.
6. Push the task branch without force.
7. Return the exact full SHA and evidence.
