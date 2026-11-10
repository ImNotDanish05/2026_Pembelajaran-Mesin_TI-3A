# Current State
Updated: 2026-11-10

## Goal in Progress
Selesai: Penambahan file dokumentasi atribusi dan kredit data `Week_11/README.md` untuk file `Week_11/emisiCO2.xlsx` sesuai peringatan atribusi SIPONGI KEMENHUT.

## Done So Far
- Membuat file `Week_11/README.md` yang memuat atribusi resmi untuk dataset `emisiCO2.xlsx`:
  - Peringatan wajib cantumkan sumber: SIPONGI KEMENHUT.
  - Tautan sumber: `https://sipongi.gakkum.kehutanan.go.id/emisi-co2`.
- Memperbarui peta struktur pada `DANISH_AI_SUMMARY.md` untuk mencatat folder `Week_11/`.

## Exactly Where I Stopped
Dokumentasi kredit `Week_11/README.md` selesai dibuat. Belum ada tugas analisis/kode lanjutan di Week 11.

## Next Steps (in order)
1. Menunggu instruksi atau materi tugas berikutnya untuk `Week_11`.

## Half-Done / Uncommitted Changes
- `Week_11/README.md` baru dibuat.
- `DANISH_AI_SUMMARY.md` diperbarui.

## Findings So Far
- `Week_11/emisiCO2.xlsx`: 1 sheet `data`, kolom `Provinsi` | `2023`. 39 provinsi (termasuk `IKN`) + baris `Total` (182.714.438) di A41 — WAJIB dibuang sebelum clustering.
- Nilai tersimpan sebagai TEKS format Indonesia (`44.938.470,00`) → hapus `.` lalu ganti `,` jadi `.` sebelum float.
- Hanya 1 fitur numerik, sangat skewed (0 s/d 44,9 juta; DKI & IKN = 0, Banten = 228). Top: Sumsel, Kalteng, Kalbar, Kalsel.
- Env Linux: `python3` sistem TIDAK punya pandas/openpyxl (dibaca via zipfile+XML). `.python_packages/` hanya berisi python-docx & lxml.

## Open Questions / Waiting on the User
- Tugas dosen (2026-11-10): training data ini dengan clustering, untuk artikel.
- KETENTUAN DOSEN (user, 2026-11-10): HANYA BOLEH data tahun 2023. Opsi B (multi-tahun) GUGUR. Tidak ada template jurnal / algoritma wajib / batas halaman.
- Output dipilih user: notebook `.ipynb` + naskah artikel `.docx` (seperti Week 10). TAPI user bilang "jangan kerja dulu" → JANGAN buat file/kode sampai user menyuruh.
- Sedang dibahas: variabel tambahan 2023. Diusulkan: luas karhutla (ha) & jumlah hotspot (SIPONGI), luas wilayah (BPS), turunan emisi/ha & % terbakar. User yang mengunduh datanya sendiri. Angka luas karhutla dari web search TIDAK diverifikasi — jangan dipakai, ambil dari SIPONGI langsung.
- Gotcha: `IKN` bukan provinsi di BPS → bisa tidak cocok saat join data luar SIPONGI.
- User menambah `Week_11/luas-karhutla-provinsi.xlsx` (SIPONGI): kolom `Kode Wilayah` | `Provinsi` | `2023` (ha, teks format Indonesia). 38 provinsi, TANPA IKN (emisiCO2 punya IKN=0 → buang IKN saat join). Baris 40 = `Total` (1.161.192,90) → buang. Nama provinsi di kedua file identik (dicek visual).
- Kredit kedua file sudah di `Week_11/README.md`. URL halaman luas karhutla belum pasti (ditulis URL utama SIPONGI) → minta user kirim URL tepatnya.

## How to Verify
- Periksa keberadaan dan isi file [Week_11/README.md](file:///media/data1/project/kuliah/2026_Pembelajaran-Mesin_TI-3A/Week_11/README.md).
