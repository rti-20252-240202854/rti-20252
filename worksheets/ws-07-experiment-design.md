# WS-07: Experimental Design & Validity

> **Bab 7 — Experimental Design & Validity**

---

## Ringkasan Materi

### Correlation ≠ Causality

Kausalitas membutuhkan 3 syarat:
1. **Covariance** — X dan Y bergerak bersama
2. **Temporal precedence** — X berubah sebelum Y
3. **Elimination of alternatives** — Tidak ada faktor lain yang menjelaskan Y

Controlled experiment adalah satu-satunya metode yang bisa membuktikan kausalitas.

### Empat Jenis Validitas

| Jenis | Pertanyaan | Ancaman Umum |
|-------|-----------|-------------|
| **Internal** | Apakah hubungan IV→DV nyata? | Confounding variable, selection bias |
| **External** | Apakah bisa digeneralisasi? | Dataset terlalu spesifik |
| **Construct** | Apakah mengukur konsep yang benar? | Metrik tidak sesuai |
| **Conclusion** | Apakah kesimpulan statistik valid? | Sample size kecil, uji salah |

Internal dan external validity sering berkonflik: semakin terkontrol (internal kuat) → semakin artificial (external lemah).

### Tiga Tipe Eksperimen dalam Riset TI

| Tipe | Deskripsi | Kapan Digunakan |
|------|----------|----------------|
| **Comparison Study** | Metode A vs B pada kondisi identik | Membandingkan pendekatan berbeda |
| **Ablation Study** | Full system → lepas komponen satu per satu | Mengukur kontribusi tiap komponen |
| **Parameter Study** | Variasikan satu parameter, amati dampak | Uji sensitifitas/robustness |

### Fairness dalam Perbandingan

Perbandingan yang adil = **kondisi identik** untuk semua metode: dataset sama, preprocessing sama, tuning effort sebanding, environment sama, metrik sama.

Contoh tidak adil: Transformer (30 fitur tambahan + Bayesian optimization) vs RF (default params) → hasilnya misleading.

### Threats to Validity = Diidentifikasi Sebelum Eksperimen

Ancaman validitas harus diidentifikasi **sebelum** eksperimen dan mitigasinya dirancang sebagai bagian dari desain — bukan ditulis sebagai boilerplate setelah selesai.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan testing | Memastikan sistem memenuhi requirement | Membuktikan hubungan kausal antar variabel |
| Baseline | Versi sebelumnya (last release) | Metode tervalidasi dari literatur |
| Kegagalan | Bug → fix → release | H₀ tidak ditolak → tetap kontribusi ilmiah |
| Sukses | 100% test pass | Evidence valid — mendukung atau menolak hipotesis |

### Istilah Penting

- **Causality** — Hubungan sebab-akibat (covariance + temporal + elimination)
- **Controlled Experiment** — Ubah satu variabel, kontrol sisanya, amati efek
- **Fairness** — Semua metode diuji pada kondisi yang benar-benar identik
- **Threats to Validity** — Faktor yang bisa melemahkan kesimpulan jika tidak dimitigasi
- **Conclusion Validity** — Validitas statistik: power, sample size, uji yang tepat

---

## Template A.7 — Desain Eksperimen Lengkap

```
EXPERIMENT DESIGN

Research Question : apakah penggunaan SMOTE dapat meningkatkan performa random forest pada deteksi anomali jaringan dibandingkan tanpa SMOTE berdasarkan akurasi, presisi, recal, dan f1 score?
Hypothesis        : penggunaan SMOTE memberikan peningkatan performa pada random forest dalam mendeteksi anomali jaringan
Tipe Eksperimen   : [v] Comparison  [ ] Ablation  [ ] Parameter

Kondisi Eksperimen:
| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control | random forest tanpa SMOTE | off | dataset dan parameter sama |
| Treatment | random forest dengan SMOTE | ON | dataset dan parameter sama |

Fairness Checklist:
  [v] Dataset identik untuk semua kondisi
  [v] Preprocessing setara
  [v] Tuning effort setara
  [v] Environment identik
  [v] Metrik evaluasi sama

Threat Analysis:
| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal    | overfitting karena SMOTE | menggunakan data testing terpisah |
| External    | dataset kurang mewakili kondisi nyata | menggunakan dataset yang lebih beragam |
| Construct   | akurasi terlalu dominan | menambahkan presisi,recall,f1 score |
| Conclusion  | jumlah data kurang | menggunakan dataset yang cukup |

Statistical Plan:
  Uji statistik   : perbandingan hasil performa model
  Justifikasi      : untuk melihat apakah SMOTE benar-benar meningkatkan performa
  Alpha            : 0.05
  Effect size min  : 5% peningkatan
```

---

## Latihan 1 — Desain Eksperimen

Susun desain eksperimen berdasarkan RQ, variabel, dan sistem dari WS-04 sampai WS-06.

**RQ:** apakah penggunaan SMOTE dapat meningkatkan performa random forest pada deteksi anomali jaringan dibandingkan tanpa SMOTE
**Tipe eksperimen:** [v] Comparison / [ ] Ablation / [ ] Parameter

| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control | RF tanpa SMOTE | off | dataset dan prameter tetap |
| Treatment | Rf menggunakan SMOTE | on | dataset dan parameter tetap |

---

## Latihan 2 — Fairness Checklist

Evaluasi apakah desain eksperimen di Latihan 1 sudah fair.

| Kriteria | Status | Detail |
|----------|--------|--------|
| Dataset identik | v | dataset sama digunakan di semua kondisi |
| Preprocessing setara | v | proses prepocessing dibuat sama |
| Tuning effort setara | v | parameter model dibuat tetap |
| Environment identik | v | pengujian dilakukan pada sistem yang sama |
| Metrik evaluasi sama | v | akurasi,presisi,recall,f1 score |

**Ada yang tidak fair?** [ ] Ya / [v] Tidak
> Jika ya, bagaimana cara memperbaikinya? ________________

---

## Latihan 3 — Threat Analysis

Identifikasi ancaman validitas untuk desain eksperimen ini.

| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal | data leakage train-test | menggunakan split data yang benar |
| External | dataset tidak realistis | menambahkan data lain |
| Construct | akurasi bisa menipu | menggunakan beberapa metrik |
| Conclusion | hasil kurang konsisten | melakukan pengujian berulang|

**Ancaman mana yang paling sulit dimitigasi?** external validity
**Mengapa?**
> dataset publik belum tentu benar-benar sama dengan kondisi jaringan nyata

---

## Refleksi

> Sebuah paper melaporkan "metode kami mengalahkan semua baseline." Apa 3 pertanyaan pertama yang harus diajukan untuk mengevaluasi klaim ini?

**Jawaban:**
1. dataset yang dipakai sama atau tidak dengan baseline?
2. parameter dan preprocessing dibuat fair atau tidak?
3. hasil bagus itu konsisten di semua metrik atau hanya di akurasi saja?
