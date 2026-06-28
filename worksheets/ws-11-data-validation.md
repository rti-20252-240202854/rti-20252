# WS-11: Data Validation & Integrity

> **Bab 11 — Validasi Data & Integritas**

---

## Ringkasan Materi

### Data Trust Model

```
Raw Data → Data Cleaning → Consistency Check → Validation Process → Trusted Data
```

Data mentah belum bisa dipercaya. Harus melewati pipeline validasi sebelum siap untuk analisis statistik.

### Empat Pilar Data Quality

| Pilar | Deskripsi | Contoh Pelanggaran |
|-------|----------|-------------------|
| **Accuracy** | Nilai dalam range masuk akal | Akurasi = 1.5 (di luar [0,1]) |
| **Consistency** | Format seragam di semua run | Run 1: CSV, Run 2: JSON |
| **Completeness** | Tidak ada data hilang dari plan | 97 dari 100 run tercatat |
| **Validity** | Data sesuai desain eksperimen | Parameter baseline tercampur treatment |

### Proses Validasi Progresif

1. **Format validation** — Tipe file, header, kolom
2. **Range validation** — Nilai dalam batas logis
3. **Consistency validation** — Format seragam antar-run
4. **Logic validation** — Data cocok dengan desain eksperimen

Jika gagal di langkah awal → tidak perlu lanjut.

### Anomaly Detection — 3 Jenis

| Jenis | Deskripsi | Deteksi |
|-------|----------|---------|
| **Statistical outlier** | Nilai di luar distribusi normal | IQR: < Q1-1.5×IQR atau > Q3+1.5×IQR |
| **Contextual anomaly** | Normal absolut, abnormal dalam konteks | Run 1-10: ~91%, Run 11-20: ~88% |
| **Pattern anomaly** | Pola sistematis (bukan random) | Performa menurun berurutan |

**Prinsip:** Detect → Investigate → Document → Decide — **JANGAN langsung hapus.**

### Engineering vs Research Validation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Data sesuai spesifikasi bisnis | Data layak untuk analisis statistik |
| Missing data | Impute / set default | Investigasi penyebab → dokumentasi |
| Outlier | Bug → fix | Mungkin temuan → investigasi |
| Dokumentasi | Minimal (log error) | Komprehensif (anomali + keputusan) |

### Jebakan Kognitif

1. "Logging otomatis ≠ data benar" → bisa ada bug di logger
2. "Outlier = hapus" → bisa jadi temuan penting
3. "Dataset kecil tidak perlu validasi" → justru lebih rentan
4. "Mean normal = data benar" → [94, 95, 93, **44**, 94] → mean 84% terlihat wajar

---

## Template A.11 — Data Validation Checklist

```
DATA VALIDATION CHECKLIST

Completeness:
  [v] Semua skenario tercakup
  [v] Jumlah run sesuai rencana
  [v] Tidak ada file output hilang
  Missing: 0 dari 5 data points

Format Consistency:
  [v] Semua file format sama (CSV/JSON/...)
  [v] Header konsisten
  [v] Tipe data konsisten (numerik tetap numerik)

Range & Logic:
  [v] Nilai dalam range masuk akal
  [v] Tidak ada waktu negatif
  [v] Metrik 0–100%, tidak di luar range
  Anomali ditemukan: Ditemukan nilai Infinity pada dataset mentah dan telah dilakukan preprocessing dengan mengubah nilai Infinity menjadi NaN kemudian menggantinya dengan nilai 0.

Cross-Validation:
  [ ] Run identik → hasil mendekati
  [ ] Trend konsisten dengan ekspektasi teori

Keputusan:
  [v] Data siap analisis
  [ ] Perlu cleaning
  [ ] Perlu re-run (skenario: ____)
```

---

## Latihan 1 — Completeness Check

Verifikasi apakah semua data yang direncanakan sudah terkumpul.

| Skenario | Run Direncanakan | Run Tercatat | Missing | Alasan |
|----------|-----------------|-------------|---------|--------|
| RF + SMOTE | 5 | 5 | 0 | - |


**Total expected:** 5 | **Total actual:** 5 | **Missing:** 0

**Keputusan untuk data missing:**
> Tidak terdapat data yang hilang karena seluruh eksperimen berhasil dijalankan dan semua hasil tercatat dengan baik.

---

## Latihan 2 — Anomaly Investigation

Periksa data Anda untuk anomali. Gunakan metode IQR atau z-score.

**Dataset sampel (atau data Anda sendiri):**

| Run | Accuracy (%) |
|-----|-------------|
| 1 | 99.9934 |
| 2 | 99.9779 |
| 3 | 99.9934 |
| 4 | 100.0000 |
| 5 | 99.9889 |

**Deteksi outlier:**
- Q1 = 99.9889 | Q3 = 99.9934 | IQR = 0.0045
- Batas bawah (Q1 - 1.5×IQR) = 99.98215
- Batas atas (Q3 + 1.5×IQR) = 100.00015
- Outlier terdeteksi: tidak ada

**Investigasi (untuk setiap outlier):**

| Outlier | Nilai | Kemungkinan Penyebab | Keputusan |
|---------|-------|---------------------|-----------|
| - | - | Tidak ditemukan outlier | Seluruh data digunakan untuk analisis |

---

## Latihan 3 — Validation Report

Buat laporan validasi ringkas untuk dataset eksperimen Anda.

**1. Completeness:** 100% data terkumpul
**2. Format:** [v] Konsisten / [ ] Ada inkonsistensi: ____
**3. Range check (anomali):** Tidak ditemukan nilai di luar rentang logis.Seluruh nilai Accuracy, Precision, Recall, dan F1-Score berada pada rentang 0–100%.
**4. Logic check:** [v] Parameter sesuai plan / [ ] Ada ketidaksesuaian: ____

**Kesimpulan:** [v] Data siap analisis / [ ] Perlu tindakan: ____

---

## Refleksi

> Apa perbedaan antara "data yang benar" dan "data yang dipercaya"? Mengapa proses validasi formal diperlukan meskipun data dikumpulkan secara otomatis?

> Data yang benar belum tentu dapat dipercaya karena masih mungkin terdapat kesalahan pencatatan, data hilang, atau inkonsistensi. Sedangkan data yang dipercaya adalah data yang telah melalui proses validasi sehingga kualitas dan keandalannya dapat dipertanggungjawabkan.
> Meskipun data dikumpulkan secara otomatis, proses validasi tetap diperlukan karena kesalahan dapat terjadi pada proses logging, preprocessing, maupun konfigurasi eksperimen. Oleh karena itu, validasi formal diperlukan agar data yang digunakan untuk analisis benar-benar sesuai dengan desain penelitian.
