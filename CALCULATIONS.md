# Calculation guide

## Question and evidence

Does combining modalities improve synthetic prediction?

Simulated interaction, attention-like and self-report features with missingness and reliability values.

**Status:** SYNTHETIC / RULE-BASED PROTOTYPE | no educational validity claim.

## Design

Shared 70/30 stratified holdout; train-only imputation/scaling; modality ablations and a test-batch rank-fusion comparator.

## Calculation and interpretation

`Fusion = (interaction_rank + reliabilityA×attention_rank + reliabilityR×report_rank)/(1+reliabilityA+reliabilityR).`

The classifier AUC is now held out. Rank fusion uses the unlabeled test batch and is therefore a transductive descriptive comparator, not an independently deployed predictor. Synthetic attention is not a measurement of real mental state.

## Evidence table

Selected recorded values (units and context shown). Full precision below is for traceability, not a claim of measurement precision.

| Quantity | Value | Unit / meaning | JSON path |
|---|---:|---|---|
| interaction_auc | 0.761 | unitless | `interaction_auc` |
| attention_auc | 0.734 | unitless | `attention_auc` |
| self_report_auc | 0.743 | unitless | `self_report_auc` |
| early_fusion_auc | 0.802 | unitless | `early_fusion_auc` |
| reliability_fusion_auc | 0.811 | unitless | `reliability_fusion_auc` |

Source: [results/demo_metrics.json](results/demo_metrics.json). Values resolve directly from this file when figures are regenerated.

This synthetic experiment compares interaction, attention-like, and self-report signals using one shared held-out partition. The revised classifier pipeline fits imputation and scaling only on training rows, correcting the earlier in-sample evaluation. A separately labeled rank-fusion comparator explores reliability weighting; neither the simulated features nor the scores validate self-regulation or attention measurement in real learners.

## Verification performed in this review

The existing suite requires unavailable dependencies; no full-suite pass is claimed. The bundled demonstration executed successfully in this review.

The figure-generation check verifies agreement between the selected source values and SVGs. It does not validate the raw dataset, fitted model, identification assumptions, or external generalization.

```bash
python scripts/build_review_figures.py
python scripts/build_review_figures.py --check
```

## Implementation map

Follow these functions to inspect each transformation. Validation helpers and private functions remain visible in the linked modules.

| Function | Purpose / documented behavior |
|---|---|
| [`main`](src/multimodal_self_regulation_lab/cli.py#L5) | Inspect the explicit implementation and its callers. |
| [`split_indices`](src/multimodal_self_regulation_lab/core.py#L12) | One shared stratified partition for all modality comparisons. |
| [`fit_auc`](src/multimodal_self_regulation_lab/core.py#L19) | Held-out AUC with imputation and scaling fitted on training rows only. |
| [`ablation_table`](src/multimodal_self_regulation_lab/core.py#L35) | Inspect the explicit implementation and its callers. |
| [`reliability_fused_score`](src/multimodal_self_regulation_lab/core.py#L52) | Inspect the explicit implementation and its callers. |
| [`make_multimodal`](src/multimodal_self_regulation_lab/synthetic.py#L3) | Inspect the explicit implementation and its callers. |

## What remains before a stronger research claim

The classifier AUC is now held out. Rank fusion uses the unlabeled test batch and is therefore a transductive descriptive comparator, not an independently deployed predictor. Synthetic attention is not a measurement of real mental state. A successful software test is not validation of a scientific construct. New experiments should state their split unit, comparator, outcome, uncertainty procedure and failure criteria before examining final test results.
