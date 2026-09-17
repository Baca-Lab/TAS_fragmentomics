import pyranges as pr
import pandas as pd
import os

site_erp = pr.read_bed('./sites/ER_pos_ATAC_hg19.bed').df.reset_index(drop=True)
site_ern = pr.read_bed('./sites/ER_neg_ATAC_hg19.bed').df.reset_index(drop=True)

def processing(site_b, label):
    site_b['mid']=(site_b['Start']+site_b['End'])//2
    site_b['Start']=site_b['mid']-5500
    site_b['End']=site_b['mid']+5500
    site_b['site']=label
    site_b['index']=label+site_b.index.astype(str)
    site_b = pr.PyRanges(site_b)

    black = pr.read_bed('./sites/hg19-blacklist.v2.bed')
    black_ov = site_b.overlap(black).df['index']
    site_bf = site_b[~site_b.index.isin(black_ov)]
    print(len(site_b), 'to', len(site_bf))
    return site_bf


site_erp = processing(site_erp, 'ATAC_ERP').df
site_ern = processing(site_ern, 'ATAC_ERN').df

sites = pd.concat([site_erp, site_ern], axis=0)
sites = sites[sites['Start']>0]

if not os.path.isdir('./intermediate'):
    os.mkdir('./intermediate')
sites[['Chromosome', 'Start', 'End', 'site']].to_csv('./intermediate/ATAC_sites.bed', sep='\t', index=False, header=False)
