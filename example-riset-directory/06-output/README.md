# 06-output

Folder ini berisi hasil pengolahan data, evaluasi model, visualisasi, serta analisis statistik yang dihasilkan selama penelitian "Analisis Pengaruh Synthetic Minority Over-sampling Technique (SMOTE) terhadap Performa Algoritma Random Forest pada Deteksi Intrusi Menggunakan Dataset CIC-IDS2017".

Seluruh output dihasilkan dari source code pada folder 05-kode, kemudian digunakan sebagai dasar analisis hasil penelitian dan penyusunan pembahasan.

Dataset CIC-IDS2017
        │
        ▼
Preprocessing Data
        │
        ▼
Random Forest
(Random Forest + SMOTE)
        │
        ▼
Multiple Run (5 Random Seed)
        │
        ▼
Evaluasi Model
        │
        ▼
Analisis Statistik
        │
        ▼
Visualisasi Hasil

## tables/
Folder ini berisi hasil evaluasi model dalam bentuk tabel.
| File                           | Isi                                                                              |
| ------------------------------ | -------------------------------------------------------------------------------- |
| **hasil_rf_tanpa_smote.py**   | Hasil evaluasi Random Forest tanpa SMOTE.                                        |
| **hasil_rf_smote.py**         | Hasil evaluasi Random Forest dengan SMOTE.                                       |
| **multiple_run.py**           | Rekapitulasi lima kali eksperimen menggunakan random seed berbeda.               |
|                         |


## figures/

| File                           | Isi                                                                              |
| ------------------------------ | -------------------------------------------------------------------------------- |
| **test_dataset.py**           |                |
| **train_test_split.py**           |                |
| **preprocessing.py**           |                |
| **statistik.py**           |                |
| **rf_tanpa_smote.py**   |                                         |
| **rf_smote.py**         |                                        |
| **multiple_run.py**           |                |
| **multiple_run_tanpa_smote.py**           |                |


Hasil yang Disajikan

Output penelitian meliputi:

-Accuracy.

-Precision.

-Recall.

-F1-Score.

-Confusion Matrix.

-Statistik Deskriptif.

-Shapiro-Wilk Test.

-Wilcoxon Signed-Rank Test.

-Effect Size (Cohen's d).

-Confidence Interval 95%.

Keterkaitan dengan Penelitian

Output pada folder ini digunakan sebagai dasar dalam:

-Analisis performa Random Forest.

-Perbandingan performa sebelum dan sesudah penerapan SMOTE.

-Analisis statistik penelitian.

-Penyusunan pembahasan hasil penelitian.

-Penyusunan kesimpulan penelitian.

