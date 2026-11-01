# Current State
Updated: 2026-11-01

## Goal in Progress
Menambahkan penjabaran hitungan manual menjadi minimal 5 sampel data untuk masing-masing soal (Soal 1 Regresi & Soal 2 Klasifikasi) pada `Week_9/JAWABAN_TUGAS_MANDIRI_FUZZY.md` serta memverifikasi kesesuaiannya dengan program Python `Week_9/verifikasi_tugas_fuzzy.py`.

## Done So Far
- Ditambahkan sampel hitungan manual ke-5 pada Soal 1: **Data Nomor 7** ($x=24^\circ\text{C}, h=35\%$, Aktual $y=15$, Prediksi $\hat{y}=15{,}43$, Galat $|e|=0{,}43$, $e^2=0{,}1837$).
- Ditambahkan sampel hitungan manual ke-5 pada Soal 2: **Data Nomor 13** ($r=28\%, s=60$, Aktual Rendah, Prediksi Tinggi / Kasus Konservatif False Positive $FP$).
- Diperbarui skrip verifikasi Python [`Week_9/verifikasi_tugas_fuzzy.py`](file:///d:/Project/Kuliah/2026_Pembelajaran-Mesin_TI-3A/Week_9/verifikasi_tugas_fuzzy.py) dengan modul penjabaran detail per sampel langkah demi langkah (`hitung_detail_soal_1` dan `hitung_detail_soal_2`).
- Skrip dijalankan dan diverifikasi 100% konsisten dengan angka dan notasi matematis di markdown.

## Exactly Where I Stopped
Semua 5 sampel manual untuk Soal 1 dan Soal 2 telah lengkap, diverifikasi, dan terdokumentasi rapi.

## Next Steps (in order)
1. Mahasiswa menyalin 5 sampel perhitungan manual per soal ke lembar folio bergaris beserta tabel rekap 20 baris data dan metrik evaluasi.
2. Selesai.

## Half-Done / Uncommitted Changes
- None.

## Findings So Far
- Data No. 7 Soal 1 memperlihatkan kondisi sejuk namun tanah kering dengan pembilang fraksi eksak $21{,}60 / 1{,}40 = 15{,}43$.
- Data No. 13 Soal 2 memberikan justifikasi pedagogis yang kuat mengenai alasan munculnya satu-satunya *False Positive* akibat ambang batas skor kredit $60$.

## Open Questions / Waiting on the User
- None.

## How to Verify
- Jalankan `python Week_9/verifikasi_tugas_fuzzy.py` untuk melihat cetak detail 5 sampel manual serta tabel 20 baris data lengkap.
