import json

file_path = '/Users/dan.brm/Desktop/antigravity/da-coding-python/lecture01-coding-basics/coding_basics.ipynb'

with open(file_path, 'r') as f:
    notebook = json.load(f)

found = False
for cell in notebook['cells']:
    if cell['cell_type'] == 'code':
        source = cell['source']
        # source is a list of strings. Join them to check content robustly, or check exact match.
        # The view showed it as a single string in the list: "1 + 2, 1 - 2, 1 * 2, 1 / 2"
        if source and source[0].strip() == "1 + 2, 1 - 2, 1 * 2, 1 / 2":
            cell['source'] = [
                "# The input consists of four separate expressions separated by commas.\n",
                "# Python automatically packs these results into a single tuple.\n",
                "1 + 2, 1 - 2, 1 * 2, 1 / 2"
            ]
            found = True
            break

if found:
    with open(file_path, 'w') as f:
        json.dump(notebook, f, indent=1)
    print("Notebook updated successfully.")
else:
    print("Target cell not found.")
