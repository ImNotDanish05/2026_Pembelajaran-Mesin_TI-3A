# Current State
Updated: 2026-11-03

## Goal in Progress
Selesai: Menyusun naskah artikel ilmiah berstandar SINTA 3 lengkap (2 kolom format IEEE) berdasarkan eksperimen pada `Week_10/Penilitian_Klasifikasi.ipynb`.

## Done So Far
- Memeriksa dan menganalisis seluruh alur kode serta hasil numerik `Week_10/Penilitian_Klasifikasi.ipynb` (4 model KNN/DT/NB/SVM, seleksi fitur Pearson 51 -> 43, validasi hold-out 80:20 dan Stratified 5-Fold Cross Validation).
- Melakukan verifikasi live via skrip Python terhadap 22 tautan/DOI referensi ilmiah (seluruhnya 100% menghasilkan status `HTTP 200 OK`).
- Mengekstrak 3 aset visual dari draft naskah sebelumnya (`assets/image1.png` Heatmap, `assets/image2.png` Confusion Matrix, `assets/image3.png` ROC Curve).
- Menyusun naskah artikel ilmiah utuh standar SINTA 3:
  - Judul bilingual (Indonesia & Inggris).
  - Metadata penulis: Danish Mahdi (adi.43324009@mhs.polines.ac.id) & Setyawan Wibisono, S.Kom., M.Cs. (setyasonny@gmail.com), Jurusan Teknik Elektro, Politeknik Negeri Semarang.
  - Abstrak & Kata Kunci bilingual (ID & EN).
  - 1. PENDAHULUAN (latar belakang, urgensi imbalanced data & telemarketing, peranan Pearson correlation, rumusan masalah).
  - 2. TINJAUAN PUSTAKA (kajian empiris Bank Marketing, filter feature selection, algoritma KNN/DT/NB/SVM, evaluasi multi-metrik).
  - 3. METODOLOGI PENELITIAN (dataset 45.211 instance, One-Hot Encoding, StandardScaler, formula korelasi Pearson, konfigurasi model, hold-out 80:20 & 5-fold CV).
  - 4. HASIL DAN PEMBAHASAN (analisis karakteristik data, reduksi 15,69% fitur, evaluasi sebelum & sesudah FS, kurva ROC, confusion matrix, heatmap korelasi, tabel 5-fold CV, dan implikasi manajerial perbankan).
  - 5. KESIMPULAN (sintesis temuan, rekomendasi bisnis, limitasi durasi & korelasi linear, saran riset lanjutan).
  - DAFTAR PUSTAKA (22 referensi IEEE terverifikasi).
- Mengompilasi naskah ke berkas Word `.docx` 2 kolom rapi di `Week_10/jurnal/Klasifikasi.docx` (serta `Klasifikasi_SINTA3_Final.docx`) dengan cadangan draft awal di `Klasifikasi_original_draft.docx`.
- Menyediakan salinan teks artikel dalam format Markdown di `Week_10/jurnal/NASKAH_JURNAL_SINTA3.md`.

## Exactly Where I Stopped
Seluruh penyusunan naskah artikel ilmiah SINTA 3 telah selesai, diverifikasi strukturnya, dan siap digunakan pengguna untuk submisi / laporan.

## Next Steps (in order)
1. Mahasiswa / Dosen me-review naskah `.docx` atau `.md`.
2. Selesai.

## Half-Done / Uncommitted Changes
- None.

## Findings So Far
- Naskah memenuhi standar IMRAD formal 2 kolom dengan 4 tabel (APA/IEEE 3-line style) dan 3 visualisasi grafik.
- Seluruh 22 referensi memiliki tautan/DOI aktif terverifikasi `HTTP 200`.

## Open Questions / Waiting on the User
- None.

## How to Verify
- Buka dan periksa dokumen `Week_10/jurnal/Klasifikasi.docx` menggunakan Microsoft Word atau LibreOffice.
- Periksa konsistensi teks pada `Week_10/jurnal/NASKAH_JURNAL_SINTA3.md`.
