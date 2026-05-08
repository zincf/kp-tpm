import pandas as pd

path = '/Users/zincf/PycharmProjects/IDO-Chemokine/data_concatenation/datasets'

### In vivo samples ###

### GSE138476 - RA (1)
expression_138476 = pd.read_csv(f'{path}/GSE138746/GSE138746_norm_counts_TPM_GRCh38.p13_NCBI.tsv', sep ='\t')
annot_138476 = pd.read_csv(f'{path}/GSE138746/Human.GRCh38.p13.annot.tsv', sep = '\t')
mtx_138476 = pd.read_csv(f'{path}/GSE138746/GSE138746_series_matrix.csv')

### GSE122612 - RA (2)
expression_122612 = pd.read_csv(f'{path}/GSE122612/GSE122612_norm_counts_TPM_GRCh38.p13_NCBI.tsv', sep ='\t')
annot_122612 = pd.read_csv(f'{path}/GSE122612/Human.GRCh38.p13.annot.tsv', sep = '\t')
mtx_122612 = pd.read_csv(f'{path}/GSE122612/GSE122612_series_matrix.csv')

### GSE118829 - RA (3)
expression_118829 = pd.read_csv(f'{path}/GSE118829/GSE118829_norm_counts_TPM_GRCh38.p13_NCBI.tsv', sep ='\t')
annot_118829 = pd.read_csv(f'{path}/GSE118829/Human.GRCh38.p13.annot.tsv', sep = '\t')
mtx_118829 = pd.read_csv(f'{path}/GSE118829/GSE118829_series_matrix.csv')

### GSE113156 - RA (4)
expression_113156 = pd.read_csv(f'{path}/GSE113156/GSE113156_norm_counts_TPM_GRCh38.p13_NCBI.tsv', sep ='\t')
annot_113156 = pd.read_csv(f'{path}/GSE113156/Human.GRCh38.p13.annot.tsv', sep = '\t')
mtx_113156 = pd.read_csv(f'{path}/GSE113156/GSE113156_series_matrix.csv')

### GSE83415 - JIA
expression_83415 = pd.read_csv(f'{path}/GSE83415/GSE83415_norm_counts_TPM_GRCh38.p13_NCBI.tsv', sep ='\t')
annot_83415 = pd.read_csv(f'{path}/GSE83415/Human.GRCh38.p13.annot.tsv', sep = '\t')
mtx_83415 = pd.read_csv(f'{path}/GSE83415/GSE83415_series_matrix.csv')

### GSE149050 - SLE
expression_149050 = pd.read_csv(f'{path}/GSE149050/GSE149050_norm_counts_TPM_GRCh38.p13_NCBI.tsv', sep ='\t')
annot_149050 = pd.read_csv(f'{path}/GSE149050/Human.GRCh38.p13.annot.tsv', sep = '\t')
mtx_149050 = pd.read_csv(f'{path}/GSE149050/GSE149050_series_matrix.csv')

### GSE172009 - MS
expression_172009 = pd.read_csv(f'{path}/GSE172009/GSE172009_norm_counts_TPM_GRCh38.p13_NCBI.tsv', sep ='\t')
annot_172009 = pd.read_csv(f'{path}/GSE172009/Human.GRCh38.p13.annot.tsv', sep = '\t')
mtx_172009 = pd.read_csv(f'{path}/GSE172009/GSE172009_series_matrix.csv')

### GSE89225 - Breast Cancer
expression_89225 = pd.read_csv(f'{path}/GSE89225/GSE89225_norm_counts_TPM_GRCh38.p13_NCBI.tsv', sep ='\t')
annot_89225 = pd.read_csv(f'{path}/GSE89225/Human.GRCh38.p13.annot.tsv', sep = '\t')
mtx_89225 = pd.read_csv(f'{path}/GSE89225/GSE89225_series_matrix.csv')

### GSE233661 - HBV
expression_233661 = pd.read_csv(f'{path}/GSE233661/GSE233661_norm_counts_TPM_GRCh38.p13_NCBI.tsv', sep ='\t')
annot_233661 = pd.read_csv(f'{path}/GSE233661/Human.GRCh38.p13.annot.tsv', sep = '\t')
mtx_233661 = pd.read_csv(f'{path}/GSE233661/GSE233661_series_matrix.csv')

### In vitro samples ###

### GSE235240 - Mast Cells
expression_235240 = pd.read_csv(f'{path}/GSE235240/GSE235240_norm_counts_TPM_GRCh38.p13_NCBI.tsv', sep ='\t')
annot_235240 = pd.read_csv(f'{path}/GSE235240/Human.GRCh38.p13.annot.tsv', sep = '\t')
mtx_235240 = pd.read_csv(f'{path}/GSE235240/GSE235240_series_matrix.csv')

### GSE126116 - CD4+ T Cells
expression_126116 = pd.read_csv(f'{path}/GSE126116/GSE126116_norm_counts_TPM_GRCh38.p13_NCBI.tsv', sep ='\t')
annot_126116 = pd.read_csv(f'{path}/GSE126116/Human.GRCh38.p13.annot.tsv', sep = '\t')
mtx_126116 = pd.read_csv(f'{path}/GSE126116/GSE126116_series_matrix.csv')

### GSE200146 - DCs
expression_200146 = pd.read_csv(f'{path}/GSE200146/GSE200146_norm_counts_TPM_GRCh38.p13_NCBI.tsv', sep ='\t')
annot_200146 = pd.read_csv(f'{path}/GSE200146/Human.GRCh38.p13.annot.tsv', sep = '\t')
mtx_200146 = pd.read_csv(f'{path}/GSE200146/GSE200146_series_matrix.csv')

### GSE84204 - pDCs (1)
expression_84204 = pd.read_csv(f'{path}/GSE84204/GSE84204_norm_counts_TPM_GRCh38.p13_NCBI.tsv', sep ='\t')
annot_84204 = pd.read_csv(f'{path}/GSE84204/Human.GRCh38.p13.annot.tsv', sep = '\t')
mtx_84204 = pd.read_csv(f'{path}/GSE84204/GSE84204_series_matrix.csv')

### GSE187381 - pDCs (2)
expression_187381 = pd.read_csv(f'{path}/GSE187381/GSE187381_norm_counts_TPM_GRCh38.p13_NCBI.tsv', sep ='\t')
annot_187381 = pd.read_csv(f'{path}/GSE187381/Human.GRCh38.p13.annot.tsv', sep = '\t')
mtx_187381 = pd.read_csv(f'{path}/GSE187381/GSE187381_series_matrix.csv')

### GSE243052 - pDCs (3)
expression_243052 = pd.read_csv(f'{path}/GSE243052/GSE243052_norm_counts_TPM_GRCh38.p13_NCBI.tsv', sep ='\t')
annot_243052 = pd.read_csv(f'{path}/GSE243052/Human.GRCh38.p13.annot.tsv', sep = '\t')
mtx_243052 = pd.read_csv(f'{path}/GSE243052/GSE243052_series_matrix.csv')

### GSE135635 - pDCs (4)
expression_135635 = pd.read_csv(f'{path}/GSE135635/GSE135635_norm_counts_TPM_GRCh38.p13_NCBI.tsv', sep ='\t')
annot_135635 = pd.read_csv(f'{path}/GSE135635/Human.GRCh38.p13.annot.tsv', sep = '\t')
mtx_135635 = pd.read_csv(f'{path}/GSE135635/GSE135635_series_matrix.csv')

### GSE79272 - pDCs (5)
expression_79272 = pd.read_csv(f'{path}/GSE79272/GSE79272_norm_counts_TPM_GRCh38.p13_NCBI.tsv', sep ='\t')
annot_79272 = pd.read_csv(f'{path}/GSE79272/Human.GRCh38.p13.annot.tsv', sep = '\t')
mtx_79272 = pd.read_csv(f'{path}/GSE79272/GSE79272_series_matrix.csv')

### GSE207028 - pDCs (6)
expression_207028 = pd.read_csv(f'{path}/GSE207028/GSE207028_norm_counts_TPM_GRCh38.p13_NCBI.tsv', sep ='\t')
annot_207028 = pd.read_csv(f'{path}/GSE207028/Human.GRCh38.p13.annot.tsv', sep = '\t')
mtx_207028 = pd.read_csv(f'{path}/GSE207028/GSE207028_series_matrix.csv')

### GSE208042 - Monocytes/Macrophages (1)
expression_208042 = pd.read_csv(f'{path}/GSE208042/GSE208042_norm_counts_TPM_GRCh38.p13_NCBI.tsv', sep ='\t')
annot_208042 = pd.read_csv(f'{path}/GSE208042/Human.GRCh38.p13.annot.tsv', sep = '\t')
mtx_208042 = pd.read_csv(f'{path}/GSE208042/GSE208042_series_matrix.csv')

### GSE96800 - Monocytes/Macrophages (2)
expression_96800 = pd.read_csv(f'{path}/GSE96800/GSE96800_norm_counts_TPM_GRCh38.p13_NCBI.tsv', sep ='\t')
annot_96800 = pd.read_csv(f'{path}/GSE96800/Human.GRCh38.p13.annot.tsv', sep = '\t')
mtx_96800 = pd.read_csv(f'{path}/GSE96800/GSE96800_series_matrix.csv')

### GSE130011 - Monocytes/Macrophages (3)
expression_130011 = pd.read_csv(f'{path}/GSE130011/GSE130011_norm_counts_TPM_GRCh38.p13_NCBI.tsv', sep ='\t')
annot_130011 = pd.read_csv(f'{path}/GSE130011/Human.GRCh38.p13.annot.tsv', sep = '\t')
mtx_130011 = pd.read_csv(f'{path}/GSE130011/GSE130011_series_matrix.csv')

### GSE150571 - Monocytes/Macrophages (4)
expression_150571 = pd.read_csv(f'{path}/GSE150571/GSE150571_norm_counts_TPM_GRCh38.p13_NCBI.tsv', sep ='\t')
annot_150571 = pd.read_csv(f'{path}/GSE150571/Human.GRCh38.p13.annot.tsv', sep = '\t')
mtx_150571 = pd.read_csv(f'{path}/GSE150571/GSE150571_series_matrix.csv')

### GSE229710 - Monocytes/Macrophages (5)
expression_229710 = pd.read_csv(f'{path}/GSE229710/GSE229710_norm_counts_TPM_GRCh38.p13_NCBI.tsv', sep ='\t')
annot_229710 = pd.read_csv(f'{path}/GSE229710/Human.GRCh38.p13.annot.tsv', sep = '\t')
mtx_229710 = pd.read_csv(f'{path}/GSE229710/GSE229710_series_matrix.csv')

### GSE206333 - Monocytes/Macrophages (6)
expression_206333 = pd.read_csv(f'{path}/GSE206333/GSE206333_norm_counts_TPM_GRCh38.p13_NCBI.tsv', sep ='\t')
annot_206333 = pd.read_csv(f'{path}/GSE206333/Human.GRCh38.p13.annot.tsv', sep = '\t')
mtx_206333 = pd.read_csv(f'{path}/GSE206333/GSE206333_series_matrix.csv')

### GSE221203 - Monocytes/Macrophages (7)
expression_221203 = pd.read_csv(f'{path}/GSE221203/GSE221203_norm_counts_TPM_GRCh38.p13_NCBI.tsv', sep ='\t')
annot_221203 = pd.read_csv(f'{path}/GSE221203/Human.GRCh38.p13.annot.tsv', sep = '\t')
mtx_221203 = pd.read_csv(f'{path}/GSE221203/GSE221203_series_matrix.csv')

### GSE136107 - Monocytes/Macrophages (8)
expression_136107 = pd.read_csv(f'{path}/GSE136107/GSE136107_norm_counts_TPM_GRCh38.p13_NCBI.tsv', sep ='\t')
annot_136107 = pd.read_csv(f'{path}/GSE136107/Human.GRCh38.p13.annot.tsv', sep = '\t')
mtx_136107 = pd.read_csv(f'{path}/GSE136107/GSE136107_series_matrix.csv')

### GSE228087 - Monocytes/Macrophages (9)
expression_228087 = pd.read_csv(f'{path}/GSE228087/GSE228087_norm_counts_TPM_GRCh38.p13_NCBI.tsv', sep ='\t')
annot_228087 = pd.read_csv(f'{path}/GSE228087/Human.GRCh38.p13.annot.tsv', sep = '\t')
mtx_228087 = pd.read_csv(f'{path}/GSE228087/GSE228087_series_matrix.csv')