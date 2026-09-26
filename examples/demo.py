from pathlib import Path
import json
from sklearn.metrics import roc_auc_score
from multimodal_self_regulation_lab.synthetic import make_multimodal
from multimodal_self_regulation_lab.core import ablation_table,reliability_fused_score,split_indices
root=Path(__file__).resolve().parents[1]; (root/'results').mkdir(exist_ok=True)
d=make_multimodal(); a=ablation_table(d); train,test=split_indices(d.target.to_numpy()); heldout=d.iloc[test]; score=reliability_fused_score(heldout); rf=roc_auc_score(heldout.target,score); a.to_csv(root/'results'/'ablation.csv',index=False); d.to_csv(root/'results'/'synthetic_multimodal.csv',index=False)
metrics={r.model+'_auc':round(float(r.auc),3) for r in a.itertuples()}; metrics['reliability_fusion_auc']=round(float(rf),3); (root/'results'/'demo_metrics.json').write_text(json.dumps(metrics,indent=2)); print(json.dumps(metrics,indent=2))
