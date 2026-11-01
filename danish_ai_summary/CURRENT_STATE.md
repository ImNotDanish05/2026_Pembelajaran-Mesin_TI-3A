# Current State
Updated: 2026-11-01

## Goal in Progress
Memverifikasi kebenaran perhitungan numerik Soal 1 dan Soal 2 pada `Week_9/JAWABAN_TUGAS_MANDIRI_FUZZY.md` menggunakan skrip komputasi Python independen.

## Done So Far
- Dibuat dan dieksekusi skrip independen [`Week_9/verifikasi_tugas_fuzzy.py`](file:///d:/Project/Kuliah/2026_Pembelajaran-Mesin_TI-3A/Week_9/verifikasi_tugas_fuzzy.py).
- Berhasil memverifikasi 100% dari 20 baris data perhitungan Soal 1 (Regresi Sugeno Orde Nol) dan Soal 2 (Klasifikasi Fuzzy Rule-Based).
- Seluruh nilai derajat keanggotaan ($\mu$), firing strength ($\alpha$), defuzzifikasi ($\hat{y}$), galat absolut, galat kuadrat, skor agregasi ($S_{\text{Tinggi}}, S_{\text{Rendah}}$), prediksi kelas, confusion matrix ($TP=12, TN=7, FP=1, FN=0$), serta metrik evaluasi (Akurasi $95\%$, Presisi $92{,}31\%$, Recall $100\%$, F1 $96\%$) terbukti identik presisi antara dokumen markdown dan eksekusi Python.

## Exactly Where I Stopped
Semua pengujian dan verifikasi selesai dan terbukti akurat 100%.

## Next Steps (in order)
1. Mahasiswa dapat menyalin hasil perhitungan dari [`Week_9/JAWABAN_TUGAS_MANDIRI_FUZZY.md`](file:///d:/Project/Kuliah/2026_Pembelajaran-Mesin_TI-3A/Week_9/JAWABAN_TUGAS_MANDIRI_FUZZY.md) ke lembar kerja kertas folio bergaris dengan keyakinan penuh.
2. Skrip [`Week_9/verifikasi_tugas_fuzzy.py`](file:///d:/Project/Kuliah/2026_Pembelajaran-Mesin_TI-3A/Week_9/verifikasi_tugas_fuzzy.py) dapat disertakan sebagai bukti pendukung komputasi jika dosen pengampu meminta kode sumber.

## Half-Done / Uncommitted Changes
- None.

## Findings So Far
- Perhitungan manual di lembar jawaban sudah teruji bebas dari *rounding error* yang merusak metrik agregat.
- Skrip Python menghasilkan nilai metrik identik hingga digit desimal keempat.

## Open Questions / Waiting on the User
- None.

## How to Verify
- Jalankan `python Week_9/verifikasi_tugas_fuzzy.py` untuk melihat output tabel komputasi dan metrik secara langsung di terminal.
