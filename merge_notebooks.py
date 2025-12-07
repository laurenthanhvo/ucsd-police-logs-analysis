import nbformat as nbf
from pathlib import Path

base = Path("notebooks")

files_in_order = [
    base / "PDF_Parser.ipynb",
    base / "Exploratory.ipynb",
    base / "Statistical_Analysis.ipynb",
]

merged = nbf.v4.new_notebook()
merged.cells = []

for path in files_in_order:
    nb = nbf.read(path, as_version=4)

    title = f"# Notebook: {path.name}\n"
    merged.cells.append(nbf.v4.new_markdown_cell(title))

    merged.cells.extend(nb.cells)

out_path = base / "Final_Notebook.ipynb"
nbf.write(merged, out_path)
print("Wrote merged notebook to:", out_path)
