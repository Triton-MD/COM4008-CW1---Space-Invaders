# Space Defenders

<!-- One or two sentences: what the game is and what this wiki documents. -->

## Team and requirement ownership

The brief requires us to state which member was assigned which requirement.

| Member | GitHub username | Requirement | Code folder |
|--------|-----------------|-------------|-------------|
|        |                 | R1 Invader fleet | `game/fleet/` |
|        |                 | R2 Player combat | `game/player/` |
|        |                 | R3 Barriers      | `game/barriers/` |

## How to run

```
pip install -r requirements.txt
python main.py
```

## How to run the tests

```
pytest
```

## Workflow rules

- [ ] `main` is protected: every change goes through a pull request
- [ ] One branch per issue, e.g. `r1/fleet-speed-up`, `r2/respawn`, `r3/pixel-erosion`
- [ ] Commit messages reference the issue: `R2: add respawn invulnerability timer (#14)`
- [ ] Small, frequent, runnable commits
- [ ] Every PR is reviewed by a teammate with at least one real comment
- [ ] Tests go in the same PR as the feature
- [ ] GitHub Actions runs pytest on every PR

## Links

- Issues board: <!-- link -->
- Project board: <!-- link -->
- Releases: <!-- link -->
