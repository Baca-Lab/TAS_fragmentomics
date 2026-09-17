import pyranges as pr
import pandas as pd
import time, glob, os
import matplotlib.pyplot as plt
import numpy as np
import multiprocessing
from multiprocessing import Pool, Manager
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--cpu', type=int, default=2)
args = parser.parse_args()

num_core = args.cpu

sheet = pd.read_csv('./data/table_s1_sub_pmid_37865722.csv', index_col=0)
sid = pd.read_csv('./data/file_name_to_sid.csv', index_col=0)
site = pr.read_bed('./intermediate/ATAC_sites.bed')

site_erp = site[site.Name=='ATAC_ERP']
site_ern = site[site.Name=='ATAC_ERN']

def run(SAMPLES, RES_erp, RES_ern):
    
    for s in SAMPLES:
        bed = pr.read_bed('./frag_bed/%s'%s)
        bed.size = bed.End-bed.Start
        bed = bed[bed.size<1000]
        
        bed_erp = bed.overlap(site_erp)
        bed_ern = bed.overlap(site_ern)
        
        
        RES_erp[sid['sample_name'][s]]=bed_erp.size.value_counts().sort_index()
        RES_ern[sid['sample_name'][s]]=bed_ern.size.value_counts().sort_index()
        
pool = multiprocessing.Pool(num_core)
m = Manager()

size_erp = m.dict()
size_ern = m.dict()
all_paths = np.array_split(list(sid.index), num_core)

pool.starmap(run, [(XXX, size_erp, size_ern) for XXX in all_paths])
pool.close()
pool.join()
size_erp = pd.DataFrame(dict(size_erp))
size_ern = pd.DataFrame(dict(size_ern))

def agg(size):
    res = {}
    for i in np.arange(19, 1005, 5):
        res[i]=size.loc[i:i+4].sum()
    return pd.DataFrame(res).T.astype(int)

size_erp = agg(size_erp.fillna(0))
size_ern = agg(size_ern.fillna(0))

size_erp.to_csv('./intermediate/temp_erp_size.csv')
size_ern.to_csv('./intermediate/temp_ern_size.csv')

import tas

res_pftas = tas.get_tas('./intermediate/temp_erp_size.csv', 'enhancer', 'pfTAS', True)/tas.get_tas('./intermediate/temp_ern_size.csv', 'enhancer', 'pfTAS', True)
res_pftas = pd.DataFrame({'pfTAS_ERP_ERN':res_pftas})
if not os.path.isdir('./output'):
    os.mkdir('./output')
res_pftas.to_csv('./output/demo_pfTAS_ratio.csv')

os.remove('./intermediate/temp_erp_size.csv')
os.remove('./intermediate/temp_ern_size.csv')