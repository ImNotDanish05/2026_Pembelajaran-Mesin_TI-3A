# Changelog

### 2026-11-10 — Authored SINTA 3 Scientific Paper on Forest Fire Clustering in Indonesia
- What: Prepared dataset attribution, cleaned & merged SIPONGI KEMENHUT 2023 data (burned area & CO2 emissions across 38 provinces).
- What: Engineered orthogonal dimension features (log burned area vs log emission intensity per hectare, r = -0.018) avoiding redundancy of log emisi vs log luas (r = 0.955).
- What: Evaluated K-Means, Agglomerative Hierarchical (Ward), and Gaussian Mixture Models across K=2..8; determined K=7 as optimal (Silhouette 0.4285, DBI 0.6712, CH 33.5641) with 7 distinct spatial typologies.
- What: Validated 26 scholarly references via automated live HTTP testing (100% HTTP 200/202 OK, zero 404/403).
- What: Authored publication-grade 2-column IEEE format Word document (.docx) and full Markdown manuscript (.md) complete with author metadata (Danish Mahdi & Setyawan Wibisono, Polines Semarang), 4 full-width anti-clipping tables, and 6 high-res figures.
- Files: Week_11/catatan/Artikel_Jurnal_SINTA3_Clustering_Karhutla.docx, Week_11/catatan/NASKAH_JURNAL_CLUSTERING_SINTA3.md, Week_11/catatan/DAFTAR_PUSTAKA_JURNAL.md, Week_11/catatan/generate_clustering_paper.py, Week_11/Main.ipynb, Week_11/output_week11/, Week_11/README.md.
- Verified: Ran python-docx generator script (1.6 MB docx output); inspected tables, figures, metadata, and notebook outputs.

### 2026-11-03 — Authored SINTA 3 Scientific Paper on Bank Marketing Classification
- What: Authored complete, publication-grade academic journal article in standard 2-column IEEE format for SINTA 3 indexing based on `Week_10/Penilitian_Klasifikasi.ipynb`.
- What: Validated 22 scholarly reference DOIs/URLs live using Python (`validate_final_references.py`), confirming 100% active status (`HTTP 200 OK`).
- What: Structured complete IMRAD manuscript: Title (ID & EN), Authors (Danish Mahdi & Setyawan Wibisono, Polines), Abstract (ID & EN), Pendahuluan, Tinjauan Pustaka, Metodologi, Hasil & Pembahasan (4 tables, 3 figures, 5-fold CV), Kesimpulan, and 22 IEEE References.
- Files: Week_10/jurnal/Klasifikasi.docx, Week_10/jurnal/Klasifikasi_SINTA3_Final.docx, Week_10/jurnal/NASKAH_JURNAL_SINTA3.md, Week_10/jurnal/generate_sinta3_paper.py.
- Verified: Ran Python docx builder generating 108 paragraphs, 4 tables, 3 images across 4 sections; inspected docx structure and verified exact metric alignment with notebook.


### 2026-11-01 — Expanded Manual Calculation Steps to 5 Samples per Task
- What: Added 5th step-by-step manual calculation to Soal 1 (Data No. 7: Suhu 24, Lembap 35, y=15 -> y_hat=15.43) and Soal 2 (Data No. 13: Rasio 28, Skor 60, Aktual Rendah -> Prediksi Tinggi / Conservative False Positive).
- What: Updated Python verification script `Week_9/verifikasi_tugas_fuzzy.py` with dedicated sample calculation printouts for all 5 instances per task.
- Files: Week_9/JAWABAN_TUGAS_MANDIRI_FUZZY.md, Week_9/verifikasi_tugas_fuzzy.py, danish_ai_summary/CURRENT_STATE.md.
- Verified: Ran `python Week_9\verifikasi_tugas_fuzzy.py` (exit code 0); confirmed 100% precision with zero calculation discrepancy.


### 2026-11-01 — Verified Fuzzy Logic Assignment Calculations via Independent Python Script
- What: Created standalone verification script `Week_9/verifikasi_tugas_fuzzy.py` to independently compute and validate all numerical values in `Week_9/JAWABAN_TUGAS_MANDIRI_FUZZY.md`.
- What: Verified 100% of 20-row calculations for Soal 1 (Sugeno Regression: μ, α, ŷ, MAE=1.59, RMSE=1.91) and Soal 2 (Fuzzy Rule-Based Classification: μ, α, conservative scoring, Confusion Matrix TP=12, TN=7, FP=1, FN=0, Akurasi=95.00%, Recall=100.00%, F1=96.00%).
- Files: Week_9/verifikasi_tugas_fuzzy.py, danish_ai_summary/CURRENT_STATE.md, danish_ai_summary/CHANGELOG.md.
- Verified: Ran `python Week_9\verifikasi_tugas_fuzzy.py` (exit code 0); all values matched the markdown tables and manual sample steps with 0 discrepancy.


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
