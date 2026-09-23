from __future__ import annotations
import numpy as np,pandas as pd
from sklearn.metrics import roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

def fit_auc(X,y):
    m=make_pipeline(StandardScaler(),LogisticRegression(max_iter=500)).fit(X,y); p=m.predict_proba(X)[:,1]; return float(roc_auc_score(y,p))
def ablation_table(df:pd.DataFrame)->pd.DataFrame:
    y=df.target.to_numpy(); groups={'interaction':['click_depth','revision_count'],'attention':['attention_stability','focus_ratio'],'self_report':['confidence','effort'],'early_fusion':['click_depth','revision_count','attention_stability','focus_ratio','confidence','effort']}
    rows=[]
    for name,cols in groups.items(): rows.append({'model':name,'auc':fit_auc(df[cols].fillna(df[cols].median()).to_numpy(),y)})
    return pd.DataFrame(rows)
def reliability_fused_score(df:pd.DataFrame)->np.ndarray:
    inter=(df.click_depth.rank(pct=True)+df.revision_count.rank(pct=True))/2
    att=(df.attention_stability.rank(pct=True)+df.focus_ratio.rank(pct=True))/2
    rep=(df.confidence.rank(pct=True)+df.effort.rank(pct=True))/2
    wa=df.attention_reliability.fillna(0).clip(0,1); wi=pd.Series(1.0,index=df.index); wr=df.self_report_reliability.fillna(0).clip(0,1)
    return ((wi*inter+wa*att.fillna(.5)+wr*rep.fillna(.5))/(wi+wa+wr+1e-9)).to_numpy()
