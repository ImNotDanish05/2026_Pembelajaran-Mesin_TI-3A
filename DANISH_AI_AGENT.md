# DANISH_AI_AGENT.md
> This file is for AI agents, not humans. Update after finishing every task. Read this BEFORE exploring other files.

## Overview
Machine learning coursework repository covering supervised learning implementations, manual numerical calculations, multi-model benchmarks, and evaluation metrics (classification and regression).

## Stack
- Python 3.10+ (use `py -3.10` where data science libraries are installed)
- Libraries: `scikit-learn`, `pandas`, `numpy`, `matplotlib`, `seaborn`
- Environment: Jupyter Notebooks (`.ipynb`) and Python scripts (`.py`)

## Commands
- Run notebook headless / execute test: `python -m pytest` or run cells via Python script / Jupyter runner
- Python check: `py -3.10 <script_path>.py`
- Package install: `py -3.10 -m pip install scikit-learn pandas numpy matplotlib seaborn`

## Structure map (top-level only, 1 line per folder)
- `Week_3/` — Logistic regression decision thresholds (0.50 vs 0.60), confusion matrix, and manual vs scikit-learn metric calculations.
- `Week_4/` — 5-model classification benchmark (Random Forest, KNN, Decision Tree, SVM, Naive Bayes) on UCI Diabetes dataset with 10-fold CV, ROC/AUC, and confusion matrices.
- `Week_7/` — K-Nearest Neighbors (KNN) module: distance metrics, scaling, manual calculations ($N=24$), assignment solution document (`JAWABAN_TUGAS_MANDIRI_KNN.md`), and plots (`visualisasi_tugas_knn.png`).

## Conventions that differ from defaults / can't be inferred
- Manual calculations MUST match scikit-learn output exactly (verify step-by-step).
- Tie-breaking rule: ties in distance or ranking must always be resolved alphabetically by point ID.
- Feature scaling (MinMaxScaler, StandardScaler) must be fit ONLY on training data; never fit on validation/test/query data (anti-leakage rule).
- Large dataset scatter plots (N > 20): label IDs only for the nearest K neighbors and query point; leave other points unlabeled to maintain visual clarity.
- Anonymity requirement: NEVER include real-world personal identity, student names, lecturer names, or college/institutional details.

## DO NOT touch
- `.git/` — repository version control metadata.
- Original dataset archives or generated artifacts unless instructed.

## Known gotchas
- PowerShell execution policy on Windows may block profile scripts (`profile.ps1`); execute commands directly without relying on custom shell profiles.
- Windows CP1252 terminal encoding can throw `UnicodeEncodeError` when printing Unicode characters (e.g. arrows, math symbols); always set UTF-8 encoding in Python scripts (`sys.stdout.reconfigure(encoding='utf-8')`).
- Omitting the tie-breaking explanation causes a standard -20% grading deduction in KNN assignments.

- 2026-10-17: Embedded direct visualisasi_tugas1_km.png and visualisasi_tugas2_rm.png into JAWABAN_TUGAS_MANDIRI_KNN.md with 2-table formats (A-X raw with Rank and sorted Rank 1-24).
- 2026-10-17: Computed and documented complete 6-stage solutions for Week 7 KNN assignments (KM & RM, N=24) with Python scikit-learn verification in JAWABAN_TUGAS_MANDIRI_KNN.md.
- 2026-10-17: Transcribed and rewritten Week 7 KNN module into pure-lesson markdown (MODUL_PEKAN_05_KNN.md) highlighting student assignments.
- 2026-10-17: Initialized DANISH_AI_AGENT.md context file mapping repository architecture, coursework across Week 3, 4, and 7, and KNN assignment requirements.
