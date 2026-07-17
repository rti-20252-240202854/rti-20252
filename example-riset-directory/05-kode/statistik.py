import pandas as pd
import numpy as np
import math

from scipy.stats import shapiro
from scipy.stats import ttest_rel
from scipy.stats import wilcoxon
from scipy.stats import t

# ============================
# Load Data
# ============================

rf = pd.read_csv("hasil_tanpa_smote.csv")
smote = pd.read_csv("hasil_smote.csv")

print("=" * 60)
print("ANALISIS STATISTIK")
print("=" * 60)

print("\nRandom Forest")
print(rf)

print("\nRandom Forest + SMOTE")
print(smote)

# ============================================
# Statistik Deskriptif
# ============================================

metrik = ["Accuracy", "Precision", "Recall", "F1"]

for m in metrik:

    print("\n")
    print("=" * 60)
    print("STATISTIK", m.upper())
    print("=" * 60)

    print("\nRandom Forest")
    print("Mean     :", rf[m].mean())
    print("Median   :", rf[m].median())
    print("Std      :", rf[m].std())
    print("Variance :", rf[m].var())
    print("Min      :", rf[m].min())
    print("Max      :", rf[m].max())

    print("\nRandom Forest + SMOTE")
    print("Mean     :", smote[m].mean())
    print("Median   :", smote[m].median())
    print("Std      :", smote[m].std())
    print("Variance :", smote[m].var())
    print("Min      :", smote[m].min())
    print("Max      :", smote[m].max())

# ============================================
# Uji Normalitas (Shapiro-Wilk)
# ============================================

print("\n")
print("=" * 60)
print("UJI NORMALITAS (SHAPIRO-WILK)")
print("=" * 60)

metrik = ["Accuracy", "Precision", "Recall", "F1"]

for m in metrik:

    stat_rf, p_rf = shapiro(rf[m])
    stat_smote, p_smote = shapiro(smote[m])

    print(f"\n{m}")

    print("Random Forest")
    print(f"Statistic : {stat_rf:.6f}")
    print(f"p-value   : {p_rf:.6f}")

    if p_rf > 0.05:
        print("Kesimpulan : Data Berdistribusi Normal")
    else:
        print("Kesimpulan : Data Tidak Normal")

    print()

    print("Random Forest + SMOTE")
    print(f"Statistic : {stat_smote:.6f}")
    print(f"p-value   : {p_smote:.6f}")

    if p_smote > 0.05:
        print("Kesimpulan : Data Berdistribusi Normal")
    else:
        print("Kesimpulan : Data Tidak Normal")

# ============================================
# Uji Hipotesis (Paired t-test atau Wilcoxon)
# ============================================

print("\n")
print("=" * 60)
print("UJI HIPOTESIS")
print("=" * 60)

metrik = ["Accuracy", "Precision", "Recall", "F1"]

for m in metrik:
    
    print(f"\n{m}")
    print("-" * 40)
    
    # Cek normalitas untuk menentukan uji yang digunakan
    _, p_rf = shapiro(rf[m])
    _, p_smote = shapiro(smote[m])
    
    # Jika kedua data normal, gunakan paired t-test
    if p_rf > 0.05 and p_smote > 0.05:
        print("Menggunakan Paired t-test (data normal)")
        stat, p = ttest_rel(rf[m], smote[m])
        print(f"Statistik t : {stat:.6f}")
        print(f"p-value    : {p:.6f}")
        
        if p < 0.05:
            print("Kesimpulan : Terdapat perbedaan signifikan (p < 0.05)")
        else:
            print("Kesimpulan : Tidak terdapat perbedaan signifikan (p >= 0.05)")
    
    # Jika salah satu atau kedua data tidak normal, gunakan Wilcoxon
    else:
        print("Menggunakan Wilcoxon Signed-Rank Test (data tidak normal)")
        stat, p = wilcoxon(rf[m], smote[m])
        print(f"Statistik W : {stat:.6f}")
        print(f"p-value    : {p:.6f}")
        
        if p < 0.05:
            print("Kesimpulan : Terdapat perbedaan signifikan (p < 0.05)")
        else:
            print("Kesimpulan : Tidak terdapat perbedaan signifikan (p >= 0.05)")

# ==========================================
# WILCOXON SIGNED-RANK TEST (Terpisah)
# ==========================================

print()
print("="*60)
print("WILCOXON SIGNED-RANK TEST")
print("="*60)

metrics = ["Accuracy", "Precision", "Recall", "F1"]

for metric in metrics:

    print()
    print(metric)

    stat, p = wilcoxon(
        rf[metric],
        smote[metric]
    )

    print("Statistic :", stat)
    print("p-value   :", p)

    alpha = 0.05

    if p < alpha:
        print("Keputusan : Tolak H0")
        print("Kesimpulan: Ada perbedaan signifikan")
    else:
        print("Keputusan : Gagal Tolak H0")
        print("Kesimpulan: Tidak ada perbedaan signifikan")

# ==========================================
# EFFECT SIZE (COHEN'S D)
# ==========================================

print()
print("="*60)
print("EFFECT SIZE (COHEN'S D)")
print("="*60)

metrics = ["Accuracy", "Precision", "Recall", "F1"]

for metric in metrics:

    x = rf[metric]
    y = smote[metric]

    mean_x = np.mean(x)
    mean_y = np.mean(y)

    std_x = np.std(x, ddof=1)
    std_y = np.std(y, ddof=1)

    pooled_std = math.sqrt(
        ((len(x)-1)*(std_x**2) + (len(y)-1)*(std_y**2))
        /
        (len(x)+len(y)-2)
    )

    if pooled_std == 0:
        d = 0
    else:
        d = (mean_y - mean_x) / pooled_std

    print()
    print(metric)
    print("Cohen's d :", round(d,6))

    nilai = abs(d)

    if nilai < 0.2:
        print("Interpretasi : Efek sangat kecil (Negligible)")
    elif nilai < 0.5:
        print("Interpretasi : Efek kecil")
    elif nilai < 0.8:
        print("Interpretasi : Efek sedang")
    else:
        print("Interpretasi : Efek besar")
print()
print("="*60)
print("95% CONFIDENCE INTERVAL")
print("="*60)

metrics = ["Accuracy","Precision","Recall","F1"]

for metric in metrics:

    print()
    print(metric)

    for nama, data in zip(
        ["Random Forest","Random Forest + SMOTE"],
        [rf, smote]
    ):

        x = data[metric]

        mean = np.mean(x)
        std = np.std(x, ddof=1)
        n = len(x)

        t_value = t.ppf(0.975, df=n-1)

        margin = t_value * (std / np.sqrt(n))

        lower = mean - margin
        upper = mean + margin

        print(nama)
        print("Mean :", round(mean,6))
        print("95% CI : [{:.6f}, {:.6f}]".format(lower, upper))
        print()