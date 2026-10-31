# Lembar Jawaban Tugas Mandiri: Logika Fuzzy (Fuzzy Logic)
> **Mata Kuliah:** Pembelajaran Mesin  
> **Modul:** Modul 07 — Logika Fuzzy untuk Regresi dan Klasifikasi ($N = 20$)  
> **Format Penulisan:** Siap Salin untuk Lembar Kerja Kertas Folio Bergaris  
> **Karakteristik Solusi:** Dilengkapi bagian *Diketahui*, formulasi rumus eksplisit, penjabaran langkah demi langkah, tabel komputasi 20 baris lengkap, serta evaluasi metrik kinerja (MAE, RMSE, Confusion Matrix, Akurasi, Presisi, Recall, F1-Score).

---

## 📝 Format Kepala Lembar Folio (Salin di Bagian Atas Kertas)

```text
NAMA MAHASISWA : ImNotDanish05
NIM            : 
KELAS / PRODI  : TI-3A / D4 Teknik Informatika
MATA KULIAH    : Pembelajaran Mesin (Machine Learning)
TOPIK TUGAS    : Tugas Mandiri Pekan 09 — Sistem Inferensi Logika Fuzzy (N = 20)
TANGGAL        : [Tuliskan Tanggal Penyerahan]
```

---

## 📑 Daftar Isi Lembar Jawaban
1. [SOAL 1: REGRESI FUZZY SUGENO — PREDIKSI LAMA PENYIRAMAN TANAMAN (N = 20)](#soal-1-regresi-fuzzy-sugeno--prediksi-lama-penyiraman-tanaman-n--20)
   - [1.1 Identifikasi Masalah & Diketahui](#11-identifikasi-masalah--diketahui)
   - [1.2 Rumus Fungsi Keanggotaan Masukan](#12-rumus-fungsi-keanggotaan-masukan)
   - [1.3 Perancangan 4 Basis Aturan Sugeno Orde Nol](#13-perancangan-4-basis-aturan-sugeno-orde-nol)
   - [1.4 Penjabaran Perhitungan Manual Langkah demi Langkah (Sampel Data)](#14-penjabaran-perhitungan-manual-langkah-demi-langkah-sampel-data)
   - [1.5 Tabel Komputasi & Prediksi Lengkap 20 Baris Data](#15-tabel-komputasi--prediksi-lengkap-20-baris-data)
   - [1.6 Perhitungan Evaluasi Galat Regresi (MAE & RMSE)](#16-perhitungan-evaluasi-galat-regresi-mae--rmse)
   - [1.7 Kesimpulan Akademis Soal 1](#17-kesimpulan-akademis-soal-1)
2. [SOAL 2: KLASIFIKASI FUZZY RULE-BASED — RISIKO KREDIT NASABAH (N = 20)](#soal-2-klasifikasi-fuzzy-rule-based--risiko-kredit-nasabah-n--20)
   - [2.1 Identifikasi Masalah & Diketahui](#21-identifikasi-masalah--diketahui)
   - [2.2 Rumus Fungsi Keanggotaan Masukan](#22-rumus-fungsi-keanggotaan-masukan)
   - [2.3 Perancangan 4 Basis Aturan & Aturan Konservatif](#23-perancangan-4-basis-aturan--aturan-konservatif)
   - [2.4 Penjabaran Perhitungan Manual Langkah demi Langkah (Sampel Data)](#24-penjabaran-perhitungan-manual-langkah-demi-langkah-sampel-data)
   - [2.5 Tabel Komputasi & Klasifikasi Lengkap 20 Baris Data](#25-tabel-komputasi--klasifikasi-lengkap-20-baris-data)
   - [2.6 Tabel Confusion Matrix & Evaluasi Kinerja (Akurasi, Presisi, Recall, F1)](#26-tabel-confusion-matrix--evaluasi-kinerja-akurasi-presisi-recall-f1)
   - [2.7 Kesimpulan Akademis Soal 2](#27-kesimpulan-akademis-soal-2)

---

# SOAL 1: REGRESI FUZZY SUGENO — PREDIKSI LAMA PENYIRAMAN TANAMAN ($N = 20$)

## 1.1 Identifikasi Masalah & Diketahui

Sistem automasi *greenhouse* menggunakan metode **Fuzzy Sugeno Orde Nol** untuk memprediksi durasi penyiraman tanaman.

### A. Variabel Masukan (Input)
1. **Suhu Udara ($x$):** Satuan Celsius ($^\circ\text{C}$).  
   Nilai data berada pada rentang $21^\circ\text{C} \le x \le 40^\circ\text{C}$.  
   Semesta pembicaraan ditetapkan: $U_{\text{Suhu}} = [20, 40]^\circ\text{C}$.
2. **Kelembapan Tanah ($h$):** Satuan persentase ($\%$).  
   Nilai data berada pada rentang $20\% \le h \le 90\%$.  
   Semesta pembicaraan ditetapkan: $U_{\text{Lembap}} = [20, 90]\%$.

### B. Variabel Keluaran (Output)
- **Lama Penyiraman ($\hat{y}$):** Satuan Menit.  
  Nilai aktual berada pada rentang $3 \le y \le 28$ menit.

### C. Logika Domain Pertanian
- Suhu udara semakin tinggi $\to$ evaporasi tanah meningkat $\to$ tanaman membutuhkan air lebih lama.
- Kelembapan tanah semakin rendah $\to$ kondisi tanah semakin kering $\to$ penyiraman membutuhkan waktu lebih lama.

---

## 1.2 Rumus Fungsi Keanggotaan Masukan

### A. Variabel Suhu Udara ($x \in [20, 40]^\circ\text{C}$)

1. **Himpunan Fuzzy DINGIN ($\mu_D$):** Kurva Linear Turun
   $$\mu_D(x) = \begin{cases} 1, & x \le 20 \\ \dfrac{40 - x}{20}, & 20 < x < 40 \\ 0, & x \ge 40 \end{cases}$$

2. **Himpunan Fuzzy PANAS ($\mu_P$):** Kurva Linear Naik
   $$\mu_P(x) = \begin{cases} 0, & x \le 20 \\ \dfrac{x - 20}{20}, & 20 < x < 40 \\ 1, & x \ge 40 \end{cases}$$

---

### B. Variabel Kelembapan Tanah ($h \in [20, 90]\%$)

Rentang interval $\Delta h = 90 - 20 = 70\%$.

1. **Himpunan Fuzzy RENDAH / KERING ($\mu_{KR}$):** Kurva Linear Turun
   $$\mu_{KR}(h) = \begin{cases} 1, & h \le 20 \\ \dfrac{90 - h}{70}, & 20 < h < 90 \\ 0, & h \ge 90 \end{cases}$$

2. **Himpunan Fuzzy TINGGI / LEMBAP ($\mu_{KT}$):** Kurva Linear Naik
   $$\mu_{KT}(h) = \begin{cases} 0, & h \le 20 \\ \dfrac{h - 20}{70}, & 20 < h < 90 \\ 1, & h \ge 90 \end{cases}$$

---

## 1.3 Perancangan 4 Basis Aturan Sugeno Orde Nol

Sistem Sugeno orde nol menggunakan luaran konstan tegas ($z_i$):

| Nomor Aturan | Anteseden (Kondisi Sensor) | Konsekuen (Keputusan Durasi) | Nilai Luaran ($z_i$) |
| :---: | :--- | :--- | :---: |
| **$R_1$** | `IF Suhu DINGIN AND Kelembapan TINGGI` | Durasi Penyiraman MINIMAL | $z_1 = 3\text{ Menit}$ |
| **$R_2$** | `IF Suhu DINGIN AND Kelembapan RENDAH` | Durasi Penyiraman SEDANG | $z_2 = 17\text{ Menit}$ |
| **$R_3$** | `IF Suhu PANAS AND Kelembapan TINGGI` | Durasi Penyiraman SEDANG | $z_3 = 10\text{ Menit}$ |
| **$R_4$** | `IF Suhu PANAS AND Kelembapan RENDAH` | Durasi Penyiraman MAKSIMAL | $z_4 = 28\text{ Menit}$ |

### Formulasi Komputasi
1. **Operator AND (Firing Strength $\alpha_i$):**
   $$\alpha_i = \min(\mu_{\text{Suhu}}, \mu_{\text{Lembap}})$$
2. **Defuzzifikasi Rata-Rata Terbobot (*Weighted Average*):**
   $$\hat{y} = \frac{\sum_{i=1}^4 \alpha_i \cdot z_i}{\sum_{i=1}^4 \alpha_i} = \frac{(\alpha_1 \cdot 3) + (\alpha_2 \cdot 17) + (\alpha_3 \cdot 10) + (\alpha_4 \cdot 28)}{\alpha_1 + \alpha_2 + \alpha_3 + \alpha_4}$$

---

## 1.4 Penjabaran Perhitungan Manual Langkah demi Langkah (Sampel Data)

*(Tuliskan penjabaran berikut di lembar folio untuk membuktikan penguasaan rumus).*

### A. Perhitungan Data Nomor 1
**Diketahui:** Suhu $x = 22^\circ\text{C}$, Kelembapan $h = 82\%$, Lama Aktual $y = 4\text{ Menit}$.

1. **Fuzzifikasi Suhu ($x = 22$):**
   $$\mu_D(22) = \frac{40 - 22}{20} = \frac{18}{20} = 0{,}90$$
   $$\mu_P(22) = \frac{22 - 20}{20} = \frac{2}{20} = 0{,}10$$

2. **Fuzzifikasi Kelembapan Tanah ($h = 82$):**
   $$\mu_{KR}(82) = \frac{90 - 82}{70} = \frac{8}{70} \approx 0{,}114 \implies 0{,}11$$
   $$\mu_{KT}(82) = \frac{82 - 20}{70} = \frac{62}{70} \approx 0{,}886 \implies 0{,}89$$

3. **Evaluasi Kekuatan 4 Aturan ($\alpha$):**
   - $\alpha_1 = \min(\mu_D, \mu_{KT}) = \min(0{,}90; 0{,}89) = 0{,}89$
   - $\alpha_2 = \min(\mu_D, \mu_{KR}) = \min(0{,}90; 0{,}11) = 0{,}11$
   - $\alpha_3 = \min(\mu_P, \mu_{KT}) = \min(0{,}10; 0{,}89) = 0{,}10$
   - $\alpha_4 = \min(\mu_P, \mu_{KR}) = \min(0{,}10; 0{,}11) = 0{,}10$

4. **Defuzzifikasi Rata-Rata Terbobot:**
   $$\text{Pembilang} = (0{,}89 \times 3) + (0{,}11 \times 17) + (0{,}10 \times 10) + (0{,}10 \times 28)$$
   $$\text{Pembilang} = 2{,}67 + 1{,}87 + 1{,}00 + 2{,}80 = 8{,}34$$
   $$\text{Penyebut} = 0{,}89 + 0{,}11 + 0{,}10 + 0{,}10 = 1{,}20$$
   $$\hat{y}_1 = \frac{8{,}34}{1{,}20} = \mathbf{7{,}00\text{ Menit}}$$

5. **Galat Prediksi Data 1:**
   - Galat Absolut: $|y_1 - \hat{y}_1| = |4 - 7{,}00| = 3{,}00\text{ Menit}$
   - Galat Kuadrat: $(y_1 - \hat{y}_1)^2 = (3{,}00)^2 = 9{,}0000$

---

### B. Perhitungan Data Nomor 4
**Diketahui:** Suhu $x = 30^\circ\text{C}$, Kelembapan $h = 50\%$, Lama Aktual $y = 14\text{ Menit}$.

1. **Fuzzifikasi Suhu ($x = 30$):**
   $$\mu_D(30) = \frac{40 - 30}{20} = \frac{10}{20} = 0{,}50$$
   $$\mu_P(30) = \frac{30 - 20}{20} = \frac{10}{20} = 0{,}50$$

2. **Fuzzifikasi Kelembapan Tanah ($h = 50$):**
   $$\mu_{KR}(50) = \frac{90 - 50}{70} = \frac{40}{70} \approx 0{,}57$$
   $$\mu_{KT}(50) = \frac{50 - 20}{70} = \frac{30}{70} \approx 0{,}43$$

3. **Evaluasi Kekuatan 4 Aturan ($\alpha$):**
   - $\alpha_1 = \min(0{,}50; 0{,}43) = 0{,}43$
   - $\alpha_2 = \min(0{,}50; 0{,}57) = 0{,}50$
   - $\alpha_3 = \min(0{,}50; 0{,}43) = 0{,}43$
   - $\alpha_4 = \min(0{,}50; 0{,}57) = 0{,}50$

4. **Defuzzifikasi Rata-Rata Terbobot:**
   $$\text{Pembilang} = (0{,}43 \times 3) + (0{,}50 \times 17) + (0{,}43 \times 10) + (0{,}50 \times 28)$$
   $$\text{Pembilang} = 1{,}29 + 8{,}50 + 4{,}30 + 14{,}00 = 28{,}09$$
   $$\text{Penyebut} = 0{,}43 + 0{,}50 + 0{,}43 + 0{,}50 = 1{,}86$$
   $$\hat{y}_4 = \frac{28{,}09}{1{,}86} \approx \mathbf{15{,}12\text{ Menit}}$$

5. **Galat Prediksi Data 4:**
   - Galat Absolut: $|14 - 15{,}12| = 1{,}12\text{ Menit}$
   - Galat Kuadrat: $(1{,}12)^2 \approx 1{,}2441$

---

### C. Perhitungan Data Nomor 12 (Batas Bawah Nilai Ekstrem)
**Diketahui:** Suhu $x = 21^\circ\text{C}$, Kelembapan $h = 90\%$, Lama Aktual $y = 3\text{ Menit}$.

1. **Fuzzifikasi:**
   $$\mu_D(21) = \frac{19}{20} = 0{,}95, \quad \mu_P(21) = \frac{1}{20} = 0{,}05$$
   $$\mu_{KR}(90) = \frac{0}{70} = 0{,}00, \quad \mu_{KT}(90) = \frac{70}{70} = 1{,}00$$

2. **Evaluasi Aturan:**
   - $\alpha_1 = \min(0{,}95; 1{,}00) = 0{,}95$
   - $\alpha_2 = \min(0{,}95; 0{,}00) = 0{,}00$
   - $\alpha_3 = \min(0{,}05; 1{,}00) = 0{,}05$
   - $\alpha_4 = \min(0{,}05; 0{,}00) = 0{,}00$

3. **Defuzzifikasi:**
   $$\hat{y}_{12} = \frac{(0{,}95 \times 3) + (0 \times 17) + (0{,}05 \times 10) + (0 \times 28)}{0{,}95 + 0 + 0{,}05 + 0} = \frac{2{,}85 + 0{,}50}{1{,}00} = \mathbf{3{,}35\text{ Menit}}$$
   - Galat Absolut: $|3 - 3{,}35| = 0{,}35\text{ Menit}$

---

### D. Perhitungan Data Nomor 20 (Batas Atas Nilai Ekstrem)
**Diketahui:** Suhu $x = 40^\circ\text{C}$, Kelembapan $h = 20\%$, Lama Aktual $y = 28\text{ Menit}$.

1. **Fuzzifikasi:**
   $$\mu_D(40) = 0{,}00, \quad \mu_P(40) = 1{,}00$$
   $$\mu_{KR}(20) = 1{,}00, \quad \mu_{KT}(20) = 0{,}00$$

2. **Evaluasi Aturan:**
   - $\alpha_1 = \min(0; 0) = 0{,}00$
   - $\alpha_2 = \min(0; 1) = 0{,}00$
   - $\alpha_3 = \min(1; 0) = 0{,}00$
   - $\alpha_4 = \min(1; 1) = 1{,}00$

3. **Defuzzifikasi:**
   $$\hat{y}_{20} = \frac{1{,}00 \times 28}{1{,}00} = \mathbf{28{,}00\text{ Menit}}$$
   - Galat Absolut: $|28 - 28{,}00| = \mathbf{0{,}00\text{ Menit}}$ (Tepat sempurna).

---

## 1.5 Tabel Komputasi & Prediksi Lengkap 20 Baris Data

*(Salin tabel rekapitulasi numerik berikut secara utuh di lembar folio Anda).*

| No | Suhu ($x$) | Lembap ($h$) | $\mu_D$ | $\mu_P$ | $\mu_{KR}$ | $\mu_{KT}$ | $\alpha_1$ | $\alpha_2$ | $\alpha_3$ | $\alpha_4$ | Aktual ($y$) | Prediksi ($\hat{y}$) | Galat Absolut ($\lvert y - \hat{y} \rvert$) | Galat Kuadrat ($(y - \hat{y})^2$) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 22 | 82 | 0,90 | 0,10 | 0,11 | 0,89 | 0,89 | 0,11 | 0,10 | 0,10 | 4 | 7,00 | 3,00 | 9,0000 |
| 2 | 25 | 70 | 0,75 | 0,25 | 0,29 | 0,71 | 0,71 | 0,29 | 0,25 | 0,25 | 7 | 11,00 | 4,00 | 16,0000 |
| 3 | 28 | 60 | 0,60 | 0,40 | 0,43 | 0,57 | 0,57 | 0,43 | 0,40 | 0,40 | 10 | 13,44 | 3,44 | 11,8642 |
| 4 | 30 | 50 | 0,50 | 0,50 | 0,57 | 0,43 | 0,43 | 0,50 | 0,43 | 0,50 | 14 | 15,12 | 1,12 | 1,2441 |
| 5 | 34 | 40 | 0,30 | 0,70 | 0,71 | 0,29 | 0,29 | 0,30 | 0,29 | 0,70 | 19 | 18,08 | 0,92 | 0,8431 |
| 6 | 38 | 25 | 0,10 | 0,90 | 0,93 | 0,07 | 0,07 | 0,10 | 0,07 | 0,90 | 26 | 24,35 | 1,65 | 2,7225 |
| 7 | 24 | 35 | 0,80 | 0,20 | 0,79 | 0,21 | 0,21 | 0,79 | 0,20 | 0,20 | 15 | 15,43 | 0,43 | 0,1837 |
| 8 | 36 | 80 | 0,20 | 0,80 | 0,14 | 0,86 | 0,20 | 0,14 | 0,80 | 0,14 | 10 | 11,69 | 1,69 | 2,8523 |
| 9 | 32 | 65 | 0,40 | 0,60 | 0,36 | 0,64 | 0,40 | 0,36 | 0,60 | 0,36 | 12 | 13,57 | 1,57 | 2,4806 |
| 10 | 27 | 45 | 0,65 | 0,35 | 0,64 | 0,36 | 0,36 | 0,64 | 0,35 | 0,35 | 14 | 14,88 | 0,88 | 0,7785 |
| 11 | 39 | 55 | 0,05 | 0,95 | 0,50 | 0,50 | 0,05 | 0,05 | 0,50 | 0,50 | 20 | 18,18 | 1,82 | 3,3058 |
| 12 | 21 | 90 | 0,95 | 0,05 | 0,00 | 1,00 | 0,95 | 0,00 | 0,05 | 0,00 | 3 | 3,35 | 0,35 | 0,1225 |
| 13 | 35 | 30 | 0,25 | 0,75 | 0,86 | 0,14 | 0,14 | 0,25 | 0,14 | 0,75 | 23 | 21,08 | 1,92 | 3,6736 |
| 14 | 29 | 85 | 0,55 | 0,45 | 0,07 | 0,93 | 0,55 | 0,07 | 0,45 | 0,07 | 6 | 8,19 | 2,19 | 4,8125 |
| 15 | 33 | 75 | 0,35 | 0,65 | 0,21 | 0,79 | 0,35 | 0,21 | 0,65 | 0,21 | 10 | 12,04 | 2,04 | 4,1412 |
| 16 | 26 | 25 | 0,70 | 0,30 | 0,93 | 0,07 | 0,07 | 0,70 | 0,07 | 0,30 | 18 | 18,57 | 0,57 | 0,3306 |
| 17 | 37 | 45 | 0,15 | 0,85 | 0,64 | 0,36 | 0,15 | 0,15 | 0,36 | 0,64 | 21 | 18,90 | 2,10 | 4,4054 |
| 18 | 23 | 55 | 0,85 | 0,15 | 0,50 | 0,50 | 0,50 | 0,50 | 0,15 | 0,15 | 10 | 12,08 | 2,08 | 4,3136 |
| 19 | 31 | 35 | 0,45 | 0,55 | 0,79 | 0,21 | 0,21 | 0,45 | 0,21 | 0,55 | 18 | 18,09 | 0,09 | 0,0072 |
| 20 | 40 | 20 | 0,00 | 1,00 | 1,00 | 0,00 | 0,00 | 0,00 | 0,00 | 1,00 | 28 | 28,00 | 0,00 | 0,0000 |
| **TOTAL** | — | — | — | — | — | — | — | — | — | — | — | — | **31,85** | **73,0815** |

---

## 1.6 Perhitungan Evaluasi Galat Regresi (MAE & RMSE)

Diketahui jumlah data $n = 20$, total galat absolut $\sum |y_i - \hat{y}_i| = 31{,}85$, dan total galat kuadrat $\sum (y_i - \hat{y}_i)^2 = 73{,}0815$.

### A. Mean Absolute Error (MAE)
$$MAE = \frac{1}{n} \sum_{i=1}^n \lvert y_i - \hat{y}_i \rvert = \frac{31{,}85}{20} = \mathbf{1{,}5925\text{ Menit}} \approx \mathbf{1{,}59\text{ Menit}}$$

### B. Mean Squared Error (MSE)
$$MSE = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2 = \frac{73{,}0815}{20} = \mathbf{3{,}6541\text{ Menit}^2}$$

### C. Root Mean Squared Error (RMSE)
$$RMSE = \sqrt{MSE} = \sqrt{3{,}6541} = \mathbf{1{,}9116\text{ Menit}} \approx \mathbf{1{,}91\text{ Menit}}$$

---

## 1.7 Kesimpulan Akademis Soal 1
Model Fuzzy Sugeno Orde Nol berhasil memprediksi durasi penyiraman tanaman dengan penyimpangan rata-rata sebesar $\mathbf{1{,}59\text{ menit}}$ dari data aktual. Nilai RMSE sebesar $\mathbf{1{,}91\text{ menit}}$ menunjukkan bahwa model stabil dan tidak menghasilkan lonjakan galat ekstrem pada data batas semesta.

---

# SOAL 2: KLASIFIKASI FUZZY RULE-BASED — RISIKO KREDIT NASABAH ($N = 20$)

## 2.1 Identifikasi Masalah & Diketahui

Sistem ditugaskan mengklasifikasikan kelayakan nasabah ke dalam dua kelas keputusan:
- **RISIKO RENDAH (Disetujui / Aman)**
- **RISIKO TINGGI (Ditolak / Waspada)**

### A. Variabel Masukan (Input)
1. **Rasio Cicilan terhadap Pendapatan ($r$):** Satuan $\%$.  
   Rentang data: $15\% \le r \le 60\%$. Batas semesta operasional: $U_{\text{Rasio}} = [10, 65]\%$.  
   Titik peralihan kritis (*crossover point*): $30\%$ s.d. $50\%$.
2. **Skor Kelayakan Kredit ($s$):** Skala numerik $0 - 100$.  
   Rentang data: $40 \le s \le 95$. Batas semesta operasional: $U_{\text{Skor}} = [30, 100]$.  
   Titik peralihan kritis (*crossover point*): $50$ s.d. $80$.

### B. Logika Domain Finansial Perbankan
- Semakin tinggi rasio cicilan $\to$ beban keuangan nasabah semakin berat $\to$ risiko gagal bayar meningkat.
- Semakin tinggi skor kredit $\to$ rekam jejak kepatuhan dan reputasi semakin baik $\to$ risiko kredit menurun.

---

## 2.2 Rumus Fungsi Keanggotaan Masukan

### A. Variabel Rasio Cicilan ($r$)
Batas ambang: $a = 30\%$, $b = 50\%$, $\Delta r = 20\%$.

1. **Himpunan Fuzzy RASIO RENDAH ($\mu_{RR}$):**
   $$\mu_{RR}(r) = \begin{cases} 1, & r \le 30 \\ \dfrac{50 - r}{20}, & 30 < r < 50 \\ 0, & r \ge 50 \end{cases}$$

2. **Himpunan Fuzzy RASIO TINGGI ($\mu_{RT}$):**
   $$\mu_{RT}(r) = \begin{cases} 0, & r \le 30 \\ \dfrac{r - 30}{20}, & 30 < r < 50 \\ 1, & r \ge 50 \end{cases}$$

---

### B. Variabel Skor Kredit ($s$)
Batas ambang: $a = 50$, $b = 80$, $\Delta s = 30$.

1. **Himpunan Fuzzy SKOR RENDAH ($\mu_{SR}$):**
   $$\mu_{SR}(s) = \begin{cases} 1, & s \le 50 \\ \dfrac{80 - s}{30}, & 50 < s < 80 \\ 0, & s \ge 80 \end{cases}$$

2. **Himpunan Fuzzy SKOR TINGGI ($\mu_{ST}$):**
   $$\mu_{ST}(s) = \begin{cases} 0, & s \le 50 \\ \dfrac{s - 50}{30}, & 50 < s < 80 \\ 1, & s \ge 80 \end{cases}$$

---

## 2.3 Perancangan 4 Basis Aturan & Aturan Konservatif

Kombinasi aturan inferensi proposisional:

| Aturan | Anteseden (Kondisi Nasabah) | Konsekuen (Keputusan Risiko) |
| :---: | :--- | :---: |
| **$R_1$** | `IF Rasio RENDAH AND Skor TINGGI` | **RISIKO RENDAH** |
| **$R_2$** | `IF Rasio RENDAH AND Skor RENDAH` | **RISIKO TINGGI** |
| **$R_3$** | `IF Rasio TINGGI AND Skor TINGGI` | **RISIKO TINGGI** |
| **$R_4$** | `IF Rasio TINGGI AND Skor RENDAH` | **RISIKO TINGGI** |

### Formulasi Agregasi & Keputusan
1. **Operator AND (Firing Strength):**
   $$\alpha_i = \min(\mu_{\text{Rasio}}, \mu_{\text{Skor}})$$
2. **Dukungan Skor Kelas (Maksimum):**
   $$S_{\text{Rendah}} = \alpha_1$$
   $$S_{\text{Tinggi}} = \max(\alpha_2, \alpha_3, \alpha_4)$$
3. **Keputusan Akhir & Aturan Konservatif (*Tie-Breaking*):**
   $$\hat{y} = \begin{cases} \text{RISIKO TINGGI}, & S_{\text{Tinggi}} \ge S_{\text{Rendah}} \\ \text{RISIKO RENDAH}, & S_{\text{Tinggi}} < S_{\text{Rendah}} \end{cases}$$
   *(Jika skor seri $S_{\text{Tinggi}} = S_{\text{Rendah}}$, perbankan memilih Risiko Tinggi untuk memitigasi kredit macet).*

---

## 2.4 Penjabaran Perhitungan Manual Langkah demi Langkah (Sampel Data)

### A. Perhitungan Data Nomor 1 (Profil Sangat Aman)
**Diketahui:** Rasio $r = 15\%$, Skor $s = 90$, Aktual = **Rendah**.

1. **Fuzzifikasi:**
   $$\mu_{RR}(15) = 1{,}00, \quad \mu_{RT}(15) = 0{,}00$$
   $$\mu_{SR}(90) = 0{,}00, \quad \mu_{ST}(90) = 1{,}00$$

2. **Evaluasi 4 Aturan:**
   - $\alpha_1 = \min(\mu_{RR}, \mu_{ST}) = \min(1{,}00; 1{,}00) = 1{,}00$
   - $\alpha_2 = \min(\mu_{RR}, \mu_{SR}) = \min(1{,}00; 0{,}00) = 0{,}00$
   - $\alpha_3 = \min(\mu_{RT}, \mu_{ST}) = \min(0{,}00; 1{,}00) = 0{,}00$
   - $\alpha_4 = \min(\mu_{RT}, \mu_{SR}) = \min(0{,}00; 0{,}00) = 0{,}00$

3. **Agregasi Skor:**
   $$S_{\text{Rendah}} = \alpha_1 = 1{,}00$$
   $$S_{\text{Tinggi}} = \max(0{,}00; 0{,}00; 0{,}00) = 0{,}00$$

4. **Keputusan:**
   Karena $S_{\text{Rendah}} (1{,}00) > S_{\text{Tinggi}} (0{,}00)$, maka:
   $$\hat{y}_1 = \mathbf{RISIKO\ RENDAH}\quad (\text{Status: Sesuai})$$

---

### B. Perhitungan Data Nomor 5 (Kondisi Ambigu / Transisi)
**Diketahui:** Rasio $r = 35\%$, Skor $s = 65$, Aktual = **Tinggi**.

1. **Fuzzifikasi:**
   $$\mu_{RR}(35) = \frac{50 - 35}{20} = \frac{15}{20} = 0{,}75, \quad \mu_{RT}(35) = \frac{35 - 30}{20} = \frac{5}{20} = 0{,}25$$
   $$\mu_{SR}(65) = \frac{80 - 65}{30} = \frac{15}{30} = 0{,}50, \quad \mu_{ST}(65) = \frac{65 - 50}{30} = \frac{15}{30} = 0{,}50$$

2. **Evaluasi 4 Aturan:**
   - $\alpha_1 = \min(0{,}75; 0{,}50) = 0{,}50$
   - $\alpha_2 = \min(0{,}75; 0{,}50) = 0{,}50$
   - $\alpha_3 = \min(0{,}25; 0{,}50) = 0{,}25$
   - $\alpha_4 = \min(0{,}25; 0{,}50) = 0{,}25$

3. **Agregasi Skor:**
   $$S_{\text{Rendah}} = \alpha_1 = 0{,}50$$
   $$S_{\text{Tinggi}} = \max(0{,}50; 0{,}25; 0{,}25) = 0{,}50$$

4. **Keputusan (Penerapan Aturan Konservatif):**
   Terjadi kondisi seri: $S_{\text{Tinggi}} = S_{\text{Rendah}} = 0{,}50$.  
   Berdasarkan kebijakan mitigasi risiko konservatif ($S_{\text{Tinggi}} \ge S_{\text{Rendah}}$), sistem menetapkan:
   $$\hat{y}_5 = \mathbf{RISIKO\ TINGGI}\quad (\text{Status: Sesuai})$$

---

### C. Perhitungan Data Nomor 11 (Rasio Rendah tapi Skor Buruk)
**Diketahui:** Rasio $r = 18\%$, Skor $s = 55$, Aktual = **Tinggi**.

1. **Fuzzifikasi:**
   $$\mu_{RR}(18) = 1{,}00, \quad \mu_{RT}(18) = 0{,}00$$
   $$\mu_{SR}(55) = \frac{80 - 55}{30} = \frac{25}{30} \approx 0{,}83, \quad \mu_{ST}(55) = \frac{55 - 50}{30} = \frac{5}{30} \approx 0{,}17$$

2. **Evaluasi Aturan:**
   - $\alpha_1 = \min(1{,}00; 0{,}17) = 0{,}17$
   - $\alpha_2 = \min(1{,}00; 0{,}83) = 0{,}83$
   - $\alpha_3 = \min(0{,}00; 0{,}17) = 0{,}00$
   - $\alpha_4 = \min(0{,}00; 0{,}83) = 0{,}00$

3. **Agregasi Skor:**
   $$S_{\text{Rendah}} = 0{,}17, \quad S_{\text{Tinggi}} = \max(0{,}83; 0; 0) = 0{,}83$$
   Karena $S_{\text{Tinggi}} (0{,}83) > S_{\text{Rendah}} (0{,}17)$, maka:
   $$\hat{y}_{11} = \mathbf{RISIKO\ TINGGI}\quad (\text{Status: Sesuai})$$

---

### D. Perhitungan Data Nomor 17 (Rasio Tinggi tapi Skor Sangat Bagus)
**Diketahui:** Rasio $r = 48\%$, Skor $s = 85$, Aktual = **Tinggi**.

1. **Fuzzifikasi:**
   $$\mu_{RR}(48) = \frac{2}{20} = 0{,}10, \quad \mu_{RT}(48) = \frac{18}{20} = 0{,}90$$
   $$\mu_{SR}(85) = 0{,}00, \quad \mu_{ST}(85) = 1{,}00$$

2. **Evaluasi Aturan:**
   - $\alpha_1 = \min(0{,}10; 1{,}00) = 0{,}10$
   - $\alpha_2 = \min(0{,}10; 0{,}00) = 0{,}00$
   - $\alpha_3 = \min(0{,}90; 1{,}00) = 0{,}90$
   - $\alpha_4 = \min(0{,}90; 0{,}00) = 0{,}00$

3. **Agregasi Skor:**
   $$S_{\text{Rendah}} = 0{,}10, \quad S_{\text{Tinggi}} = \max(0{,}00; 0{,}90; 0{,}00) = 0{,}90$$
   Karena beban cicilan mendekati $50\%$ ($R_3$ aktif kuat), sistem menetapkan:
   $$\hat{y}_{17} = \mathbf{RISIKO\ TINGGI}\quad (\text{Status: Sesuai})$$

---

## 2.5 Tabel Komputasi & Klasifikasi Lengkap 20 Baris Data

*(Salin tabel rekapitulasi numerik berikut secara utuh di lembar folio Anda).*

| No | Rasio ($r$) | Skor ($s$) | $\mu_{RR}$ | $\mu_{RT}$ | $\mu_{SR}$ | $\mu_{ST}$ | $\alpha_1$ | $\alpha_2$ | $\alpha_3$ | $\alpha_4$ | $S_{\text{Tinggi}}$ | $S_{\text{Rendah}}$ | Prediksi Fuzzy | Aktual | Status Evaluasi |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 15 | 90 | 1,00 | 0,00 | 0,00 | 1,00 | 1,00 | 0,00 | 0,00 | 0,00 | 0,00 | 1,00 | Rendah | Rendah | Sesuai (TN) |
| 2 | 20 | 85 | 1,00 | 0,00 | 0,00 | 1,00 | 1,00 | 0,00 | 0,00 | 0,00 | 0,00 | 1,00 | Rendah | Rendah | Sesuai (TN) |
| 3 | 25 | 75 | 1,00 | 0,00 | 0,17 | 0,83 | 0,83 | 0,17 | 0,00 | 0,00 | 0,17 | 0,83 | Rendah | Rendah | Sesuai (TN) |
| 4 | 30 | 70 | 1,00 | 0,00 | 0,33 | 0,67 | 0,67 | 0,33 | 0,00 | 0,00 | 0,33 | 0,67 | Rendah | Rendah | Sesuai (TN) |
| 5 | 35 | 65 | 0,75 | 0,25 | 0,50 | 0,50 | 0,50 | 0,50 | 0,25 | 0,25 | 0,50 | 0,50 | Tinggi | Tinggi | Sesuai (TP) |
| 6 | 40 | 60 | 0,50 | 0,50 | 0,67 | 0,33 | 0,33 | 0,50 | 0,33 | 0,50 | 0,50 | 0,33 | Tinggi | Tinggi | Sesuai (TP) |
| 7 | 45 | 55 | 0,25 | 0,75 | 0,83 | 0,17 | 0,17 | 0,25 | 0,17 | 0,75 | 0,75 | 0,17 | Tinggi | Tinggi | Sesuai (TP) |
| 8 | 50 | 50 | 0,00 | 1,00 | 1,00 | 0,00 | 0,00 | 0,00 | 0,00 | 1,00 | 1,00 | 0,00 | Tinggi | Tinggi | Sesuai (TP) |
| 9 | 55 | 45 | 0,00 | 1,00 | 1,00 | 0,00 | 0,00 | 0,00 | 0,00 | 1,00 | 1,00 | 0,00 | Tinggi | Tinggi | Sesuai (TP) |
| 10 | 60 | 40 | 0,00 | 1,00 | 1,00 | 0,00 | 0,00 | 0,00 | 0,00 | 1,00 | 1,00 | 0,00 | Tinggi | Tinggi | Sesuai (TP) |
| 11 | 18 | 55 | 1,00 | 0,00 | 0,83 | 0,17 | 0,17 | 0,83 | 0,00 | 0,00 | 0,83 | 0,17 | Tinggi | Tinggi | Sesuai (TP) |
| 12 | 22 | 95 | 1,00 | 0,00 | 0,00 | 1,00 | 1,00 | 0,00 | 0,00 | 0,00 | 0,00 | 1,00 | Rendah | Rendah | Sesuai (TN) |
| 13 | 28 | 60 | 1,00 | 0,00 | 0,67 | 0,33 | 0,33 | 0,67 | 0,00 | 0,00 | 0,67 | 0,33 | Tinggi | Rendah | Konservatif (FP) |
| 14 | 33 | 80 | 0,85 | 0,15 | 0,00 | 1,00 | 0,85 | 0,00 | 0,15 | 0,00 | 0,15 | 0,85 | Rendah | Rendah | Sesuai (TN) |
| 15 | 38 | 90 | 0,60 | 0,40 | 0,00 | 1,00 | 0,60 | 0,00 | 0,40 | 0,00 | 0,40 | 0,60 | Rendah | Rendah | Sesuai (TN) |
| 16 | 42 | 75 | 0,40 | 0,60 | 0,17 | 0,83 | 0,40 | 0,17 | 0,60 | 0,17 | 0,60 | 0,40 | Tinggi | Tinggi | Sesuai (TP) |
| 17 | 48 | 85 | 0,10 | 0,90 | 0,00 | 1,00 | 0,10 | 0,00 | 0,90 | 0,00 | 0,90 | 0,10 | Tinggi | Tinggi | Sesuai (TP) |
| 18 | 52 | 65 | 0,00 | 1,00 | 0,50 | 0,50 | 0,00 | 0,00 | 0,50 | 0,50 | 0,50 | 0,00 | Tinggi | Tinggi | Sesuai (TP) |
| 19 | 27 | 45 | 1,00 | 0,00 | 1,00 | 0,00 | 0,00 | 1,00 | 0,00 | 0,00 | 1,00 | 0,00 | Tinggi | Tinggi | Sesuai (TP) |
| 20 | 58 | 95 | 0,00 | 1,00 | 0,00 | 1,00 | 0,00 | 0,00 | 1,00 | 0,00 | 1,00 | 0,00 | Tinggi | Tinggi | Sesuai (TP) |

---

## 2.6 Tabel Confusion Matrix & Evaluasi Kinerja (Akurasi, Presisi, Recall, F1)

Dengan menetapkan **RISIKO TINGGI** sebagai **Kelas Positif (Target Intervensi Perbankan)**:
- **True Positive ($TP$):** $12$ (Nasabah risiko tinggi berhasil terdeteksi benar).
- **True Negative ($TN$):** $7$ (Nasabah risiko rendah berhasil terdeteksi benar).
- **False Positive ($FP$):** $1$ (Nasabah risiko rendah terprediksi sebagai risiko tinggi pada Data 13).
- **False Negative ($FN$):** $0$ (Tidak ada nasabah risiko tinggi yang terlewat).

### A. Tabel Confusion Matrix

| Aktual \ Prediksi | Prediksi: Risiko Tinggi | Prediksi: Risiko Rendah | Total Aktual |
| :---: | :---: | :---: | :---: |
| **Aktual: Risiko Tinggi** | **$12$ ($TP$)** | **$0$ ($FN$)** | **$12$** |
| **Aktual: Risiko Rendah** | **$1$ ($FP$)** | **$7$ ($TN$)** | **$8$** |
| **Total Prediksi** | **$13$** | **$7$** | **$N = 20$** |

---

### B. Perhitungan Metrik Evaluasi

1. **Akurasi (Accuracy):**
   $$\text{Akurasi} = \frac{TP + TN}{TP + TN + FP + FN} = \frac{12 + 7}{12 + 7 + 1 + 0} = \frac{19}{20} = \mathbf{95{,}00\%}$$

2. **Presisi (Precision):**
   $$\text{Presisi} = \frac{TP}{TP + FP} = \frac{12}{12 + 1} = \frac{12}{13} \approx \mathbf{92{,}31\%}$$

3. **Recall / Sensitivitas:**
   $$\text{Recall} = \frac{TP}{TP + FN} = \frac{12}{12 + 0} = \frac{12}{12} = \mathbf{100{,}00\%}$$

4. **F1-Score:**
   $$\text{F1-Score} = 2 \times \frac{\text{Presisi} \times \text{Recall}}{\text{Presisi} + \text{Recall}} = 2 \times \frac{0{,}9231 \times 1{,}0000}{0{,}9231 + 1{,}0000} = \frac{1{,}8462}{1{,}9231} \approx \mathbf{96{,}00\%}$$

---

## 2.7 Kesimpulan Akademis Soal 2
Sistem pengklasifikasi Fuzzy menghasilkan kinerja yang sangat unggul dengan tingkat **Akurasi $95\%$** dan **Recall sempurna $100\%$**. Dalam operasional industri perbankan, nilai *Recall 100%* merupakan pencapaian paling krusial karena sistem berhasil mencegah *False Negative* ($FN = 0$), sehingga seluruh potensi kredit macet dapat terdeteksi sejak awal tanpa ada nasabah berisiko tinggi yang terabaikan.

