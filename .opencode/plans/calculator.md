# Calculator

## Objective

Add a minimal Python calculator library with `add(a, b)` and `subtract(a, b)` plus standard-library `unittest` coverage.

## Current state

The repository currently contains Engineering OS artifacts only. There is no existing Python library layout, no `src/` tree, and no `tests/` suite.

## Proposed design

Implement a single module at `src/calculator.py` that exposes `add(a, b)` and `subtract(a, b)`. Each function should accept only `int` and `float` operands while explicitly rejecting `bool` and all other types with `TypeError`. Add `unittest` coverage under `tests/` for valid integer and float operations plus invalid-type rejection behavior.

## Alternatives considered

- Add a shared internal validator helper inside `src/calculator.py` to centralize type checks. Recommended because it keeps behavior consistent without expanding scope beyond one small module.
- Inline validation separately in each public function. Simpler initially, but easier to drift if behavior changes.

## Interfaces and assumptions

- Public interface: `add(a, b) -> int | float`, `subtract(a, b) -> int | float`
- Accepted inputs: `int`, `float`
- Rejected inputs: `bool` and every non-numeric or non-supported type via `TypeError`
- Assumes tests can import the module directly from the repository layout used by the developer task.

## Dependency graph

- T01 calculator implementation

## Task summary

- T01 creates `src/calculator.py` and `tests/` coverage within the allowed writable scope.

## Parallelization

No parallel work. The feature is constrained to exactly one implementation task.

## Verification strategy

- Required feature verification: `python3 -m unittest discover -s tests -v`
- Repository hygiene checks in the task contract: `git diff --check`, `git status --short`, `git rev-parse HEAD`

## Integration strategy

After planning artifacts are committed to `main`, execute T01 in its isolated worktree on `agent/T01-calculator`, then run review and integration per `AGENTS.md`.

## Risks and blockers

- Import-path assumptions must remain simple because the task scope does not permit broader packaging/config changes.
- `bool` is a subclass of `int` in Python, so the implementation must reject it explicitly rather than relying on `isinstance(x, (int, float))` alone.
