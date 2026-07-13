---
name: independent-review
description: Review an exact implementation commit independently against its task contract and produce an actionable approval or changes-requested artifact.
compatibility: opencode
metadata:
  owner: engineering-os
  version: "1.0"
---

# Independent review

## Inputs

- task contract
- base branch
- implementation branch
- exact commit SHA
- optional developer completion report

## Review order

1. Verify branch and exact commit.
2. Inspect the actual diff against the base branch.
3. Check allowed and forbidden paths.
4. Check requirements and acceptance criteria.
5. Assess correctness and edge cases.
6. Assess tests and verification evidence.
7. Assess error handling, security, and data integrity.
8. Assess maintainability, performance, and integration risks.

## Verdict

- `APPROVED`: no blocking issues for the exact commit.
- `CHANGES_REQUESTED`: at least one actionable blocking finding.

Use severity `BLOCKER`, `HIGH`, `MEDIUM`, or `LOW`. Any `BLOCKER` or
`HIGH` finding requires changes. Findings must identify file, line when
possible, evidence, and required change.
