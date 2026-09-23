from multimodal_self_regulation_lab.synthetic import make_multimodal
from multimodal_self_regulation_lab.core import ablation_table,reliability_fused_score

def test_ablation_and_fusion():
    d=make_multimodal(150,4); a=ablation_table(d); assert len(a)==4; assert a.auc.between(0,1).all(); s=reliability_fused_score(d); assert len(s)==len(d); assert ((s>=0)&(s<=1)).all()
