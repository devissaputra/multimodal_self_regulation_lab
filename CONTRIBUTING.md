# Contributing

Contributions are welcome when they make the research logic easier to inspect, reproduce, or challenge.

## Before opening a pull request

1. Keep the core baseline runnable without private APIs or proprietary data.
2. Add or update tests for every behavior change.
3. Label simulated or synthetic results clearly.
4. Document new assumptions in `docs/research_design.md`.
5. Do not add real learner or teacher data to the repository.
6. Run `scripts/reproduce.sh` and confirm it completes successfully.

Small, well-argued changes are preferred to large opaque rewrites.
