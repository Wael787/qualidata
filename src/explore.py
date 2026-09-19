import pandas as pd

def explorer(chemin):
    df = pd.read_csv(chemin, sep=";", low_memory=False)
    print(chemin)
    print(df.shape)
    print(df.dtypes)
    print(df.isna().sum())
    print(df.nunique())
    print()
    return df

caract = explorer("data/caract-2024.csv")
lieux = explorer("data/lieux-2024.csv")
vehicules = explorer("data/vehicules-2024.csv")
usagers = explorer("data/usagers-2024.csv")