# WS-13: Data Preprocessing

> **Bab 13 — Preprocessing & Persiapan Data untuk Analisis**

---

## Ringkasan Materi

### Data Refinement Pipeline

```
Raw Data → Cleaning → Transformation → Normalization → Processed Data → Analysis Ready
```

Setiap tahap memiliki tujuan berbeda. **Preprocessing bukan langkah teknis biasa** — setiap keputusan preprocessing adalah keputusan riset yang bisa mengubah kesimpulan.

### Empat Prinsip Preprocessing

| Prinsip | Deskripsi |
|---------|----------|
| **Consistency** | Metode sama untuk data yang sama |
| **Transparency** | Setiap langkah terdokumentasi |
| **Reproducibility** | Orang lain bisa mengulang dengan hasil sama |
| **Minimal Distortion** | Ubah sesedikit mungkin; jika normalisasi tidak perlu, jangan lakukan |

### Cleaning Triad

| Masalah | Strategi | Risiko |
|---------|---------|--------|
| **Missing values** | | |
| — Listwise deletion | Missing < 5%, random | Data loss |
| — Mean/median imputation | Sedikit missing, dist. normal | Mengurangi variabilitas |
| — Model-based imputation | Banyak missing, pola sistematis | Introduces dependency |
| — Flag & separate | Missing karena alasan substantif | Kompleksitas analisis |
| **Duplikat** | Identifikasi → verifikasi → hapus | False positive (data mirip ≠ duplikat) |
| **Error format** | Standardisasi tipe, encoding | Kehilangan informasi saat konversi |

### Normalisasi — Kapan & Metode Mana

| Metode | Formula | Output | Sensitif Outlier? |
|--------|---------|--------|-------------------|
| Min-max | (x-min)/(max-min) | [0, 1] | Ya |
| Z-score | (x-mean)/std | Unbounded | Lebih robust |
| Robust scaling | (x-median)/IQR | Unbounded | Paling robust |

**Kunci:** Parameter normalisasi harus dihitung dari **training set saja** — bukan seluruh data. Pelanggaran = **data leakage**.

### Data Leakage Prevention

Data leakage terjadi ketika informasi dari test set "bocor" ke preprocessing:
- Normalisasi parameter dari seluruh dataset ← **SALAH**
- Cross-validation dilakukan sebelum split ← **SALAH**
- Feature selection menggunakan label test set ← **SALAH**

### Jebakan Kognitif

1. "Preprocessing cuma teknis — tidak perlu detail" → bisa ubah kesimpulan
2. "Lebih banyak preprocessing = lebih bersih = lebih baik" → over-processing distorsi data
3. "Normalisasi selalu diperlukan" → belum tentu, tergantung metode analisis
4. "Imputation sama untuk semua situasi" → strategi harus sesuai konteks

---

## Template A.13 — Preprocessing Documentation Log

```
PREPROCESSING LOG

Dataset           : CIC-IDS2017
Jumlah data awal  : 225.745 records

Cleaning:
| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| Missing |      4      | Nilai NaN diisi dengan 0 (fillna(0)) | Agar tidak terjadi error saat proses training Random Forest. |
| Duplikat|      0      | Tidak ada tindakan | Tidak ditemukan data duplikat pada dataset yang digunakan. |
| Error   |      64      | Nilai Infinity dan -Infinity diubah menjadi NaN, kemudian diisi 0 | Random Forest tidak dapat memproses nilai Infinity sehingga perlu dibersihkan terlebih dahulu. |

Transformation:
| Transformasi | Variabel | Detail | Alasan |
|-------------   |----------|--------|--------|
| Label Encoding | Label | Mengubah label kategorikal menjadi numerik menggunakan LabelEncoder | Agar label dapat diproses oleh Random Forest |
| Train-Test Split | Dataset | Membagi data menjadi 80% data latih dan 20% data uji | Memisahkan data pelatihan dan pengujian |
| SMOTE | Data training | Menyeimbangkan jumlah kelas pada data latih | Mengurangi ketidakseimbangan kelas (class imbalance) |

Normalization:
  Metode    : tidak dilakukan
  Alasan    : Random Forest merupakan algoritma berbasis pohon keputusan sehingga tidak memerlukan normalisasi fitur.
  Parameter : -

Leakage Check:
  [v] Parameter normalisasi dari training set saja
  [v] Tidak ada informasi test set dalam preprocessing
  [v] Cross-validation dilakukan setelah split

Jumlah data akhir : 225.745 records
Script tersedia   : [v] Ya | [ ] Belum
Path :
src/preprocessing.py
src/train_test_split.py
src/rf_smote.py

---

## Latihan 1 — Cleaning Plan

Periksa dataset Anda (atau dataset contoh) dan dokumentasikan masalah yang ditemukan.

| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| Nilai Infinity | Ditemukan pada beberapa fitur | Diubah menjadi NaN lalu diisi 0 | Agar model dapat memproses seluruh data |
| Missing Value | Berasal dari konversi Infinity | Diisi dengan nilai 0 | Menghindari error saat training |
| Duplikat | Tidak ditemukan | Tidak ada tindakan | Dataset tetap konsisten |
| | | | |

**Jumlah data sebelum cleaning:** 225.745 records
**Jumlah data setelah cleaning:** 225.745 records
**Persentase data yang hilang/berubah:** 0 %

---

## Latihan 2 — Normalisasi Decision

Tentukan apakah data Anda perlu normalisasi, dan jika ya, metode apa yang tepat.

| Variabel | Range Asli | Distribusi | Outlier? | Metode Normalisasi | Alasan |
|----------|-----------|-----------|----------|-------------------|--------|
| Fitur trafik jaringan | Bervariasi | Beragam | ada | Tidak dilakukan | Random Forest tidak memerlukan normalisasi fitur |

**Apakah normalisasi diperlukan?** [ ] Ya / [v] Tidak
**Justifikasi:**
> Normalisasi tidak dilakukan karena algoritma Random Forest tidak dipengaruhi oleh perbedaan skala antar fitur. Oleh karena itu, proses normalisasi tidak diperlukan pada penelitian ini.

**Leakage check:**
- [v] Parameter dihitung dari training set saja
- [v] Normalisasi diterapkan setelah train-test split
Walaupun normalisasi tidak dilakukan, proses pembagian data train-test telah dilakukan sebelum SMOTE sehingga tidak terjadi data leakage.

## Latihan 3 — Preprocessing Report

Buat ringkasan preprocessing lengkap — dokumentasi yang cukup bagi orang lain untuk mereplikasi.

```
PREPROCESSING SUMMARY

1. Dataset: CIC-IDS2017 (Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv)
2. Data awal: 225.745 records, 79 features
3. Cleaning:
   - Missing values: Ditangani dengan pengisian nilai 0 setelah konversi Infinity
   - Duplikat: Tidak ditemukan.
   - Error: Nilai Infinity diubah menjadi NaN kemudian diisi dengan 0.
4. Transformation: Label Encoding, Train-Test Split (80:20), dan SMOTE pada data training.
5. Normalisasi: Tidak dilakukan karena Random Forest tidak memerlukan normalisasi fitur._
6. Data akhir: 225.745 records, 79 features
7. Leakage check: [v] Lulus / [ ] Ada masalah
```

---

## Refleksi

> Apakah Anda pernah melakukan normalisasi "karena biasa dilakukan" tanpa mempertimbangkan apakah benar-benar diperlukan? Apa risiko over-preprocessing?
Sebelumnya saya menganggap normalisasi selalu diperlukan dalam setiap penelitian machine learning. Setelah mempelajari materi ini, saya memahami bahwa preprocessing harus disesuaikan dengan karakteristik algoritma yang digunakan. Pada penelitian ini, normalisasi tidak dilakukan karena Random Forest tidak dipengaruhi oleh skala fitur. Selain itu, preprocessing yang berlebihan dapat mengubah karakteristik data dan berpotensi memengaruhi hasil penelitian.
