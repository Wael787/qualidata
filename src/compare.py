import pandas as pd

v1 = pd.read_csv("data/vehicules-2024.csv", sep=";", low_memory=False)
v2 = pd.read_csv("data/vehicules_baac_2024.csv", sep=";", low_memory=False)

print(v1.shape, v2.shape)
print(sorted(v1.columns))
print(sorted(v2.columns))