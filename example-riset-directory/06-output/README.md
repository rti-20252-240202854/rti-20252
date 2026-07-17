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
| File                            | Isi                                                                                                                                                                    |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **test_dataset.py**             | Program untuk melakukan pengecekan dataset, struktur data, jumlah atribut, serta distribusi kelas sebelum preprocessing.                                               |
| **train_test_split.py**         | Program untuk membagi dataset menjadi data training dan data testing menggunakan random seed yang telah ditentukan.                                                    |
| **preprocessing.py**            | Program preprocessing yang meliputi pembersihan data, penanganan missing value, encoding label, dan persiapan dataset sebelum pelatihan model.                         |
| **rf_tanpa_smote.py**           | Implementasi Random Forest sebagai model baseline tanpa menggunakan SMOTE.                                                                                             |
| **rf_smote.py**                 | Implementasi Random Forest dengan penerapan Synthetic Minority Over-sampling Technique (SMOTE) pada data training.                                                     |
| **multiple_run.py**             | Program untuk menjalankan eksperimen Random Forest dengan SMOTE sebanyak lima kali menggunakan random seed berbeda.                                                    |
| **multiple_run_tanpa_smote.py** | Program untuk menjalankan eksperimen Random Forest tanpa SMOTE sebanyak lima kali menggunakan random seed berbeda.                                                     |
| **statistik.py**                | Program analisis statistik yang menghasilkan statistik deskriptif, Shapiro-Wilk Test, Wilcoxon Signed-Rank Test, Effect Size (Cohen's d), dan Confidence Interval 95%. |



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

