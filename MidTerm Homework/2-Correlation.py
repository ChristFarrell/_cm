import pandas as pd
import numpy as np

df = pd.read_csv("CSV/PopulationFull.csv")

years = [2020, 2021, 2022, 2023]

def corr(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    num = np.sum((x - x_mean) * (y - y_mean))
    den = np.sqrt(np.sum((x - x_mean)**2) * np.sum((y - y_mean)**2))
    return num / den

for year in years:
    print(f"\n========== CORRELATION IN {year} ==========")

    cols = [
        f"{year}-15-24",
        f"{year}-25-54",
        f"{year}-55+"
    ]

    data = df[cols]

    corr_matrix = pd.DataFrame(index=cols, columns=cols)

    for c1 in cols:
        for c2 in cols:
            corr_matrix.loc[c1, c2] = corr(data[c1], data[c2])

    print(corr_matrix)
