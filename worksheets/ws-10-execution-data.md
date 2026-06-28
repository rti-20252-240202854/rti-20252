# WS-10: Experiment Execution & Data Collection

> **Bab 10 — Eksekusi Eksperimen & Pengumpulan Data**

---

## Ringkasan Materi

### Experiment Execution Pipeline

```
Design → Execution Plan → Controlled Execution → Data Collection → Data Logging → Dataset for Analysis
```

### Multiple Run = Non-Negotiable

Single run **tidak pernah cukup** untuk klaim ilmiah. Minimum 5-10 run per skenario dengan seed berbeda. Multiple run menghasilkan:
- Mean, std, confidence interval
- Distribusi hasil → uji statistik
- Variabilitas → error bar di grafik

### Execution Plan

Setiap eksperimen harus memiliki plan sebelum eksekusi:
- Daftar skenario
- Jumlah run per skenario
- Random seed per run (pre-determined!)
- Urutan eksekusi (randomisasi/counterbalancing)
- Pre-execution checklist

### Data Logging Komprehensif

Setiap run menghasilkan log terstruktur:
1. **Identitas** — Run ID, timestamp, skenario
2. **Konfigurasi** — Semua parameter, seed, code version
3. **Hasil** — Semua metrik, output detail
4. **Metadata** — Waktu eksekusi, resource usage, warning/error

Format: CSV/JSON/database — **bukan stdout yang di-copy-paste**.

### Engineering vs Research Execution

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Run | Sekali (deploy) | Multiple (min 5-10, seed berbeda) |
| Logging | Error log, access log | Semua parameter, metrik, metadata |
| Anomali | Bug → fix → redeploy | Investigasi → dokumentasi → analisis |
| Urutan | Tidak penting | Bisa bias — perlu randomisasi |

### Anomali = Dokumentasi, Bukan Hapus

Run gagal/anomali tidak boleh dihapus tanpa dokumentasi. Bisa jadi:
- **Bug** → fix & re-run (dokumentasikan!)
- **Batas kemampuan metode** → DNF = temuan
- **Data yang bias** jika hanya simpan run "berhasil"

### Jebakan Kognitif

1. "Satu angka cukup" → tanpa distribusi, tidak bisa diuji
2. "Seed tidak penting" → bahkan algoritma deterministik bisa dipengaruhi library stokastik
3. "Run gagal langsung hapus" → kehilangan temuan potensial
4. "Semua run harus hari ini" → thermal throttling, fatigue

---

## Template A.10 — Execution Plan & Data Log

```
EXECUTION PLAN

| Run # | Skenario   | Seed | Parameter Kunci  | Status |
| ----- | ---------- | ---- | ---------------- | ------ |
| 1     | RF + SMOTE | 42   | n_estimators=100 | Done   |
| 2     | RF + SMOTE | 123  | n_estimators=100 | Done   |
| 3     | RF + SMOTE | 999  | n_estimators=100 | Done   |
| 4     | RF + SMOTE | 2025 | n_estimators=100 | Done   |
| 5     | RF + SMOTE | 777  | n_estimators=100 | Done   |

Jumlah runs per skenario : 5
Total runs               : 5

DATA LOG (per run):
Run ID    : run-001
Timestamp : 28-06-2026
Skenario  : Random Forest + SMOTE
Input     : Dataset CIC-IDS2017 (Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv)
Output    : Accuracy=0.999934, Precision=0.999961, Recall=0.999922, F1=0.999941
Anomali   : Ditemukan nilai Infinity pada dataset dan dilakukan preprocessing.
Catatan   : Eksperimen dijalankan menggunakan Python 3.13 dan RandomForestClassifier (n_estimators=100).

Run ID    : run-002
Timestamp : 28-06-2026
Skenario  : RF + SMOTE
Input     : CIC-IDS2017
Output    : Acc=0.999779, Prec=0.999961, Rec=0.999649, F1=0.999805
Anomali   : Tidak ada
Catatan   : Seed=123

Run ID    : run-003
Timestamp : 28-06-2026
Skenario  : RF + SMOTE
Input     : CIC-IDS2017
Output    : Acc=0.999934, Prec=1.000000, Rec=0.999883, F1=0.999941
Anomali   : Tidak ada
Catatan   : Seed=999

Run ID    : run-004
Timestamp : 28-06-2026
Skenario  : RF + SMOTE
Input     : CIC-IDS2017
Output    : Acc=1.000000, Prec=1.000000, Rec=1.000000, F1=1.000000
Anomali   : Tidak ada
Catatan   : Seed=2025

Run ID    : run-005
Timestamp : 28-06-2026
Skenario  : RF + SMOTE
Input     : CIC-IDS2017
Output    : Acc=0.999889, Prec=0.999961, Rec=0.999844, F1=0.999902
Anomali   : Tidak ada
Catatan   : Seed=777
```

---

## Latihan 1 — Execution Plan

Susun execution plan untuk eksperimen Anda. Tentukan skenario, jumlah run, dan seed sebelum eksekusi.

| Run # | Skenario | Seed | Parameter Kunci | Status |
|-------|----------|------|----------------|--------|
| 1     | RF + SMOTE | 42   | n_estimators=100 | Done   |
| 2     | RF + SMOTE | 123  | n_estimators=100 | Done   |
| 3     | RF + SMOTE | 999  | n_estimators=100 | Done   |
| 4     | RF + SMOTE | 2025 | n_estimators=100 | Done   |
| 5     | RF + SMOTE | 777  | n_estimators=100 | Done   |

**Total skenario:** 1
**Run per skenario:** 5
**Total run keseluruhan:** 5

---

## Latihan 2 — Data Log Terstruktur

Desain format data log untuk eksperimen Anda. Tentukan field apa saja yang akan dicatat.

**Identitas:**
| Field | Contoh |
|-------|--------|
| Run ID | run-001 |
| Timestamp | 28-06-2026 |
| skenario | RF + SMOTE |

**Konfigurasi:**
| Field | Contoh |
|-------|--------|
| Seed         | 42                                |
| Code version | CIC-IDS2017 Friday Afternoon DDoS |
| n_estimators | 100                               |
| Test Size    | 0.2                               |
| Random State | 42                                |

**Hasil:**
| Metrik | Tipe Data | Range Valid |
|--------|----------|-------------|
| Accuracy | float | 0–1 |
| Precision | float | 0-1 |
| Recall | float | 0-1 |
| F1-Score | float | 0-1 |

**Format output:** [v] CSV / [ ] JSON / [ ] Database / [ ] Lainnya: ____

---

## Latihan 3 — Anomaly Protocol

Rencanakan bagaimana menangani anomali. Untuk setiap jenis, tentukan langkah yang diambil.

| Jenis Anomali | Contoh | Tindakan |
|---------------|--------|----------|
| Run gagal (crash) | Error Infinity pada dataset | Melakukan preprocessing dan mengganti nilai Infinity menjadi NaN lalu mengisi dengan 0 |
| Hasil ekstrem | Accuracy 100% pada seed 2025 | Tetap dicatat dan dianalisis |
| Waktu eksekusi anomali | Training lebih lama | Dokumentasi dan pengulangan jika diperlukan |
| Inkonsistensi dengan run lain | Nilai F1 berbeda sedikit | Menghitung rata-rata dari seluruh run |

**Prinsip:** Detect → Investigate → Document → Decide

---

## Refleksi

> Pernahkah Anda melaporkan hasil riset/tugas dari single run? Apa risikonya? Bagaimana multiple run mengubah kepercayaan terhadap hasil?

**Pengalaman sebelumnya:**
> Sebelumnya saya sering menggunakan hasil dari satu kali pengujian saja. Setelah melakukan multiple run, saya menyadari bahwa hasil eksperimen dapat sedikit berubah tergantung random seed yang digunakan.
**Yang akan dilakukan berbeda:**
> Selalu melakukan beberapa kali pengujian dan menggunakan nilai rata-rata agar hasil penelitian lebih valid dan dapat dipercaya.
