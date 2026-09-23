# Experiment roadmap

## E0 — Reproducibility baseline

Run the bundled synthetic experiment from a clean environment and verify that unit tests and stored metrics are reproducible.

## E1 — Measurement audit

Challenge the operational definitions in the baseline. Compare alternative feature definitions, quantify missingness, and document which conclusions change.

## E2 — Model or policy ablation

Remove one information source or decision rule at a time. Report not only headline performance but the cases that changed and why.

## E3 — Robustness

Stress-test thresholds, seeds, subgroup composition, measurement noise, and distribution shift. Report confidence intervals rather than a single number.

## E4 — Human-centered evaluation

Put the output in front of the people expected to use it. Measure comprehension, trust calibration, actionability, and failure recovery instead of asking only whether they “liked” the interface.

## E5 — Field validation

Only after the previous steps, evaluate the system in an authentic learning setting with appropriate ethics and data-governance procedures.
