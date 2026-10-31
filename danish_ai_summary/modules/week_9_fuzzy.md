# Week 9: Logika Fuzzy (Fuzzy Logic)

- **Purpose:** Konsep dasar logika fuzzy, himpunan fuzzy, fungsi keanggotaan (linear naik/turun, segitiga), Fuzzy Inference System (Mamdani, Sugeno, Tsukamoto), latihan terbimbing regresi & klasifikasi, serta tugas mandiri mahasiswa.
- **Key Files:**
  - `Week_9/MODUL-07-LOGIKA FUZZY.pdf` — Original lecture module (41 pages).
  - `Week_9/MODUL_07_LOGIKA_FUZZY.md` — Transcribed and comprehensive pure markdown module.
  - `Week_9/JAWABAN_TUGAS_MANDIRI_FUZZY.md` — Complete, folio-ready assignment solutions for Soal 1 (Regresi N=20) and Soal 2 (Klasifikasi N=20).
  - `Week_9/ilustrasi_segitiga_fuzzy.png` — Diagram kurva fungsi keanggotaan segitiga.
  - `Week_9/alur_sistem_fuzzy_fis.png` — Flowchart grafis arsitektur 5 tahap Fuzzy Inference System (FIS).
  - `Week_9/fuzzy_vs_machine_learning.png` — Diagram taksonomi perbandingan Logika Fuzzy vs Machine Learning vs ANFIS.
- **Key Methods & Concepts:**
  - **Sugeno Orde Nol Regresi:** Luaran berupa konstanta numerik, defuzzifikasi rata-rata terbobot:
    $$z = \frac{\sum \alpha_i z_i}{\sum \alpha_i}$$
  - **Fuzzy Rule-Based Classification:** Operator AND via minimum, agregasi skor kelas via maximum, tie-breaking konservatif (pilih kelas risiko tinggi).
  - **Evaluasi:**
    - Regresi ($N=15$): MAE ($\sim 1{,}80$), RMSE ($\sim 2{,}13$).
    - Klasifikasi ($N=15$): Accuracy (100%), Precision (100%), Recall (100%), F1 (100%).
- **Tugas Mandiri Mahasiswa:**
  - Soal 1 (Regresi): Prediksi Lama Penyiraman Tanaman ($N=20$, Suhu Udara vs Kelembapan Tanah vs Menit).
  - Soal 2 (Klasifikasi): Klasifikasi Risiko Kredit Nasabah ($N=20$, Rasio Cicilan vs Skor Kredit vs Risiko Rendah/Tinggi).
- **Last touched:** 2026-10-31

