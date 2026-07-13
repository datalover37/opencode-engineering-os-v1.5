# POC: calculator through the manual Engineering OS

This POC uses Python's standard-library `unittest`; no `uv`, pytest, or package
installation is required.

## 1. Start OpenCode

```bash
oc
```

Select a strong model for the primary `leader` agent.

## 2. Create plan and task artifacts

```text
/feature Build a small Python calculator library.

Requirements:
- create src/calculator.py
- provide add(a, b)
- provide subtract(a, b)
- accept int and float only
- reject bool and every other type with TypeError
- create standard-library unittest tests under tests/
- use no third-party dependencies

Constraints:
- create exactly one implementation task
- feature slug: calculator
- task ID: T01
- base branch: main
- branch: agent/T01-calculator
- worktree: .worktrees/T01-calculator
- allowed paths: src/** and tests/**
- verification: python3 -m unittest discover -s tests -v
```

Expected artifacts:

```text
.opencode/plans/calculator.md
.opencode/tasks/T01-calculator.yaml
```

Review them, then commit so the task is visible from new worktrees:

```bash
git add .opencode/plans .opencode/tasks
git commit -m "docs: plan calculator feature"
git push
```

## 3. Implement

After replacing the model placeholder in the command file:

```text
/develop-deepseek .opencode/tasks/T01-calculator.yaml
```

Alternative:

```text
/develop-glm .opencode/tasks/T01-calculator.yaml
```

The developer should create the worktree, implement, run tests, commit, push,
and return a full commit SHA.

## 4. Review

Use the exact SHA returned by the developer:

```text
/review .opencode/tasks/T01-calculator.yaml agent/T01-calculator <FULL_SHA> .opencode/reviews/T01-calculator.yaml
```

Inspect:

```bash
cat .opencode/reviews/T01-calculator.yaml
```

### When changes are requested

Run a correction pass with the task and review artifact:

```text
/develop-glm .opencode/tasks/T01-calculator.yaml .opencode/reviews/T01-calculator.yaml
```

Then review the new exact SHA again, overwriting/updating the same review file.

### When approved

Commit the review artifact for auditability:

```bash
git add .opencode/reviews/T01-calculator.yaml
git commit -m "docs: approve calculator task T01"
git push
```

## 5. Integrate

```text
/integrate Base branch: main
Integration branch: integration/calculator
Task: .opencode/tasks/T01-calculator.yaml
Review: .opencode/reviews/T01-calculator.yaml
Merge order: T01
Verification: python3 -m unittest discover -s tests -v
```

The integrator should push `integration/calculator`. Open a pull request from
that branch to `main`.

## Useful Git inspection

```bash
git worktree list
git branch -a
git log --oneline --all --decorate --graph
```
