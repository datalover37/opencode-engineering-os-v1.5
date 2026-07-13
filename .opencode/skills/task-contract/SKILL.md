---
name: task-contract
description: Create concise, machine-readable implementation task contracts with explicit Git isolation, scope, acceptance criteria, verification, and deliverables.
compatibility: opencode
metadata:
  owner: engineering-os
  version: "1.0"
---

# Task contract

Use this skill when creating or revising `.opencode/tasks/*.yaml`.

## Required fields

```yaml
schema_version: 1
task_id: T01
feature: feature-slug
title: concise title
status: ready | blocked
recommended_command: /develop-deepseek

base_branch: main
branch: agent/T01-task-slug
worktree: .worktrees/T01-task-slug

depends_on: []

context:
  architecture: concise relevant context
  interfaces: []
  assumptions: []

scope:
  allowed_paths: []
  forbidden_paths:
    - .opencode/**
    - AGENTS.md
    - opencode.jsonc

requirements: []
acceptance_criteria: []

verification:
  baseline: []
  final:
    - project-specific command
    - git diff --check
    - git status --short
    - git rev-parse HEAD

deliverables:
  - implementation
  - tests
  - pushed branch
  - exact commit SHA
  - structured completion report

blockers: []
```

## Rules

- Use observable acceptance criteria.
- Prefer verification commands already used by the repository.
- Include configuration files in `allowed_paths` when the task must create or
  change test/build configuration.
- Parallel tasks must not have overlapping writable scopes unless sequencing is
  explicit.
- Do not include model IDs. Store only the recommended command/profile.
- Mark the task `blocked` when prerequisites are missing.
