# TUGAS MANDIRI PERHITUNGAN MATEMATIKA KLASTERING
## Studi Kasus: Segmentasi Perilaku Pelanggan Minimarket
> **Metode:** K-Means Clustering & Hierarchical Agglomerative Clustering (HAC)  
> **Format Pengerjaan:** Panduan Langkah demi Langkah Siap Salin ke Kertas Folio Bergaris  
> **Karakteristik Skala:** Sumbu $X_1$ (Kunjungan) dan Sumbu $X_2$ (Total Belanja dinormalisasi dalam satuan ratusan ribu rupiah agar mudah digambar pada grafik).

---

## 📋 DAFTAR ISI PENGERJAAN

- [1. Data Awal & Penyederhanaan Skala Grafik](#1-data-awal--penyederhanaan-skala-grafik)
- [2. ALGORITMA 1: K-MEANS CLUSTERING](#2-algoritma-1-k-means-clustering)
  - [2.1 Parameter Awal ($K=2$) & Pemilihan Centroid](#21-parameter-awal-k2--pemilihan-centroid)
  - [2.2 Iterasi 1: Perhitungan Jarak Euclidean & Pengelompokan](#22-iterasi-1-perhitungan-jarak-euclidean--pengelompokan)
  - [2.3 Pembaruan Centroid (Centroid Baru Iterasi 2)](#23-pembaruan-centroid-centroid-baru-iterasi-2)
  - [2.4 Iterasi 2: Pengujian Konvergensi](#24-iterasi-2-pengujian-konvergensi)
  - [2.5 Evaluasi Kekompakan Klaster (WCSS)](#25-evaluasi-kekompakan-klaster-wcss)
- [3. ALGORITMA 2: HIERARCHICAL AGGLOMERATIVE CLUSTERING (HAC)](#3-algoritma-2-hierarchical-agglomerative-clustering-hac)
  - [3.1 Prinsip Kerja & Matriks Jarak Awal ($D_0$)](#31-prinsip-kerja--matriks-jarak-awal-d_0)
  - [3.2 Iterasi 1: Penggabungan $P_1$ dan $P_2$](#32-iterasi-1-penggabungan-p_1-dan-p_2)
  - [3.3 Iterasi 2: Penggabungan $(P_{12})$ dan $P_3$](#33-iterasi-2-penggabungan-p_12-dan-p_3)
  - [3.4 Iterasi 3: Penggabungan $P_5$ dan $P_6$](#34-iterasi-3-penggabungan-p_5-dan-p_6)
  - [3.5 Iterasi 4: Penggabungan $P_4$ dan $(P_{56})$](#35-iterasi-4-penggabungan-p_4-dan-p_56)
  - [3.6 Iterasi 5: Penggabungan Akhir Seluruh Objek](#36-iterasi-5-penggabungan-akhir-seluruh-objek)
  - [3.7 Pemotongan Dendrogram ($K=2$)](#37-pemotongan-dendrogram-k2)
- [4. PANDUAN MENGGAMBAR GRAFIK DI KERTAS FOLIO](#4-panduan-menggambar-grafik-di-kertas-folio)
  - [4.1 Grafik 1: Scatter Plot 2D K-Means & Posisi Centroid](#41-grafik-1-scatter-plot-2d-k-means--posisi-centroid)
  - [4.2 Grafik 2: Dendrogram Agglomerative Clustering](#42-grafik-2-dendrogram-agglomerative-clustering)
- [5. KESIMPULAN & INTERPRETASI BISNIS](#5-kesimpulan--interpretasi-bisnis)

---

## 1. Data Awal & Penyederhanaan Skala Grafik

Sesuai instruksi dosen, data pengeluaran/total belanja disederhanakan skalanya dengan membagi nilai nominal sebesar $100.000$ (skala ratusan ribu rupiah), sehingga rentang nilai seimbang dengan variabel jumlah kunjungan dan sangat mudah diplot pada kertas grafik/folio.

- **Variabel $X_1$:** Jumlah Kunjungan (kali/bulan)
- **Variabel $X_2$:** Total Belanja (dalam ratusan ribu rupiah, $\text{Rp } 100.000 = 1,0$)

### Tabel 1. Data Koordinat Siap Hitung

| Pelanggan | Kunjungan ($X_1$) | Belanja Asli (Rp) | Skala Belanja ($X_2$) | Koordinat Titik $(X_1, X_2)$ |
| :---: | :---: | :---: | :---: | :---: |
| **P1** | 2 | 100.000 | **1,0** | **$(2; 1,0)$** |
| **P2** | 3 | 150.000 | **1,5** | **$(3; 1,5)$** |
| **P3** | 4 | 200.000 | **2,0** | **$(4; 2,0)$** |
| **P4** | 12 | 800.000 | **8,0** | **$(12; 8,0)$** |
| **P5** | 14 | 900.000 | **9,0** | **$(14; 9,0)$** |
| **P6** | 15 | 1.000.000 | **10,0** | **$(15; 10,0)$** |

---

## 2. ALGORITMA 1: K-MEANS CLUSTERING

### 2.1 Parameter Awal ($K=2$) & Pemilihan Centroid

1. **Jumlah Klaster ($K$):** Ditentukan $K = 2$ (mencari kelompok pelanggan belanja rendah vs belanja tinggi).
2. **Penentuan Centroid Awal ($C_1, C_2$):**  
   Mengikuti standar modul (Bagian 8), centroid awal diambil dari perwakilan awal masing-masing sebaran kelompok:
   - **Centroid Klaster 1 ($C_1$):** Titik $P_1 = (2; 1,0)$
   - **Centroid Klaster 2 ($C_2$):** Titik $P_4 = (12; 8,0)$

> *Catatan Tambahan untuk Folio:* Jika dosen menghendaki centroid awal titik ekstrem $P_1$ dan $P_6$, atau titik berdekatan $P_1$ dan $P_2$, hasil klaster akhir tetap **100% identik** karena data memiliki pemisahan alami yang sangat tegas.

---

### 2.2 Iterasi 1: Perhitungan Jarak Euclidean & Pengelompokan

Rumus Euclidean Distance antara titik $P(x_1, x_2)$ dan Centroid $C(c_1, c_2)$:
$$d(P, C) = \sqrt{(x_1 - c_1)^2 + (x_2 - c_2)^2}$$

#### A. Perhitungan Manual Jarak Tiap Objek:

1. **Objek P1 $(2; 1,0)$:**
   - Jarak ke $C_1(2; 1,0)$:
     $$d(P_1, C_1) = \sqrt{(2-2)^2 + (1-1)^2} = \sqrt{0 + 0} = \mathbf{0}$$
   - Jarak ke $C_2(12; 8,0)$:
     $$d(P_1, C_2) = \sqrt{(2-12)^2 + (1-8)^2} = \sqrt{(-10)^2 + (-7)^2} = \sqrt{100 + 49} = \sqrt{149} \approx \mathbf{12,207}$$
   - $\min(0; 12,207) = 0 \implies \mathbf{Klaster\ 1}$

2. **Objek P2 $(3; 1,5)$:**
   - Jarak ke $C_1(2; 1,0)$:
     $$d(P_2, C_1) = \sqrt{(3-2)^2 + (1,5-1)^2} = \sqrt{1^2 + 0,5^2} = \sqrt{1 + 0,25} = \sqrt{1,25} \approx \mathbf{1,118}$$
   - Jarak ke $C_2(12; 8,0)$:
     $$d(P_2, C_2) = \sqrt{(3-12)^2 + (1,5-8)^2} = \sqrt{(-9)^2 + (-6,5)^2} = \sqrt{81 + 42,25} = \sqrt{123,25} \approx \mathbf{11,102}$$
   - $\min(1,118; 11,102) = 1,118 \implies \mathbf{Klaster\ 1}$

3. **Objek P3 $(4; 2,0)$:**
   - Jarak ke $C_1(2; 1,0)$:
     $$d(P_3, C_1) = \sqrt{(4-2)^2 + (2-1)^2} = \sqrt{2^2 + 1^2} = \sqrt{4 + 1} = \sqrt{5} \approx \mathbf{2,236}$$
   - Jarak ke $C_2(12; 8,0)$:
     $$d(P_3, C_2) = \sqrt{(4-12)^2 + (2-8)^2} = \sqrt{(-8)^2 + (-6)^2} = \sqrt{64 + 36} = \sqrt{100} = \mathbf{10,000}$$
   - $\min(2,236; 10,000) = 2,236 \implies \mathbf{Klaster\ 1}$

4. **Objek P4 $(12; 8,0)$:**
   - Jarak ke $C_1(2; 1,0)$:
     $$d(P_4, C_1) = \sqrt{(12-2)^2 + (8-1)^2} = \sqrt{10^2 + 7^2} = \sqrt{100 + 49} = \sqrt{149} \approx \mathbf{12,207}$$
   - Jarak ke $C_2(12; 8,0)$:
     $$d(P_4, C_2) = \sqrt{(12-12)^2 + (8-8)^2} = \sqrt{0 + 0} = \mathbf{0}$$
   - $\min(12,207; 0) = 0 \implies \mathbf{Klaster\ 2}$

5. **Objek P5 $(14; 9,0)$:**
   - Jarak ke $C_1(2; 1,0)$:
     $$d(P_5, C_1) = \sqrt{(14-2)^2 + (9-1)^2} = \sqrt{12^2 + 8^2} = \sqrt{144 + 64} = \sqrt{208} \approx \mathbf{14,422}$$
   - Jarak ke $C_2(12; 8,0)$:
     $$d(P_5, C_2) = \sqrt{(14-12)^2 + (9-8)^2} = \sqrt{2^2 + 1^2} = \sqrt{4 + 1} = \sqrt{5} \approx \mathbf{2,236}$$
   - $\min(14,422; 2,236) = 2,236 \implies \mathbf{Klaster\ 2}$

6. **Objek P6 $(15; 10,0)$:**
   - Jarak ke $C_1(2; 1,0)$:
     $$d(P_6, C_1) = \sqrt{(15-2)^2 + (10-1)^2} = \sqrt{13^2 + 9^2} = \sqrt{169 + 81} = \sqrt{250} \approx \mathbf{15,811}$$
   - Jarak ke $C_2(12; 8,0)$:
     $$d(P_6, C_2) = \sqrt{(15-12)^2 + (10-8)^2} = \sqrt{3^2 + 2^2} = \sqrt{9 + 4} = \sqrt{13} \approx \mathbf{3,606}$$
   - $\min(15,811; 3,606) = 3,606 \implies \mathbf{Klaster\ 2}$

---

#### Tabel Rekapitulasi Iterasi 1

| Objek | Koordinat | Jarak ke $C_1(2; 1)$ | Jarak ke $C_2(12; 8)$ | Jarak Minimum | Klaster Terpilih |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **P1** | $(2; 1,0)$ | **0,000** | 12,207 | 0,000 | **Klaster 1** |
| **P2** | $(3; 1,5)$ | **1,118** | 11,102 | 1,118 | **Klaster 1** |
| **P3** | $(4; 2,0)$ | **2,236** | 10,000 | 2,236 | **Klaster 1** |
| **P4** | $(12; 8,0)$ | 12,207 | **0,000** | 0,000 | **Klaster 2** |
| **P5** | $(14; 9,0)$ | 14,422 | **2,236** | 2,236 | **Klaster 2** |
| **P6** | $(15; 10,0)$ | 15,811 | **3,606** | 3,606 | **Klaster 2** |

**Keanggotaan Iterasi 1:**
- **Klaster 1:** $\{P_1, P_2, P_3\}$
- **Klaster 2:** $\{P_4, P_5, P_6\}$

---

### 2.3 Pembaruan Centroid (Centroid Baru Iterasi 2)

Hitung nilai rata-rata (*mean*) dari seluruh objek di setiap klaster:

$$\mu_k = \left( \frac{\sum X_1}{|C_k|}, \frac{\sum X_2}{|C_k|} \right)$$

1. **Centroid Baru Klaster 1 ($C_1^{\text{baru}}$):**
   - $\mu_{1,1} = \frac{2 + 3 + 4}{3} = \frac{9}{3} = \mathbf{3,000}$
   - $\mu_{1,2} = \frac{1,0 + 1,5 + 2,0}{3} = \frac{4,5}{3} = \mathbf{1,500}$
   - $\mathbf{C_1^{\text{baru}} = (3,000;\ 1,500)}$ *(tepat pada koordinat titik $P_2$)*

2. **Centroid Baru Klaster 2 ($C_2^{\text{baru}}$):**
   - $\mu_{2,1} = \frac{12 + 14 + 15}{3} = \frac{41}{3} \approx \mathbf{13,667}$
   - $\mu_{2,2} = \frac{8,0 + 9,0 + 10,0}{3} = \frac{27}{3} = \mathbf{9,000}$
   - $\mathbf{C_2^{\text{baru}} = (13,667;\ 9,000)}$

---

### 2.4 Iterasi 2: Pengujian Konvergensi

Hitung kembali jarak seluruh objek terhadap $C_1(3,000; 1,500)$ dan $C_2(13,667; 9,000)$:

1. **P1 $(2; 1,0)$:**
   - $d(P_1, C_1) = \sqrt{(2-3)^2 + (1-1,5)^2} = \sqrt{1 + 0,25} = \sqrt{1,25} \approx \mathbf{1,118}$
   - $d(P_1, C_2) = \sqrt{(2-13,667)^2 + (1-9)^2} = \sqrt{(-11,667)^2 + (-8)^2} = \sqrt{136,119 + 64} = \sqrt{200,119} \approx \mathbf{14,146}$
   - $\min(1,118; 14,146) = 1,118 \implies \mathbf{Klaster\ 1}$

2. **P2 $(3; 1,5)$:**
   - $d(P_2, C_1) = \sqrt{(3-3)^2 + (1,5-1,5)^2} = \mathbf{0,000}$
   - $d(P_2, C_2) = \sqrt{(3-13,667)^2 + (1,5-9)^2} = \sqrt{(-10,667)^2 + (-7,5)^2} = \sqrt{113,785 + 56,25} \approx \mathbf{13,040}$
   - $\min(0; 13,040) = 0 \implies \mathbf{Klaster\ 1}$

3. **P3 $(4; 2,0)$:**
   - $d(P_3, C_1) = \sqrt{(4-3)^2 + (2-1,5)^2} = \sqrt{1 + 0,25} = \sqrt{1,25} \approx \mathbf{1,118}$
   - $d(P_3, C_2) = \sqrt{(4-13,667)^2 + (2-9)^2} = \sqrt{(-9,667)^2 + (-7)^2} = \sqrt{93,451 + 49} \approx \mathbf{11,935}$
   - $\min(1,118; 11,935) = 1,118 \implies \mathbf{Klaster\ 1}$

4. **P4 $(12; 8,0)$:**
   - $d(P_4, C_1) = \sqrt{(12-3)^2 + (8-1,5)^2} = \sqrt{81 + 42,25} = \sqrt{123,25} \approx \mathbf{11,102}$
   - $d(P_4, C_2) = \sqrt{(12-13,667)^2 + (8-9)^2} = \sqrt{(-1,667)^2 + (-1)^2} = \sqrt{2,779 + 1} \approx \mathbf{1,944}$
   - $\min(11,102; 1,944) = 1,944 \implies \mathbf{Klaster\ 2}$

5. **P5 $(14; 9,0)$:**
   - $d(P_5, C_1) = \sqrt{(14-3)^2 + (9-1,5)^2} = \sqrt{121 + 56,25} = \sqrt{177,25} \approx \mathbf{13,314}$
   - $d(P_5, C_2) = \sqrt{(14-13,667)^2 + (9-9)^2} = \sqrt{(0,333)^2 + 0} \approx \mathbf{0,333}$
   - $\min(13,314; 0,333) = 0,333 \implies \mathbf{Klaster\ 2}$

6. **P6 $(15; 10,0)$:**
   - $d(P_6, C_1) = \sqrt{(15-3)^2 + (10-1,5)^2} = \sqrt{144 + 72,25} = \sqrt{216,25} \approx \mathbf{14,705}$
   - $d(P_6, C_2) = \sqrt{(15-13,667)^2 + (10-9)^2} = \sqrt{(1,333)^2 + 1^2} = \sqrt{1,777 + 1} \approx \mathbf{1,667}$
   - $\min(14,705; 1,667) = 1,667 \implies \mathbf{Klaster\ 2}$

---

#### Tabel Rekapitulasi Iterasi 2

| Objek | Koordinat | Jarak ke $C_1(3; 1,5)$ | Jarak ke $C_2(13,667; 9)$ | Jarak Minimum | Klaster Iterasi 2 | Status Perubahan |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **P1** | $(2; 1,0)$ | **1,118** | 14,146 | 1,118 | **Klaster 1** | Tetap |
| **P2** | $(3; 1,5)$ | **0,000** | 13,040 | 0,000 | **Klaster 1** | Tetap |
| **P3** | $(4; 2,0)$ | **1,118** | 11,935 | 1,118 | **Klaster 1** | Tetap |
| **P4** | $(12; 8,0)$ | 11,102 | **1,944** | 1,944 | **Klaster 2** | Tetap |
| **P5** | $(14; 9,0)$ | 13,314 | **0,333** | 0,333 | **Klaster 2** | Tetap |
| **P6** | $(15; 10,0)$ | 14,705 | **1,667** | 1,667 | **Klaster 2** | Tetap |

> **KONDISI KONVERGENSI TERCAPAI:**  
> Karena anggota seluruh klaster pada **Iterasi 2 identik dengan Iterasi 1** (tidak ada objek yang berpindah klaster), maka algoritma K-Means dinyatakan **KONVERGEN** dan iterasi dihentikan.

---

### 2.5 Evaluasi Kekompakan Klaster (WCSS)

Rumus Within-Cluster Sum of Squares (WCSS):
$$WCSS = \sum_{x_i \in C_1} \|x_i - \mu_1\|^2 + \sum_{x_i \in C_2} \|x_i - \mu_2\|^2$$

1. **Klaster 1 ($C_1 = (3; 1,5)$):**
   - $\|P_1 - C_1\|^2 = (2-3)^2 + (1-1,5)^2 = (-1)^2 + (-0,5)^2 = 1 + 0,25 = 1,25$
   - $\|P_2 - C_1\|^2 = (3-3)^2 + (1,5-1,5)^2 = 0 + 0 = 0$
   - $\|P_3 - C_1\|^2 = (4-3)^2 + (2-1,5)^2 = 1^2 + 0,5^2 = 1 + 0,25 = 1,25$
   - $SS_1 = 1,25 + 0 + 1,25 = \mathbf{2,500}$

2. **Klaster 2 ($C_2 = (13,667; 9,0)$):**
   - $\|P_4 - C_2\|^2 = (12-13,667)^2 + (8-9)^2 = (-1,667)^2 + (-1)^2 = 2,778 + 1 = 3,778$
   - $\|P_5 - C_2\|^2 = (14-13,667)^2 + (9-9)^2 = (0,333)^2 + 0 = 0,111$
   - $\|P_6 - C_2\|^2 = (15-13,667)^2 + (10-9)^2 = (1,333)^2 + 1^2 = 1,778 + 1 = 2,778$
   - $SS_2 = 3,778 + 0,111 + 2,778 = \mathbf{6,667}$

$$\mathbf{WCSS = SS_1 + SS_2 = 2,500 + 6,667 = 9,167}$$

---

## 3. ALGORITMA 2: HIERARCHICAL AGGLOMERATIVE CLUSTERING (HAC)

Pendekatan: **Bottom-Up** (setiap objek awalnya adalah 1 klaster tersendiri).  
Metode Linkage Utama: **Single Linkage** (jarak minimum / *nearest neighbor* antaranggota klaster):
$$d(A, B) = \min \{ d(x, y) \mid x \in A, y \in B \}$$

### 3.1 Prinsip Kerja & Matriks Jarak Awal ($D_0$)

Hitung jarak Euclidean antar seluruh pasangan objek ($6 \times 6$):
- $d(P_1, P_2) = \sqrt{(3-2)^2 + (1,5-1)^2} = \sqrt{1 + 0,25} = \sqrt{1,25} \approx \mathbf{1,1180}$
- $d(P_1, P_3) = \sqrt{(4-2)^2 + (2-1)^2} = \sqrt{4 + 1} = \sqrt{5} \approx \mathbf{2,2361}$
- $d(P_1, P_4) = \sqrt{(12-2)^2 + (8-1)^2} = \sqrt{100 + 49} = \sqrt{149} \approx \mathbf{12,2066}$
- $d(P_1, P_5) = \sqrt{(14-2)^2 + (9-1)^2} = \sqrt{144 + 64} = \sqrt{208} \approx \mathbf{14,4222}$
- $d(P_1, P_6) = \sqrt{(15-2)^2 + (10-1)^2} = \sqrt{169 + 81} = \sqrt{250} \approx \mathbf{15,8114}$
- $d(P_2, P_3) = \sqrt{(4-3)^2 + (2-1,5)^2} = \sqrt{1 + 0,25} = \sqrt{1,25} \approx \mathbf{1,1180}$
- $d(P_2, P_4) = \sqrt{(12-3)^2 + (8-1,5)^2} = \sqrt{81 + 42,25} = \sqrt{123,25} \approx \mathbf{11,1018}$
- $d(P_2, P_5) = \sqrt{(14-3)^2 + (9-1,5)^2} = \sqrt{121 + 56,25} = \sqrt{177,25} \approx \mathbf{13,3135}$
- $d(P_2, P_6) = \sqrt{(15-3)^2 + (10-1,5)^2} = \sqrt{144 + 72,25} = \sqrt{216,25} \approx \mathbf{14,7054}$
- $d(P_3, P_4) = \sqrt{(12-4)^2 + (8-2)^2} = \sqrt{64 + 36} = \sqrt{100} = \mathbf{10,0000}$
- $d(P_3, P_5) = \sqrt{(14-4)^2 + (9-2)^2} = \sqrt{100 + 49} = \sqrt{149} \approx \mathbf{12,2066}$
- $d(P_3, P_6) = \sqrt{(15-4)^2 + (10-2)^2} = \sqrt{121 + 64} = \sqrt{185} \approx \mathbf{13,6015}$
- $d(P_4, P_5) = \sqrt{(14-12)^2 + (9-8)^2} = \sqrt{4 + 1} = \sqrt{5} \approx \mathbf{2,2361}$
- $d(P_4, P_6) = \sqrt{(15-12)^2 + (10-8)^2} = \sqrt{9 + 4} = \sqrt{13} \approx \mathbf{3,6056}$
- $d(P_5, P_6) = \sqrt{(15-14)^2 + (10-9)^2} = \sqrt{1 + 1} = \sqrt{2} \approx \mathbf{1,4142}$

#### Matriks Jarak Awal $D_0$ ($6 \times 6$)

| | P1 | P2 | P3 | P4 | P5 | P6 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **P1** | 0,0000 | **1,1180** | 2,2361 | 12,2066 | 14,4222 | 15,8114 |
| **P2** | **1,1180** | 0,0000 | **1,1180** | 11,1018 | 13,3135 | 14,7054 |
| **P3** | 2,2361 | **1,1180** | 0,0000 | 10,0000 | 12,2066 | 13,6015 |
| **P4** | 12,2066 | 11,1018 | 10,0000 | 0,0000 | 2,2361 | 3,6056 |
| **P5** | 14,4222 | 13,3135 | 12,2066 | 2,2361 | 0,0000 | 1,4142 |
| **P6** | 15,8114 | 14,7054 | 13,6015 | 3,6056 | 1,4142 | 0,0000 |

---

### 3.2 Iterasi 1: Penggabungan $P_1$ dan $P_2$

1. **Cari Jarak Minimum:**
   Terdapat nilai terkecil yang sama (*tie*):
   - $d(P_1, P_2) = 1,1180$
   - $d(P_2, P_3) = 1,1180$
2. **Aturan Tie-Breaking:**
   Secara leksikografis/urutan indeks alfabet, pilih pasangan $(P_1, P_2)$ terlebih dahulu.
3. **Aksi:** Gabungkan $P_1$ dan $P_2$ menjadi klaster baru $(P_{12})$ pada jarak $d = \mathbf{1,1180}$.
4. **Pembaruan Jarak Single Linkage:**
   - $d((P_{12}), P_3) = \min(d(P_1, P_3), d(P_2, P_3)) = \min(2,2361; 1,1180) = \mathbf{1,1180}$
   - $d((P_{12}), P_4) = \min(d(P_1, P_4), d(P_2, P_4)) = \min(12,2066; 11,1018) = \mathbf{11,1018}$
   - $d((P_{12}), P_5) = \min(d(P_1, P_5), d(P_2, P_5)) = \min(14,4222; 13,3135) = \mathbf{13,3135}$
   - $d((P_{12}), P_6) = \min(d(P_1, P_6), d(P_2, P_6)) = \min(15,8114; 14,7054) = \mathbf{14,7054}$

#### Matriks Jarak $D_1$ ($5 \times 5$)

| | (P1, P2) | P3 | P4 | P5 | P6 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **(P1, P2)** | 0,0000 | **1,1180** | 11,1018 | 13,3135 | 14,7054 |
| **P3** | **1,1180** | 0,0000 | 10,0000 | 12,2066 | 13,6015 |
| **P4** | 11,1018 | 10,0000 | 0,0000 | 2,2361 | 3,6056 |
| **P5** | 13,3135 | 12,2066 | 2,2361 | 0,0000 | 1,4142 |
| **P6** | 14,7054 | 13,6015 | 3,6056 | 1,4142 | 0,0000 |

---

### 3.3 Iterasi 2: Penggabungan $(P_{12})$ dan $P_3$

1. **Cari Jarak Minimum:** Nilai terkecil pada matriks $D_1$ adalah $d((P_{12}), P_3) = \mathbf{1,1180}$.
2. **Aksi:** Gabungkan $(P_{12})$ dan $P_3$ membentuk klaster baru $(P_{123})$ pada jarak $d = \mathbf{1,1180}$.
3. **Pembaruan Jarak Single Linkage:**
   - $d((P_{123}), P_4) = \min(d((P_{12}), P_4), d(P_3, P_4)) = \min(11,1018; 10,0000) = \mathbf{10,0000}$
   - $d((P_{123}), P_5) = \min(d((P_{12}), P_5), d(P_3, P_5)) = \min(13,3135; 12,2066) = \mathbf{12,2066}$
   - $d((P_{123}), P_6) = \min(d((P_{12}), P_6), d(P_3, P_6)) = \min(14,7054; 13,6015) = \mathbf{13,6015}$

#### Matriks Jarak $D_2$ ($4 \times 4$)

| | (P1, P2, P3) | P4 | P5 | P6 |
| :---: | :---: | :---: | :---: | :---: |
| **(P1, P2, P3)** | 0,0000 | 10,0000 | 12,2066 | 13,6015 |
| **P4** | 10,0000 | 0,0000 | 2,2361 | 3,6056 |
| **P5** | 12,2066 | 2,2361 | 0,0000 | **1,4142** |
| **P6** | 13,6015 | 3,6056 | **1,4142** | 0,0000 |

---

### 3.4 Iterasi 3: Penggabungan $P_5$ dan $P_6$

1. **Cari Jarak Minimum:** Nilai terkecil pada matriks $D_2$ adalah $d(P_5, P_6) = \mathbf{1,4142}$.
2. **Aksi:** Gabungkan $P_5$ dan $P_6$ membentuk klaster baru $(P_{56})$ pada jarak $d = \mathbf{1,4142}$.
3. **Pembaruan Jarak Single Linkage:**
   - $d(P_4, (P_{56})) = \min(d(P_4, P_5), d(P_4, P_6)) = \min(2,2361; 3,6056) = \mathbf{2,2361}$
   - $d((P_{123}), (P_{56})) = \min(d((P_{123}), P_5), d((P_{123}), P_6)) = \min(12,2066; 13,6015) = \mathbf{12,2066}$

#### Matriks Jarak $D_3$ ($3 \times 3$)

| | (P1, P2, P3) | P4 | (P5, P6) |
| :---: | :---: | :---: | :---: |
| **(P1, P2, P3)** | 0,0000 | 10,0000 | 12,2066 |
| **P4** | 10,0000 | 0,0000 | **2,2361** |
| **(P5, P6)** | 12,2066 | **2,2361** | 0,0000 |

---

### 3.5 Iterasi 4: Penggabungan $P_4$ dan $(P_{56})$

1. **Cari Jarak Minimum:** Nilai terkecil pada matriks $D_3$ adalah $d(P_4, (P_{56})) = \mathbf{2,2361}$.
2. **Aksi:** Gabungkan $P_4$ dan $(P_{56})$ membentuk klaster baru $(P_{456})$ pada jarak $d = \mathbf{2,2361}$.
3. **Pembaruan Jarak Single Linkage:**
   - $d((P_{123}), (P_{456})) = \min(d((P_{123}), P_4), d((P_{123}), (P_{56}))) = \min(10,0000; 12,2066) = \mathbf{10,0000}$

#### Matriks Jarak $D_4$ ($2 \times 2$)

| | (P1, P2, P3) | (P4, P5, P6) |
| :---: | :---: | :---: |
| **(P1, P2, P3)** | 0,0000 | **10,0000** |
| **(P4, P5, P6)** | **10,0000** | 0,0000 |

---

### 3.6 Iterasi 5: Penggabungan Akhir Seluruh Objek

1. **Aksi:** Menggabungkan dua klaster terakhir $(P_{123})$ dan $(P_{456})$ membentuk satu klaster tunggal $(P_{123456})$ pada jarak $d = \mathbf{10,0000}$.
2. Seluruh 6 objek telah selesai dikelompokkan ke dalam hierarki pohon (dendrogram).

---

### Tabel Ringkasan Seluruh Tahapan Penggabungan (Hierarki)

| Tahap | Pasangan yang Digabung | Jarak Penggabungan ($d$) | Jumlah Klaster Tersisa | Daftar Klaster yang Terbentuk |
| :---: | :---: | :---: | :---: | :---: |
| **Mulai** | - | 0,0000 | 6 | $\{P_1\}, \{P_2\}, \{P_3\}, \{P_4\}, \{P_5\}, \{P_6\}$ |
| **Iterasi 1** | $P_1$ dan $P_2$ | **1,1180** | 5 | $\{P_1, P_2\}, \{P_3\}, \{P_4\}, \{P_5\}, \{P_6\}$ |
| **Iterasi 2** | $\{P_1, P_2\}$ dan $P_3$ | **1,1180** | 4 | $\{P_1, P_2, P_3\}, \{P_4\}, \{P_5\}, \{P_6\}$ |
| **Iterasi 3** | $P_5$ dan $P_6$ | **1,4142** | 3 | $\{P_1, P_2, P_3\}, \{P_4\}, \{P_5, P_6\}$ |
| **Iterasi 4** | $P_4$ dan $\{P_5, P_6\}$ | **2,2361** | 2 | **$\{P_1, P_2, P_3\}, \{P_4, P_5, P_6\}$** |
| **Iterasi 5** | $\{P_1, P_2, P_3\}$ dan $\{P_4, P_5, P_6\}$ | **10,0000** | 1 | $\{P_1, P_2, P_3, P_4, P_5, P_6\}$ |

---

### 3.7 Pemotongan Dendrogram ($K=2$)

Untuk mendapatkan $K=2$ klaster, dilakukan pemotongan garis horizontal (*cut-off threshold*) $h$ pada ketinggian:
$$2,2361 < h < 10,0000 \quad (\text{misal dipilih } h = 5,0)$$

Hasil pemotongan menghasilkan 2 klaster:
- **Klaster 1:** $\{P_1, P_2, P_3\}$
- **Klaster 2:** $\{P_4, P_5, P_6\}$

> **Perbandingan Antar-Metode Linkage:**  
> Baik menggunakan Single Linkage, Complete Linkage ($d_{\max} = 15,8114$), maupun Average Linkage ($d_{\text{avg}} = 13,0410$), pemotongan pada $K=2$ menghasilkan pembagian objek yang **100% konsisten dan identik**.

---

## 4. PANDUAN MENGGAMBAR GRAFIK DI KERTAS FOLIO

Saat menyalin ke kertas bergaris/folio, buatlah 2 gambar berikut menggunakan penggaris dan pensil/pulpen warna:

### 4.1 Grafik 1: Scatter Plot 2D K-Means & Posisi Centroid

- **Sumbu Horizontal ($X$):** Jumlah Kunjungan (skala 0 s/d 16, kelipatan 2).
- **Sumbu Vertikal ($Y$):** Belanja Ternormalisasi (skala 0 s/d 11, kelipatan 1).

```text
Belanja (X2)
  ^
10|                                              ● P6 (15, 10)
 9|                                      ● P5 (14, 9)
 8|                              ● P4 (12, 8)
 7|
 6|                     [KLASTER 2: TINGGI]
 5|                              ▲ C2 (13.67, 9.0)
 4|
 3|
 2|          ● P3 (4, 2)
 1|    ● P1 (2, 1)   [KLASTER 1: RENDAH]
  |       ▲ C1 = P2 (3, 1.5)
 0+----+----+----+----+----+----+----+----+----+--> Kunjungan (X1)
  0    2    4    6    8    10   12   14   16
```

**Keterangan Gambar di Folio:**
- Titik Bulat (●): Posisi objek pelanggan ($P_1$ s/d $P_6$).
- Segitiga / Tanda Silang (▲): Titik Centroid akhir ($C_1$ dan $C_2$).
- Berikan arsiran atau lingkaran garis putus-putus untuk membatasi kelompok Klaster 1 dan Klaster 2.

---

### 4.2 Grafik 2: Dendrogram Agglomerative Clustering

- **Sumbu Vertikal ($Y$):** Ketinggian Jarak Penggabungan ($d$).
- **Sumbu Horizontal ($X$):** Objek data ($P_1, P_2, P_3, P_4, P_5, P_6$).

```text
Jarak (d)
  ^
10|---------------------------+ (d = 10.0000)
  |                           |
 8|                           |
  |                           |  - - - - - - Garis Potong h = 5.0 (K = 2)
 6|                           |
  |                           |
 4|                           |
  |                           +-------+ (d = 2.2361)
 2|             +-------+     |       |
  |     +---+   |       |     |   +---+ (d = 1.4142)
  |     |   |   | (d=1.1180)  |   |   |
 0+-----+---+---+-------------+---+---+---> Objek
       P1  P2  P3            P4  P5  P6
        \_____/               \_____/
        Klaster 1             Klaster 2
```

---

## 5. KESIMPULAN & INTERPRETASI BISNIS

Berdasarkan perhitungan lengkap menggunakan **K-Means Clustering** dan **Hierarchical Agglomerative Clustering (HAC)**:

1. **Konsistensi Hasil Kedua Algoritma:**
   Kedua algoritma menghasilkan partisi kelompok yang identik sempurna:
   - **Klaster 1:** Pelanggan $\{P_1, P_2, P_3\}$
   - **Klaster 2:** Pelanggan $\{P_4, P_5, P_6\}$

2. **Profil Karakteristik Klaster:**
   - **Klaster 1 (Pelanggan Segmen Ekonomis / Frekuensi Rendah):**  
     Memiliki rata-rata kunjungan $3$ kali/bulan dan rata-rata belanja Rp $150.000$/bulan. Karakteristik: berbelanja kebutuhan pokok insidental dalam jumlah sedikit.
   - **Klaster 2 (Pelanggan Segmen Loyal / Frekuensi & Belanja Tinggi):**  
     Memiliki rata-rata kunjungan $13,67$ kali/bulan dan rata-rata belanja Rp $900.000$/bulan. Karakteristik: pelanggan rutin mingguan/harian dengan nilai transaksi besar.

3. **Implikasi Pengambilan Keputusan (Bisnis Minimarket):**
   - **Untuk Klaster 1:** Diberikan program kupon potongan harga atau promosi *bundling* produk hemat untuk mendorong frekuensi belanja.
   - **Untuk Klaster 2:** Diberikan program loyalitas (*member VIP*), fasilitas *cashback*, dan penawaran produk premium untuk mempertahankan retensi pelanggan.
