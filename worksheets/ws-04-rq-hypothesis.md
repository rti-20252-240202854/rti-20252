# WS-04: Research Question & Hypothesis

> **Bab 4 — Research Question, Contribution & Hypothesis**

---

## Ringkasan Materi

### RQ Bukan Pertanyaan Biasa

Research Question yang baik secara implisit mengandung cetak biru eksperimen: subjek, baseline, metrik, domain, dataset.

| Kualitas | Contoh |
|----------|--------|
| **Buruk** | "Bagaimana pengaruh deep learning terhadap deteksi malware?" |
| **Baik** | "Apakah CNN menghasilkan F1-Score lebih tinggi dari RF pada CIC-MalMem-2022?" |

Perbedaan: RQ yang baik menyebutkan **metode spesifik**, **metrik terukur**, **baseline**, dan **dataset**.

### Tiga Jenis RQ

| Jenis | Pola | Kebutuhan |
|-------|------|-----------|
| **Comparison** | A vs B → mana lebih baik? | ≥ 2 metode, metrik sama |
| **Improvement** | A' vs A → modifikasi lebih baik? | Pre/post, bukti perbaikan |
| **Exploratory** | Faktor X₁...Xₙ → pengaruh terhadap Y? | Multi-variabel, korelasi/regresi |

### Contribution Statement

Tiga jenis kontribusi: **Improvement** (metode terbukti lebih baik), **Comparison** (perbandingan sistematis yang belum ada), **Novel Approach** (pendekatan baru). Kontribusi harus terhubung langsung dengan gap — kontribusi tanpa gap = klaim tanpa justifikasi.

### Hypothesis H₀ / H₁

- **H₀** (Null) = Tidak ada perbedaan signifikan — asumsi default, harus dibuktikan salah
- **H₁** (Alternative) = Ada perbedaan signifikan — diterima hanya jika H₀ ditolak
- Harus **falsifiable**, mengandung **metrik terukur**, dirumuskan **SEBELUM eksperimen**

### Rantai Operasionalisasi

```
RQ → Variable → Metric → Data → Analysis
```

Jika rantai ini tidak lengkap, RQ belum mature. Bi-directional: RQ yang tidak bisa jadi hipotesis testable harus direvisi mundur.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan pertanyaan | Apa yang harus dibangun? | Apa yang harus dibuktikan? |
| Bentuk jawaban | Sistem yang berfungsi | Bukti empiris terukur |
| Sukses diukur oleh | User satisfaction, uptime | Signifikansi statistik, effect size |
| Jika gagal | Debug dan perbaiki | Laporkan, analisis mengapa |

### Istilah Penting

- **Research Question (RQ)** — Pertanyaan spesifik: variabel terukur + metrik + konteks
- **Contribution Statement** — Apa yang diketahui setelah riset selesai yang sebelumnya belum ada
- **H₀ / H₁** — Null vs Alternative Hypothesis
- **Falsifiability** — Kondisi hipotesis ditolak harus bisa didefinisikan sebelum eksperimen
- **Operationalization** — Proses mewujudkan konsep abstrak menjadi variabel terukur

---

## Template A.4 — RQ-Contribution-Hypothesis

```
RQ-CONTRIBUTION-HYPOTHESIS

Gap Statement  :Banyak penelitian menggunakan SMOTE untuk meningkatkan performa deteksi anomali jaringan, tetapi penggunaan data sintetis berpotensi menyebabkan distorsi sehingga hasil model belum tentu mencerminkan kondisi nyata.

Research Question:
  Tipe         : [ ] Comparison  [v] Improvement  [ ] Exploratory
  Formulasi    : Bagaimana pengaruh penggunaan SMOTE terhadap performa Random Forest pada dataset CIC-IDS2017 dibandingkan Random Forest tanpa SMOTE berdasarkan accuracy, precision, recall, dan F1-score?
  Variabel IV  : Penggunaan SMOTE
  Variabel DV  : Performa model Random Forest
  Metrik       : Akurasi, precision, recall, dan F1-score
  Dataset      : CIC-IDS2017
  Baseline     : Random Forest tanpa SMOTE

Quality Check RQ:
  [v] Variabel spesifik
  [v] Metrik jelas
  [v] Baseline ada
  [v] Konteks disebutkan
  [v] Memerlukan eksperimen (bukan hanya survei literatur)

Contribution Statement:
  Apa yang baru diketahui : Mengetahui pengaruh penggunaan SMOTE terhadap performa Random Forest pada dataset CIC-IDS2017 serta mengevaluasi apakah peningkatan performa dipengaruhi oleh perubahan distribusi data akibat oversampling..
  Jenis kontribusi        : [v] Improvement  [ ] Comparison  [ ] Novel approach
  Gap yang diisi          : Data Gap dan Performance gap pada penggunaan SMOTE dalam deteksi anomali jaringan.

Hypothesis Pair:
  H₀ : Penggunaan SMOTE tidak memberikan peningkatan signifikan terhadap performa Random Forest pada dataset CIC-IDS2017.
  H₁ : Penggunaan SMOTE memberikan peningkatan signifikan terhadap performa Random Forest pada dataset CIC-IDS2017.
  Threshold              : Tidak ditentukan secara spesifik, peningkatan performa dinilai berdasarkan perbedaan nilai accuracy, precision, recall, dan F1-score antara model tanpa SMOTE dan dengan SMOTE.
  Justifikasi threshold  : karena F1-score dianggap cukup mewakili keseimbangan precision dan recall dalam deteksi anomali.
```

---

## Latihan 1 — Dari Gap ke RQ

Gunakan gap yang ditemukan di WS-03. Transformasikan menjadi Research Question.

**Gap dari WS-03:** penggunaan SMOTE menghasilkan data sintetis yang dapat mempengaruhi validitas performa model

**RQ versi pertama (tulis bebas):**
> apakah SMOTE membuat performa model Random Forest menjadi lebih baik?

**Evaluasi RQ:**

| Komponen | Ada? | Isi |
|----------|------|-----|
| Metode spesifik | ya | random forest + SMOTE |
| Metrik terukur | ya | akurasi,presisi,recall,f1-score |
| Baseline | ya | random forest tanpa SMOTE |
| Dataset/konteks | ya | dataset CIC-IDS2017. |

**Tipe RQ:** [ ] Comparison / [v] Improvement / [ ] Exploratory

**RQ versi revisi (setelah evaluasi):**
> Apakah penggunaan SMOTE dapat meningkatkan performa Random Forest pada deteksi anomali jaringan dibandingkan Random Forest tanpa SMOTE berdasarkan akurasi, presisi, recall, dan f1-score?

---

## Latihan 2 — Hypothesis Pair

Rumuskan pasangan hipotesis dari RQ di Latihan 1.

| Komponen | Isi |
|----------|-----|
| H₀ | tidak ada peningkatan signifikan performa Random Forest setelah menggunakan SMOTE |
| H₁ | ada peningkatan signifikan performa random fores setelah menggunakan SMOTE |
| Metrik | akurasi,presisi,recal,f1 score |
| Threshold | 5% peningkatan f1 score |
| Justifikasi threshold | karena F1-score cukup penting untuk evaluasi deteksi anomali |

**Apakah hipotesis ini falsifiable?** [v] Ya / [ ] Tidak
> Bagaimana cara membuktikannya salah? 
engan membandingkan hasil random forest dengan dan tanpa SMOTE. Jika peningkatan performanya tidak signifikan, maka H₁ ditolak.

---

## Latihan 3 — Rantai Operasionalisasi

Lengkapi rantai dari RQ hingga metode analisis.

| Tahap | Isi |
|-------|-----|
| RQ | apakah SMOTE meningkatkan performa Random Forest pada deteksi anomali jaringan |
| Variable (IV) | penggunaan SMOTE |
| Variable (DV) | performa random forest |
| Metric | akurasi,presisi,recal,f1 score |
| Data source | dataset CIC-IDS2017. |
| Analysis method | membandingkan nilai accuracy, precision, recall, dan F1-score antara Random Forest tanpa SMOTE dan Random Forest dengan SMOTE. |

**Apakah rantai lengkap?** [v] Ya / [ ] Tidak
> Jika tidak, tahap mana yang perlu direvisi? ______________

---

## Refleksi

> Ambil satu judul skripsi/paper yang pernah dibaca. Coba ekstrak RQ-nya. Apakah RQ tersebut memenuhi semua komponen (metode, metrik, baseline, konteks)? Jika tidak, apa yang hilang?

**Judul:** Penerapan Teknik SMOTE untuk Mendeteksi Perilaku Jaringan Berbasis Trafik Enkripsi
**RQ yang diekstrak:** apakah penggunaan SMOTE dapat meningkatkan performa model deteksi anomali jaringan
**Komponen yang hilang:** metrik, baseline, dan dataset belum disebutkan secara jelas di dalam RQ
