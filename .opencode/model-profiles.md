# Model profiles

Update this file before starting a feature when quota or availability changes.

## Leader

- Selected manually with `/models` in the primary `leader` session.
- Use the strongest available planning/reasoning model.

## Developer commands

- `/develop-deepseek`: preferred cheap coding profile
- `/develop-glm`: fallback cheap coding profile
- `/develop`: uses the current leader model; use only when intentional

Current availability:

- DeepSeek: available
- GLM: available

## Reviewer

- `/review` uses the current primary model because the command does not pin a
  model. Keep a strong model selected when review quality matters.

## Integrator

- `/integrate` uses the current primary model. Integration is constrained by
  exact approved commits and verification commands.
