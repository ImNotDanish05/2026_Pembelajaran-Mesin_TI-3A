# Conventions and Gotchas

## Core Coursework Conventions
- **Exact Numerical Match:** Manual calculations MUST match scikit-learn output exactly (verify step-by-step).
- **Tie-Breaking Rule:** Ties in distance or ranking must always be resolved alphabetically by point ID.
- **Anti-Leakage Rule (Scaling):** Feature scaling (MinMaxScaler, StandardScaler) must be fit ONLY on training data; never fit on validation/test/query data.
- **Plot Readability:** Large dataset scatter plots (N > 20): label IDs only for the nearest K neighbors and query point; leave other points unlabeled to maintain visual clarity.
- **Anonymity Requirement:** NEVER include real-world personal identity, student names, lecturer names, or college/institutional details.

## DO NOT Touch
- `.git/` — repository version control metadata.
- Original dataset archives or generated artifacts unless instructed.

## Known Gotchas
- **Windows PowerShell Profile:** PowerShell execution policy on Windows may block profile scripts (`profile.ps1`); execute commands directly without relying on custom shell profiles. *(Note: currently running in Linux environment, but applies if user runs on Windows).*
- **Windows Terminal Encoding:** Windows CP1252 terminal encoding can throw `UnicodeEncodeError` when printing Unicode characters (e.g. arrows, math symbols); always set UTF-8 encoding in Python scripts (`sys.stdout.reconfigure(encoding='utf-8')`).
- **Grading Penalty:** Omitting the tie-breaking explanation causes a standard -20% grading deduction in KNN assignments.

## User Preferences
*(None explicitly recorded yet; add standing instructions here as stated by user).*

