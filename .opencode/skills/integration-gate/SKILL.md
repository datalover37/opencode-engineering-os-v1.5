---
name: integration-gate
description: Integrate only exact review-approved commits in dependency order using a dedicated worktree and full verification.
compatibility: opencode
metadata:
  owner: engineering-os
  version: "1.0"
---

# Integration gate

## Preconditions

For every task, require:

- task contract;
- review artifact with `verdict: APPROVED`;
- matching task ID, branch, and exact commit;
- declared dependency and merge order;
- integration verification commands.

Stop on missing, rejected, stale, or mismatched review data.

## Procedure

1. Fetch remotes.
2. Confirm every approved SHA belongs to its stated branch.
3. Create or reuse a dedicated integration worktree and branch from the stated
   base branch.
4. Integrate in dependency order.
5. Resolve only mechanical conflicts consistent with approved contracts.
6. Stop for architecture or behavior decisions.
7. Run full verification and inspect Git history/diff.
8. Push the integration branch without force.
9. Report exact branch, SHA, verification, risks, and PR next action.
