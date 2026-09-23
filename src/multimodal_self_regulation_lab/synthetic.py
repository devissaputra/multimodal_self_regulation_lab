import numpy as np,pandas as pd

def make_multimodal(n=900,seed=47):
    rng=np.random.default_rng(seed); z=rng.normal(size=n); y=(z+rng.normal(0,.8,n)>0).astype(int)
    df=pd.DataFrame({'click_depth':np.clip(4+1.4*z+rng.normal(0,1.8,n),0,None),'revision_count':np.clip(2+.9*z+rng.normal(0,1.2,n),0,None),'attention_stability':np.clip(.55+.16*z+rng.normal(0,.18,n),0,1),'focus_ratio':np.clip(.6+.14*z+rng.normal(0,.16,n),0,1),'confidence':np.clip(.55+.1*z+rng.normal(0,.2,n),0,1),'effort':np.clip(.5+.12*z+rng.normal(0,.2,n),0,1),'target':y})
    df['attention_reliability']=rng.uniform(.45,1,n); df['self_report_reliability']=rng.uniform(.55,1,n)
    miss=rng.random(n)<.18; df.loc[miss,['attention_stability','focus_ratio']]=np.nan; df.loc[miss,'attention_reliability']=0
    return df
