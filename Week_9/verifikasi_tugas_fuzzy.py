"""
Skrip Verifikasi Perhitungan Mandiri Logika Fuzzy Pekan 09
Memverifikasi Soal 1 (Regresi Sugeno Orde Nol) dan Soal 2 (Klasifikasi Fuzzy Rule-Based)
Serta memverifikasi 5 sampel penjabaran manual langkah demi langkah untuk setiap soal.
Sesuai spesifikasi pada MODUL_07_LOGIKA_FUZZY.md dan JAWABAN_TUGAS_MANDIRI_FUZZY.md
"""

import sys
import math

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# DATASET DEFINITIONS
# ==============================================================================

# Soal 1: (No, Suhu x, Kelembapan h, Aktual y)
DATA_SOAL_1 = [
    (1, 22, 82, 4),
    (2, 25, 70, 7),
    (3, 28, 60, 10),
    (4, 30, 50, 14),
    (5, 34, 40, 19),
    (6, 38, 25, 26),
    (7, 24, 35, 15),
    (8, 36, 80, 10),
    (9, 32, 65, 12),
    (10, 27, 45, 14),
    (11, 39, 55, 20),
    (12, 21, 90, 3),
    (13, 35, 30, 23),
    (14, 29, 85, 6),
    (15, 33, 75, 10),
    (16, 26, 25, 18),
    (17, 37, 45, 21),
    (18, 23, 55, 10),
    (19, 31, 35, 18),
    (20, 40, 20, 28)
]

# Soal 2: (No, Rasio Cicilan r, Skor Kredit s, Aktual)
DATA_SOAL_2 = [
    (1, 15, 90, "Rendah"),
    (2, 20, 85, "Rendah"),
    (3, 25, 75, "Rendah"),
    (4, 30, 70, "Rendah"),
    (5, 35, 65, "Tinggi"),
    (6, 40, 60, "Tinggi"),
    (7, 45, 55, "Tinggi"),
    (8, 50, 50, "Tinggi"),
    (9, 55, 45, "Tinggi"),
    (10, 60, 40, "Tinggi"),
    (11, 18, 55, "Tinggi"),
    (12, 22, 95, "Rendah"),
    (13, 28, 60, "Rendah"),
    (14, 33, 80, "Rendah"),
    (15, 38, 90, "Rendah"),
    (16, 42, 75, "Tinggi"),
    (17, 48, 85, "Tinggi"),
    (18, 52, 65, "Tinggi"),
    (19, 27, 45, "Tinggi"),
    (20, 58, 95, "Tinggi")
]

# ==============================================================================
# FUNGSI KEANGGOTAAN
# ==============================================================================

# Soal 1
def mu_dingin(x):
    if x <= 20: return 1.0
    if x >= 40: return 0.0
    return (40.0 - x) / 20.0

def mu_panas(x):
    if x <= 20: return 0.0
    if x >= 40: return 1.0
    return (x - 20.0) / 20.0

def mu_kering(h):
    if h <= 20: return 1.0
    if h >= 90: return 0.0
    return (90.0 - h) / 70.0

def mu_lembap(h):
    if h <= 20: return 0.0
    if h >= 90: return 1.0
    return (h - 20.0) / 70.0

# Soal 2
def mu_rasio_rendah(r):
    if r <= 30: return 1.0
    if r >= 50: return 0.0
    return (50.0 - r) / 20.0

def mu_rasio_tinggi(r):
    if r <= 30: return 0.0
    if r >= 50: return 1.0
    return (r - 30.0) / 20.0

def mu_skor_rendah(s):
    if s <= 50: return 1.0
    if s >= 80: return 0.0
    return (80.0 - s) / 30.0

def mu_skor_tinggi(s):
    if s <= 50: return 0.0
    if s >= 80: return 1.0
    return (s - 50.0) / 30.0


# ==============================================================================
# VERIFIKASI 5 SAMPEL MANUAL SOAL 1
# ==============================================================================

def hitung_detail_soal_1(no):
    item = next(d for d in DATA_SOAL_1 if d[0] == no)
    _, x, h, y = item
    md = mu_dingin(x)
    mp = mu_panas(x)
    mkr = mu_kering(h)
    mkt = mu_lembap(h)
    
    a1 = min(md, mkt)
    a2 = min(md, mkr)
    a3 = min(mp, mkt)
    a4 = min(mp, mkr)
    
    z = [3.0, 17.0, 10.0, 28.0]
    pembilang = (a1 * z[0]) + (a2 * z[1]) + (a3 * z[2]) + (a4 * z[3])
    penyebut = a1 + a2 + a3 + a4
    y_hat = pembilang / penyebut if penyebut != 0 else 0
    abs_err = abs(y - y_hat)
    sq_err = (y - y_hat) ** 2
    
    print(f"\n--- [DETAIL DATA NO. {no}] ---")
    print(f"Input: Suhu x = {x}°C, Kelembapan h = {h}%, Aktual y = {y} menit")
    print(f"Fuzzifikasi: mu_D={md:.4f} (~{md:.2f}), mu_P={mp:.4f} (~{mp:.2f}), mu_KR={mkr:.4f} (~{mkr:.2f}), mu_KT={mkt:.4f} (~{mkt:.2f})")
    print(f"Firing Strength: a1={a1:.4f} (~{a1:.2f}), a2={a2:.4f} (~{a2:.2f}), a3={a3:.4f} (~{a3:.2f}), a4={a4:.4f} (~{a4:.2f})")
    print(f"Defuzzifikasi: Pembilang={pembilang:.4f}, Penyebut={penyebut:.4f} -> Prediksi y_hat = {y_hat:.2f} menit")
    print(f"Galat: |y - y_hat| = {abs_err:.2f} menit, (y - y_hat)^2 = {sq_err:.4f}")
    return y_hat, abs_err, sq_err


# ==============================================================================
# VERIFIKASI 5 SAMPEL MANUAL SOAL 2
# ==============================================================================

def hitung_detail_soal_2(no):
    item = next(d for d in DATA_SOAL_2 if d[0] == no)
    _, r, s, aktual = item
    mrr = mu_rasio_rendah(r)
    mrt = mu_rasio_tinggi(r)
    msr = mu_skor_rendah(s)
    mst = mu_skor_tinggi(s)
    
    a1 = min(mrr, mst) # Rendah
    a2 = min(mrr, msr) # Tinggi
    a3 = min(mrt, mst) # Tinggi
    a4 = min(mrt, msr) # Tinggi
    
    s_rendah = a1
    s_tinggi = max(a2, a3, a4)
    pred = "Tinggi" if s_tinggi >= s_rendah else "Rendah"
    
    eval_str = "Sesuai" if pred == aktual else ("Konservatif (FP)" if pred == "Tinggi" else "Salah (FN)")
    
    print(f"\n--- [DETAIL DATA NO. {no}] ---")
    print(f"Input: Rasio r = {r}%, Skor s = {s}, Aktual = {aktual}")
    print(f"Fuzzifikasi: mu_RR={mrr:.4f} (~{mrr:.2f}), mu_RT={mrt:.4f} (~{mrt:.2f}), mu_SR={msr:.4f} (~{msr:.2f}), mu_ST={mst:.4f} (~{mst:.2f})")
    print(f"Firing Strength: a1={a1:.4f} (~{a1:.2f}), a2={a2:.4f} (~{a2:.2f}), a3={a3:.4f} (~{a3:.2f}), a4={a4:.4f} (~{a4:.2f})")
    print(f"Agregasi Skor: S_Rendah = {s_rendah:.4f} (~{s_rendah:.2f}), S_Tinggi = {s_tinggi:.4f} (~{s_tinggi:.2f})")
    print(f"Keputusan: Prediksi = {pred} (Kondisi: S_Tinggi {' >= ' if s_tinggi >= s_rendah else ' < '} S_Rendah) | Status: {eval_str}")
    return pred, eval_str


def run_full_verification():
    print("=" * 90)
    print("PROGRAM VERIFIKASI LOGIKA FUZZY PEKAN 09 (REGRESI & KLASIFIKASI)")
    print("=" * 90)
    
    # --- SOAL 1 ---
    print("\n[1] PENJABARAN 5 SAMPEL HITUNGAN MANUAL SOAL 1 (REGRESI SUGENO):")
    sampel_soal_1 = [1, 4, 7, 12, 20]
    for s in sampel_soal_1:
        hitung_detail_soal_1(s)
        
    print("\n" + "=" * 90)
    print("[2] TABEL LENGKAP 20 BARIS DATA SOAL 1:")
    print(f"{'No':<3} | {'Suhu':<4} {'Lemb':<4} | {'mu_D':<5} {'mu_P':<5} {'mu_KR':<5} {'mu_KT':<5} | "
          f"{'a1':<5} {'a2':<5} {'a3':<5} {'a4':<5} | {'y':<3} {'y_hat':<6} | {'|e|':<6} {'e^2':<7}")
    print("-" * 90)
    
    z = [3.0, 17.0, 10.0, 28.0]
    tot_abs, tot_sq = 0.0, 0.0
    for no, x, h, y in DATA_SOAL_1:
        md = mu_dingin(x)
        mp = mu_panas(x)
        mkr = mu_kering(h)
        mkt = mu_lembap(h)
        a1, a2, a3, a4 = min(md, mkt), min(md, mkr), min(mp, mkt), min(mp, mkr)
        sum_a = a1 + a2 + a3 + a4
        y_hat = (a1*z[0] + a2*z[1] + a3*z[2] + a4*z[3]) / sum_a
        abs_err = abs(y - y_hat)
        sq_err = (y - y_hat) ** 2
        tot_abs += abs_err
        tot_sq += sq_err
        print(f"{no:<3} | {x:<4} {h:<4} | {md:<5.2f} {mp:<5.2f} {mkr:<5.2f} {mkt:<5.2f} | "
              f"{a1:<5.2f} {a2:<5.2f} {a3:<5.2f} {a4:<5.2f} | {y:<3} {y_hat:<6.2f} | {abs_err:<6.2f} {sq_err:<7.4f}")
              
    n1 = len(DATA_SOAL_1)
    mae = tot_abs / n1
    mse = tot_sq / n1
    rmse = math.sqrt(mse)
    print("-" * 90)
    print(f"METRIK EVALUASI SOAL 1: Total |e|={tot_abs:.4f}, Total e^2={tot_sq:.4f}, MAE={mae:.4f} menit, RMSE={rmse:.4f} menit")
    
    # --- SOAL 2 ---
    print("\n" + "=" * 90)
    print("[3] PENJABARAN 5 SAMPEL HITUNGAN MANUAL SOAL 2 (KLASIFIKASI KREDIT):")
    sampel_soal_2 = [1, 5, 11, 13, 17]
    for s in sampel_soal_2:
        hitung_detail_soal_2(s)
        
    print("\n" + "=" * 90)
    print("[4] TABEL LENGKAP 20 BARIS DATA SOAL 2:")
    print(f"{'No':<3} | {'r':<3} {'s':<3} | {'mu_RR':<5} {'mu_RT':<5} {'mu_SR':<5} {'mu_ST':<5} | "
          f"{'a1':<5} {'a2':<5} {'a3':<5} {'a4':<5} | {'S_Tgt':<5} {'S_Rnd':<5} | {'Pred':<6} {'Aktual':<6} | {'Evaluasi'}")
    print("-" * 90)
    
    tp, tn, fp, fn = 0, 0, 0, 0
    for no, r, s, aktual in DATA_SOAL_2:
        mrr = mu_rasio_rendah(r)
        mrt = mu_rasio_tinggi(r)
        msr = mu_skor_rendah(s)
        mst = mu_skor_tinggi(s)
        a1, a2, a3, a4 = min(mrr, mst), min(mrr, msr), min(mrt, mst), min(mrt, msr)
        s_rendah = a1
        s_tinggi = max(a2, a3, a4)
        pred = "Tinggi" if s_tinggi >= s_rendah else "Rendah"
        
        if aktual == "Tinggi" and pred == "Tinggi":
            ev = "Sesuai (TP)"
            tp += 1
        elif aktual == "Rendah" and pred == "Rendah":
            ev = "Sesuai (TN)"
            tn += 1
        elif aktual == "Rendah" and pred == "Tinggi":
            ev = "Konservatif (FP)"
            fp += 1
        else:
            ev = "Salah (FN)"
            fn += 1
            
        print(f"{no:<3} | {r:<3} {s:<3} | {mrr:<5.2f} {mrt:<5.2f} {msr:<5.2f} {mst:<5.2f} | "
              f"{a1:<5.2f} {a2:<5.2f} {a3:<5.2f} {a4:<5.2f} | {s_tinggi:<5.2f} {s_rendah:<5.2f} | "
              f"{pred:<6} {aktual:<6} | {ev}")
              
    n2 = len(DATA_SOAL_2)
    acc = (tp + tn) / n2
    prec = tp / (tp + fp) if (tp + fp) > 0 else 0
    rec = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * (prec * rec) / (prec + rec) if (prec + rec) > 0 else 0
    
    print("-" * 90)
    print(f"CONFUSION MATRIX: TP={tp}, TN={tn}, FP={fp}, FN={fn}")
    print(f"METRIK EVALUASI: Akurasi={acc*100:.2f}%, Presisi={prec*100:.2f}%, Recall={rec*100:.2f}%, F1-Score={f1*100:.2f}%")


if __name__ == "__main__":
    run_full_verification()
