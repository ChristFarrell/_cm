import numpy as np
import pandas as pd
from scipy.stats import ttest_rel
from math import sqrt

df = pd.read_csv("CSV/PopulationFull.csv")

# 2a. FUNGSI Z-TEST
def two_sample_ztest(y1, y2):
    x1 = df[f'Rata-rata_{y1}']
    x2 = df[f'Rata-rata_{y2}']
    
    mean1 = x1.mean()
    mean2 = x2.mean()
    
    # pooled standard deviation
    pooled_std = np.sqrt((x1.var(ddof=1) + x2.var(ddof=1)) / 2)
    n = len(df)
    
    z = (mean2 - mean1) / (pooled_std / sqrt(n))
    return mean1, mean2, z

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

print("\n=== Z-TEST RESULT ===")
for y1, y2 in year_pairs:
    m1, m2, z = two_sample_ztest(y1, y2)
    print(f"\n{y1}-{y2} Period")
    print(f"First Mean  : {m1:.2f}")
    print(f"Second Mean : {m2:.2f}")
    print(f"Z-Score     : {z:.3f}")
    print(f"Result      : {'SIGNIFICANT' if abs(z) > 1.96 else 'NOT SIGNIFCANT'}")

print("\n=== PAIRED T-TEST RESULT ===")
for y1, y2 in year_pairs:
    print(f"\n--- {y1} vs {y2} ---")
    
    for age in ages:
        t, p = do_ttest(df[f"{y1}-{age}"], df[f"{y2}-{age}"])
        print(f"\nAge {age}")
        print_significance(t, p)