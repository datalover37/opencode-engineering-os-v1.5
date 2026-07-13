# Project engineering rules

## Roles

- `leader`: analyze, plan, decompose, and create planning artifacts
- `developer`: implement one explicit task in an isolated worktree
- `reviewer`: independently inspect one exact branch and commit
- `researcher`: investigate a focused technical question without editing code
- `integrator`: combine only review-approved commits

## Manual delivery lifecycle

1. Run `/feature` with a strong planning model.
2. Review the generated plan and task files.
3. Commit planning artifacts to `main` so future worktrees can read them.
4. Run one `/develop-*` command per task.
5. Run `/review` for the exact pushed commit.
6. If review requests changes, run `/develop-*` again with the review artifact.
7. Review the new commit.
8. Run `/integrate` only after every required task is approved.
9. Open a pull request from the integration branch to `main`.

## Git safety

- Never implement directly on `main`.
- Use `agent/<task-id>-<slug>` for task branches.
- Use `integration/<feature-slug>` for integration branches.
- Use `.worktrees/<task-id>-<slug>` for task worktrees.
- Never force-push.
- Never use destructive reset or cleanup commands.
- Never commit unrelated changes.
- Never integrate an unreviewed commit.

## Task isolation

Every task must define:

- base branch
- task branch
- worktree path
- dependencies
- allowed paths
- forbidden paths
- requirements
- acceptance criteria
- verification commands
- deliverables

Parallel tasks must have non-overlapping writable scopes and stable interfaces.

## Verification

Claims require fresh evidence. Statements such as "tests should pass" or
"the change looks correct" are not evidence.

A task is complete only when:

- required verification passes;
- intended files are committed;
- the branch is pushed;
- the exact commit SHA is reported;
- the reviewer records `APPROVED` for that exact commit.
