# Changelog

### 2026-10-31 — Solved Week 9 Fuzzy Logic Independent Assignments in Markdown (Folio-Ready)
- What: Created dedicated assignment solution document `Week_9/JAWABAN_TUGAS_MANDIRI_FUZZY.md` (481 lines) structured specifically for handwriting onto folio paper.
- What: Fully calculated and formatted Soal 1 (Regresi Sugeno Orde Nol, N=20) with step-by-step sample calculations, 20-row table with all μ and α, MAE=1.59, and RMSE=1.91.
- What: Fully calculated and formatted Soal 2 (Klasifikasi Berbasis Aturan, N=20) with step-by-step sample calculations, conservative tie-breaking, 20-row table, Confusion Matrix (TP=12, TN=7, FP=1, FN=0), Accuracy=95.0%, and Recall=100.0%.
- Files: Week_9/JAWABAN_TUGAS_MANDIRI_FUZZY.md, danish_ai_summary/modules/week_9_fuzzy.md.
- Verified: Automated Python table validator confirmed 100% column syntax; Python script verified mathematical calculations across all 40 instances.

### 2026-10-31 — Generated Visual Flowchart Images & Fixed Regression Table Formatting
- What: Replaced ASCII flowcharts with high-resolution visual diagrams: `alur_sistem_fuzzy_fis.png` (Section 7: FIS 5-stage architecture) and `fuzzy_vs_machine_learning.png` (Section 10: AI taxonomy & ANFIS).
- What: Fixed corrupted markdown table in Section 6 (Tabel Prediksi Lengkap Seluruh Dataset Regresi) caused by raw unescaped vertical pipes `|y - ŷ|` in column header; corrected syntax using `\lvert y - \hat{y} \rvert`.
- What: Added companion Table 1.2 showing detailed fuzzification values (μ_D, μ_P, μ_KR, μ_KT) and firing strengths (α1, α2, α3, α4) for all 15 instances.
- Files: Week_9/MODUL_07_LOGIKA_FUZZY.md, Week_9/alur_sistem_fuzzy_fis.png, Week_9/fuzzy_vs_machine_learning.png, danish_ai_summary/modules/week_9_fuzzy.md.
- Verified: Automated Python table validator confirmed 100% column consistency across all tables; images verified visually via `read_file`.

### 2026-10-31 — Migrated to Danish AI Summary & Converted Week 9 Fuzzy Logic Module
- What: Migrated legacy single-file DANISH_AI_AGENT.md into DANISH_AI_SUMMARY.md + danish_ai_summary/ directory structure without losing any facts, conventions, or rules.
- What: Extracted and transcribed 41-page Week 9 PDF (`MODUL-07-LOGIKA FUZZY.pdf`) into complete, academic-grade Markdown (`Week_9/MODUL_07_LOGIKA_FUZZY.md`).
- What: Extracted and embedded vector/raster graphic `Week_9/ilustrasi_segitiga_fuzzy.png` for triangular membership functions.
- Why: User requested `/danish-ai-summary` migration followed by conversion of Week 9 Fuzzy Logic module to Markdown.
- Files: DANISH_AI_SUMMARY.md, danish_ai_summary/*, Week_9/MODUL_07_LOGIKA_FUZZY.md, Week_9/ilustrasi_segitiga_fuzzy.png.
- Verified: `pdftotext` extracted 41 pages; verified regression formulas and classification confusion matrix; verified file sizes and table layouts.
- Follow-ups: Ready for students/users to implement practical Python scripts or solutions for Tugas Mandiri Soal 1 and Soal 2.

### 2026-10-17 — Week 7 KNN Visualizations and Assignments
- What: Regenerated visualisasi_tugas1_km.png and visualisasi_tugas2_rm.png with full labels for all 24 points (A-X) and golden badge highlights for Top-7 neighbors.
- What: Embedded direct images into JAWABAN_TUGAS_MANDIRI_KNN.md with 2-table formats (A-X raw with Rank and sorted Rank 1-24).
- What: Computed and documented complete 6-stage solutions for Week 7 KNN assignments (KM & RM, N=24) with Python scikit-learn verification in JAWABAN_TUGAS_MANDIRI_KNN.md.
- What: Transcribed and rewritten Week 7 KNN module into pure-lesson markdown (MODUL_PEKAN_05_KNN.md) highlighting student assignments.
- What: Initialized DANISH_AI_AGENT.md context file mapping repository architecture, coursework across Week 3, 4, and 7, and KNN assignment requirements.
