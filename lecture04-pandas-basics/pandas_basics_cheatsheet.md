# Pandas Basics Cheatsheet

Summary of concepts from `01_pandas_basics.ipynb`.

## Imports
```python
import pandas as pd
import numpy as np
```

## Pandas Series
One-dimensional array-like object containing a sequence of values and an associated array of data labels, called its index.

### Creation
```python
# From a list
ps = pd.Series(["a", 2, np.pi, 36])

# From a dictionary (keys become index)
dc_city_pop = {'Tokyo': 37339804, 'Delhi': 31181376}
ps_city_pop = pd.Series(dc_city_pop)

# With explicit data and index
ps = pd.Series(
    data=["mozzarella", "schnitzel"],
    index=["appetizer", "main"]
)
```

### Accessing Data
```python
# Values and Index
ps.values  # array of values
ps.index   # index object

# Slicing (like lists)
ps[1:3]

# By Index Label (.loc)
ps.loc[["appetizer", "main"]]

# By Position (.iloc)
ps.iloc[1:3]
```

## Pandas DataFrames
Two-dimensional, size-mutable, potentially heterogeneous tabular data.

### Creation
```python
# Concatenating Series (axis=1 for columns)
df_cities = pd.concat([ps_city_pop, ps_city_countries], axis=1)

# From list of lists
data = [["Tokyo", 37339804, "Japan"], ["Delhi", 31181376, "India"]]
df_cities_ = pd.DataFrame(data=data, columns=["city", "population", "country"])
```

### Column Management
```python
# Renaming columns (assigning list)
df_cities.columns = ['population', 'country']

# Renaming specific columns (using dict)
df_cities.rename({"index": "city"}, axis="columns", inplace=True)

# Reordering columns
df_cities = df_cities[["city", "country", "population"]]
```

### Index Management
```python
# Reset index (moves index to a column)
df_cities.reset_index(drop=False, inplace=True)
```

### Slicing and Filtering DataFrames

#### By Position (`.iloc`)
```python
# Rows 2 to 5
df_cities.iloc[2:5]

# Rows 2 to 5, Column 1
df_cities.iloc[2:5, 1]
```

#### By Label (`.loc`)
```python
# Specific rows by index label
df_cities.loc[["Shanghai", "Dhaka"]]

# Specific rows and specific column
df_cities.loc[["Shanghai", "Dhaka"], "country"]

# Range of labels
df_cities.loc["Tokyo":"Sao Paulo"]
```

#### Boolean Indexing (Filtering)
```python
# Filter by condition
df_cities[df_cities.population > 30_000_000]

# Filter by list membership (.isin)
df_cities[df_cities.country.isin(["Japan", "India"])]

# NOT in list (~)
df_cities[~df_cities.country.isin(["Japan", "India"])]
```

## Inspection
```python
# DataFrame summary
df_cities.info()

# Dimensions (rows, columns)
df_cities.shape
df_cities.shape[0] # row count
```
