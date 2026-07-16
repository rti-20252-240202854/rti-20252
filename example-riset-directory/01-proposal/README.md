# 01-proposal

Folder ini berisi dokumen proposal penelitian yang menjadi dasar pelaksanaan penelitian "Analisis Pengaruh Synthetic Minority Over-sampling Technique (SMOTE) terhadap Performa Algoritma Random Forest pada Deteksi Intrusi Menggunakan Dataset CIC-IDS2017". Proposal disusun sebagai acuan dalam menentukan permasalahan penelitian, tujuan, metodologi, serta tahapan pelaksanaan penelitian.

## Isi yang diharapkan
| Keterangan           | Informasi                                                                                                                                                           |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Judul Penelitian** | Analisis Pengaruh Synthetic Minority Over-sampling Technique (SMOTE) terhadap Performa Algoritma Random Forest pada Deteksi Intrusi Menggunakan Dataset CIC-IDS2017 |
| **Peneliti**         | Azzam Zaidan                                                                                                                                                        |
| **NIM**              | 240202854                                                                                                                                                    |
| **Program Studi**    | S1 Teknik Informatika                                                                                                                                               |
| **Universitas**      | Universitas Putra Bangsa                                                                                                                                            |
| **Dosen Pembimbing** | Helmi Bahar Alim, S.Kom., M.Kom.                                                                                                                                    |
| **Status Proposal**  | ✅ Telah direvisi                                                                                                                                                    |

Latar Belakang

Perkembangan teknologi informasi yang semakin pesat menyebabkan meningkatnya ancaman keamanan jaringan komputer, seperti serangan Distributed Denial of Service (DDoS), Brute Force, Port Scan, dan berbagai jenis intrusi lainnya. Intrusion Detection System (IDS) menjadi salah satu solusi yang digunakan untuk mendeteksi aktivitas mencurigakan pada jaringan komputer secara otomatis.
Salah satu algoritma machine learning yang banyak digunakan dalam IDS adalah Random Forest karena memiliki kemampuan klasifikasi yang baik serta tahan terhadap overfitting. Namun demikian, performa Random Forest dapat dipengaruhi oleh kondisi ketidakseimbangan kelas (class imbalance) yang umum terjadi pada dataset keamanan jaringan, termasuk dataset CIC-IDS2017.
Salah satu metode yang banyak digunakan untuk mengatasi permasalahan tersebut adalah Synthetic Minority Over-sampling Technique (SMOTE). Metode ini menghasilkan data sintetis pada kelas minoritas sehingga distribusi data menjadi lebih seimbang. Meskipun demikian, berbagai penelitian menunjukkan bahwa penerapan SMOTE tidak selalu menghasilkan peningkatan performa klasifikasi pada semua jenis dataset.
Berdasarkan kondisi tersebut, penelitian ini bertujuan untuk menganalisis pengaruh penggunaan SMOTE terhadap performa algoritma Random Forest menggunakan dataset CIC-IDS2017 melalui beberapa skenario pengujian, evaluasi statistik, serta analisis signifikansi hasil penelitian.

Rumusan Masalah

Bagaimana implementasi algoritma Random Forest untuk mendeteksi intrusi pada dataset CIC-IDS2017?
Bagaimana pengaruh penerapan SMOTE terhadap performa Random Forest berdasarkan Accuracy, Precision, Recall, dan F1-Score?
Apakah terdapat perbedaan performa yang signifikan antara Random Forest tanpa SMOTE dan Random Forest dengan SMOTE berdasarkan uji statistik?

Tujuan Penelitian

Mengimplementasikan algoritma Random Forest untuk klasifikasi intrusi menggunakan dataset CIC-IDS2017.
Menerapkan metode SMOTE sebagai teknik penyeimbangan data sebelum proses pelatihan model.
Mengevaluasi performa model menggunakan metrik Accuracy, Precision, Recall, dan F1-Score.
Menganalisis signifikansi pengaruh SMOTE menggunakan uji statistik seperti Shapiro-Wilk Test, Wilcoxon Signed-Rank Test, Effect Size (Cohen's d), dan Confidence Interval 95%.

Metodologi Penelitian

Tahapan penelitian terdiri dari:
Studi Literatur
Pengumpulan Dataset CIC-IDS2017
Preprocessing Data
Pembagian Data Training dan Testing
Implementasi Random Forest (Baseline)
Implementasi SMOTE
Pelatihan Model Random Forest dengan SMOTE
Multiple Run menggunakan beberapa Random Seed
Evaluasi Model menggunakan Accuracy, Precision, Recall, dan F1-Score
Analisis Statistik (Shapiro-Wilk, Wilcoxon Signed-Rank Test, Cohen's d, Confidence Interval 95%)
Analisis Hasil Penelitian
Penyusunan Laporan Penelitian

## Berkas

-  — draf proposal (rekonstruksi retrospektif berdasarkan hasil Tahap 1-4)

## Acuan

Ringkasan topik & roadmap penelitian: [../09-docs/rencana-penelitian.md](../09-docs/rencana-penelitian.md)
