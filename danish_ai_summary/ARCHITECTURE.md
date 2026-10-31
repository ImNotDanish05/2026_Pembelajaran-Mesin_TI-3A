# Architecture & Repository Structure

## Overview
Machine learning coursework repository covering supervised learning implementations, manual numerical calculations, multi-model benchmarks, and evaluation metrics (classification and regression).

## Tech Stack & Environment
- **Python:** 3.10+ (use `py -3.10` on Windows where data science libraries are installed, or system `python3` on Linux).
- **Core Libraries:** `scikit-learn`, `pandas`, `numpy`, `matplotlib`, `seaborn`.
- **Formats:** Jupyter Notebooks (`.ipynb`), Python scripts (`.py`), Markdown documentation (`.md`).

## Folder Structure
- `Week_3/` — Logistic regression decision thresholds (0.50 vs 0.60), confusion matrix, and manual vs scikit-learn metric calculations.
- `Week_4/` — 5-model classification benchmark (Random Forest, KNN, Decision Tree, SVM, Naive Bayes) on UCI Diabetes dataset with 10-fold CV, ROC/AUC, and confusion matrices.
- `Week_7/` — K-Nearest Neighbors (KNN) module: distance metrics, scaling, manual calculations ($N=24$), assignment solution document (`JAWABAN_TUGAS_MANDIRI_KNN.md`), and plots (`visualisasi_tugas_knn.png`).
- `Week_8/` — Feature Selection (`FiturSelection.ipynb`).
- `Week_9/` — Fuzzy Logic module (`MODUL-07-LOGIKA FUZZY.pdf`).

## Data Flow & Calculation Verification
1. Raw problem / dataset definition (features & target).
2. Data preprocessing & scaling (fit strictly on training data).
3. Algorithmic steps executed manually step-by-step with explicit formulas.
4. Numerical verification via `scikit-learn` / Python scripts to ensure 100% precision alignment.
5. Visualization with labeled targets, thresholds, or neighbors.

