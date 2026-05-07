from data_concatenation.analysis import utils, graphing

### Concatenation and plotting from utils.py and graphing.py
class Analysis:

    def __init__(self, expression, annotation, matrix, mapping):

        self.expression = expression
        self.annotation = annotation
        self.matrix = matrix
        self.mapping = mapping
        # self.GEO = GEO

    def run_analysis_and_plotting(self):

        # Preprocessing and combining dataframes
        expression_inserted = utils.annot_merge(expression=self.expression, annotation=self.annotation)
        response_processed = utils.mtx_extract(matrix=self.matrix)
        expression_cleaned = utils.mtx_merge(expression=expression_inserted, matrix=response_processed)

        # Averaging and filtering expression dataframe
        expression_processed_mean = utils.avg_expression(expression=expression_cleaned)
        filtered_expression = utils.filtered_expression(expression=expression_processed_mean)

        # Processing of expression dataframe for plotting
        renamed_expression = utils.rename_groups(filtered_expression, mapping = self.mapping)
        ad_expression = utils.dataframe_to_anndata(expression=renamed_expression)

        # Plotting scanpy matrixplot
        return graphing.scanpy_matrixplot(adata=ad_expression)

        # Plotting sns heatmap for cross-validation
        # return graphing.sns_heatmap(expression=filtered_expression)

    def run_analysis_and_plotting_without_map(self):
        expression_inserted = utils.annot_merge(expression=self.expression, annotation=self.annotation)
        response_processed = utils.mtx_extract(matrix=self.matrix)
        expression_cleaned = utils.mtx_merge(expression=expression_inserted, matrix=response_processed)

        # Averaging and filtering expression dataframe
        expression_processed_mean = utils.avg_expression(expression=expression_cleaned)
        filtered_expression = utils.filtered_expression(expression=expression_processed_mean)

        # Processing of expression dataframe for plotting
        ad_expression = utils.dataframe_to_anndata(expression=filtered_expression)

        # Plotting scanpy matrixplot
        return graphing.scanpy_matrixplot(adata=ad_expression)

        # Plotting sns heatmap for cross-validation
        # return graphing.sns_heatmap(expression=filtered_expression)

    def run_analysis_only(self):

        # Preprocessing and combining dataframes
        expression_inserted = utils.annot_merge(expression=self.expression, annotation=self.annotation)
        response_processed = utils.mtx_extract(matrix=self.matrix)
        expression_cleaned = utils.mtx_merge(expression=expression_inserted, matrix=response_processed)

        # Averaging and filtering expression dataframe
        expression_processed_mean = utils.avg_expression(expression=expression_cleaned)
        filtered_expression = utils.filtered_expression(expression=expression_processed_mean)

        # Renaming dataframe
        renamed_expression = utils.rename_groups(filtered_expression, mapping = self.mapping)
        return renamed_expression