# 04-data
Folder ini berisi dokumentasi mengenai dataset, hasil eksperimen, serta data evaluasi yang digunakan dalam penelitian "Analisis Pengaruh Synthetic Minority Over-sampling Technique (SMOTE) terhadap Performa Algoritma Random Forest pada Deteksi Intrusi Menggunakan Dataset CIC-IDS2017".

Karena ukuran dataset CIC-IDS2017 cukup besar (lebih dari batas penyimpanan GitHub), dataset asli tidak disertakan dalam repository ini. Sebagai gantinya, folder ini menyediakan dokumentasi struktur data, hasil pengujian, serta petunjuk untuk memperoleh dataset dari sumber resminya.

## Isi yang diharapkan

Dataset Penelitian

Penelitian ini menggunakan dataset CIC-IDS2017 (Canadian Institute for Cybersecurity Intrusion Detection Evaluation Dataset).

Dataset tersebut dipilih karena merupakan salah satu dataset benchmark yang banyak digunakan pada penelitian Intrusion Detection System (IDS) berbasis Machine Learning.

Pada penelitian ini digunakan subset:

Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv

Subset tersebut berisi lalu lintas jaringan normal dan serangan Distributed Denial of Service (DDoS) yang digunakan sebagai data klasifikasi.

Cara Memperoleh Dataset

Dataset dapat diperoleh melalui situs resmi Canadian Institute for Cybersecurity (CIC).

Sumber Dataset

Canadian Institute for Cybersecurity (CIC)
Dataset: CIC-IDS2017

Setelah diunduh, letakkan dataset pada struktur folder berikut:

data/
└── CIC_IDS2017/
    └── Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv

Selanjutnya sesuaikan path dataset pada file konfigurasi atau source code apabila diperlukan.

Data Hasil Pengujian

| File                     | Deskripsi                                                          |
| ------------------------ | ------------------------------------------------------------------ |
| hasil_rf_tanpa_smote.csv | Hasil evaluasi Random Forest tanpa SMOTE.                          |
| hasil_rf_smote.csv       | Hasil evaluasi Random Forest dengan SMOTE.                         |
| multiple_run.csv         | Rekapitulasi lima kali eksperimen menggunakan random seed berbeda. |
| hasil_statistik.csv      | Hasil analisis statistik penelitian.                               |

Multiple Run

Eksperimen dilakukan sebanyak lima kali menggunakan random seed berbeda untuk meningkatkan reliabilitas hasil penelitian.

Random seed yang digunakan:

42
123
777
999
2025

Setiap eksperimen menghasilkan nilai:

Accuracy
Precision
Recall
F1-Score

Seluruh hasil digunakan sebagai input analisis statistik.

Keterkaitan dengan Penelitian

Data pada folder ini digunakan sebagai dasar dalam:

Pelatihan model Random Forest.

Implementasi SMOTE pada data training.

Evaluasi performa model.

Perbandingan Random Forest sebelum dan sesudah SMOTE.

Analisis statistik menggunakan Shapiro-Wilk Test.

Pengujian hipotesis menggunakan Wilcoxon Signed-Rank Test.

Perhitungan Effect Size (Cohen's d).

Perhitungan Confidence Interval 95%.

Penyusunan pembahasan dan kesimpulan penelitian.

## Catatan

Dataset CIC-IDS2017 tidak disertakan pada repository karena ukuran file yang sangat besar. Pengguna dapat mengunduh dataset dari sumber resmi dan menempatkannya pada direktori yang telah dijelaskan di atas.
