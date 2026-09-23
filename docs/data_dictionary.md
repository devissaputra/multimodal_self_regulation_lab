# Data dictionary

The baseline code documents its expected columns directly in `src/multimodal_self_regulation_lab/core.py` and `src/multimodal_self_regulation_lab/synthetic.py`. This keeps the schema close to the executable logic.

## Principles

- Use the minimum data needed for the research question.
- Separate identifiers from analytic features.
- Record provenance for derived variables.
- Treat missingness as information about the measurement process, not merely a nuisance.
- Never convert a research proxy into a high-stakes label without validation.
