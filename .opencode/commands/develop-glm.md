---
description: Execute one task with the general developer using the configured GLM model.
agent: developer
subtask: true
model: opencode/big-pickle
---

Execute one task contract through the full worktree delivery workflow.

Arguments must contain:

1. the task YAML path;
2. optionally, a review artifact path for a correction pass.

Read every supplied file completely. Implement, verify, commit, push, and return
the structured completion report required by the developer agent.

$ARGUMENTS
