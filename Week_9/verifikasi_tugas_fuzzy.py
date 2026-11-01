"""
Skrip Verifikasi Perhitungan Mandiri Logika Fuzzy Pekan 09
Memverifikasi Soal 1 (Regresi Sugeno Orde Nol) dan Soal 2 (Klasifikasi Fuzzy Rule-Based)
Sesuai spesifikasi pada MODUL_07_LOGIKA_FUZZY.md dan JAWABAN_TUGAS_MANDIRI_FUZZY.md
"""

import sys
import math

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def verifikasi_soal_1():
    print("=" * 80)
    print("VERIFIKASI SOAL 1: REGRESI FUZZY SUGENO ORDE NOL (DURASI PENYIRAMAN)")
    print("=" * 80)
    
    # Dataset Soal 1 (N = 20)
    # No, Suhu (x), Kelembapan (h), Aktual (y)
    data_soal_1 = [
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
    
    # Fungsi keanggotaan Suhu (x in [20, 40])
    def mu_dingin(x):
        if x <= 20: return 1.0
        if x >= 40: return 0.0
        return (40.0 - x) / 20.0
        
    def mu_panas(x):
        if x <= 20: return 0.0
        if x >= 40: return 1.0
        return (x - 20.0) / 20.0
        
    # Fungsi keanggotaan Kelembapan (h in [20, 90])
    def mu_kering(h):
        if h <= 20: return 1.0
        if h >= 90: return 0.0
        return (90.0 - h) / 70.0
        
    def mu_lembap(h):
        if h <= 20: return 0.0
        if h >= 90: return 1.0
        return (h - 20.0) / 70.0

    # Nilai konsekuen Sugeno orde nol (zi)
    # R1: DINGIN AND LEMBAP -> 3
    # R2: DINGIN AND KERING -> 17
    # R3: PANAS AND LEMBAP  -> 10
    # R4: PANAS AND KERING  -> 28
    z = [3.0, 17.0, 10.0, 28.0]
    
    total_abs_error = 0.0
    total_sq_error = 0.0
    
    print(f"{'No':<3} | {'Suhu':<4} {'Lemb':<4} | {'mu_D':<5} {'mu_P':<5} {'mu_KR':<5} {'mu_KT':<5} | "
          f"{'a1':<5} {'a2':<5} {'a3':<5} {'a4':<5} | {'y':<3} {'y_hat':<6} | {'|e|':<6} {'e^2':<7}")
    print("-" * 95)
    
    for no, x, h, y in data_soal_1:
        md = mu_dingin(x)
        mp = mu_panas(x)
        mkr = mu_kering(h)
        mkt = mu_lembap(h)
        
        # Aturan Sugeno
        a1 = min(md, mkt)
        a2 = min(md, mkr)
        a3 = min(mp, mkt)
        a4 = min(mp, mkr)
        
        sum_alpha = a1 + a2 + a3 + a4
        y_hat = (a1*z[0] + a2*z[1] + a3*z[2] + a4*z[3]) / sum_alpha
        
        abs_err = abs(y - y_hat)
        sq_err = (y - y_hat) ** 2
        
        total_abs_error += abs_err
        total_sq_error += sq_err
        
        print(f"{no:<3} | {x:<4} {h:<4} | {md:<5.2f} {mp:<5.2f} {mkr:<5.2f} {mkt:<5.2f} | "
              f"{a1:<5.2f} {a2:<5.2f} {a3:<5.2f} {a4:<5.2f} | {y:<3} {y_hat:<6.2f} | {abs_err:<6.2f} {sq_err:<7.4f}")
              
    n = len(data_soal_1)
    mae = total_abs_error / n
    mse = total_sq_error / n
    rmse = math.sqrt(mse)
    
    print("-" * 95)
    print(f"Total Abs Error = {total_abs_error:.4f} (di markdown tertulis 31.85)")
    print(f"Total Sq Error  = {total_sq_error:.4f} (di markdown tertulis 73.0815)")
    print(f"MAE             = {mae:.4f} menit (di markdown: ~1.59 menit)")
    print(f"MSE             = {mse:.4f} menit^2 (di markdown: ~3.65 menit^2)")
    print(f"RMSE            = {rmse:.4f} menit (di markdown: ~1.91 menit)")


def verifikasi_soal_2():
    print("\n" + "=" * 80)
    print("VERIFIKASI SOAL 2: KLASIFIKASI FUZZY RULE-BASED (RISIKO KREDIT NASABAH)")
    print("=" * 80)
    
    # Dataset Soal 2 (N = 20)
    # No, Rasio Cicilan (r), Skor Kredit (s), Risiko Aktual
    data_soal_2 = [
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
    
    # Fungsi keanggotaan Rasio Cicilan (r)
    # Ambang: 30 s.d. 50, lebar 20
    def mu_rasio_rendah(r):
        if r <= 30: return 1.0
        if r >= 50: return 0.0
        return (50.0 - r) / 20.0
        
    def mu_rasio_tinggi(r):
        if r <= 30: return 0.0
        if r >= 50: return 1.0
        return (r - 30.0) / 20.0
        
    # Fungsi keanggotaan Skor Kredit (s)
    # Ambang: 50 s.d. 80, lebar 30
    def mu_skor_rendah(s):
        if s <= 50: return 1.0
        if s >= 80: return 0.0
        return (80.0 - s) / 30.0
        
    def mu_skor_tinggi(s):
        if s <= 50: return 0.0
        if s >= 80: return 1.0
        return (s - 50.0) / 30.0
        
    # Basis Aturan:
    # R1: Rasio RENDAH AND Skor TINGGI -> RISIKO RENDAH
    # R2: Rasio RENDAH AND Skor RENDAH -> RISIKO TINGGI
    # R3: Rasio TINGGI AND Skor TINGGI -> RISIKO TINGGI
    # R4: Rasio TINGGI AND Skor RENDAH -> RISIKO TINGGI
    
    tp = 0 # Aktual: Tinggi, Pred: Tinggi
    tn = 0 # Aktual: Rendah, Pred: Rendah
    fp = 0 # Aktual: Rendah, Pred: Tinggi
    fn = 0 # Aktual: Tinggi, Pred: Rendah
    
    print(f"{'No':<3} | {'r':<3} {'s':<3} | {'mu_RR':<5} {'mu_RT':<5} {'mu_SR':<5} {'mu_ST':<5} | "
          f"{'a1':<5} {'a2':<5} {'a3':<5} {'a4':<5} | {'S_Tgt':<5} {'S_Rnd':<5} | {'Pred':<6} {'Aktual':<6} | {'Evaluasi'}")
    print("-" * 105)
    
    for no, r, s, aktual in data_soal_2:
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
        
        # Aturan konservatif perbankan: jika s_tinggi >= s_rendah -> Tinggi
        pred = "Tinggi" if s_tinggi >= s_rendah else "Rendah"
        
        if aktual == "Tinggi" and pred == "Tinggi":
            eval_str = "Sesuai (TP)"
            tp += 1
        elif aktual == "Rendah" and pred == "Rendah":
            eval_str = "Sesuai (TN)"
            tn += 1
        elif aktual == "Rendah" and pred == "Tinggi":
            eval_str = "Konservatif (FP)"
            fp += 1
        else: # aktual == "Tinggi" and pred == "Rendah"
            eval_str = "Salah (FN)"
            fn += 1
            
        print(f"{no:<3} | {r:<3} {s:<3} | {mrr:<5.2f} {mrt:<5.2f} {msr:<5.2f} {mst:<5.2f} | "
              f"{a1:<5.2f} {a2:<5.2f} {a3:<5.2f} {a4:<5.2f} | {s_tinggi:<5.2f} {s_rendah:<5.2f} | "
              f"{pred:<6} {aktual:<6} | {eval_str}")
              
    n = len(data_soal_2)
    accuracy = (tp + tn) / n
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    
    print("-" * 105)
    print("HASIL CONFUSION MATRIX:")
    print(f"TP (True Positive)  = {tp}")
    print(f"TN (True Negative)  = {tn}")
    print(f"FP (False Positive) = {fp}")
    print(f"FN (False Negative) = {fn}")
    print("\nMETRIK EVALUASI:")
    print(f"Akurasi   = {accuracy * 100:.2f}% (19/20)")
    print(f"Presisi   = {precision * 100:.2f}% (12/13)")
    print(f"Recall    = {recall * 100:.2f}% (12/12)")
    print(f"F1-Score  = {f1 * 100:.2f}%")


if __name__ == "__main__":
    verifikasi_soal_1()
    verifikasi_soal_2()

