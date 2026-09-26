# Calculation reading guide: ../CALCULATIONS.md (repository root).
# Fusion = (interaction_rank + reliabilityA×attention_rank + reliabilityR×report_rank)/(1+reliabilityA+reliabilityR).
# The classifier AUC is now held out. Rank fusion uses the unlabeled test batch and is therefore a transductive descriptive comparator, not an independently deployed predictor. Synthetic attention is not a measurement of real mental state.

from __future__ import annotations
import numpy as np,pandas as pd
from sklearn.metrics import roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

def split_indices(y, seed=42, test_size=0.30):
    """One shared stratified partition for all modality comparisons."""
    from sklearn.model_selection import train_test_split
    return train_test_split(np.arange(len(y)), test_size=test_size,
                            random_state=seed, stratify=y)


def fit_auc(X, y, train_indices=None, test_indices=None):
    """Held-out AUC with imputation and scaling fitted on training rows only."""
    from sklearn.impute import SimpleImputer
    X, y = np.asarray(X), np.asarray(y)
    if train_indices is None and test_indices is None:
        train_indices, test_indices = split_indices(y)
    elif train_indices is None or test_indices is None:
        raise ValueError("Supply both train and test indices")
    if set(train_indices) & set(test_indices):
        raise ValueError("Training and test rows must be disjoint")
    model = make_pipeline(SimpleImputer(strategy="median"), StandardScaler(),
                          LogisticRegression(max_iter=500))
    model.fit(X[train_indices], y[train_indices])
    return float(roc_auc_score(y[test_indices], model.predict_proba(X[test_indices])[:, 1]))


def ablation_table(df: pd.DataFrame) -> pd.DataFrame:
    y = df.target.to_numpy()
    train, test = split_indices(y)
    groups = {
        "interaction": ["click_depth", "revision_count"],
        "attention": ["attention_stability", "focus_ratio"],
        "self_report": ["confidence", "effort"],
        "early_fusion": ["click_depth", "revision_count", "attention_stability",
                         "focus_ratio", "confidence", "effort"],
    }
    return pd.DataFrame([
        {"model": name, "auc": fit_auc(df[cols].to_numpy(), y, train, test),
         "n_train": len(train), "n_test": len(test)}
        for name, cols in groups.items()
    ])


def reliability_fused_score(df:pd.DataFrame)->np.ndarray:
    inter=(df.click_depth.rank(pct=True)+df.revision_count.rank(pct=True))/2
    att=(df.attention_stability.rank(pct=True)+df.focus_ratio.rank(pct=True))/2
    rep=(df.confidence.rank(pct=True)+df.effort.rank(pct=True))/2
    wa=df.attention_reliability.fillna(0).clip(0,1); wi=pd.Series(1.0,index=df.index); wr=df.self_report_reliability.fillna(0).clip(0,1)
    return ((wi*inter+wa*att.fillna(.5)+wr*rep.fillna(.5))/(wi+wa+wr+1e-9)).to_numpy()
