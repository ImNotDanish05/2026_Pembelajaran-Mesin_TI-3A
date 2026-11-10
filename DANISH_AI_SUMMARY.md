# DANISH_AI_SUMMARY.md
> Written by AI agents, for AI agents. Read this, then danish_ai_summary/CURRENT_STATE.md, BEFORE exploring other files.
> Detailed notes live in danish_ai_summary/. Update them as you work, not just at the end.

## Overview
Machine learning coursework repository covering supervised learning implementations, manual numerical calculations, multi-model benchmarks, and evaluation metrics (classification and regression).

## Must-know (Avoid Common Failures)
1. **Exact Numerical Match:** Manual calculations MUST match scikit-learn output exactly (verify step-by-step).
2. **Tie-Breaking Rule:** Ties in distance or ranking must always be resolved alphabetically by point ID. Omitting this causes a -20% grading deduction.
3. **Anti-Leakage Rule:** Feature scaling (MinMaxScaler, StandardScaler) must be fit ONLY on training data; never fit on validation/test/query data.
4. **Anonymity Requirement:** NEVER include real-world personal identity, student names, lecturer names, or college/institutional details.
5. **Plot Clarity:** Large dataset scatter plots ($N > 20$): label IDs only for the nearest K neighbors and query point; leave other points unlabeled.
6. **Encoding Gotcha:** Set UTF-8 encoding in Python scripts (`sys.stdout.reconfigure(encoding='utf-8')`) when running on Windows to avoid CP1252 `UnicodeEncodeError`.

## Stack
- Python 3.10+ (use `py -3.10` on Windows, or system `python3` on Linux)
- Libraries: `scikit-learn`, `pandas`, `numpy`, `matplotlib`, `seaborn`
- Environment: Jupyter Notebooks (`.ipynb`) and Python scripts (`.py`)

## Commands
- Run notebook headless / execute test: `python -m pytest` or run cells via Python script / Jupyter runner
- Python check: `python3 <script_path>.py` (or `py -3.10 <script_path>.py` on Windows)
- Package install: `python3 -m pip install scikit-learn pandas numpy matplotlib seaborn`

## Structure map (top-level, one line per folder)
- `Week_3/` — Logistic regression decision thresholds (0.50 vs 0.60), confusion matrix, and manual vs scikit-learn metric calculations.
- `Week_4/` — 5-model classification benchmark (Random Forest, KNN, Decision Tree, SVM, Naive Bayes) on UCI Diabetes dataset with 10-fold CV, ROC/AUC, and confusion matrices.
- `Week_7/` — K-Nearest Neighbors (KNN) module: distance metrics, scaling, manual calculations ($N=24$), assignment solution document (`JAWABAN_TUGAS_MANDIRI_KNN.md`), and plots (`visualisasi_tugas_knn.png`).
- `Week_8/` — Feature Selection (`FiturSelection.ipynb`).
- `Week_9/` — Fuzzy Logic module (`MODUL_07_LOGIKA_FUZZY.md`, `MODUL-07-LOGIKA FUZZY.pdf`).
- `Week_10/` — Research and SINTA 3 Journal publications for Classification (Bank Marketing UCI with Pearson Selection 51->43, KNN, DT, NB, SVM, 5-Fold CV: `jurnal/Klasifikasi.docx`) and Regression (Advertising Dataset multi-channel TV/Radio/Newspaper with Simple Linear, Multiple Linear, Polynomial Regression Degree 2, 10-Fold CV: `jurnal/Regresi.docx`, `jurnal/NASKAH_JURNAL_REGRESI_SINTA3.md`).
- `Week_11/` — Dataset emisi CO2 (`emisiCO2.xlsx`) bersumber dari SIPONGI KEMENHUT beserta atribusi / kredit (`README.md`).

## Notes index (what to read when)
| Need | Read |
|---|---|
| Where did we stop? | danish_ai_summary/CURRENT_STATE.md |
| Big picture & data flow | danish_ai_summary/ARCHITECTURE.md |
| Before writing code / rules | danish_ai_summary/CONVENTIONS.md |
| Why is it like this? | danish_ai_summary/DECISIONS.md |
| Changelog & history | danish_ai_summary/CHANGELOG.md |
| Week 7 KNN details | danish_ai_summary/modules/week_7_knn.md |
| Week 9 Fuzzy Logic | danish_ai_summary/modules/week_9_fuzzy.md |
| Older history | danish_ai_summary/archive/ (only if needed) |

## DO NOT touch
- `.git/` — repository version control metadata.
- Original dataset archives or generated artifacts unless instructed.

<!-- last verified: 2026-11-01 -->
