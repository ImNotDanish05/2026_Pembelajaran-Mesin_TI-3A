# Decisions Log

### D-004 — Full academic Markdown transcription for Week 9 Fuzzy Logic module (2026-10-31)
- **Context:** User requested conversion of `Week_9/MODUL-07-LOGIKA FUZZY.pdf` (41 pages) into Markdown.
- **Decision:** Transcribe the entire PDF into `Week_9/MODUL_07_LOGIKA_FUZZY.md` retaining all 3 main sections (Konsep Dasar, Latihan Terbimbing Regresi & Klasifikasi, Tugas Mandiri), using KaTeX math blocks (`$$...$$`), standard tables, GitHub alerts (`[!NOTE]`, `[!IMPORTANT]`), and extracted diagram `ilustrasi_segitiga_fuzzy.png`.
- **Reason:** Provides an identical reading and study experience to `Week_7/MODUL_PEKAN_05_KNN.md`.

### D-003 — Dual-table distance ranking presentation (2026-10-17)
- **Context:** Students and graders need to see both the original point order and the ranked order to grade easily.
- **Decision:** Present KNN distance tables in two formats: (1) Raw order A-X with rank column, and (2) Sorted order Rank 1 to N.
- **Alternative rejected:** Single sorted table (makes it harder to look up a specific point ID).

### D-002 — Alphabetical tie-breaking policy (2026-10-17)
- **Context:** Ties in distance or ranking can lead to non-deterministic neighbor selection.
- **Decision:** Always break ties by alphabetical order of point IDs ($A < B < C \dots$).
- **Consequence:** Essential for grading consistency; omitting causes -20% grading deduction.

### D-001 — Strict anonymity policy (2026-10-17)
- **Context:** Coursework files and markdown docs may be shared or committed to public/semi-public repos.
- **Decision:** NEVER include real-world personal identity, student names, lecturer names, or institutional details.
