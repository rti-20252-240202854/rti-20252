# WS-02: Problem Statement

> **Bab 2 — Problem Formulation & System Context**

---

## Ringkasan Materi

### Problem Formation Model

Masalah riset melewati 5 tahap transformasi. Melompat langsung dari Reality ke Variable adalah kesalahan paling umum.

```
Reality → Observed Issue (Symptom) → Diagnosed Problem (Root Cause)
→ Researchable Problem (Scoped) → Measurable Variable (Operationalized)
```

### Topic ≠ Problem ≠ Research Problem

| Level | Contoh | Status |
|-------|--------|--------|
| **Topik** | Keamanan IoT | Terlalu luas, tidak bisa diuji |
| **Problem** | MQTT tidak terenkripsi | Spesifik tapi belum riset |
| **Research Problem** | Belum ada studi membandingkan overhead TLS 1.3 vs DTLS pada MQTT di IoT RAM < 64KB | Bisa dirancang eksperimennya |

### Symptom vs Root Cause

Apa yang diamati (gejala) ≠ mengapa terjadi (akar masalah). Gunakan **5 Whys** atau **Fishbone Diagram** untuk menggali.

Contoh: "User meninggalkan checkout" (symptom) → "Waktu loading > 8 detik karena API call sequential" (root cause).

### System Thinking

Setiap masalah riset TI harus terikat pada komponen sistem: **Input → Process → Output → Outcome → Constraints → Stakeholders**.

### Problem Quality Check

Masalah riset yang layak harus memenuhi 5 kriteria:
- **Clarity** — Satu orang membaca akan paham
- **Measurability** — Ada metrik kuantitatif
- **Relevance** — Penting untuk domain
- **Testability** — Bisa gagal (falsifiable)
- **Impact** — Ada kontribusi jika terjawab

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Menyelesaikan masalah (*solve*) | Memahami dan membuktikan (*understand & prove*) |
| Masalah | Bug, error, fitur belum ada | Gap dalam pengetahuan |
| Scope | Selesaikan semua yang perlu | Batasi agar bisa dibuktikan |
| Output | Working system | Evidence, paper, replicable findings |

### Istilah Penting

- **Problem Statement** — Formulasi tertulis: konteks sistem + gap + dampak + justifikasi
- **System Context** — Deskripsi lengkap: input, proses, output, outcome, constraints, stakeholders
- **Problem Drift** — Masalah "bermutasi" dari pendahuluan ke metodologi karena statement awal tidak presisi
- **Solution-First Thinking** — Memulai dari solusi tanpa masalah yang jelas — berbahaya dalam riset
- **Operational Definition** — Definisi variabel yang cukup jelas agar peneliti lain bisa mengukur hal yang sama

---

## Template A.2 — Problem Statement Builder

```
PROBLEM STATEMENT BUILDER

Domain & Konteks
  Domain   : Keamanan jaringan / machine learning
  Konteks  : Deteksi anomali trafik jaringan menggunakan SMOTE dan Random Forest

System Context
  Input       : Dataset CIC-IDS2017 yang berisi trafik normal dan berbagai jenis serangan jaringan.
  Process     : Preprocessing data - SMOTE - training model Random Forest
  Output      : Hasil prediksi + nilai akurasi, precision, recall, F1-score
  Outcome     : Mengetahui pengaruh penggunaan SMOTE terhadap performa Random Forest pada deteksi anomali jaringan.
  Constraints : Dataset CIC-IDS2017 merupakan benchmark dataset sehingga belum tentu merepresentasikan seluruh kondisi jaringan nyata.
  Stakeholders: Peneliti, praktisi keamanan jaringan

Fenomena → Problem
  Fenomena yang diamati             : Penggunaan SMOTE meningkatkan performa model deteksi anomali
  Gejala (symptom) yang terukur     : Nilai akurasi, precision, recall, dan F1-score meningkat setelah SMOTE
  Masalah yang didiagnosis          : SMOTE menghasilkan data sintetis yang mengubah distribusi data asli
  Masalah riset (researchable)      : Belum diketahui apakah peningkatan performa Random Forest setelah penggunaan SMOTE benar-benar menunjukkan peningkatan kemampuan model atau dipengaruhi oleh perubahan distribusi data akibat oversampling.   
  Variabel yang terukur             : Akurasi,Precision, Recall,F1-score,Perbandingan performa (dengan vs tanpa SMOTE)

Problem Quality Check
  [v] Clarity — Apakah satu orang membaca akan paham?
  [v] Measurability — Apakah ada metrik kuantitatif?
  [v] Relevance — Apakah penting untuk domain?
  [v] Testability — Apakah bisa gagal?
  [v] Impact — Apakah ada kontribusi jika terjawab?

Problem Statement (1 paragraf):
Penggunaan SMOTE dalam deteksi anomali jaringan sering dilaporkan dapat meningkatkan performa model, yang ditunjukkan melalui kenaikan nilai accuracy, precision, recall, dan F1-score. Namun, SMOTE menghasilkan data sintetis yang dapat mengubah distribusi data asli sehingga peningkatan performa tersebut belum tentu mencerminkan kondisi jaringan yang sebenarnya. Oleh karena itu, penelitian ini bertujuan untuk menganalisis pengaruh penggunaan SMOTE terhadap performa Random Forest pada dataset CIC-IDS2017 dengan membandingkan kondisi tanpa SMOTE dan dengan SMOTE menggunakan metrik evaluasi yang sama.


## Latihan 1 — Deteksi anomali jaringan dengan SMOTE

Pilih satu topik di bidang TI yang diminati. Transformasikan melalui 5 tahap Problem Formation Model.

**Topik awal:** ________________________________________

| Tahap | Hasil |
|-------|-------|
| Reality | Model digunakan untuk deteksi anomali jaringan |
| Observed Issue (Symptom) | Performa meningkat setelah SMOTE |
| Diagnosed Problem (Root Cause) | Data berubah karena SMOTE |
| Researchable Problem | Belum jelas apakah performa meningkat itu valid |
| Measurable Variable | Akurasi, precision, recall, F1-score |

**Apakah terjebak solution-first thinking?** [ ] Ya / [v] Tidak
> Jika ya, kembali ke tahap mana? ________________________

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | Dataset CIC-IDS2017 |
| Process | SMOTE + training model |
| Output | Hasil prediksi & metrik |
| Outcome | Mengetahui pengaruh penggunaan SMOTE terhadap performa Random Forest. |
| Constraints | Dataset yang digunakan belum tentu merepresentasikan seluruh kondisi jaringan di dunia nyata. |
| Stakeholders | Peneliti & praktisi |

**Komponen mana yang paling relevan dengan masalah riset?** Process,karena masalah ada di SMOTE

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | 5 | jelas fokus ke SMOTE |
| Measurability | 5 | pakai matriks jelas |
| Relevance | 5 | penting di ML |
| Testability | 5 | bisa dibandingkan |
| Impact | 4 | berguna untuk validasi metode |

**Skor total:** 24 / 25

**Problem statement versi final (1 paragraf):**
SMOTE sering dilaporkan dapat meningkatkan performa model deteksi anomali jaringan. Namun, karena menghasilkan data sintetis, peningkatan tersebut belum tentu mencerminkan kondisi jaringan yang sebenarnya. Oleh karena itu, penelitian ini dilakukan untuk menganalisis pengaruh penggunaan SMOTE terhadap performa Random Forest pada dataset CIC-IDS2017.
---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> Masalah saat coding biasanya jelas dan langsung kelihatan, misalnya error, bug, atau fitur yang nggak jalan. Cara ngatasinnya juga langsung: cari penyebabnya di kode terus diperbaiki sampai sistem jalan normal.

> Sedangkan masalah riset itu nggak selalu kelihatan jelas. Kita harus nyari dulu akar masalahnya, bahkan kadang harus mempertanyakan apakah masalahnya memang benar ada atau cuma asumsi. Di riset juga nggak langsung nyari solusi, tapi lebih ke memahami masalah dan membuktikan dengan data apakah suatu klaim itu benar atau nggak.
