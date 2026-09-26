# Research design

## Project aim

Multimodal learning analytics often jumps straight from sensor streams to a model score. This repo makes the fusion logic explicit. It simulates interaction, gaze-like attention, and self-report features, tracks missing modalities, and compares early fusion with reliability-weighted fusion.

## Research questions

1. When does adding another modality improve prediction rather than add noise?
2. How should a system react when one modality is missing or unreliable?
3. Can reliability-weighted fusion remain interpretable enough for learning-science analysis?

## Baseline analytic pipeline

1. Modal signals
2. Per-modality normalization
3. Reliability estimation
4. Fusion
5. Ablation evaluation

## Construct-to-measure discipline

The repository intentionally distinguishes **constructs** from **proxies**. A behavioral feature may be consistent with a construct without proving that construct exists. A real study should establish content validity, reliability, sensitivity to context, and convergent/discriminant evidence before attaching strong interpretations.

## Minimum empirical extension

1. Pre-register the main research question and analysis plan.
2. Recruit a context-appropriate sample with consent and a documented data-governance plan.
3. Establish annotation reliability or measurement reliability before model comparison.
4. Split exploratory analysis from confirmatory evaluation.
5. Report uncertainty, subgroup performance, missing-data patterns, and negative findings.
6. Evaluate whether the output is understandable and useful to the people expected to act on it.

## Threats to validity

- Synthetic “attention” variables are not eye-tracking measures and should not be interpreted as such.
- In-sample AUC is used only for a compact demo; real studies require held-out evaluation.
- Multimodal data raise privacy and consent issues that must be addressed before collection.

## Next experiments

- Use nested cross-validation and subgroup robustness checks.
- Add explicit sensor-quality models and late-fusion baselines.
- Test whether multimodal feedback is understandable and actionable for learners and educators.


## Evaluation correction

Classifier AUC now uses a shared seed-42 stratified 70/30 holdout. Median imputation and standardization are fitted only on training rows. The rank-fusion comparator uses ranks within the unlabeled held-out batch and is explicitly transductive. It does not fit the target labels, but should not be interpreted as a deployable independently normalized predictor.
