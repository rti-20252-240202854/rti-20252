# WS-14: Analysis, Interpretation & Failure Analysis

> **Bab 14 — Analisis Data, Interpretasi & Failure Analysis**

---

## Ringkasan Materi

### Data → Knowledge Model

```
Data → Analysis → Interpretation → Explanation → Knowledge
```

Tiga level yang berbeda:
- **Analysis** — "Apa yang terjadi?" (deskriptif + inferensial)
- **Interpretation** — "Apa artinya?" (konteks RQ + literatur)
- **Failure Analysis** — "Mengapa tidak berhasil?" (boundary conditions)

### Beyond p-value

**Statistical significance ≠ practical significance.** Selalu laporkan:
1. p-value (signifikansi statistik)
2. Effect size (besarnya efek)
3. Confidence interval (rentang ketidakpastian)

| Effect Size (Cohen's d) | Interpretasi |
|-------------------------|-------------|
| < 0.2 | Small |
| 0.2 – 0.8 | Medium |
| > 0.8 | Large |

### Pemilihan Uji Statistik

| Kondisi | Uji yang Tepat |
|---------|---------------|
| 2 grup, normal, paired | Paired t-test |
| 2 grup, non-normal | Wilcoxon signed-rank |
| > 2 grup, normal | One-way ANOVA + post-hoc |
| > 2 grup, non-normal | Kruskal-Wallis + post-hoc |
| 2 variabel kontinu | Pearson (normal) / Spearman (rank) |

### Failure Analysis as Contribution

Hipotesis yang ditolak adalah **temuan yang berharga**:

| Dataset | New (F1) | Baseline (F1) | p-value | Cohen's d |
|---------|---------|--------------|---------|-----------|
| DS-1 (small, clean) | 94.2±1.1 | 89.3±1.5 | <0.001 | **3.7** |
| DS-4 (medium, noisy) | 78.3±3.2 | 82.1±2.8 | 0.008 | **-1.3** |
| DS-5 (large, noisy) | 71.6±4.1 | 80.5±3.0 | <0.001 | **-2.5** |

**Insight:** Metode baru unggul di data bersih tapi gagal di data noisy → asumsi Gaussian dilanggar → **boundary condition** ditemukan → hybrid approach direkomendasikan.

**Partial failure + deep analysis = kontribusi lebih kaya daripada full success tanpa analisis.**

### Limitation Types

| Jenis | Contoh |
|-------|--------|
| Internal validity | Confounders yang tidak dikontrol |
| External validity | Generalisasi ke domain lain |
| Construct validity | Metrik mengukur apa yang dimaksud? |
| Statistical limitation | Sample size, asumsi distribusi |

### Jebakan Kognitif

1. "Signifikan statistik = penting secara praktis" → cek effect size
2. "Hipotesis tidak didukung → cari sudut baru" → p-hacking
3. "Kegagalan tidak perlu dilaporkan detail" → missed insight
4. "Limitasi cukup disebutkan, tidak perlu dianalisis" → kedalaman hilang

---

## Template A.14 — Analysis & Interpretation Report

```
ANALYSIS & INTERPRETATION

1. Statistik Deskriptif:
   | Skenario | Mean | Std | Median | Min | Max | n |
   |----------|------|-----|--------|-----|-----|---|
   | Random Forest | 0.999907 | 0.000082 | 0.999956 | 0.999779 | 0.999956 | 5 |
   | Random Forest | 0.999907 | 0.000082 | 0.999934 | 0.999778 | 1.000000 | 5 |

2. Uji Hipotesis:
   2. Uji Hipotesis

Uji yang digunakan :
Wilcoxon Signed-Rank Test

Justifikasi :
Digunakan karena hasil uji normalitas menunjukkan bahwa tidak seluruh metrik berdistribusi normal sehingga digunakan uji non-parametrik untuk membandingkan performa Random Forest sebelum dan sesudah penerapan SMOTE.

Hasil :

Accuracy
p-value = 1.000

Precision
p-value = 0.500

Recall
p-value = 0.250

F1-Score
p-value = 0.875

Effect Size (Cohen's d)

Accuracy  = 0.000
Precision = 0.848
Recall    = -0.184
F1-Score  = -0.000

CI 95%

Accuracy
RF          : [0.999811, 1.000003]
RF + SMOTE  : [0.999805, 1.000009]

Precision
RF          : [0.999913, 0.999994]
RF + SMOTE  : [0.999950, 1.000003]

Recall
RF          : [0.999729, 1.000036]
RF + SMOTE  : [0.999696, 1.000022]

F1-Score
RF          : [0.999833, 1.000003]
RF + SMOTE  : [0.999828, 1.000008]
3. Keputusan:
   [ ] H₀ ditolak → H₁ diterima
   [v] H₀ tidak ditolak

4. Interpretasi:
   Hubungan ke RQ       :Berdasarkan hasil pengujian statistik, penggunaan SMOTE pada dataset CIC-IDS2017 tidak memberikan peningkatan performa yang signifikan terhadap algoritma Random Forest berdasarkan metrik Accuracy, Precision, Recall, dan F1-Score.
   Practical significance: Walaupun terdapat sedikit perubahan nilai performa setelah menggunakan SMOTE, perubahan tersebut sangat kecil sehingga secara praktis tidak memberikan peningkatan yang berarti.
   Perbandingan literatur: Hasil ini menunjukkan bahwa efektivitas SMOTE bergantung pada tingkat ketidakseimbangan data. Pada dataset CIC-IDS2017 yang digunakan, distribusi kelas relatif tidak terlalu timpang sehingga Random Forest sudah mampu menghasilkan performa yang sangat tinggi tanpa bantuan SMOTE.

5. Limitation:
   | Jenis | Ancaman | Dampak | Mitigasi |
   |-------|---------|--------|----------|
   | Statistical | Hanya 5 kali pengujian (5 seed) | Variasi hasil belum sepenuhnya mewakili seluruh kemungkinan | Menambah jumlah run pada penelitian selanjutnya |
   | Dataset | Menggunakan satu subset CIC-IDS2017 | Generalisasi terbatas | Menguji seluruh subset dataset CIC-IDS2017 |
   | External Validity | Hanya menggunakan Random Forest | Belum dapat dibandingkan dengan algoritma lain | Menambahkan SVM, XGBoost, atau LightGBM pada penelitian selanjutnya |

6. Failure Analysis (jika H₀ tidak ditolak):

   Penyebab potensial  : Dataset yang digunakan tidak memiliki tingkat ketidakseimbangan kelas yang ekstrem sehingga Random Forest telah mampu melakukan klasifikasi dengan sangat baik tanpa proses oversampling.
   Boundary condition   : SMOTE kemungkinan akan memberikan manfaat yang lebih besar pada dataset dengan rasio ketidakseimbangan kelas yang jauh lebih tinggi dibandingkan dataset yang digunakan dalam penelitian ini.
   Insight              : Penelitian ini menunjukkan bahwa penggunaan SMOTE tidak selalu meningkatkan performa klasifikasi. Efektivitas SMOTE bergantung pada karakteristik dataset, khususnya tingkat ketidakseimbangan kelas.
```

---

## Latihan 1 — Pemilihan Uji Statistik

Tentukan uji statistik yang tepat untuk eksperimen Anda.

| Pertanyaan | Jawaban |
|-----------|---------|
| Berapa grup yang dibandingkan? | 2 grup (Random Forest dan Random Forest + SMOTE) |
| Apakah data berpasangan (paired)? | ya |
| Apakah distribusi normal? (uji normalitas) | Tidak seluruh metrik berdistribusi normal |
| **Uji yang dipilih:** | Wilcoxon Signed-Rank Test |
| **Justifikasi:** | Karena data berpasangan dan tidak seluruhnya memenuhi asumsi normalitas |

**Effect size yang akan dilaporkan:** [v] Cohen's d / [ ] Eta-squared / [ ] Lainnya: ____

---

## Latihan 2 — Interpretasi Hasil

Gunakan data berikut (atau data riil Anda) untuk berlatih interpretasi.

**Data:**
| Model | Accuracy (mean ± std) | n |
|-------|----------------------|---|
| Random Forest         | 0.999907 ± 0.000082 | 5 |
| Random Forest + SMOTE | 0.999907 ± 0.000082 | 5 |

p = 1.000, Cohen's d = 0.00, 
CI 95% =
Random Forest
[0.999811, 1.000003]

Random Forest + SMOTE
[0.999805, 1.000009]

| Aspek | Interpretasi |
|-------|-------------|
| Signifikansi statistik | Nilai p-value = 1.000 (> 0.05) sehingga tidak terdapat perbedaan yang signifikan antara Random Forest dan Random Forest + SMOTE. |
| Effect size | Nilai Cohen's d ≈ 0.00, menunjukkan efek sangat kecil (negligible). |
| Practical significance | Secara praktis, penggunaan SMOTE tidak memberikan peningkatan performa yang berarti karena Random Forest sudah memiliki akurasi yang sangat tinggi tanpa SMOTE. |
| Hubungan ke RQ | Hasil penelitian menunjukkan bahwa penggunaan SMOTE tidak memberikan pengaruh signifikan terhadap performa Random Forest pada dataset CIC-IDS2017 berdasarkan Accuracy, Precision, Recall, dan F1-Score. |
| Perbandingan literatur | Hasil ini menunjukkan bahwa efektivitas SMOTE bergantung pada karakteristik dataset. Pada dataset yang tidak terlalu tidak seimbang, Random Forest mampu bekerja optimal tanpa proses oversampling. |

---

## Latihan 3 — Failure Analysis

Latih kemampuan failure analysis: hipotesis TIDAK didukung. Apa yang bisa dipelajari?

**Skenario:** Metode baru Anda mendapat F1 = 83.2%, baseline = 84.7%. p = 0.12 (tidak signifikan).

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah ini "gagal"? | Tidak. Hipotesis tidak terdukung merupakan hasil penelitian yang valid dan tetap memberikan kontribusi ilmiah. |
| Kemungkinan penyebab? | Dataset CIC-IDS2017 yang digunakan memiliki tingkat ketidakseimbangan kelas yang relatif rendah sehingga Random Forest sudah mampu mengklasifikasikan data dengan sangat baik tanpa bantuan SMOTE. |
| Boundary condition? | SMOTE diperkirakan akan lebih efektif pada dataset dengan tingkat ketidakseimbangan kelas yang jauh lebih tinggi dibandingkan dataset yang digunakan dalam penelitian ini. |
| Insight yang bisa diambil? | Penggunaan SMOTE tidak selalu meningkatkan performa klasifikasi. Pemilihan teknik oversampling harus mempertimbangkan karakteristik distribusi data. |
| Apakah layak dilaporkan? Mengapa? | Ya. Hasil negatif tetap merupakan kontribusi penelitian karena menunjukkan bahwa penerapan SMOTE tidak selalu memberikan peningkatan performa dan dapat menjadi referensi bagi penelitian selanjutnya. |

**Limitation terkait:**
| Jenis | Ancaman | Dampak |
|-------|---------|--------|
| Statistical | Jumlah pengujian hanya 5 run | Variasi hasil masih terbatas. |
| Dataset | Menggunakan satu subset CIC-IDS2017 | Generalisasi hasil ke dataset lain masih terbatas. |
| Model | Hanya menggunakan algoritma Random Forest | Belum diketahui apakah hasil yang sama berlaku untuk algoritma lain seperti XGBoost, SVM, atau LightGBM. |

---

## Refleksi

> Apakah "failure" dalam riset benar-benar gagal, atau justru kontribusi? Bagaimana failure analysis mengubah cara Anda melihat hasil negatif?
Dalam penelitian, hasil yang tidak mendukung hipotesis bukan berarti penelitian gagal. Hasil tersebut tetap memberikan kontribusi ilmiah karena menunjukkan kondisi atau karakteristik tertentu di mana suatu metode tidak memberikan peningkatan performa. Failure analysis membantu peneliti memahami penyebab hasil tersebut sehingga dapat menjadi dasar pengembangan penelitian berikutnya dan mencegah penerapan metode yang kurang sesuai pada dataset dengan karakteristik serupa.
