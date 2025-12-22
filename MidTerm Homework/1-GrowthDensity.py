import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("CSV/Population and Area.csv")

df = df.rename(columns={
    "Jumlah Penduduk 2020": "2020",
    "Jumlah Penduduk 2021": "2021",
    "Jumlah Penduduk 2022": "2022",
    "Jumlah Penduduk 2023": "2023",
})

year_cols = ["2020", "2021", "2022", "2023"]
df[year_cols] = df[year_cols].apply(pd.to_numeric, errors="coerce")

# ================================
# GROWTH RATE
# ================================
def growth(prev, curr):
    return round((curr - prev) / prev * 100, 2)

df_growth = pd.DataFrame()
df_growth["Provinsi"] = df["Provinsi"]

df_growth["Growth 2020-2021 (%)"] = growth(df["2020"], df["2021"])
df_growth["Growth 2021-2022 (%)"] = growth(df["2021"], df["2022"])
df_growth["Growth 2022-2023 (%)"] = growth(df["2022"], df["2023"])

# ================================
# (DENSITY)
# ================================
df_density = pd.DataFrame()
df_density["Provinsi"] = df["Provinsi"]

for year in year_cols:
    df_density[f"Density {year}"] = (df[year] / df["Luas Daerah"]).round(2)

print("\n=== POPULATION GROWTH (%) ===")
print(df_growth.to_string(index=False))

print("\n=== POPULATION DENSITY ===")
print(df_density.to_string(index=False))

growth_cols = [
    "Growth 2020-2021 (%)",
    "Growth 2021-2022 (%)",
    "Growth 2022-2023 (%)",
]

plt.figure(figsize=(26, 9))

x = np.arange(len(df_growth["Provinsi"]))
offsets = [-0.15, -0.05, 0.05, 0.15]

for col, off in zip(growth_cols, offsets):
    y = df_growth[col]
    plt.plot(x + off, y, marker='o', linewidth=2)

    for i, val in enumerate(y):
        plt.text(i + off, val + 0.05, f"{val:.2f}", fontsize=7, ha='center')

plt.xticks(x, df_growth["Provinsi"], rotation=90, fontsize=8)

plt.title("Growth of Indonesia Population (2020–2023)", fontsize=15)
plt.ylabel("Persentase (%)")
plt.ylim(min(df_growth[growth_cols].min()) - 0.5,
         max(df_growth[growth_cols].max()) + 0.5)

plt.grid(True, alpha=0.3)
plt.legend(growth_cols, fontsize=10)
plt.tight_layout(rect=[0, 0.1, 1, 0.95])
plt.show()

year_cols = ["Density 2020", "Density 2021", "Density 2022", "Density 2023"]
years = ["2020", "2021", "2022", "2023"]

ranking = pd.DataFrame()
ranking["Provinsi"] = df_density["Provinsi"]

for yc, y in zip(year_cols, years):
    ranking[y] = df_density[yc].rank(ascending=False, method='min')

plt.figure(figsize=(26, 9))

x = np.arange(len(ranking["Provinsi"]))
offsets = [-0.15, -0.05, 0.05, 0.15]

for (y, off) in zip(years, offsets):
    plt.plot(x + off, ranking[y], marker='o', linewidth=3, label=y)

plt.gca().invert_yaxis()
plt.xticks(x, ranking["Provinsi"], rotation=90, fontsize=8)

plt.title("Bump Chart – Ranking of Population Density 2020–2023", fontsize=15)
plt.grid(alpha=0.3)
plt.legend(title="Year", fontsize=12)

plt.tight_layout(rect=[0, 0.1, 1, 0.95])
plt.show()



