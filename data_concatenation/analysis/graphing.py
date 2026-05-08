import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns
import anndata as ad
import scanpy as sc

### Plotting with scanpy heatmap function
def scanpy_matrixplot(
    adata: ad.AnnData,
    groupby: str = "group",
    figsize: tuple | None = None,
    cmap: str = "coolwarm",
    log: bool = True,
    # standard_scale: str | None = "var",
    save: str | None = None,
):
    genes = adata.var_names.tolist()
    n_genes = len(genes)
    n_groups = adata.obs[groupby].nunique()

    if figsize is None:
        width = max(8, min(int(0.35 * n_genes + 3), 27))
        height = max(5, min(int(0.55 * n_groups + 1.5), 12))
        figsize = (width, height)

    sc.set_figure_params(fontsize=12, dpi_save=300)

    mp = sc.pl.matrixplot(
        adata,
        var_names=genes,
        groupby=groupby,
        log=log,
        cmap=cmap,
        # standard_scale=standard_scale,
        figsize=figsize,
        return_fig=True,
        colorbar_title="Mean expression\nin group",
    )

    mp.make_figure()

    main_ax = mp.ax_dict.get("mainplot_ax", None)
    if main_ax is not None:
        main_ax.tick_params(axis="x", labelrotation=90, labelsize=12)
        main_ax.tick_params(axis="y", labelsize=12)

    if save is not None:
        plt.savefig(save, bbox_inches="tight", dpi=500)

    plt.show()

### Original Plotting Function in Scanpy
def scanpy_matrixplot_og(adata: ad.AnnData):
    sc.set_figure_params(fontsize=12, dpi_save=300)
    sc.pl.matrixplot(
    adata,
    var_names=adata.var_names.tolist(),
    groupby="group",
    log=True,
    cmap="coolwarm",
    )

### Heatmap graphing support function with seaborn
def sns_heatmap(expression):
    plt.figure(figsize=(6, 12))
    sns.heatmap(expression,
            norm=mcolors.LogNorm(),
            cmap="coolwarm",
            linewidths=0.5)
    plt.show()

