---
description: Integrate review-approved task commits into a dedicated integration branch.
agent: integrator
subtask: true
---

Integrate the approved tasks described in the arguments.

Supply:

- base branch;
- integration branch;
- task YAML paths;
- matching review artifact paths;
- merge order;
- full integration verification commands.

Reject missing, stale, mismatched, or non-approved reviews. Create a dedicated
integration worktree, integrate only exact approved commits, verify, push, and
return the structured integration report.

$ARGUMENTS
