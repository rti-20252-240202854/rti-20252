# WS-15: Scientific Writing

> **Bab 15 — Penulisan Ilmiah**

---

## Ringkasan Materi

### Scientific Argument Flow

```
Problem → Gap → RQ → Method → Result → Analysis → Conclusion → Contribution
```

Paper ilmiah adalah **satu argumen utuh** dari masalah ke kontribusi. Setiap node harus terhubung logis ke node sebelum dan sesudahnya.

### Struktur IMRAD

| Section | Peran | Pertanyaan Kunci |
|---------|-------|-----------------|
| **Introduction** | Motivasi + frame | Why is this needed? |
| **Method** | Deskripsi (reproducible) | How was it done? |
| **Results** | Laporan objektif | What was found? |
| **Discussion** | Interpretasi + refleksi | What does it mean? |
| **Conclusion** | Ringkasan + kontribusi | So what? |

### Logical Flow — "Red Thread"

Setiap paragraf menjawab satu pertanyaan dan memicu pertanyaan berikutnya. Alur logis ini harus terasa di tiga level:
1. **Antar-kalimat** dalam paragraf
2. **Antar-paragraf** dalam section
3. **Antar-section** dalam paper

### Internal Consistency

Setiap elemen yang dijanjikan di Introduction harus hadir di Discussion/Conclusion.

**Consistency Matrix:**
```
           Intro  Method  Result  Discuss  Conclude
RQ1          ✓      ✓       ✓       ✓        ✓
RQ2          ✓      ✓       ✓       ✗ ←      ✓
Metrik-X     ✗      ✗       ✓ ←     ✗        ✗
```
**Masalah:** RQ2 dibahas di semua bagian kecuali Discussion. Metrik-X muncul di Result tapi tidak diperkenalkan di Method.

### Writing Quality Triad

| Kualitas | Deskripsi | Contoh Buruk → Baik |
|----------|----------|---------------------|
| **Clarity** | Dipahami sekali baca | "Performa meningkat" → "Accuracy meningkat dari 85.3% ke 89.7%" |
| **Precision** | Istilah eksak, tanpa ambiguitas | "signifikan" → "signifikan secara statistik (p=0.003, d=1.2)" |
| **Conciseness** | Setiap kata menambah informasi | Hapus kalimat redundan, filler words |

### Urutan Penulisan yang Disarankan

1. **Method & Results** — paling stabil, tulis pertama
2. **Discussion** — interpretasi berdasarkan hasil
3. **Introduction** — frame sesuai temuan aktual
4. **Abstract & Conclusion** — terakhir

### Target Jumlah Kata

| Section | Target |
|---------|--------|
| Introduction | 500–700 |
| Related Work | 700–1000 |
| Method | 800–1200 |
| Results | 500–800 |
| Discussion | 600–900 |
| Conclusion | 200–400 |

### Jebakan Kognitif

1. "Lebih panjang = lebih lengkap" → conciseness lebih berharga
2. "Introduction harus ditulis pertama" → justru ditulis terakhir
3. "Jargon teknis = lebih ilmiah" → clarity lebih penting
4. "Discussion = ringkasan Results" → Discussion = interpretasi + konteks

---

## Template A.15 — Paper Structure Checklist

```
PAPER STRUCTURE CHECKLIST

Title   : Pengaruh Penggunaan SMOTE terhadap Performa Random Forest pada Dataset CIC-IDS2017 untuk Deteksi Intrusi
Target  : [ ] Jurnal  [ ] Konferensi  [v] Laporan

Section Check:
  [v] Abstract — masalah, metode, hasil utama, kontribusi (max 250 kata)
  [v] Introduction — konteks → gap → RQ → kontribusi → struktur paper
  [v] Related Work — concept-centric, gap positioning
  [v] Method — reproducible: desain, variabel, metrik, setup, prosedur
  [v] Results — tabel + grafik + observasi (tanpa interpretasi)
  [v] Discussion — interpretasi, perbandingan, implikasi, limitation
  [v] Conclusion — jawaban RQ, kontribusi, future work

Consistency Matrix:
  [v] RQ di Introduction = RQ di Method = RQ di Conclusion
  [v] Variabel di Method = variabel di Results
  [v] Klaim di Discussion didukung data di Results
  [v] Limitasi di Discussion di-address di Conclusion/Future Work

Writing Quality:
  [v] Clarity — mudah dipahami tanpa re-read
  [v] Precision — tidak ada istilah ambigu
  [v] Conciseness — tidak ada kalimat redundan
```

---

## Latihan 1 — Paper Outline

Buat outline paper untuk riset Anda menggunakan struktur IMRAD.

| Section | Konten Utama (2-3 kalimat) | Target Kata |
|---------|---------------------------|------------|
| Abstract | Penelitian ini menganalisis pengaruh penggunaan SMOTE terhadap performa Random Forest pada dataset CIC-IDS2017. Evaluasi dilakukan menggunakan Accuracy, Precision, Recall, dan F1-Score melalui lima kali pengujian dengan random seed berbeda. Hasil menunjukkan bahwa SMOTE tidak memberikan peningkatan performa yang signifikan dibandingkan Random Forest tanpa SMOTE. | 200-250 |
| Introduction | Menjelaskan pentingnya Intrusion Detection System (IDS), permasalahan class imbalance, penggunaan SMOTE, Research Question, tujuan penelitian, dan kontribusi penelitian. | 500-700 |
| Related Work | Membahas penelitian terdahulu mengenai Random Forest, SMOTE, IDS, serta dataset CIC-IDS2017 dan menunjukkan research gap penelitian ini. | 700-1000 |
| Method | Menjelaskan dataset, preprocessing, train-test split, Random Forest, SMOTE, multiple run, metrik evaluasi, dan uji statistik yang digunakan. | 800-1200 |
| Results | Menampilkan hasil Accuracy, Precision, Recall, F1-Score, statistik deskriptif, uji normalitas, uji Wilcoxon, effect size, dan confidence interval. | 500-800 |
| Discussion | Menginterpretasikan hasil eksperimen, menjawab Research Question, membandingkan dengan penelitian terdahulu, menjelaskan limitation dan implikasi penelitian. | 600-900 |
| Conclusion | Menyimpulkan bahwa SMOTE tidak memberikan peningkatan performa yang signifikan pada dataset CIC-IDS2017 serta memberikan rekomendasi penelitian selanjutnya. | 200-400 |

---

## Latihan 2 — Consistency Matrix

Buat consistency matrix untuk memverifikasi internal consistency paper Anda.

|                                     | Intro | Method | Result | Discussion | Conclusion |
| ----------------------------------- | ----- | ------ | ------ | ---------- | ---------- |
| **RQ1**                             | ✓     | ✓      | ✓      | ✓          | ✓          |
| **Metrik Accuracy**                 | ✓     | ✓      | ✓      | ✓          | ✓          |
| **Metrik Precision**                | ✓     | ✓      | ✓      | ✓          | ✓          |
| **Metrik Recall**                   | ✓     | ✓      | ✓      | ✓          | ✓          |
| **Metrik F1-Score**                 | ✓     | ✓      | ✓      | ✓          | ✓          |
| **Variabel Independen (SMOTE)**     | ✓     | ✓      | ✓      | ✓          | ✓          |
| **Variabel Dependen (Performa RF)** | ✓     | ✓      | ✓      | ✓          | ✓          |
| **Kontribusi Penelitian**           | ✓     | ✓      | ✓      | ✓          | ✓          |


**Isi setiap sel:** ✓ (ada & konsisten), ✗ (missing), ~ (ada tapi inkonsisten)

**Inkonsistensi yang ditemukan:**
> Tidak ditemukan inkonsistensi antara Research Question, metode, hasil, pembahasan, dan kesimpulan. Seluruh bagian saling mendukung sesuai alur penelitian.

**Tindakan perbaikan:**
> Memastikan seluruh metrik evaluasi yang dijelaskan pada bagian metode juga dilaporkan pada bagian hasil, pembahasan, dan kesimpulan agar konsisten.

---

## Latihan 3 — Writing Quality Check

Ambil satu paragraf dari tulisan Anda (atau tulis paragraf baru) dan evaluasi kualitasnya.

**Paragraf asli:**
> Penelitian ini menggunakan metode Random Forest dan SMOTE pada dataset CIC-IDS2017. Setelah dilakukan pengujian sebanyak lima kali menggunakan random seed yang berbeda, diperoleh hasil bahwa performa Random Forest dengan SMOTE hampir sama dengan Random Forest tanpa S

| Kriteria | Evaluasi | Perbaikan |
|----------|---------|-----------|
| Clarity | Sudah cukup jelas tetapi belum menyebutkan metrik evaluasi. | Tambahkan Accuracy, Precision, Recall, dan F1-Score. |
| Precision | Belum menyebutkan hasil statistik. | Tambahkan p-value dan effect size. |
| Conciseness | Sudah ringkas. | Tidak perlu perubahan besar. |

**Paragraf setelah perbaikan:**
Penelitian ini mengevaluasi pengaruh penggunaan SMOTE terhadap performa algoritma Random Forest pada dataset CIC-IDS2017 menggunakan metrik Accuracy, Precision, Recall, dan F1-Score. Berdasarkan lima kali pengujian dengan random seed yang berbeda, hasil uji Wilcoxon menunjukkan seluruh p-value lebih besar dari 0,05 sehingga tidak terdapat perbedaan performa yang signifikan antara Random Forest dengan dan tanpa SMOTE. Nilai effect size juga menunjukkan bahwa pengaruh penggunaan SMOTE terhadap performa model relatif kecil pada dataset yang digunakan.

## Refleksi

> Apa perbedaan antara menulis "tentang" riset dan menulis sebagai "argumen" riset? Bagaimana urutan penulisan (Method → Discussion → Introduction) mengubah kualitas tulisan?

Menulis tentang riset berarti hanya mendeskripsikan proses dan hasil penelitian, sedangkan menulis sebagai argumen riset berarti menyusun alasan yang didukung oleh bukti ilmiah untuk menjawab Research Question. Pendekatan ini membuat setiap bagian saling terhubung dan memperkuat kontribusi penelitian. Menulis dimulai dari Method, kemudian Results dan Discussion, baru Introduction membantu menjaga konsistensi antara tujuan penelitian dengan hasil yang benar-benar diperoleh.
