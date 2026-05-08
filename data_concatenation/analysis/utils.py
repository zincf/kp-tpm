import pandas as pd
import anndata as ad
from data_concatenation.analysis.genelist import ordered_plot_genes

### Merge gene name from annotation with expression
'''
Input: Expression and annotation dataframe
Output: Gene names merged with expression dataframe
'''
def annot_merge(expression:pd.DataFrame, annotation:pd.DataFrame) -> pd.DataFrame:

    expression.insert(1, "genes", annotation['Symbol'])

    return expression

### Extract relevant information from the series matrix
'''
Input: Matrix dataframe
Output: Filtered matrix dataframe - geo accession and characteristics
Warning: Relevant sample characteristics must be labelled as "...ch1-cell_type" and/or "...ch1-response and/or "...ch1-others"
'''
def mtx_extract(matrix: pd.DataFrame) -> pd.DataFrame:

    response = matrix[matrix['!Sample_title'].isin(
        ['!Sample_geo_accession', '!Sample_characteristics_ch1-cell_type', '!Sample_characteristics_ch1-response', '!Sample_characteristics_ch1-others', '!Sample_characteristics_ch1-others2'])]
    response.columns = response.iloc[0] # set geo accession as column labels
    response_processed = response.iloc[1:].reset_index(drop=True)

    return response_processed

### Merge relevant information from series matrix with expression
'''
Input: Expression and matrix dataframe, both with GEO accession as df.columns
Output: Concatenated expression and matrix dataframe matched with GEO accession
Warning: GeneID column is dropped
'''
def mtx_merge(expression: pd.DataFrame, matrix: pd.DataFrame) -> pd.DataFrame:

    expression_processed = pd.concat([expression.iloc[:0], matrix, expression.iloc[0:]], ignore_index=True)
    expression_cleaned = expression_processed.drop('GeneID', axis = 1)

    ### Quality check
    # expression_cleaned.to_csv("expression_cleaned.csv")
    # print("expression_cleaned")
    # print(expression_cleaned)

    return expression_cleaned

### Take average gene expression based on differential conditions
'''
Input: Cleaned expression dataframe, with GEO succession as columns and numerical indicies
Output: Average gene expression based on combinatorial categorization of metadata rows
Warning: Indices must be numerical

Metadata rows are stacked at the top and have NaN in the 'genes' column. 
Stop once real gene rows begin.
'''
def avg_expression(expression: pd.DataFrame) -> pd.DataFrame:

    indices = []
    response_status = "_"

    for l in range (0, len(expression)):
        if pd.isna(expression.loc[l, 'genes']):
            indices.append(l)
        else:
            break

    for l in indices:
        response_status += expression.loc[l] + "_"

    expression_processed = expression.drop(index = indices).set_index('genes') # gene names are now the indicies

    ### Quality Check
    # print("expression_processed")
    # print(expression_processed)

    expression_processed_mean = expression_processed.T.groupby(response_status).mean().dropna()

    return expression_processed_mean.T

### Extract expression data for relevant genes
'''
Input: Expression dataframe
Output: Filtered expression dataframe
'''
def filtered_expression(expression: pd.DataFrame) -> pd.DataFrame:

    ordered_genes_present = [g for g in ordered_plot_genes if g in expression.index]
    expression_filtered_str = expression.loc[ordered_genes_present]
    expression_filtered_float = expression_filtered_str.apply(pd.to_numeric, errors="coerce")

    # Print df.column for labelling
    # print(expression_filtered_float.columns.values)

    return expression_filtered_float

### Rename groups in filtered expression dataframe for plotting purposes
'''
Input: Filtered expression dataframe
Output: Renamed expression dataframe from dict.py and export dataframe as a csv file.
'''
def rename_groups(expression: pd.DataFrame, mapping: dict, succession: str) -> pd.DataFrame:

    expression = expression.copy()
    ordered_original = [col for col in mapping if col in expression.columns]
    remaining_original = [col for col in expression.columns if col not in mapping]
    expression = expression[ordered_original + remaining_original]
    expression.columns = [mapping.get(col, col) for col in expression.columns]

    # Export dataframe as csv
    # expression.to_csv(f'{succession}.csv')

    return expression

### Convert filtered expression dataframe to anndata for plotting purposes
'''
Input: Expression dataframe
Output: Anndata format of expression dataframe for sc.pl plotting
'''
def dataframe_to_anndata(expression: pd.DataFrame) -> ad.AnnData:
    adata = ad.AnnData(X=expression.T)
    adata.obs_names = expression.columns.values.tolist()
    adata.var_names = expression.index.values.tolist()
    adata.obs["group"] = adata.obs_names
    return adata
