# 04-data

Folder ini berisi dataset penelitian, hasil pengujian model, serta data yang digunakan sebagai input dalam proses analisis statistik pada penelitian "Analisis Pengaruh Synthetic Minority Over-sampling Technique (SMOTE) terhadap Performa Algoritma Random Forest pada Deteksi Intrusi Menggunakan Dataset CIC-IDS2017".

Data yang tersimpan merupakan hasil eksperimen menggunakan dua skenario, yaitu Random Forest tanpa SMOTE (Baseline) dan Random Forest dengan SMOTE, yang kemudian dianalisis menggunakan statistik deskriptif dan statistik inferensial.

## Isi yang diharapkan

Folder ini berisi beberapa data berikut.

Dataset CIC-IDS2017 yang digunakan sebagai objek penelitian.
Hasil preprocessing dataset.
Hasil pengujian Random Forest tanpa SMOTE.
Hasil pengujian Random Forest menggunakan SMOTE.
Hasil multiple run menggunakan lima random seed berbeda.
Data hasil evaluasi Accuracy, Precision, Recall, dan F1-Score.
Data yang digunakan untuk analisis statistik (Shapiro-Wilk, Wilcoxon Signed-Rank Test, Cohen's d, dan Confidence Interval).

## Catatan

Data di folder ini bersifat mentah (raw) dan belum diolah. Hasil olahan (statistik, grafik) disimpan di [../06-output/](../06-output/).
