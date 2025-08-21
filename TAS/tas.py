# Author: Garyoung Gary Lee

import pandas as pd
import numpy as np
import warnings

def pfTAS(frag_df, c_w, aggreated):
    c_w = c_w.loc[:,-5000:4590]
    weight = c_w.median(axis=1)
    
    if aggreated:
        weighted = frag_df.multiply(weight, axis=0)
    else:
        weighted = frag_df.sum(axis=1)*weight
    tas_nu = weighted[weighted>0].sum()
    tas_de = -weighted[weighted<0].sum()
    pftas = tas_nu/tas_de
    return pftas


def TAS(frag_df, c_w, d_sig=1000):
    c_w = c_w.loc[:,-5000:4590]
    d_w = pd.Series({x:np.exp((-1/2)*(x/d_sig)**2) for x in c_w.columns})
    weight = c_w*d_w
    
    weighted = frag_df*weight
    weighted = weighted.loc[:,-5000:4950]
    tas_nu = weighted[weighted>0].sum().sum()
    tas_de = -weighted[weighted<0].sum().sum()
    tas = tas_nu/tas_de
    return tas

def get_tas(frag_path, ge, mode, aggreated):
    frag_df = pd.read_csv(frag_path, index_col=0)
    if aggreated==False:
        try:
            frag_df.columns = frag_df.columns.astype(float)
        except:
            raise ValueError('Input matrix should be distance (column) X fragment size (row)')
    frag_df.index = frag_df.index.astype(float)
    
    if ge=='enhancer':
        cij = pd.read_csv('./correlation_matrix/enhancer_smoothed.csv', index_col=0)
    elif ge=='promoter':
        cij = pd.read_csv('./correlation_matrix/promoter_smoothed.csv', index_col=0)
    else:
        raise ValueError('Please specify either enhancer or promoter')
    cij.columns = cij.columns.astype(float)
    cij.index = cij.index.astype(float)
    
    # test
    if aggreated==True:
        try:
            frag_df.columns = frag_df.columns.astype(float)
            
            if len(set(frag_df.columns)-set(cij.columns))==0:
                warnings.warn('-a (--agg) is set to True, but your input does not appear to be aggregated', UserWarning)
        except:
            pass
    
    
    if mode == 'TAS' and aggreated==False:
        tas = TAS(frag_df, cij)
    elif mode =='pfTAS' and aggreated==False:
        tas = pfTAS(frag_df, cij, False)
    elif mode =='pfTAS' and aggreated==True:
        tas = pfTAS(frag_df, cij, True)
    else:
        raise ValueError('Please specify either TAS or pfTAS. TAS is, by definition, incompatible with aggreated = True')
    return tas