# Module Note: Week 12 — Clustering (K-Means & Hierarchical Agglomerative Clustering)
Updated: 2026-11-18

## Overview
Week 12 covers unsupervised machine learning clustering techniques with both theoretical foundations, comprehensive manual calculations, evaluation metrics, and practical implementations.

## Key Files & Artifacts
- `Week_12/Modul_11_Klastering_Rev06.docx`: Original lecture module in Word document format.
- `Week_12/Modul_11_Klastering_Rev06.md`: High-fidelity markdown conversion (3,130 lines, 80,636 chars) capturing all 20 concept sections, K-Means Karhutla simulation manual calculations, Hierarchical Agglomerative Clustering (HAC) Single Linkage manual calculations, 44 tables, 9 original figures, and Python implementation.
- `Week_12/JAWABAN_TUGAS_KLASTERING_KMEANS_AGLOMERATIF.md`: Complete handwritten-ready solution document for assignment on Minimarket Customer Behavior dataset ($N=6$, features: $X_1$ Visits, $X_2$ Total Spend scaled to hundreds of thousands IDR: $1.0$ to $10.0$).
- `Week_12/images/`: Extracted module images (`image1.png`–`image9.png`) and newly generated assignment charts:
  - `grafik_koordinat_pelanggan_kmeans.png`: Scatter plot with clean white background (no grid/drop lines), 1:1 aspect ratio, coordinates for $P_1$..$P_6$ and centroids $C_1, C_2$.
  - `grafik_dendrogram_agglomerative.png`: Tree dendrogram with clean white background, linkage distance values, and $h=5.0$ cut-off threshold.

## Numerical Details & Ground Truth (Minimarket Dataset)
- Data Points:
  - $P_1 = (2;\ 1.0)$
  - $P_2 = (3;\ 1.5)$
  - $P_3 = (4;\ 2.0)$
  - $P_4 = (12;\ 8.0)$
  - $P_5 = (14;\ 9.0)$
  - $P_6 = (15;\ 10.0)$
- K-Means ($K=2$):
  - Initial centroids: $C_1 = P_1(2;\ 1.0)$, $C_2 = P_4(12;\ 8.0)$
  - Iteration 1 clusters: $C_1 = \{P_1, P_2, P_3\}$, $C_2 = \{P_4, P_5, P_6\}$
  - New centroids: $C_1^{\text{baru}} = (3.0;\ 1.5)$ [coincides with $P_2$], $C_2^{\text{baru}} = (13.667;\ 9.0)$
  - Iteration 2: Clusters remain $\{P_1, P_2, P_3\}$ and $\{P_4, P_5, P_6\}$ $\rightarrow$ Converged.
  - WCSS: $SS_1 = 2.500$, $SS_2 = 6.667$, $\text{Total } WCSS = 9.167$.
- Agglomerative Clustering (Single Linkage):
  - $D_0$ min distance: $d(P_1, P_2) = d(P_2, P_3) = 1.1180$. Tie-breaking alphabetically selects $(P_1, P_2)$.
  - Step 1: Merge $P_1, P_2$ at $d = 1.1180$.
  - Step 2: Merge $(P_1, P_2)$ with $P_3$ at $d = 1.1180$.
  - Step 3: Merge $P_5, P_6$ at $d = 1.4142$.
  - Step 4: Merge $P_4$ with $(P_5, P_6)$ at $d = 2.2361$.
  - Step 5: Merge $(P_1, P_2, P_3)$ with $(P_4, P_5, P_6)$ at $d = 10.0000$.
  - Cut-off at $h = 5.0$ ($2.2361 < h < 10.0000$) produces identical 2 clusters: $\{P_1, P_2, P_3\}$ and $\{P_4, P_5, P_6\}$.

## Conventions & Rules for this Week
1. **Scaled Spend Feature:** When drawing plots or calculating distances, $X_2$ is scaled in units of Rp 100,000 (e.g. 100,000 $\to$ 1.0, 150,000 $\to$ 1.5) so that $X_1$ and $X_2$ have comparable ranges and can be drawn on standard square-ruled paper.
2. **Clean Plot Preference:** Avoid busy internal grid lines or arbitrary tilted ellipses on the scatter plot; maintain clean white backgrounds with clear axes, ticks, and distinct point/centroid markers.
3. **Tie-Breaking Rule:** Alphabetical point ID order is strictly enforced on tie distances.
