import numpy as np
import pandas as pd
from scipy.stats import ttest_rel

df = pd.read_csv("CSV/PopulationFull.csv")

def get_means(y1, y2):
    mean1 = df[f'Rata-rata_{y1}'].mean()
    mean2 = df[f'Rata-rata_{y2}'].mean()
    return mean1, mean2

year_pairs = [(2020, 2021), (2021, 2022), (2022, 2023)]

# 2b. FUNGSI T-TEST
def do_ttest(col1, col2):
    t, p = ttest_rel(col1, col2)
    return t, p

year_pairs = [(2020, 2021), (2021, 2022), (2022, 2023)]
ages = ["15-24", "25-54", "55+"]

def print_significance(t, p):
    print(f"t-value : {t:.4f}")
    print(f"p-value : {p:.6f}")
    if p < 0.05:
        print(">> SIGNIFICANT")
    else:
        print(">> NOT SIGNIFCANT")

print("\n=== MEAN RESULT ===")
for y1, y2 in year_pairs:
    m1, m2 = get_means(y1, y2)
    print(f"\n{y1}–{y2}")
    print(f"Mean {y1}: {m1:,.2f}")
    print(f"Mean {y2}: {m2:,.2f}")

print("\n=== PAIRED T-TEST RESULT ===")
for y1, y2 in year_pairs:
    print(f"\n--- {y1} vs {y2} ---")
    
    for age in ages:
        t, p = do_ttest(df[f"{y1}-{age}"], df[f"{y2}-{age}"])
        print(f"\nAge {age}")
        print_significance(t, p)