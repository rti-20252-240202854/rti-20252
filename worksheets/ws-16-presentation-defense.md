# WS-16: Presentation & Defense (UAS)

> **Bab 16 — Presentasi & Pertahanan Ilmiah**

---

## Ringkasan Materi

### Scientific Defense Model

```
Research Work → Presentation → Questioning → Defense → Evaluation → Acceptance
```

### Presentasi ≠ Ringkasan Paper

| Paper | Presentasi |
|-------|-----------|
| Dibaca (self-paced) | Didengar (presenter-paced) |
| Detail lengkap | Ide kunci + highlight |
| Tabel numerik detail | Grafik visual + angka kunci |
| Pembaca bisa re-read | Audiens dengar sekali |

**Prinsip:** Presentasi membutuhkan **reformulasi**, bukan kompresi. Medium berbeda = pendekatan berbeda.

### Claim-Evidence-Reasoning (CER)

Setiap jawaban defense harus memiliki:
1. **Claim** — Pernyataan yang dijawab
2. **Evidence** — Data/fakta pendukung
3. **Reasoning** — Logika yang menghubungkan evidence ke claim

**Contoh:**
| Pertanyaan | Bad Answer | Good Answer (CER) |
|-----------|-----------|-------------------|
| "Kenapa hanya 3 dataset?" | "Tiga sudah cukup" | "3 dataset mewakili variasi: small-clean, medium-clean, medium-noisy [E]. Generalisasi perlu validasi lanjut — listed as limitation [R]" |
| "Hasil DS-3 menurun?" | "Itu outlier" | "Ya, karena distribusi heavy-tail melanggar asumsi Gaussian [E]. Ini menunjukkan boundary condition metode [R]" |
| "Effect size?" | "p=0.003, jadi signifikan" | "Cohen's d=1.2 (large effect) [E] — bukan hanya signifikan tapi substansial [R]" |

### Slide Design — One Slide, One Message

**Optimal 9-Slide Plan (15 menit):**

| # | Slide | Waktu | Pesan |
|---|-------|-------|-------|
| 1 | Title + context | 1 min | Apa ini tentang apa |
| 2 | Problem + motivation | 2 min | Mengapa penting |
| 3 | Gap + RQ | 1.5 min | Apa yang belum terjawab |
| 4 | Method overview | 2 min | Bagaimana dijawab (diagram) |
| 5 | Key result — tabel | 2 min | Temuan utama |
| 6 | Key result — grafik | 2 min | Pola visual |
| 7 | Interpretation + failure | 2 min | Apa artinya |
| 8 | Limitation + future | 1.5 min | Batasan & arah |
| 9 | Conclusion + contribution | 1 min | Closing message |

### Anticipatory Defense

Prediksi pertanyaan berdasarkan kategori:

| Kategori | Contoh Pertanyaan |
|---------|------------------|
| Problem | "Mengapa masalah ini penting?" |
| Gap | "Bagaimana dengan studi X yang sudah menjawab ini?" |
| Method | "Mengapa metode ini, bukan Y?" |
| Results | "Bagaimana menjelaskan anomali di DS-3?" |
| Generalization | "Apakah bisa diterapkan di domain lain?" |

### Tiga Prinsip Jawaban

1. **Direct** — Jawab dulu, elaborasi kemudian
2. **Data-based** — Tunjuk evidence spesifik
3. **Honest** — Akui limitasi jika memang ada

### Jebakan Kognitif

1. "Presentasi = semua yang ada di paper" → terlalu padat
2. "Slide cantik = presentasi bagus" → konten > estetika
3. "Tidak bisa jawab = gagal" → "I don't know, but..." menunjukkan kejujuran
4. "Tidak perlu latihan — saya paham riset saya" → latihan = menemukan celah

---

## Template A.16 — Defense Preparation Sheet

```
DEFENSE PREPARATION

Slide Deck Plan:
  Total slides   : 10 (9 konten + 1 penutup)
  Time per slide : kurang lebih 1,5 menit
  Total time     : kurang lebih 15 menit

Slide Outline:
| # | Pesan Utama | Visual | Waktu |
|---|-------------|--------|-------|
| 1 | Judul Penelitian | Cover + Logo Kampus | 1-2 menit |
| 2 | Latar Belakang Masalah | Diagram IDS + Ilustrasi Class Imbalance | 2-3 menit  |
| 3 | Research Gap & Research Question | Diagram penelitian terdahulu | 3 menit  |
| 4 | Metodologi Penelitian | Flowchart Dataset → SMOTE → Random Forest → Evaluasi | 3 menit  |
| 5 | Hasil Eksperimen | Tabel Accuracy, Precision, Recall, F1-Score | 3 menit  |
| 6 | Hasil Statistik | Grafik perbandingan + p-value + Cohen's d | 3 menit  |
| 7 | Interpretasi & Failure Analysis | Diagram penyebab SMOTE tidak signifikan | 3 menit  |
| 8 | Limitation & Future Work | Diagram limitation dan rekomendasi | 5 menit  |
| 9 | Kesimpulan | Ringkasan kontribusi penelitian | 2 menit  |
| ..|             |        |       |

Anticipatory Defense Matrix:
| Kategori | Pertanyaan Potensial | Jawaban (CER) |
|----------|---------------------|---------------|
| Problem  | Mengapa memilih topik IDS? | Claim: IDS penting untuk keamanan jaringan. Evidence: Serangan siber terus meningkat sehingga diperlukan model deteksi yang akurat. Reasoning: Penelitian bertujuan meningkatkan kualitas deteksi intrusi. |
| Gap      | Mengapa menggunakan SMOTE? | Claim: Banyak penelitian menggunakan SMOTE untuk mengatasi class imbalance. Evidence: Literatur menunjukkan SMOTE efektif pada dataset yang sangat tidak seimbang. Reasoning: Penelitian ini menguji apakah kondisi tersebut juga berlaku pada CIC-IDS2017. |
| Method   | Mengapa memilih Random Forest? | Claim: Random Forest memiliki performa tinggi pada klasifikasi IDS. Evidence: Banyak penelitian menjadikan Random Forest sebagai baseline karena stabil dan akurat. Reasoning: Cocok untuk mengevaluasi pengaruh SMOTE. |
| Results  | Mengapa SMOTE tidak meningkatkan hasil? | Claim: Dataset sudah memiliki performa sangat tinggi tanpa SMOTE. Evidence: Accuracy sekitar 99,99% baik sebelum maupun sesudah SMOTE, p-value seluruh metrik > 0,05. Reasoning: Oversampling tidak memberikan perubahan signifikan karena Random Forest sudah mampu mengklasifikasikan data dengan baik. |
| Generalization | Apakah hasil ini berlaku pada dataset lain? | Claim: Belum tentu. Evidence: Penelitian hanya menggunakan satu subset CIC-IDS2017. Reasoning: Perlu pengujian pada dataset lain sebelum dilakukan generalisasi. |

Latihan:
  Latihan 1: [10 juli 2026]
  - Menyusun slide presentasi.
  - Memastikan alur penelitian sesuai Research Question.
  - Estimasi waktu presentasi sekitar 15 menit.

  Latihan 2: [12 juli 2026]
  - Melakukan simulasi presentasi.
  - Mengecek konsistensi jawaban berdasarkan hasil uji statistik.
  - Memperbaiki beberapa penjelasan pada bagian Discussion dan Conclusion.

  Latihan 3: [15 juli 2026] — [catatan timing & feedback]
  - Latihan menjawab pertanyaan penguji.
  - Menyiapkan jawaban terkait pemilihan metode, hasil statistik, limitation, dan future work.
  - Waktu presentasi sudah sesuai target.


## Latihan 1 — Slide Outline

Rencanakan presentasi 15 menit untuk riset Anda.

| # | Pesan Utama | Visual yang Digunakan | Waktu |
|---|-------------|----------------------|-------|
| 1 | Judul penelitian | Cover + Logo | 2 menit |
| 2 | Pentingnya Intrusion Detection System dan class imbalance | Diagram IDS | 2 menit |
| 3 | Research Gap dan Research Question | Tabel penelitian terdahulu | 2 menit |
| 4 | Dataset, SMOTE, Random Forest, Flow Penelitian | Flowchart | 3 menit |
| 5 | Hasil Accuracy, Precision, Recall, F1-Score | Tabel hasil eksperimen | 3 menit |
| 6 | Hasil Uji Statistik (Shapiro, Wilcoxon, Cohen's d, CI) | Grafik dan tabel statistik | 2 menit |
| 7 | Interpretasi hasil dan Failure Analysis | Diagram penyebab | 3 menit |
| 8 | Limitasi dan Future Work | Diagram | 3 menit |
| 9 | Kesimpulan | Bullet point | 2 menit |

**Total waktu estimasi:** kurang lebih 30 menit

---

## Latihan 2 — Anticipatory Defense

Prediksi 5 pertanyaan yang mungkin diajukan penguji, lalu siapkan jawaban CER.

| # | Kategori | Pertanyaan | Claim | Evidence | Reasoning |
|---|----------|-----------|-------|----------|-----------|
| 1 | Problem | Mengapa memilih IDS? | IDS penting untuk keamanan jaringan. | Banyak serangan siber menargetkan jaringan komputer. | IDS membantu mendeteksi serangan secara otomatis. |
| 2 | Method | Mengapa menggunakan Random Forest? | Random Forest merupakan algoritma yang stabil dan akurat. | Banyak penelitian IDS menggunakan Random Forest sebagai baseline. | Cocok untuk mengevaluasi pengaruh SMOTE. |
| 3 | Method | Mengapa menggunakan SMOTE? | Untuk mengatasi ketidakseimbangan kelas. | SMOTE menghasilkan data sintetis pada kelas minoritas. | Diharapkan meningkatkan kemampuan klasifikasi kelas minoritas. |
| 4 | Results | Mengapa hasil tidak meningkat? | Dataset sudah memiliki performa tinggi tanpa SMOTE. | Accuracy sekitar 99,99% dan seluruh p-value > 0,05. | Tidak ada ruang peningkatan yang signifikan. |
| 5 | Generalization | Apakah bisa diterapkan pada dataset lain? | Belum tentu. | Penelitian hanya menggunakan satu subset CIC-IDS2017. | Perlu validasi pada dataset lain agar hasil lebih umum. |

---

## Latihan 3 — Simulasi Q&A

Minta teman/kolega mengajukan 3 pertanyaan tentang riset Anda. Catat pertanyaan dan evaluasi jawaban Anda.

| # | Pertanyaan | Jawaban Saya | Evaluasi |
|---|-----------|-------------|---------|| *1* | *Contoh: "Mengapa tidak membandingkan dengan metode Y?"* | *Contoh: "Karena Y memerlukan dataset labeled yang tidak tersedia. Disebutkan sebagai limitasi di halaman X."* | *[✓] Direct [✓] Data-based [✓] Honest* |
| 1 | Mengapa tidak menggunakan algoritma lain seperti XGBoost? | Fokus penelitian adalah mengevaluasi pengaruh SMOTE terhadap Random Forest sehingga algoritma lain menjadi ruang penelitian selanjutnya. | [v] Direct [v] Data-based [v] Honest |
| 2 | Mengapa hanya menggunakan lima kali pengujian? | Lima random seed digunakan untuk melihat konsistensi performa model. Jumlah run dicatat sebagai salah satu keterbatasan penelitian. | [v] Direct [v] Data-based [v] Honest |
| 3 | Mengapa hasil SMOTE tidak signifikan? | Karena Random Forest telah mencapai performa sangat tinggi pada dataset yang digunakan sehingga tambahan data sintetis tidak memberikan peningkatan berarti. | [ ] Direct [ ] Data-based [ ] Honest |

**Pertanyaan yang paling sulit dijawab:**
> Apakah hasil penelitian ini masih berlaku jika menggunakan dataset IDS lain dengan tingkat ketidakseimbangan kelas yang lebih tinggi?

**Apa yang perlu disiapkan lebih baik:**
> Menambah referensi penelitian terdahulu mengenai performa SMOTE pada berbagai dataset IDS serta menyiapkan eksperimen tambahan menggunakan algoritma lain sebagai pembanding.

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-16 — dari paradigma riset hingga presentasi — bagian mana yang paling mengubah cara Anda berpikir tentang riset? Apa satu hal yang akan selalu Anda terapkan di riset berikutnya?
Dari seluruh proses WS-01 sampai WS-16, bagian yang paling mengubah cara berpikir saya adalah pentingnya melakukan analisis statistik setelah memperoleh hasil eksperimen. Sebelumnya saya menganggap peningkatan nilai metrik sudah cukup untuk menyimpulkan keberhasilan suatu metode. Namun setelah mempelajari uji normalitas, uji hipotesis, effect size, dan confidence interval, saya memahami bahwa kesimpulan penelitian harus didukung oleh bukti statistik yang kuat.

**Insight terbesar:**
> Hasil penelitian yang tidak menunjukkan peningkatan signifikan tetap memiliki nilai ilmiah karena dapat menjelaskan batas efektivitas suatu metode pada karakteristik dataset tertentu.

**Yang akan selalu diterapkan:**
> Pada penelitian berikutnya saya akan selalu melakukan validasi data, analisis statistik, serta mendokumentasikan seluruh proses eksperimen agar hasil penelitian dapat dipertanggungjawabkan dan direproduksi oleh peneliti lain.
