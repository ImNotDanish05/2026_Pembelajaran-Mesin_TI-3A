# Modul Pembelajaran Mandiri: Distance Metric & K-Nearest Neighbors (K-NN)
> **Topik:** Klasifikasi & Regresi K-NN, Metrik Jarak, Normalisasi Skala, Evaluasi Model, Perhitungan Manual Bertingkat, dan Praktikum Python  
> **Karakteristik Pembelajaran:** Setiap perhitungan manual diverifikasi secara numerik dan wajib identik dengan implementasi Python (`scikit-learn`).

---

## 📋 Daftar Isi & Peta Pembelajaran

- [1. Panduan & Jalur Belajar Mahasiswa](#1-panduan--jalur-belajar-mahasiswa)
- [2. Konsep Intuitif & Alur Kerja K-NN](#2-konsep-intuitif--alur-kerja-k-nn)
- [3. Bab A — Konsep Dasar & Metrik Jarak](#3-bab-a--konsep-dasar--metrik-jarak)
  - [3.1 Euclidean Distance](#31-euclidean-distance)
  - [3.2 Manhattan Distance](#32-manhattan-distance)
  - [3.3 Minkowski Distance](#33-minkowski-distance)
  - [3.4 Hamming Distance](#34-hamming-distance)
- [4. Bab B — K-NN untuk Klasifikasi](#4-bab-b--k-nn-untuk-klasifikasi)
  - [4.1 Mekanisme Majority Voting (Contoh Induk)](#41-mekanisme-majority-voting-contoh-induk)
  - [4.2 Pengaruh Pemilihan Nilai K](#42-pengaruh-pemilihan-nilai-k)
  - [4.3 Weighted K-NN (Voting Berbobot Jarak)](#43-weighted-k-nn-voting-berbobot-jarak)
- [5. Bab C — K-NN untuk Regresi](#5-bab-c--k-nn-untuk-regresi)
  - [5.1 Prediksi Kontinu dengan Rerata Tetangga](#51-prediksi-kontinu-dengan-rerata-tetangga)
  - [5.2 Weighted K-NN Regression](#52-weighted-k-nn-regression)
- [6. Bab D — Normalisasi Fitur & Evaluasi Model](#6-bab-d--normalisasi-fitur--evaluasi-model)
  - [6.1 Urgensi Normalisasi (Min-Max vs StandardScaler)](#61-urgensi-normalisasi-min-max-vs-standardscaler)
  - [6.2 Aturan Anti-Kebocoran Data (Data Leakage)](#62-aturan-anti-kebocoran-data-data-leakage)
  - [6.3 Evaluasi Klasifikasi (Confusion Matrix & F1-Score)](#63-evaluasi-klasifikasi-confusion-matrix--f1-score)
  - [6.4 Evaluasi Regresi (MAE, MSE, RMSE, R²)](#64-evaluasi-regresi-mae-mse-rmse-r)
- [7. Bab E — Praktikum Python](#7-bab-e--praktikum-python)
- [8. Bab F — Latihan Bertingkat & Rubrik Penilaian Induk](#8-bab-f--latihan-bertingkat--rubrik-penilaian-induk)
- [9. Bab G — Kasus Terpadu & Metodologi Penelitian Sahih](#9-bab-g--kasus-terpadu--metodologi-penelitian-sahih)
- [10. Bab H — Pengayaan Akademis & Glosarium](#10-bab-h--pengayaan-akademis--glosarium)
- [11. Bab I — Latihan Berbimbing Skala Besar (N = 24)](#11-bab-i--latihan-berbimbing-skala-besar-n--24)
- [12. Bab J — TUGAS MANDIRI MAHASISWA (WAJIB)](#12-bab-j--tugas-mandiri-mahasiswa-wajib)
  - [📌 Tugas 1: KM — Klasifikasi Kenyamanan Ruangan ($N=24$)](#-tugas-1-km--klasifikasi-kenyamanan-ruangan-n24)
  - [📌 Tugas 2: RM — Regresi Konsumsi Energi Lab ($N=24$)](#-tugas-2-rm--regresi-konsumsi-energi-lab-n24)
  - [📌 Tugas 3: Mini-Proyek Terpandu](#-tugas-3-mini-proyek-terpandu)
  - [⚖️ Standar Penilaian & Rubrik Operasional](#️-standar-penilaian--rubrik-operasional)

---

## 1. Panduan & Jalur Belajar Mahasiswa

Modul ini dirancang bertingkat dengan alokasi setara 6 jam tatap muka + tugas mandiri:

| Jalur | Cakupan Materi | Target & Status |
| :--- | :--- | :--- |
| **Jalur Minimal** *(Syarat Kelulusan)* | Bab A–D (Konsep jarak, 1 contoh klasifikasi, 1 contoh regresi, scaling, evaluasi) + Praktikum Bab E. | **Wajib bagi seluruh mahasiswa.** |
| **Jalur Lengkap** *(Target Nilai Unggul)* | Jalur Minimal + Bab G (Kasus komprehensif, regresi multi-fitur, pipeline anti-leakage) + **Bab J (Tugas Mandiri KM & RM)** + Mini-Proyek. | **Wajib untuk penguasaan mandiri dan portofolio.** |

> [!IMPORTANT]
> **Prinsip Utama Modul:**
> 1. Setiap angka perhitungan manual **harus cocok persis** dengan luaran Python `scikit-learn`.
> 2. **Aturan Seri (Tie-Breaking):** Apabila terdapat dua titik atau lebih dengan jarak yang sama persis, urutan prioritas **wajib** diselesaikan menurut urutan alfabetis ID titik ($A, B, C, \dots$). Mengabaikan aturan seri berakibat pengurangan nilai **20%**.

---

## 2. Konsep Intuitif & Alur Kerja K-NN

Algoritma **K-Nearest Neighbors (K-NN)** didasarkan pada prinsip kemiripan: *objek yang memiliki atribut serupa akan saling berdekatan dalam ruang fitur*.

```
[Data Latih] ──► [Normalisasi / Scaling] ──► [Hitung Jarak ke Query]
                                                       │
                                                       ▼
[Prediksi Akhir] ◄── [Voting / Rerata] ◄── [Ambil K Terdekat] ◄── [Urutkan Jarak]
```

### 3 Kata Kunci Utama:
1. **Query ($Q$ atau $Z$):** Titik data baru yang nilai targetnya belum diketahui dan ingin diprediksi.
2. **Tetangga (Neighbors):** Titik-titik data latih yang memiliki jarak geometris terkecil terhadap query.
3. **Nilai $K$:** Parameter jumlah tetangga terdekat yang dilibatkan dalam pengambilan keputusan (*voting* untuk klasifikasi, *rerata* untuk regresi).

> [!NOTE]
> Jarak bukanlah probabilitas. Jarak mengukur ketidakmiripan (*dissimilarity*) antar titik menurut metrik matematis yang dipilih.

---

## 3. Bab A — Konsep Dasar & Metrik Jarak

Misalkan terdapat dua titik dalam ruang 2 dimensi: $P_1 = (x_1, y_1)$ dan $P_2 = (x_2, y_2)$.

### 3.1 Euclidean Distance
Jarak garis lurus (hipotenusa) antara dua titik dalam ruang Euclidean:
$$d_{\text{Euclidean}}(P_1, P_2) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

Untuk dimensi $n$:
$$d(P_1, P_2) = \sqrt{\sum_{i=1}^n (x_{2i} - x_{1i})^2}$$

*Contoh Manual:*  
Titik $A = (1, 1)$ dan $B = (5, 4)$:  
$$\Delta x = 5 - 1 = 4, \quad \Delta y = 4 - 1 = 3$$  
$$s = 4^2 + 3^2 = 16 + 9 = 25 \implies d = \sqrt{25} = 5$$

---

### 3.2 Manhattan Distance (City Block / $L_1$ Norm)
Jarak lintasan tegak lurus (hanya bergerak horizontal dan vertikal seperti blok jalan kota):
$$d_{\text{Manhattan}}(P_1, P_2) = |x_2 - x_1| + |y_2 - y_1|$$

Untuk dimensi $n$:
$$d(P_1, P_2) = \sum_{i=1}^n |x_{2i} - x_{1i}|$$

*Contoh Manual:*  
Titik $A = (1, 1)$ dan $B = (5, 4)$:  
$$d_{\text{Manhattan}} = |5 - 1| + |4 - 1| = 4 + 3 = 7$$

---

### 3.3 Minkowski Distance (Generalisasi $L_p$ Norm)
Bentuk umum keluarga metrik jarak parametrik $p \ge 1$:
$$d_{\text{Minkowski}}(P_1, P_2) = \left( \sum_{i=1}^n |x_{2i} - x_{1i}|^p \right)^{1/p}$$
- Jika $p = 1$, menjadi **Manhattan Distance**.
- Jika $p = 2$, menjadi **Euclidean Distance**.
- Jika $p \to \infty$, menjadi **Chebyshev Distance** ($\max_i |x_{2i} - x_{1i}|$).

---

### 3.4 Hamming Distance
Digunakan khusus untuk data kategorikal, biner, atau teks/string dengan panjang sama: menghitung berapa banyak posisi fitur yang berbeda.
$$d_{\text{Hamming}}(u, v) = \sum_{i=1}^n \mathbb{I}(u_i \ne v_i)$$

*Contoh:*  
Vektor fitur biner $u = [1, 0, 1, 1]$ dan $v = [1, 1, 0, 1]$.  
Perbedaan ada pada indeks ke-2 dan ke-3 $\implies d_{\text{Hamming}} = 2$.

---

## 4. Bab B — K-NN untuk Klasifikasi

### 4.1 Mekanisme Majority Voting (Contoh Induk)

Diberikan dataset latih 6 titik dan 1 titik query $P(4, 4)$:

| ID | $x_1$ | $x_2$ | Kelas Aktual |
| :---: | :---: | :---: | :---: |
| **A** | 1 | 1 | Tidak |
| **B** | 2 | 1 | Tidak |
| **C** | 1 | 3 | Tidak |
| **D** | 3 | 3 | Ya |
| **E** | 5 | 5 | Ya |
| **F** | 4 | 5 | Ya |
| **$P$ (Query)** | **4** | **4** | **?** |

#### Langkah 1: Hitung Jarak Euclidean ke Query $P(4, 4)$
Gunakan nilai jumlah kuadrat selisih ($s = \Delta x_1^2 + \Delta x_2^2$) agar efisien:
- Titik A: $(1-4)^2 + (1-4)^2 = (-3)^2 + (-3)^2 = 9 + 9 = 18 \implies d = \sqrt{18} \approx 4.243$
- Titik B: $(2-4)^2 + (1-4)^2 = (-2)^2 + (-3)^2 = 4 + 9 = 13 \implies d = \sqrt{13} \approx 3.606$
- Titik C: $(1-4)^2 + (3-4)^2 = (-3)^2 + (-1)^2 = 9 + 1 = 10 \implies d = \sqrt{10} \approx 3.162$
- Titik D: $(3-4)^2 + (3-4)^2 = (-1)^2 + (-1)^2 = 1 + 1 = 2 \implies d = \sqrt{2} \approx 1.414$
- Titik E: $(5-4)^2 + (5-4)^2 = 1^2 + 1^2 = 1 + 1 = 2 \implies d = \sqrt{2} \approx 1.414$
- Titik F: $(4-4)^2 + (5-4)^2 = 0^2 + 1^2 = 0 + 1 = 1 \implies d = \sqrt{1} = 1.000$

#### Langkah 2: Urutkan Tetangga (Terapkan Aturan Seri Alfabetis)
Titik D dan E sama-sama memiliki $s = 2$ ($d \approx 1.414$). Urutkan berdasarkan ID: **D sebelum E**.

| Peringkat | ID | $s$ | Jarak ($d$) | Kelas | Status Tetangga |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | **F** | 1 | 1.000 | **Ya** | Terpilih ($K=1, 3, 5$) |
| **2** | **D** | 2 | 1.414 | **Ya** | Terpilih ($K=3, 5$) |
| **3** | **E** | 2 | 1.414 | **Ya** | Terpilih ($K=3, 5$) |
| **4** | **C** | 10 | 3.162 | Tidak | Terpilih ($K=5$) |
| **5** | **B** | 13 | 3.606 | Tidak | Terpilih ($K=5$) |
| **6** | **A** | 18 | 4.243 | Tidak | Di luar $K=5$ |

#### Langkah 3: Ambil Keputusan Voting
- **Untuk $K = 1$:** Tetangga terdekat = {F} $\implies$ Prediksi: **Ya**.
- **Untuk $K = 3$:** 3 Tetangga terdekat = {F (Ya), D (Ya), E (Ya)} $\implies$ Voting: 3 Ya vs 0 Tidak $\implies$ Prediksi: **Ya**.
- **Untuk $K = 5$:** 5 Tetangga terdekat = {F (Ya), D (Ya), E (Ya), C (Tidak), B (Tidak)} $\implies$ Voting: 3 Ya vs 2 Tidak $\implies$ Prediksi: **Ya**.

---

### 4.2 Pengaruh Pemilihan Nilai K

| Nilai $K$ | Karakteristik Batas Keputusan | Potensi Masalah | Rekomendasi Praktis |
| :--- | :--- | :--- | :--- |
| **$K = 1$** (Terlalu Kecil) | Batas keputusan sangat rumit & bergerigi (*complex/flexible boundary*). | Sangat rentan terhadap noise/outlier (**Overfitting**, High Variance). | Hindari kecuali dataset sangat bersih dan bebas noise. |
| **$K$ Moderat (Optimal)** | Batas keputusan mulus dan menangkap pola umum data. | Keseimbangan bias dan variansi terbaik. | Dicari melalui validasi silang (Cross-Validation). |
| **$K$ Terlalu Besar** ($K \to N$) | Batas keputusan sangat datar (*over-smoothed*). | Mengabaikan pola lokal (**Underfitting**, High Bias). | Selalu pilih $K \ll N$ dan pilih bilangan ganjil untuk klasifikasi biner. |

---

### 4.3 Weighted K-NN (Voting Berbobot Jarak)

Pada majority voting biasa (*uniform*), tetangga yang sangat dekat memiliki bobot suara yang sama persis dengan tetangga yang jauh di pinggir batas $K$.  
Pada **Weighted K-NN**, tetangga yang lebih dekat diberikan bobot suara lebih besar:
$$w_i = \frac{1}{d_i} \quad \text{atau} \quad w_i = \frac{1}{d_i^2}$$
*(Catatan: jika $d_i = 0$, tetangga tersebut langsung menentukan kelas dengan bobot tak hingga).*

**Perhitungan Skor Kelas $c$:**
$$\text{Score}(c) = \sum_{i \in \text{Top-K}, y_i = c} w_i$$

*Contoh Kasus:* $K = 3$, tetangga berjarak $d = [1, 2, 4]$ dengan kelas $[A, B, B]$.
- Voting Biasa: Kelas A = 1 suara, Kelas B = 2 suara $\implies$ **Menang Kelas B**.
- Weighted Voting ($w = 1/d$):
  - $w_A = \frac{1}{1} = 1.0$
  - $w_B = \frac{1}{2} + \frac{1}{4} = 0.5 + 0.25 = 0.75$
  - Karena $w_A (1.0) > w_B (0.75)$, maka **Menang Kelas A**!  
  *(Terbukti bobot jarak mampu membalik hasil voting jika tetangga terdekat sangat dominan).*

---

## 5. Bab C — K-NN untuk Regresi

### 5.1 Prediksi Kontinu dengan Rerata Tetangga

Pada permasalahan regresi, target $y$ berupa bilangan riil kontinu. Prediksi untuk query $x_q$ dihitung dari rata-rata nilai target $K$ tetangga terdekat:
$$\hat{y}(x_q) = \frac{1}{K} \sum_{i=1}^K y_i$$

*Contoh Manual (Durasi Penggunaan vs Konsumsi Energi Wh):*

| ID | Durasi Jam ($x$) | Energi Wh ($y$) |
| :---: | :---: | :---: |
| A | 1 | 20 |
| B | 2 | 24 |
| C | 3 | 28 |
| D | 5 | 36 |
| E | 6 | 40 |

Query $x_q = 4$ jam. Jarak 1D dihitung menggunakan selisih absolut $|x_i - x_q|$:
- $|1 - 4| = 3$
- $|2 - 4| = 2$
- $|3 - 4| = 1$ (Tetangga 1, ID C)
- $|5 - 4| = 1$ (Tetangga 2, ID D, seri dengan C diurutkan alfabetis)
- $|6 - 4| = 2$ (Tetangga 3, ID B seri dengan E: B dipilih karena alfabetis lebih awal)

Tiga tetangga terdekat untuk $K = 3$ adalah **C ($y=28$), D ($y=36$), dan B ($y=24$)**:
$$\hat{y} = \frac{28 + 36 + 24}{3} = \frac{88}{3} \approx 29.333 \text{ Wh}$$

---

### 5.2 Weighted K-NN Regression
Prediksi dihitung menggunakan rata-rata tertimbang (*weighted average*):
$$\hat{y}(x_q) = \frac{\sum_{i=1}^K w_i \cdot y_i}{\sum_{i=1}^K w_i}, \quad \text{dengan } w_i = \frac{1}{d_i}$$

---

## 6. Bab D — Normalisasi Fitur & Evaluasi Model

### 6.1 Urgensi Normalisasi (Min-Max vs StandardScaler)

> [!WARNING]
> **Dominasi Skala Fitur:**  
> K-NN menghitung jarak geometris. Jika Fitur 1 bernilai ratusan (misal: Luas Tanah 50–500 m²) dan Fitur 2 bernilai satuan (misal: Jumlah Kamar 1–5), selisih Fitur 1 akan mendominasi perhitungan jarak hingga 99%, membuat Fitur 2 seolah-olah tidak ada!

#### 1. Min-Max Scaling (Normalisasi ke Rentang $[0, 1]$)
$$x' = \frac{x - x_{\min}}{x_{\max} - x_{\min}}$$

#### 2. Standard Scaling (Z-Score Standardization: $\mu = 0, \sigma = 1$)
$$z = \frac{x - \mu}{\sigma}$$

---

### 6.2 Aturan Anti-Kebocoran Data (Data Leakage)

> [!CAUTION]
> **ATURAN EMAS SCALING:**  
> Parameter scaling ($x_{\min}, x_{\max}, \mu, \sigma$) **HANYA** boleh dihitung (*fit*) menggunakan **Data Latih (Training Set)**!  
> Kemudian transformasi (*transform*) diterapkan ke data latih, data uji (test set), maupun query baru.  
> Melakukan `fit` pada seluruh dataset sebelum split = **Kebocoran Data Fatal (Data Leakage)** yang membatalkan validitas riset!

---

### 6.3 Evaluasi Klasifikasi (Confusion Matrix & F1-Score)

| | Prediksi Positif (1) | Prediksi Negatif (0) |
| :--- | :---: | :---: |
| **Aktual Positif (1)** | **True Positive (TP)** | **False Negative (FN)** |
| **Aktual Negatif (0)** | **False Positive (FP)** | **True Negative (TN)** |

1. **Akurasi (Accuracy):**
   $$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$
2. **Presisi (Precision):**
   $$\text{Precision} = \frac{TP}{TP + FP}$$
3. **Recall / Sensitivitas:**
   $$\text{Recall} = \frac{TP}{TP + FN}$$
4. **Spesifisitas (Specificity):**
   $$\text{Specificity} = \frac{TN}{TN + FP}$$
5. **F1-Score (Harmonic Mean):**
   $$F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

---

### 6.4 Evaluasi Regresi (MAE, MSE, RMSE, R²)

1. **Mean Absolute Error (MAE):**
   $$\text{MAE} = \frac{1}{n} \sum_{i=1}^n |y_i - \hat{y}_i|$$
2. **Mean Squared Error (MSE):**
   $$\text{MSE} = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2$$
3. **Root Mean Squared Error (RMSE):**
   $$\text{RMSE} = \sqrt{\text{MSE}}$$
4. **Koefisien Determinasi ($R^2$):**
   $$R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}$$

---

## 7. Bab E — Praktikum Python

Kode berikut merupakan implementasi acuan menggunakan `scikit-learn`:

```python
import numpy as np
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, cross_val_score

# 1. Verifikasi Manual Klasifikasi Contoh Induk
X_train = np.array([[1, 1], [2, 1], [1, 3], [3, 3], [5, 5], [4, 5]])
y_train = np.array(['Tidak', 'Tidak', 'Tidak', 'Ya', 'Ya', 'Ya'])
query = np.array([[4, 4]])

knn = KNeighborsClassifier(n_neighbors=3, metric='euclidean')
knn.fit(X_train, y_train)
pred = knn.predict(query)
print("Prediksi K=3 Query P(4,4):", pred[0]) # Output: Ya

# 2. Pipeline Anti-Leakage (Scaling + KNN)
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier(n_neighbors=5))
])
# pipe.fit(X_train, y_train)
```

---

## 8. Bab F — Latihan Bertingkat & Rubrik Penilaian Induk

### 8.1 Latihan Bertingkat
- **Tingkat 1 (Dasar):**
  - Titik $A(0,0)$ dan $B(3,4)$. Hitung jarak Euclidean dan Manhattan! (Rambu: pola segitiga 3-4-5).
  - Jelaskan perbedaan mendasar klasifikasi (label diskrit) vs regresi (bilangan kontinu) pada K-NN!
- **Tingkat 2 (Menengah):**
  - Diberikan data $A(1,1, \text{Tidak}), B(2,2, \text{Tidak}), C(5,5, \text{Ya}), D(6,5, \text{Ya})$ dan Query $P(4,4)$. Hitung Euclidean, tentukan urutan, dan klasifikasikan untuk $K=1$ dan $K=3$!
- **Tingkat 3 (Lanjutan):**
  - Tunjukkan pergeseran urutan tetangga sebelum vs sesudah Min-Max Scaling pada dataset dua fitur dengan rentang beda.
  - Simulasikan kurva Bias-Variance berbentuk huruf U saat $K$ bergerak dari 1 hingga 25.

### 8.2 Rubrik Penilaian Induk (Tabel 9)

| Aspek Penilaian | Bobot | Indikator Kinerja |
| :--- | :---: | :--- |
| **1. Ketepatan Perhitungan Manual** | **35%** | Penulisan rumus lengkap, substitusi nilai per baris ($s$ dan $d$), penyusunan tabel urutan peringkat dengan aturan seri, serta ketepatan hasil voting/rerata. |
| **2. Grafik & Visualisasi** | **20%** | Kelengkapan sumbu berlabel, legenda simbol kelas, penanda query yang jelas, batas plot proporsional, serta penerapan aturan label hanya untuk tetangga terdekat pada $N > 20$. |
| **3. Program & Evaluasi** | **30%** | Kode Python tereksekusi tanpa galat, pipeline preprocessing bebas leakage, evaluasi metrik lengkap, dan verifikasi bahwa luaran Python identik dengan manual. |
| **4. Laporan Akademik & Interpretasi** | **15%** | Transparansi metodologi (aturan tie-breaking, metrik jarak, nilai $K$), analisis trade-off, pembahasan keterbatasan model, dan kejujuran ilmiah. |

---

## 9. Bab G — Kasus Terpadu & Metodologi Penelitian Sahih

### Kasus Klasifikasi Rumah: Dampak Nyata Scaling

| ID | Luas ($m^2$) | Kamar | Kategori | Jarak Tanpa Scaling ($d_{\text{raw}}$) | Peringkat Asli | Jarak Standardized ($d_{\text{std}}$) | Peringkat Scaled |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| A | 40 | 1 | Kecil | 15.033 | 4 | 2.054 | 4 |
| B | 45 | 1 | Kecil | 10.050 | 3 | 1.701 | 3 |
| C | 50 | 2 | Kecil | 5.000 | **1** | 0.589 | **1** |
| D | 65 | 2 | Besar | 10.000 | **2** | 0.471 | **2** |
| E | 70 | 3 | Besar | 15.033 | 5 | 1.520 | 5 |
| F | 80 | 3 | Besar | 25.020 | 6 | 2.224 | 6 |

> [!NOTE]
> Perhatikan bahwa pada skala asli, fitur Luas (puluhan) mendominasi Kamar (satuan). Normalisasi merestorasi bobot geometris yang adil bagi setiap fitur.

---

## 10. Bab H — Pengayaan Akademis & Glosarium

1. **Curse of Dimensionality:** Semakin tinggi dimensi ruang fitur ($D$), volume ruang berkembang secara eksponensial sehingga semua titik data menjadi saling berjauhan, mengakibatkan metrik jarak kehilangan daya diskriminatifnya.
2. **Lazy Learner (Instance-Based Learning):** K-NN tidak membangun model eksplisit selama fase *training* ($\mathcal{O}(1)$). Beban komputasi seluruhnya bergeser ke fase *testing/inferensi* ($\mathcal{O}(N \cdot D)$).
3. **K Ganjil vs Genap:** Memilih $K$ ganjil pada klasifikasi biner mencegah kebuntuan suara (*tie vote*).

---

## 11. Bab I — Latihan Berbimbing Skala Besar (N = 24)

### Strategi Praktis untuk Data Besar ($N = 24$):
Untuk menghitung 24 baris tanpa kalkulator saintifik yang melelahkan:
1. Hitung selisih $\Delta x$ dan $\Delta y$.
2. Hitung jumlah kuadrat $s = \Delta x^2 + \Delta y^2$.
3. **Gunakan nilai $s$ untuk mengurutkan tetangga!** Karena fungsi $f(s) = \sqrt{s}$ monoton naik, urutan berdasarkan $s$ dijamin identik dengan urutan berdasarkan $d = \sqrt{s}$. Kita cukup menarik akar untuk beberapa kandidat tetangga teratas ($K$).

---

## 12. Bab J — TUGAS MANDIRI MAHASISWA (WAJIB)

> [!IMPORTANT]
> ### 🎯 PANDUAN PENGERJAAN TUGAS MANDIRI
> Bagian ini memuat tugas individu mahasiswa. Mahasiswa **WAJIB** menyelesaikan kedua tugas ($KM$ dan $RM$) secara mandiri dengan mengikuti sistematika baku 6 tahap:
> 1. **Tahap 1 — Rumus:** Tuliskan rumus metrik jarak yang digunakan secara eksplisit.
> 2. **Tahap 2 — Substitusi Nilai 24 Baris:** Hitung nilai selisih $\Delta x, \Delta y$, nilai jumlah kuadrat $s$, dan jarak $d$ untuk seluruh 24 titik.
> 3. **Tahap 3 — Tabel Peringkat 24 Baris:** Susun tabel urutan jarak 1 s/d 24 dari terkecil ke terbesar. Jika ada jarak kembar ($s$ sama), **wajib** terapkan aturan alfabetis ID titik.
> 4. **Tahap 4 — Voting / Rerata:** Lakukan prediksi untuk variasi $K = 3, 5, 7$ (unweighted dan distance-weighted).
> 5. **Tahap 5 — Visualisasi Scatter Plot:** Buat grafik sebaran data. Terapkan aturan visualisasi $N > 20$: *cantumkan label teks ID hanya pada titik query dan 7 tetangga terdekat agar grafik tetap bersih dan informatif*.
> 6. **Tahap 6 — Interpretasi & Verifikasi Python:** Berikan penjelasan ilmiah atas keputusan model dan sertakan kode Python pembukti yang menghasilkan angka identik.

---

### 📌 Tugas 1: KM — Klasifikasi Kenyamanan Ruangan ($N=24$)

#### 1. Deskripsi Masalah
- **Fitur $x$:** Indeks suhu ruangan (skala 0–10)
- **Fitur $y$:** Indeks kelembapan ruangan (skala 0–10)
- **Kelas:** `Gerah` (kondisi tidak nyaman, AC/kipas perlu dinyalakan) vs `Nyaman` (kondisi ruangan optimal)
- **Titik Query $Z$:** $(x_q = 6, y_q = 4)$

#### 2. Dataset Lengkap (Tabel 20)

| ID | $x$ (Suhu) | $y$ (Kelembapan) | Kelas Aktual |
| :---: | :---: | :---: | :---: |
| **A** | 1 | 2 | Gerah |
| **B** | 2 | 1 | Gerah |
| **C** | 2 | 3 | Gerah |
| **D** | 3 | 2 | Gerah |
| **E** | 1 | 5 | Gerah |
| **F** | 5 | 1 | Gerah |
| **G** | 3 | 5 | Gerah |
| **H** | 5 | 3 | Gerah |
| **I** | 2 | 6 | Gerah |
| **J** | 6 | 2 | Gerah |
| **K** | 4 | 5 | Gerah |
| **L** | 5 | 4 | Gerah |
| **M** | 7 | 6 | Nyaman |
| **N** | 8 | 5 | Nyaman |
| **O** | 6 | 7 | Nyaman |
| **P** | 7 | 8 | Nyaman |
| **Q** | 8 | 7 | Nyaman |
| **R** | 8 | 8 | Nyaman |
| **S** | 9 | 7 | Nyaman |
| **T** | 7 | 5 | Nyaman |
| **U** | 6 | 6 | Nyaman |
| **V** | 9 | 6 | Nyaman |
| **W** | 8 | 6 | Nyaman |
| **X** | 7 | 7 | Nyaman |
| **$Z$ (Query)** | **6** | **4** | **? (Prediksi)** |

#### 3. Instruksi Pengerjaan Spesifik Mahasiswa
1. Hitung jarak seluruh 24 titik ke Query $Z(6, 4)$ dengan $d = \sqrt{(x-6)^2 + (y-4)^2}$.
2. Nilai $s$ yang akan muncul adalah: $1, 2, 4, 5, 8, 9, 10, 13, 17, 18, 20, 25, 26, 29$.
3. Perhatikan kasus seri pada $s = 2, 4, 5, 10, 13, 17, 20$: selesaikan dengan urutan alfabetis!
4. Tentukan hasil voting kelas untuk $K = 3, 5, 7$.
5. Hitung Weighted Voting ($w = 1/d$) untuk $K = 3$.
6. Verifikasi manual Anda dengan kode Python.

#### 4. Kunci Validasi Akhir (Tabel Kunci J)
- **Top 7 Tetangga:**
  1. Rank 1: **L** ($s=1, d=1.0000$, Gerah)
  2. Rank 2: **H** ($s=2, d=1.4142$, Gerah) *(seri dengan T, H menang alfabet)*
  3. Rank 3: **T** ($s=2, d=1.4142$, Nyaman)
  4. Rank 4: **J** ($s=4, d=2.0000$, Gerah) *(seri dengan U, J menang alfabet)*
  5. Rank 5: **U** ($s=4, d=2.0000$, Nyaman)
  6. Rank 6: **K** ($s=5, d=2.2361$, Gerah) *(seri dengan M dan N, K menang alfabet)*
  7. Rank 7: **M** ($s=5, d=2.2361$, Nyaman) *(seri dengan N, M menang alfabet)*
- **Keputusan:**
  - $K=3$: Gerah (2 suara: L, H) vs Nyaman (1 suara: T) $\implies$ **Gerah**
  - $K=5$: Gerah (3 suara: L, H, J) vs Nyaman (2 suara: T, U) $\implies$ **Gerah**
  - $K=7$: Gerah (4 suara: L, H, J, K) vs Nyaman (3 suara: T, U, M) $\implies$ **Gerah**
  - **Weighted $K=3$:** Gerah ($1.0 + 0.7071 = 1.7071$) vs Nyaman ($0.7071$) $\implies$ **Gerah**

---

### 📌 Tugas 2: RM — Regresi Konsumsi Energi Lab ($N=24$)

#### 1. Deskripsi Masalah
- **Fitur $x$:** Durasi operasional laboratorium dalam jam (skala 1–8)
- **Fitur $y$:** Jumlah unit perangkat aktif (skala 1–4)
- **Target kontinu:** Estimasi konsumsi energi listrik (kWh)
- **Titik Query $Z$:** $(x_q = 5.5, y_q = 2.5)$

#### 2. Dataset Lengkap (Tabel 21)

| ID | Jam ($x$) | Perangkat ($y$) | Energi Listrik (kWh) |
| :---: | :---: | :---: | :---: |
| **A** | 2 | 1 | 35 |
| **B** | 3 | 1 | 45 |
| **C** | 4 | 1 | 55 |
| **D** | 5 | 1 | 65 |
| **E** | 6 | 1 | 75 |
| **F** | 7 | 1 | 85 |
| **G** | 2 | 2 | 45 |
| **H** | 3 | 2 | 55 |
| **I** | 4 | 2 | 65 |
| **J** | 5 | 2 | 75 |
| **K** | 6 | 2 | 85 |
| **L** | 7 | 2 | 95 |
| **M** | 2 | 3 | 55 |
| **N** | 3 | 3 | 65 |
| **O** | 4 | 3 | 75 |
| **P** | 6 | 3 | 95 |
| **Q** | 7 | 3 | 105 |
| **R** | 8 | 3 | 115 |
| **S** | 3 | 4 | 75 |
| **T** | 4 | 4 | 85 |
| **U** | 5 | 4 | 95 |
| **V** | 6 | 4 | 105 |
| **W** | 7 | 4 | 115 |
| **X** | 8 | 4 | 125 |
| **$Z$ (Query)** | **5.5** | **2.5** | **? (Prediksi)** |

#### 3. Instruksi Pengerjaan Spesifik Mahasiswa
1. Hitung jarak seluruh 24 titik ke Query $Z(5.5, 2.5)$ dengan $d = \sqrt{(x-5.5)^2 + (y-2.5)^2}$.
2. Perhatikan bahwa nilai $s$ memiliki pecahan kelipatan $0.5$ (misalnya: $0.50, 2.50, 4.50$). Jangan dibulatkan secara kasar sebelum pengurutan!
3. Tiga tetangga terdekat memiliki jarak yang sama persis ($s = 0.50, d \approx 0.7071$). Buktikan bahwa untuk $K=3$, hasil prediksi *uniform* dan *distance-weighted* adalah **identik**!
4. Hitung prediksi untuk $K = 3, 5, 7$ baik menggunakan rerata biasa (*uniform*) maupun rerata tertimbang (*distance-weighted*).
5. Jelaskan secara analitis mengapa pada $K = 5$ dan $K = 7$ prediksi berbobot menghasilkan nilai yang lebih tinggi daripada rerata biasa!

#### 4. Kunci Validasi Akhir (Tabel Kunci J)
- **Trio Terdekat:** Titik **J, K, P** ($s = 0.50, d \approx 0.7071$)
- **Prediksi $K=3$:** Uniform $= \frac{75 + 85 + 95}{3} = \mathbf{85.000}$ kWh | Distance-Weighted $= \mathbf{85.000}$ kWh
- **Prediksi $K=5$:** Uniform $= \mathbf{79.000}$ kWh | Distance-Weighted $\approx \mathbf{81.555}$ kWh
- **Prediksi $K=7$:** Uniform $\approx \mathbf{79.286}$ kWh | Distance-Weighted $\approx \mathbf{81.265}$ kWh
- **Analisis:** Prediksi berbobot lebih tinggi karena 3 titik terdekat (J, K, P) yang bernilai besar mendapatkan bobot jauh lebih tinggi ($w \approx 1.4142$) dibanding tetangga lapis berikutnya ($w \approx 0.6325$).

---

### 📌 Tugas 3: Mini-Proyek Terpandu

- **Judul Proyek:** *Estimasi Konsumsi Energi Laboratorium Menggunakan K-NN Regression*
- **Komponen Luaran:**
  1. Tabel data fitur dan target.
  2. Visualisasi sebaran fitur dan query.
  3. Bukti perhitungan manual lengkap ($K=3$).
  4. Skrip Python yang menghasilkan angka identik dengan manual.
  5. Pengujian pada *test set* terpisah menggunakan pipeline anti-kebocoran data (`Pipeline([('scaler', ...), ('knn', ...)])`).
  6. Pembahasan evaluasi (MAE, RMSE, $R^2$) serta analisis keterbatasan model.

---

### ⚖️ Standar Penilaian & Rubrik Operasional

Penilaian Tugas Mandiri Bagian J dihitung menggunakan pemetaan operasional terhadap **Rubrik Induk (Tabel 9b)**:

```
Total Nilai = [Ketepatan Manual (35%)] + [Grafik & Interpretasi (20%)] + [Program & Evaluasi (30%)] + [Laporan Akademik (15%)]
```

| Komponen Operasional | Bobot Relatif | Deskripsi Penilaian |
| :--- | :---: | :--- |
| **$n_1$: Tabel Peringkat 24 Baris** | **30%** | Tabel urutan jarak lengkap dan benar dari baris 1 sampai 24. |
| **$n_2$: Substitusi Rumus $s$ dan $d$** | **25%** | Ketepatan langkah perhitungan $\Delta x, \Delta y, s = \Delta x^2 + \Delta y^2$, dan penarikan akar. |
| **$n_3$: Voting / Rerata & Weighted** | **20%** | Perhitungan suara terbanyak atau rerata tertimbang untuk $K=3, 5, 7$. |
| **$n_4$: Visualisasi Scatter Plot ($N>20$)** | **15%** | Kerapian grafik: label teks ID dicantumkan **hanya** pada titik query dan 7 tetangga terdekat. |
| **$n_{5a} + n_{5b}$: Verifikasi Python & Laporan** | **10%** | Kode Python tereksekusi tanpa error dan mencocokkan angka manual (5%), disertai pembahasan interpretasi (5%). |

> [!CAUTION]
> **PENALTI KRITIS:**  
> Jika aturan penyelesaian seri (*tie-breaking*) tidak dituliskan atau tidak diterapkan secara konsisten, total nilai tugas **langsung dipotong sebesar 20%**!

