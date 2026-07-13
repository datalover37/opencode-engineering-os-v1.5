---
description: Independently review one exact task branch and commit, then write a review artifact.
agent: reviewer
subtask: true
---

Review one exact implementation.

Required arguments:

1. task YAML path;
2. implementation branch;
3. exact full commit SHA;
4. review artifact path under `.opencode/reviews/`.

Inspect the actual diff, run relevant verification where practical, and write
the structured review artifact. Do not modify production code.

$ARGUMENTS
