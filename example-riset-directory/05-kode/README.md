# 05-kode

Folder ini berisi seluruh source code yang digunakan dalam penelitian "Analisis Pengaruh Synthetic Minority Over-sampling Technique (SMOTE) terhadap Performa Algoritma Random Forest pada Deteksi Intrusi Menggunakan Dataset CIC-IDS2017".

Kode program dikembangkan menggunakan bahasa Python dengan memanfaatkan beberapa pustaka seperti Scikit-learn, Imbalanced-learn, Pandas, NumPy, dan SciPy untuk proses preprocessing data, pelatihan model, evaluasi performa, serta analisis statistik.

## Struktur yang direncanakan

```
05-kode/
│
├── src/
│   ├── preprocessing.py
│   ├── random_forest.py
│   ├── random_forest_smote.py
│   ├── multiple_run.py
│   ├── multiple_run_tanpa_smote.py
│   ├── statistik.py
│   └── test_dataset.py
│
├── data/
│   └── CIC_IDS2017/
│
├── requirements.txt
│
└── README.md

Penjelasan file
| File                            | Fungsi                                                                                                                                        |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **preprocessing.py**            | Membersihkan dataset, menangani missing value, encoding label, serta mempersiapkan data sebelum proses pelatihan model.                       |
| **random_forest.py**            | Implementasi algoritma Random Forest tanpa menggunakan SMOTE sebagai model baseline.                                                          |
| **random_forest_smote.py**      | Implementasi Random Forest dengan penerapan SMOTE pada data training.                                                                         |
| **multiple_run.py**             | Melakukan eksperimen sebanyak lima kali menggunakan Random Forest dengan SMOTE menggunakan random seed berbeda.                               |
| **multiple_run_tanpa_smote.py** | Melakukan eksperimen Random Forest tanpa SMOTE menggunakan lima random seed berbeda.                                                          |
| **statistik.py**                | Melakukan analisis statistik meliputi statistik deskriptif, Shapiro-Wilk Test, Wilcoxon Signed-Rank Test, Cohen's d, dan Confidence Interval. |
| **test_dataset.py**             | Digunakan untuk melakukan pengecekan dataset sebelum proses eksperimen.                                                                       |

Library yang Digunakan

Penelitian ini menggunakan beberapa library Python sebagai berikut.

| Library          | Fungsi                                         |
| ---------------- | ---------------------------------------------- |
| Pandas           | Pengolahan dataset                             |
| NumPy            | Operasi numerik                                |
| Scikit-learn     | Implementasi Random Forest dan metrik evaluasi |
| Imbalanced-learn | Implementasi SMOTE                             |
| SciPy            | Analisis statistik (Shapiro-Wilk dan Wilcoxon) |
| Matplotlib       | Visualisasi hasil penelitian                   |
    

Tahapan Implementasi

Source code dikembangkan melalui beberapa tahapan, yaitu:

Persiapan dataset CIC-IDS2017.

Preprocessing data.

Pembagian data training dan testing.

Implementasi Random Forest (Baseline).

Implementasi SMOTE pada data training.

Pelatihan model.

Multiple Run menggunakan lima random seed.

Evaluasi menggunakan Accuracy, Precision, Recall, dan F1-Score.

Analisis statistik menggunakan Shapiro-Wilk Test, Wilcoxon Signed-Rank Test, Cohen's d, dan Confidence Interval.


## Acuan

Implementasi program pada folder ini mengacu pada metodologi penelitian yang telah dijelaskan pada proposal penelitian, meliputi:

Implementasi algoritma Random Forest sebagai model klasifikasi.

Implementasi Synthetic Minority Over-sampling Technique (SMOTE) sebagai teknik penyeimbangan data.

Multiple Run menggunakan lima random seed berbeda.

Evaluasi performa menggunakan Accuracy, Precision, Recall, dan F1-Score.

Analisis statistik menggunakan Shapiro-Wilk Test, Wilcoxon Signed-Rank Test, Effect Size (Cohen's d), dan Confidence Interval 95%.
