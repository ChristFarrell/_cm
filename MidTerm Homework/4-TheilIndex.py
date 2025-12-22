import numpy as np
import pandas as pd

# Load data
df = pd.read_csv('CSV/PopulationFull.csv')
years = [2020, 2021, 2022, 2023]

for year in years:
    y = df[f"Rata-rata_{year}"]
    pop = df[f"Jumlah_Penduduk_{year}"]
    
    # Komponen Dasar
    Y = y * pop
    Y_total = Y.sum()
    pop_total = pop.sum()
    mu = Y_total / pop_total
    
    # Formula: (Yi / Y_total) * ln(yi / mu)
    w_i = Y / Y_total      # Pangsa Pendapatan
    ratio_i = y / mu       # Rasio pendapatan prov terhadap rata-rata nasional
    contrib = w_i * np.log(ratio_i)
    
    print(f"\n" + "="*70)
    print(f" THEIL INDEX EVERY YEAR {year} ".center(70, "="))
    print(f"="*70)
    print(f"{'Provinsi':<25} | {'Pendapatan':<12} | {'Pop Share':<10} | {'Theil Contrib':<12}")
    print("-" * 70)
    
    for i in range(len(df)):
        p_share = pop[i] / pop_total
        print(f"{df['Provinsi'][i]:<25} | {y[i]:>12,.0f} | {p_share:>9.2%} | {contrib[i]:>12.6f}")

    # --- PERSIAPAN RANKING & DEKOMPOSISI ---
    df_temp = pd.DataFrame({
        'Provinsi': df['Provinsi'],
        'y': y,
        'contrib': contrib,
        'pop': pop,
        'Y': Y
    })
    
    # Ranking
    df_rank = df_temp.sort_values(by='contrib', ascending=False)
    
    # Median untuk Dekomposisi
    median_val = y.median()
    df_temp["group"] = df_temp["y"].apply(lambda x: "High" if x >= median_val else "Low")
    
    # Hitung Between & Within
    T_total = contrib.sum()
    group = df_temp.groupby("group").agg(Yg=("Y", "sum"), Ng=("pop", "sum"))
    group["wg"] = group["Yg"] / Y_total
    group["mu_g"] = group["Yg"] / group["Ng"]
    
    T_between = (group["wg"] * np.log(group["mu_g"] / mu)).sum()
    T_within = T_total - T_between

    # --- OUTPUT RINGKASAN ---
    print(f"\n--- TOP 3 BIGGEST POSITIVE ---")
    for _, row in df_rank.head(3).iterrows():
        print(f"{row['Provinsi']:<25}: {row['contrib']:.6f}")

    print(f"\n--- TOP 3 BIGGEST NEGATIVE ---")
    for _, row in df_rank.tail(3).iterrows():
        print(f"{row['Provinsi']:<25}: {row['contrib']:.6f}")

    print(f"\n--- DECOMPOSITION OF MEDIAN ---")
    print(f"Median Income     : {median_val:,.2f}")
    print(f"Theil Total       : {T_total:.5f}")
    print(f"Within Group      : {T_within:.5f} ({T_within/T_total*100:.1f}%)")
    print(f"Between Group     : {T_between:.5f} ({T_between/T_total*100:.1f}%)")