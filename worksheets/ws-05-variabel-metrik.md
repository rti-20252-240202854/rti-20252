# WS-05: Variabel & Metrik

> **Bab 5 — Metric, Measurement & Data**

---

## Ringkasan Materi

### Measurement Alignment Model

Setiap pengukuran yang valid harus bisa ditelusuri melalui rantai ini tanpa lompatan logis:

```
Problem → Concept → Variable → Metric → Data → Result
```

### Operationalization = Keputusan Desain

Menerjemahkan konsep abstrak menjadi variabel terukur bukan proses mekanis. "Code quality" yang diukur via SonarQube code smells membawa asumsi implisit. Setiap operasionalisasi harus didokumentasikan dan dijustifikasi.

### Empat Tipe Data (NOIR)

| Tipe | Ciri | Contoh | Operasi Valid |
|------|------|--------|---------------|
| **Nominal** | Kategori, tanpa urutan | Jenis algoritma (RF, SVM, CNN) | Modus, chi-square |
| **Ordinal** | Urutan, interval tidak sama | Skala Likert (1-5) | Median, Spearman |
| **Interval** | Jarak bermakna, tanpa nol absolut | Suhu Celsius | Mean, Pearson, t-test |
| **Ratio** | Jarak bermakna + nol absolut | Waktu eksekusi (ms) | Semua operasi |

Tipe data menentukan uji statistik yang valid. Kebanyakan metrik performa TI = ratio; persepsi pengguna = ordinal.

### Kriteria Pemilihan Metrik

- **Representative** — Mewakili konsep yang diteliti
- **Sensitive** — Cukup peka menangkap perbedaan bermakna (hindari ceiling effect)
- **Feasible** — Bisa dikumpulkan dalam batasan waktu dan biaya

### Pre-registration

Metrik harus ditentukan **sebelum** eksperimen. Memilih metrik setelah melihat data = **p-hacking**. Metrik tambahan yang ditemukan kemudian dilaporkan sebagai *exploratory*, bukan *confirmatory*.

### Primary vs Secondary Metric

- **Primary Metric** — Langsung terikat ke hipotesis, menentukan kesimpulan
- **Secondary Metric** — Pendukung, dilaporkan di samping primary; statusnya suplementer

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Pemilihan metrik | Berdasarkan kebiasaan/tool yang ada | Berdasarkan construct validity |
| Anomali | Dihapus untuk laporan bersih | Diinvestigasi — bisa jadi temuan |
| Kapan dipilih | Setelah sistem jadi (monitoring) | Sebelum eksperimen (by design) |

### Istilah Penting

- **Operationalization** — Transformasi konsep abstrak menjadi variabel terukur
- **Construct Validity** — Sejauh mana pengukuran benar-benar mengukur konsep yang dimaksud
- **Measurement Scale** — Klasifikasi data (NOIR) yang menentukan analisis valid
- **Multi-metric Evaluation** — Menggunakan beberapa metrik untuk menangkap konsep kompleks

---

## Template A.5 — Definisi Variabel, Metrik & Justifikasi

```
VARIABLE & METRIC DEFINITION

Research Question: apakah penggunaan SMOTE dapat meningkatkan performa Random Forest pada deteksi anomali jaringan dibandingkan random fores tanpa SMOTE berdasarkan akurasi, presisi, recal, dan f1-score?

| Variabel | Tipe | Konsep | Metrik | Skala | Satuan | Cara Mengukur | Justifikasi |
|----------|------|--------|--------|-------|--------|---------------|-------------|
| penggunaan SMOTE | IV   | teknik preprocessing data | dengan/tanpa SMOTE | nomminal | - | membandingkan 2 kondisi model | karena fokus penelitian ada di pengaruh SMOTE |
| performa model | DV   | kemampuan model mendeteksi anomali | akurasi,presisi,recal,f1 score | rasio | % | menghitung evaluasi model | metrik ini umum dipakai pada deteksi anomali |
| dataset dan parameter model | CV   | kondisi pengujian tetap | dataset dan model seting yang sama | normal | - | menggunakan dataset dan parameter yang sama | agar hasil perbandingan lebih adil |

Alignment Check:
  RQ → Concept → Variable → Metric → Data → Result
  [v] Setiap langkah terdokumentasi
  [v] Tidak ada "lompatan logis"
  [v4] Metrik mengukur apa yang dimaksud (construct validity)
```

---

## Latihan 1 — Operationalization Chain

Gunakan RQ dari WS-04. Definisikan variabel dan metriknya.

**RQ:** apakah penggunaan SMOTE dapat meningkatkan performa Random Forest pada deteksi anomali jaringan dibandingkan Random Forest tanpa SMOTE berdasarkan akurasi, precision, recall, dan F1-score?

| Variabel | Tipe | Konsep Abstrak | Metrik Konkret | Skala (NOIR) | Satuan |
|----------|------|---------------|----------------|-------------|--------|
| penggunaan SMOTE | IV | teknik balancing data | dengan/tanpa SMOTE | nominal | - |
| performa model | DV | kemampuan deteksi anomali | akurasi,presisi,recal,f1 score | rasio | % |
| dataset & parameter | CV | konsisten pengujian | dataset dan parameter tetap | nominal | - |

**Apakah ada lompatan logis dalam rantai?** [ ] Ya / [v] Tidak
> Jika ya, di mana? ____________________________________

---

## Latihan 2 — Evaluasi Metrik

Evaluasi metrik DV yang dipilih di Latihan 1 menggunakan 3 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Representative | 5 | f1 score cukup untuk keseimbangan presisi dan recal |
| Sensitive | 4 | perubahan performa model masih bisa terlihat jelas |
| Feasible | 5 | mudah dihitung |

**Apakah perlu secondary metric?** [v] Ya / [ ] Tidak
> Jika ya, apa dan mengapa? penting untuk melihat kemampuan model mendeteksi anomali yang jumlahnya sedikit

**Contoh kasus ceiling effect untuk metrik ini:**
> kalau akurasi model sudah terlalu tinggi dari awal, misalnya 99%, maka peningkatan kecil jadi susah terlihat walaupun sebenarnya model berubah

---

## Latihan 3 — Data Quality Check

Bayangkan data yang akan dikumpulkan dari eksperimen. Evaluasi 4 dimensi kualitas data.

| Dimensi | Pertanyaan | Jawaban | Strategi Mitigasi |
|---------|-----------|---------|------------------|
| Completeness | *Apakah semua data point terkumpul?* | ada data yang bisa hikang | mengecek ulang dataset |
| Consistency | *Apakah ada kontradiksi internal?* | bisa terjadi perbedaan label data | validasi label dataset |
| Validity | *Apakah benar-benar mengukur yang dimaksud?* | betul,karena menggunakan metrik model evaluasi | menggunakan metrik yang umum dipakai |
| Representativeness | *Apakah sampel mewakili populasi target?* | belum tentu | menggunakan dataset yang beragam |

---

## Refleksi

> Mengapa memilih metrik setelah melihat data dianggap p-hacking? Apa bedanya dengan eksplorasi data yang sah?

**Jawaban:**
> memilih metrik setelah melihat hasil data disebut p-hacking karena peneliti bisa memilih metrik yang paling menguntungkan hasil penelitiannya. Akibatnya, hasil jadi kurang objektif
> sedangkan eksplorasi data yang benar dilakukan untuk memahami pola data, bukan untuk mengubah hasil supaya terlihat lebih bagus
