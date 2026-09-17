import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ranksums
import numpy as np

res = pd.read_csv('./output/demo_pfTAS_ratio.csv', index_col=0)
sheet = pd.read_csv('./data/table_s1_sub_pmid_37865722.csv',index_col=0)

erp = sheet[sheet['cancer_subtype'].isin(['ER+', 'ER+,HER2+'])].index
ern = list(set(sheet.index)-set(erp))


_plot = res['pfTAS_ERP_ERN']
x1 = _plot.loc[erp].dropna()
x2 = _plot.loc[ern].dropna()

p = ranksums(x1, x2)[-1]

plt.figure(figsize=(3, 3))

plt.boxplot([x1, x2], widths=0.5, showfliers=False)

plt.scatter(1 + np.random.normal(0, 0.1, len(x1)), x1, alpha=0.7, s=20)
plt.scatter(2 + np.random.normal(0, 0.1, len(x2)), x2, alpha=0.7, s=20)

plt.xticks([1, 2], ["ER+", "ER-"])
plt.title(f"p = {p:.2e}")
plt.ylabel('pfTAS ratio \n(ER+ ATAC / ER- ATAC)')
plt.tight_layout()
plt.savefig('./output/demo_plot.png', dpi=300, bbox_inches='tight', facecolor='white')