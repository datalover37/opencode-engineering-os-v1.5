# OpenCode Engineering OS v1.5

A project-local, manual-dispatch multi-agent workflow for OpenCode.

It deliberately avoids custom tools, SDK orchestration, parsers, queues, and
state machines. OpenCode handles each role; the user manually advances the
workflow with a few commands.

## Flow

```text
/feature
  → leader creates plan + task YAML
  → user reviews and commits artifacts
/develop-deepseek or /develop-glm
  → developer uses worktree, tests, commits, pushes
/review
  → reviewer writes APPROVED or CHANGES_REQUESTED artifact
/develop-* again when needed
/integrate
  → integrator combines only approved commits
```

## Structure

```text
.
├── opencode.jsonc
├── AGENTS.md
├── README.md
├── .gitignore
├── docs/
│   └── POC.md
└── .opencode/
    ├── agents/
    │   ├── leader.md
    │   ├── developer.md
    │   ├── reviewer.md
    │   ├── researcher.md
    │   └── integrator.md
    ├── commands/
    │   ├── feature.md
    │   ├── develop.md
    │   ├── develop-deepseek.md
    │   ├── develop-glm.md
    │   ├── review.md
    │   ├── research.md
    │   └── integrate.md
    ├── skills/
    │   ├── task-contract/SKILL.md
    │   ├── worktree-delivery/SKILL.md
    │   ├── independent-review/SKILL.md
    │   └── integration-gate/SKILL.md
    ├── templates/
    ├── plans/
    ├── tasks/
    ├── reviews/
    └── model-profiles.md
```

## Configure model commands

List exact IDs:

```bash
oc models
```

Replace:

```text
REPLACE_DEEPSEEK_MODEL_ID
REPLACE_GLM_MODEL_ID
```

in:

```text
.opencode/commands/develop-deepseek.md
.opencode/commands/develop-glm.md
```

Check:

```bash
grep -R "REPLACE_" .opencode/commands
```

The generic `/develop` command has no model override; its subagent inherits the
current primary model.

## Initialize

```bash
git init -b main
git add .
git commit -m "chore: initialize OpenCode Engineering OS v1.5"
```

Add an `origin` remote because the developer and integrator are required to
push branches.

```bash
git remote add origin git@github.com:<username>/<repo>.git
git push -u origin main
```

Start:

```bash
oc
```

Only `leader` appears in the primary-agent switcher. The other roles are
subagents and appear under `@` autocomplete or are invoked by commands.

## First test

Follow [`docs/POC.md`](docs/POC.md).

## Manual control is intentional

The user decides when to:

- accept the leader's task decomposition;
- choose DeepSeek, GLM, or the current model;
- send a commit to review;
- request another correction pass;
- integrate approved work.

This retains role separation, worktree isolation, independent review, and model
choice without maintaining a workflow engine.
