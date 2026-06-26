# WS-03: Literature Mapping & Gap

> **Bab 3 — Literature Review, Research Gap & Baseline**

---

## Ringkasan Materi

### Literature Review = Positioning, Bukan Ringkasan

Literature review bukan merangkum paper satu per satu. Pendekatan yang benar adalah **concept-centric** — organisasi berdasarkan tema, metode, atau variabel. Tujuan: menemukan **pola, kontradiksi, dan gap**.

**Perbandingan pendekatan Author-centric vs Concept-centric:**

| Aspek | Author-centric (Hindari) | Concept-centric (Gunakan) |
|-------|--------------------------|---------------------------|
| Struktur | Per penulis/paper ("Rahman et al. menyatakan...") | Per konsep/metode ("Pendekatan berbasis transformer") |
| Tujuan | Ringkasan isi paper | Perbandingan metode & identifikasi gap |
| Contoh paragraph | "Rahman (2023) pakai CNN. Lee (2022) pakai LSTM. Zhang (2021) pakai RF." | "Tiga pendekatan dominan: CNN digunakan oleh 4 paper untuk representasi fitur visual; LSTM untuk data sekuensial; RF sebagai baseline klasik." |
| Hasil akhir | Daftar paper | Peta pengetahuan + gap yang teridentifikasi |

### Empat Jenis Research Gap

| Jenis Gap | Deskripsi | Contoh |
|-----------|----------|--------|
| **Performance Gap** | Performa belum memadai | Akurasi deteksi hanya 78% pada kasus tertentu |
| **Method Gap** | Pendekatan belum diterapkan | Belum ada yang pakai transformer untuk task ini |
| **Data Gap** | Dataset terbatas/tidak representatif | Semua studi pakai dataset sintetis |
| **Context Gap** | Belum diuji pada konteks berbeda | Belum ada evaluasi di negara berkembang |

Gap terkuat = kombinasi 2+ jenis.

### Systematic Search Strategy

1. **Database utama**: IEEE Xplore, ACM DL, Scopus
   - Akses IEEE/ACM melalui jaringan kampus atau VPN institusi
   - Alternatif bebas biaya: Google Scholar, ResearchGate ([researchgate.net](https://www.researchgate.net)), arXiv ([arxiv.org](https://arxiv.org))
2. **Boolean query** yang terdokumentasi eksplisit
   - Contoh: `("anomaly detection" OR "intrusion detection") AND ("deep learning" OR "neural network") NOT ("medical imaging")`
   - Gunakan tanda kutip untuk frasa eksak; AND/OR/NOT mengontrol scope
3. **Snowballing** — dua arah:
   - **Backward snowballing**: buka daftar referensi di paper kunci → telusuri paper yang dikutip
   - **Forward snowballing**: di Google Scholar, klik "Cited by" di bawah paper kunci → temukan paper yang mengutipnya
   - Ulangi 1–2 tingkat untuk membangun cakupan komprehensif
4. Klaim "belum ada penelitian" harus didukung **bukti pencarian**

### Baseline Selection — 3 Kriteria

| Kriteria | Pertanyaan |
|----------|-----------|
| **Relevan** | Apakah menyelesaikan masalah yang sama? |
| **Representatif** | Apakah mewakili common practice? |
| **State-of-the-Art** | Apakah terbaru/terbaik? |

Membandingkan deep learning 2024 dengan decision tree sederhana tanpa justifikasi = **straw man comparison** (perbandingan tidak jujur).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan baca literatur | Mencari solusi yang sudah ada | Memahami apa yang belum terjawab |
| Cara membaca paper | Tutorial, how-to | Metode, limitasi, gap |
| Baseline | Framework terpopuler | State-of-the-art yang rigorous |
| Dokumentasi pencarian | Tidak diperlukan | Wajib (reproducible) |

### Istilah Penting

- **Concept-centric** — Organisasi literatur berdasarkan konsep/metode, bukan per penulis
- **Snowballing** — Backward (telusuri referensi) + Forward (cari yang mengutip paper kunci)
- **Research Position** — Pernyataan eksplisit posisi riset terhadap studi sebelumnya
- **Straw man comparison** — Memilih baseline lemah agar metode sendiri terlihat lebih baik

---

## Template A.3 — Literature Mapping & Gap Identification

```
LITERATURE MAPPING

Topik      : Deteksi anomali jaringan menggunakan SMOTE dan Random Forest
Database   : Google Scholar
Query      : ("intrusion detection" OR "anomaly detection")
               AND ("SMOTE")
               AND ("Random Forest")
               AND ("CIC-IDS2017")
Tahun      : 2020-2025
Hasil awal : 20 paper → Screening → 5 paper final

Literature Matrix (concept-centric):

| Study | Tahun | Method | Data | Result | Limitation |
|-------|-------|--------|------|--------|------------|
|   Fadil et al.   |   2025    |    SMOTE + Random Forest    |   Trafik jaringan   |    akuasi meningkat    |      Data sintetis      |
|   Study A   |   2023    |    SMOTE + SVM   |   Dataset IDS publik   |    Recall meningkat    |      Overfitting      |
|   Study B   |   2022    |    Random Forest   |   Trafik Jaringan   |    Stabil    |     Data tidak seimbang     |
|   Study C   |   2021    |    SMOTE + Neural Network   |   Dataset publik   |    Akurasi Tinggi    |     Tidak Realistis     |
|   Study D   |   2020    |    Decision Tree   |   Trafik jaringan   |    Cepat    |     Performa Rendah     |

Pola yang ditemukan:
  Metode dominan     : SMOTE + Machine Learning (RF, SVM, NN)
  Dataset umum       : Dataset benchmark IDS seperti CIC-IDS2017 dan dataset trafik jaringan publik.
  Limitasi berulang  : Data sintetis, distribusi tidak realistis, overfitting

GAP IDENTIFICATION

Gap 1: janis data gap
  Deskripsi    : Banyak penelitian menggunakan SMOTE untuk mengatasi ketidakseimbangan data, namun belum banyak mengevaluasi                      dampak data sintetis terhadap validitas hasil model.
  Bukti        : Mayoritas studi dalam tabel menggunakan SMOTE sebagai preprocessing
  Signifikansi : Data sintetis bisa tidak mencerminkan kondisi nyata

Gap 2: Jenis:Performance Gap + Validity Gap
  Deskripsi    : Peningkatan performa setelah penggunaan SMOTE belum tentu menunjukkan peningkatan kemampuan model yang                           sebenarnya karena distribusi data telah berubah.
  Bukti        : Akurasi meningkat setelah SMOTE, tapi distribusi data berubah
  Signifikansi : Bisa menghasilkan kesimpulan yang menyesatkan

Baseline Selection:
| Baseline | Mengapa Relevan | Mengapa Representatif | Source |
|----------|-----------|---------------|--------|
|Random Forest tanpa SMOTE|Task sama|Metode umum pada IDS|Study B|
|Random Forest + SMOTE|Sama algoritma, berbeda preprocessing|Digunakan pada penelitian Fadil et al.|Fadil et al.|
```

---

## Latihan 1 — Concept-Centric Literature Table

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan database akademik.

> **Panduan pencarian:**
> - Database: IEEE Xplore, ACM DL, Google Scholar, atau ResearchGate
> - Tulis query Boolean yang digunakan: contoh `("object detection" OR "image classification") AND ("edge computing") NOT ("medical")`. Dokumentasikan query secara eksplisit.
> - Akses gratis: buka Google Scholar → cari judul paper → klik [PDF] jika tersedia, atau akses lewat campus VPN

**Topik riset:** Deteksi anomali jaringan dengan SMOTE pada dataset CIC-IDS2017
**Query pencarian:** ("anomaly detection") AND ("SMOTE") AND ("machine learning")
**Database:** Google Scholar

| # | Study | Tahun | Method | Dataset | Result | Limitasi |
|---|-------|-------|--------|---------|--------|----------|
| 1 | Fadil et al. | 2025 | SMOTE + RF | Trafik jaringan | Akurasi naik | Data sintetis |
| 2 | Study A | 2023 | SMOTE + SVM | IDS dataset | Recall naik | Overfitting |
| 3 | Study B | 2022 | RF | Trafik jaringan | Stabil | Imbalance |
| 4 | Study C | 2021 | SMOTE + NN | Dataset publik | Tinggi | Tidak realistis |
| 5 | Study D | 2020 | Decision Tree | Trafik jaringan | Cepat | Kurang akurat |

**Pola yang terlihat — Metode dominan:** SMOTE + ML
**Limitasi yang berulang:** Data sintetis, distribusi data berubah, dan potensi overfitting.

---

## Latihan 2 — Gap Identification

Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap | Ditemukan? | Gap Statement |
|-----------|-----------|---------------|
| Performance Gap | [v] Ya / [ ] Tidak | Performa meningkat setelah SMOTE tapi belum tentu valid |
| Method Gap | [ ] Ya / [v] Tidak | |
| Data Gap | [v] Ya / [ ] Tidak | Banyak studi menggunakan data sintetis |
| Context Gap | [ ] Ya / [v] Tidak | |

**Gap utama yang dipilih:** Data Gap + Performance Gap
**Mengapa gap ini penting (bukan sekadar "belum ada yang meneliti")?**
> Karena model yang dilatih dari data sintetis bisa menghasilkan performa tinggi di penelitian, tapi belum tentu bekerja dengan baik di kondisi nyata.

---

## Latihan 3 — Baseline Selection

Pilih 2 baseline dari literatur yang sudah dibaca.

| # | Baseline | Mengapa Relevan | Mengapa Representatif | Apakah SOTA? | Sumber |
|---|----------|----------------|----------------------|-------------|--------|
| 1 | Random Forest tanpa SMOTE | Task sama | Umum digunakan | Bukan | Study B |
| 2 | SVM + SMOTE | Sama metode preprocessing | Banyak Dipakai | Bukan | Study A |

**Apakah pemilihan baseline ini bisa dianggap straw man?** [ ] Ya / [v] Tidak
> Justifikasi: Baseline yang dipilih masih relevan dan umum digunakan, bukan metode yang sengaja dilemahkan.

---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
“Belum ada yang meneliti” itu belum tentu benar, bisa jadi kita kurang cari referensi. Sedangkan research gap itu harus ada bukti dari beberapa penelitian yang menunjukkan kekurangan yang sama.
Cara membuktikan gap itu ada adalah dengan membaca beberapa paper, lalu melihat pola yang sama, misalnya banyak penelitian menggunakan SMOTE tapi punya masalah yang sama yaitu data menjadi tidak realistis. Dari situ baru bisa disimpulkan bahwa memang ada gap yang perlu diteliti.
