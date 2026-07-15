# Jadwal & Log Pelaksanaan Penelitian

Catatan kronologis pelaksanaan tiap tahap (sumber: riwayat commit git & dokumen `09-docs/tahap-N-*.md`). Tanggal mengikuti `git log`.

## Log Pelaksanaan

| Tanggal | Tahap | Aktivitas | Referensi |
|---|---|---|---|
| 2026-07-05 | Tahap 1 | Studi literatur mengenai Intrusion Detection System (IDS), Random Forest, SMOTE, serta dataset CIC-IDS2017. Menentukan topik penelitian dan Research Question. | [09-docs/tahap-1-arsitektur-dan-skema-database.md](../09-docs/tahap-1-arsitektur-dan-skema-database.md), [09-docs/tahap-2-implementasi-gateway.md](../09-docs/tahap-2-implementasi-gateway.md) |
| 2026-07-06 | Tahap 2 | Menentukan metode penelitian, variabel penelitian, dataset, algoritma Random Forest, teknik SMOTE, serta metrik evaluasi Accuracy, Precision, Recall, dan F1-Score. | [09-docs/tahap-3-pengujian-k6.md](../09-docs/tahap-3-pengujian-k6.md) |
| 2026-07-12 | Tahap 3 | Implementasi program menggunakan Python (preprocessing, multiple run Random Forest, Random Forest + SMOTE), serta pengujian sebanyak 5 kali menggunakan random seed berbeda. | commit "Mark Tahap 3 complete after running full 50-run k6 matrix" (2026-06-13 02:00) |
| 2026-07-12 | Tahap 4 | Analisis hasil eksperimen menggunakan statistik deskriptif, uji normalitas Shapiro-Wilk, Wilcoxon Signed-Rank Test, Effect Size (Cohen's d), dan Confidence Interval (95%). | [09-docs/tahap-4-analisis-data.md](../09-docs/tahap-4-analisis-data.md), [06-output/](../06-output/) |
| 2026-06-13 | Tahap 5 | Interpretasi hasil penelitian, penyusunan laporan, pengisian worksheet WS-10 sampai WS-16, serta penyusunan kesimpulan dan persiapan presentasi penelitian. | [09-docs/tahap-5-draf-paper.md](../09-docs/tahap-5-draf-paper.md), [08-laporan/laporan-penelitian.md](../08-laporan/laporan-penelitian.md) |


## Status Ringkas

- **Tahap 1–4**: Selesai (dataset final: matrix 400 run / 40 replikasi per kombinasi, 2026-06-15).
- **Tahap 5**: Konten naskah selesai dengan statistik n=40 (termasuk tinjauan pustaka & verifikasi CVE-2026-48524); menyisakan keputusan bahasa final dan pemindahan ke template jurnal tujuan (dilakukan oleh peneliti).

## Item Tindak Lanjut (Checklist Sebelum Submission)

- [x] Lengkapi matriks literatur dengan paper *related work* nyata ([02-literatur/matriks-literatur.md](../02-literatur/matriks-literatur.md)) — 18 referensi terverifikasi
- [x] Verifikasi CVE-2026-48524 terhadap basis data NVD/MITRE — terkonfirmasi via GHSA-fhv5-28vv-h8m8 (PyJWT, CVSS 3.7)
- [ ] Tetapkan bahasa final naskah (Indonesia/Inggris) sesuai jurnal tujuan
- [ ] Pindahkan konten [07-manuskrip/naskah-jurnal.md](../07-manuskrip/naskah-jurnal.md)/`.docx` ke template jurnal tujuan
- [ ] Finalisasi penempatan figure/tabel sesuai gaya jurnal
- [ ] Review akhir seluruh klaim numerik agar konsisten antar dokumen (lihat daftar pada [07-manuskrip/00-outline.md](../07-manuskrip/00-outline.md))

## Korespondensi

*(belum ada — tambahkan catatan korespondensi dengan pembimbing/editor jurnal di sini saat tersedia)*
