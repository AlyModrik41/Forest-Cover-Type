import nbformat
import os

# Load the notebook
notebook_path = "/mnt/data/Forest Cover Type.ipynb"
with open(notebook_path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

# Extract useful information: imports, models used, plots, etc.
imports = []
models = []
plots = []
metrics = []

for cell in nb.cells:
    if cell.cell_type == "code":
        src = cell.source.lower()
        if "import" in src:
            imports.append(cell.source)
        if "randomforest" in src or "xgb" in src or "logistic" in src or "svm" in src:
            models.append(cell.source)
        if "plt.plot" in src or "plt.savefig" in src:
            plots.append(cell.source)
        if "accuracy" in src or "classification_report" in src or "roc_auc" in src:
            metrics.append(cell.source)

imports = list(set(imports))
models = list(set(models))

imports[:5], models[:5], len(plots), len(metrics)
