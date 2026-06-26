# WS-01: Distorsi & Paradigma

> **Bab 1 — Research Mindset in IT**

---

## Ringkasan Materi

### Research Trust Model

Pengetahuan ilmiah tidak muncul langsung dari kenyataan. Ia melewati **6 tahap transformasi** yang masing-masing rawan distorsi:

```
Reality → Data → Processing → Analysis → Inference → Knowledge
```

Etika mencegah distorsi yang disengaja (fabrikasi, cherry-picking). Validitas mendeteksi distorsi yang tidak disengaja (confounding variable, sampling bias).

### Tiga Jenis Validitas

| Jenis | Pertanyaan | Contoh Ancaman |
|-------|-----------|----------------|
| **Internal Validity** | Apakah hubungan kausal benar ada? | Confounding variable |
| **External Validity** | Apakah bisa digeneralisasi? | Dataset terlalu homogen |
| **Construct Validity** | Apakah mengukur hal yang benar? | Metrik tidak sesuai klaim |

### Paradigma Riset

Mata kuliah ini menggunakan pendekatan **Positivist** (fenomena TI bisa diukur objektif melalui eksperimen terkontrol) diperkuat **Design Science Research** (DSR). Penting untuk membedakan keduanya:

| Paradigma | Cara Kerja | Contoh di TI |
|-----------|-----------|---------------|
| **Positivis** | Uji hipotesis dengan eksperimen terkontrol | Apakah CNN lebih akurat dari RF pada dataset X? |
| **Design Science Research** | Bangun artefak (sistem/model/framework) untuk menguji proposisi | Dapatkah arsitektur hybrid CNN+LSTM membuktikan peningkatan recall ≥5%? |
| **Interpretivis** | Pahami makna melalui konteks & kualitatif | Bagaimana peneliti manafsirkan anomali data sensor IoT? |

Dalam DSR, artefak **bukan tujuan akhir** — ia adalah instrumen untuk menghasilkan pengetahuan. Pertanyaan riset tetap harus difalsifikasi.

### Mode Berpikir Peneliti

**Curious** (mempertanyakan fenomena) → **Critical** (mengevaluasi klaim berdasarkan bukti) → **Systematic** (merancang investigasi terstruktur dan reproducible).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Membuat sistem yang bekerja | Menghasilkan pengetahuan yang valid |
| Pertanyaan khas | "Bagaimana membuatnya jalan?" | "Apakah klaim ini benar?" |
| Ukuran sukses | Sistem berfungsi, client puas | Hipotesis terjawab, temuan tervalidasi |
| Kegagalan | Harus dihindari | Harus dilaporkan (negative result = kontribusi) |

### Istilah Penting

- **Research Mindset** — Pola pikir yang menuntut bukti dan mempertanyakan asumsi
- **Research Ethics** — Prinsip perilaku: kejujuran, objektivitas, keterbukaan, akuntabilitas
- **HARKing** — Hypothesizing After Results are Known — merumuskan hipotesis setelah melihat data
- **Falsifiability** — Hipotesis harus bisa dibuktikan salah

---

## Template A.1 — Research Mindset Self-Assessment

```
Nama Peneliti    : Azzam Zain Zaidan Sudiyono
Tanggal          : 24 April 2026

1. Ketika membaca klaim "metode X 95% akurat":
   - Pertanyaan pertama saya: Dataset apa yang digunakan? Apakah dibandingkan dengan baseline yang fair?
   - Data yang dibutuhkan untuk verifikasi: Confusion matrix, ukuran dataset, distribusi data, metode evaluasi (cross-validation / holdout)

2. Posisi paradigma:
   - Pendekatan: [v] Positivis  [ ] Interpretivis  [ ] Design Science  [ ] Mixed
   - Alasan:Penelitian ini berfokus pada pengujian pengaruh penggunaan SMOTE terhadap performa Random Forest menggunakan data                numerik dan eksperimen terkontrol, sehingga lebih sesuai dengan paradigma positivis.

3. Identifikasi distorsi:
   - Asumsi tersembunyi: dataset CIC-IDS2017 dianggap dapat mewakili kondisi jaringan nyata, padahal belum tentu menggambarkan                            seluruh kondisi jaringan sebenarnya.
   - Sumber bias potensial: dataset tidak sepenuhnya mewakili kondisi jaringan nyata dan kemungkinan overfitting akibat data                                 sintetis hasil SMOTE.
   - Langkah mitigasi: menggunakan data yang beragam,validasi menyilang,dan pengujian data yang berbeda

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: data eksperimen dan hasil evaluasi model
   - Batasan yang diakui sejak awal: model hanya diuji pada dataset tertentu
```

---

## Latihan 1 — Identifikasi Distorsi

Pilih satu paper riset di bidang TI yang mengklaim "metode X meningkatkan performa." Telusuri setiap tahap Research Trust Model.

> **Panduan pencarian paper:** Gunakan [IEEE Xplore](https://ieeexplore.ieee.org), [ACM Digital Library](https://dl.acm.org), atau Google Scholar. Pilih paper **tahun 2020 ke atas**, di topik yang Anda minati: deteksi anomali, klasifikasi citra, NLP, keamanan siber, IoT, dsb.
>
> **Contoh domain TI:** "Deteksi anomali lalu-lintas jaringan menggunakan CNN — akurasi meningkat 94% vs baseline SVM 87%." Distorsi potensial: apakah dataset normal/anomali seimbang? Apakah hanya diuji pada satu vendor traffic?

**Paper yang dipilih:**
> Judul: Penerapan Teknik SMOTE untuk Mendeteksi Perilaku Jaringan Berbasis Trafik Enkripsi
> Penulis (Tahun): Ulfi Muzayyanah Fadil(2025)
> Sumber/Link DOI: (https://doi.org/10.23960/jitet.v14i1.8880)

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | Menggunakan dataset publik CIC-IDS2017 yang berisi trafik normal dan berbagai jenis serangan jaringan. | Dataset bisa tidak representatif terhadap kondisi jaringan nyata |
| Data → Processing |Data dinormalisasi dan diseimbangkan menggunakan SMOTE |Data sintetis hasil SMOTE tidak sepenuhnya mencerminkan data asli |
| Processing → Analysis |Model Random Forest dilatih dengan data sebelum dan sesudah SMOTE|Overfitting karena data hasil oversampling |
| Analysis → Inference |Performa model dibandingkan menggunakan akurasi, precision, recall, dan F1-score |Metrik bisa bias karena distribusi data sudah diubah |
| Inference → Knowledge |Disimpulkan bahwa SMOTE meningkatkan performa deteksi anomali|Generalisasi berlebihan ke semua kasus jaringan |

**Distorsi paling besar di tahap:** Processing

Alasan:
Karena pada tahap ini dilakukan proses oversampling menggunakan SMOTE yang menghasilkan data sintetis. Data tambahan tersebut dapat mengubah distribusi data asli sehingga peningkatan performa model belum tentu mencerminkan kemampuan model pada kondisi jaringan nyata.

**Dua distorsi spesifik yang teridentifikasi:**
1. Bias karena data buatan
   SMOTE menghasilkan data anomali tambahan yang bukan berasal dari kejadian nyata, melainkan dibentuk dari pola data yang sudah    ada.
2. Bias karena distribusi data berubah
   Setelah dilakukan SMOTE, distribusi data menjadi lebih seimbang dibanding kondisi aslinya. Padahal pada kondisi nyata, data      anomali biasanya tetap lebih sedikit daripada data normal sehingga hasil model belum tentu dapat digeneralisasi ke semua         kondisi jaringan. 


## Latihan 2 — Analisis Kasus Etika

Skenario: Seorang peneliti menemukan bahwa jika 3 data point outlier dihapus, hasil eksperimennya menjadi signifikan. Dengan outlier, hasilnya tidak signifikan.

| Perspektif | Analisis |
|------------|---------|
| Kejujuran ilmiah |Peneliti harus jujur dan tidak boleh menghapus data hanya supaya hasilnya terlihat bagus |
| Transparansi |Kalau memang outlier mau dihapus, harus dijelaskan alasannya dan tetap ditampilkan hasil sebelum & sesudah |
| Peer review |Reviewer biasanya akan mempertanyakan kenapa data dihapus dan apakah itu mempengaruhi hasil penelitian |

**Keputusan akhir dan justifikasi:**
Menurut saya, data outlier tidak boleh dihapus hanya untuk membuat hasil yang bagus.
Kalau memang outlier itu kesalahan data (misalnya error sistem), boleh dihapus, tapi harus dijelaskan juga alasannya serta tetap ditampilkan hasil sebelum dan sesudah.

## Latihan 3 — Posisi Paradigma

**Topik riset:** Deteksi anomali jaringan menggunakan SMOTE dan Random Forest

> **Skala 1–5:** 1 = tidak sesuai sama sekali dengan topik ini, 5 = sangat sesuai dan dominan digunakan pada riset bertopik serupa.

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian dengan topik (1–5) | 4 | 1 | 3 |
| Jenis data yang dikumpulkan | Data numerik (dataset jaringan, metrik akurasi, recall) | Tidak relevan | Hasil eksperimen model |
| Limitasi paradigma |Tidak melihat konteks dunia nyata secara mendalam |Tidak cocok untuk penelitian berbasis data & model |Fokus ke sistem, bukan pengujian hipotesis |

**Paradigma yang dipilih:** Positivis
**Alasan:** Karena penelitian ini menggunakan data numerik,menguji performa model,membandingkan hasil sebelum dan sesdah SMOTE. Jadi menurut saya lebih cocok ke ke positivis 

---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
> Sebelum membaca materi ini, saya biasanya langsung percaya saja kalau melihat klaim seperti “95% akurat” tanpa terlalu mempertanyakan bagaimana hasil itu didapatkan
> Setelah memahami adanya kemungkinan distorsi di setiap tahap penelitian, sekarang saya jadi lebih berpikir luas dan akan terpikirkan pertanyaan seperti:
   -Data apa yang digunakan? Apakah seimbang atau tidak?
   -Apakah ada preprocessing seperti SMOTE yang bisa mempengaruhi hasil?
   -Metode evaluasi yang dipakai apa?
   -Apakah dibandingkan dengan metode lain secara adil?
   -Dan apakah hasilnya bisa diterapkan di kondisi nyata atau hanya di dataset tertentu saja?
