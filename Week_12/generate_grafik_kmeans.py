#!/usr/bin/env python3
"""
Script Generator Visualisasi Grafik 2D Koordinat Pelanggan & Hasil K-Means
Format: Skala Konsisten 1:1 (X dan Y sama-sama berinterval 1 unit: 0, 1, 2, 3...)
File output: Week_12/images/grafik_koordinat_pelanggan_kmeans.png
"""

import cairo
import math

# Dimensi Gambar
WIDTH = 1080
HEIGHT = 860

# Margin
MARGIN_LEFT = 95
MARGIN_RIGHT = 65
MARGIN_TOP = 110
MARGIN_BOTTOM = 85

# Rentang Sumbu Data
X_MIN, X_MAX = 0, 16
Y_MIN, Y_MAX = 0, 12

# Hitung Skala Piksel per Unit (Wajib Sama Persis 1:1)
# Tersedia lebar plot: WIDTH - MARGIN_LEFT - MARGIN_RIGHT = 1080 - 160 = 920 px
# Tersedia tinggi plot: HEIGHT - MARGIN_TOP - MARGIN_BOTTOM = 860 - 195 = 665 px
# X_MAX - X_MIN = 16 unit -> 920 / 16 = 57.5 px
# Y_MAX - Y_MIN = 12 unit -> 665 / 12 = 55.4 px
# Kita tetapkan skala bulat presisi: 54.0 piksel per 1 unit data!
SCALE = 54.0

PLOT_WIDTH = (X_MAX - X_MIN) * SCALE   # 16 * 54 = 864 px
PLOT_HEIGHT = (Y_MAX - Y_MIN) * SCALE  # 12 * 54 = 648 px

# Posisi Titik Asal (0, 0) dalam Piksel
ORIGIN_X = MARGIN_LEFT
ORIGIN_Y = MARGIN_TOP + PLOT_HEIGHT

def to_pixel(x, y):
    px = ORIGIN_X + (x - X_MIN) * SCALE
    py = ORIGIN_Y - (y - Y_MIN) * SCALE
    return px, py

# Buat Cairo Surface & Context
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

# 1. Latar Belakang Putih Bersih
ctx.set_source_rgb(1.0, 1.0, 1.0)
ctx.paint()

# 2. Garis Kisi Halus (Subtle 1x1 Grid)
# Membantu pembaca memverifikasi skala 1:1 dan menghitung kotak folio tanpa mendistraksi
ctx.set_line_width(0.8)
ctx.set_source_rgb(0.92, 0.94, 0.96)  # Abu-abu sangat lembut

for x_val in range(X_MIN, X_MAX + 1):
    px, _ = to_pixel(x_val, 0)
    ctx.move_to(px, ORIGIN_Y)
    ctx.line_to(px, MARGIN_TOP)
    ctx.stroke()

for y_val in range(Y_MIN, Y_MAX + 1):
    _, py = to_pixel(0, y_val)
    ctx.move_to(ORIGIN_X, py)
    ctx.line_to(ORIGIN_X + PLOT_WIDTH, py)
    ctx.stroke()

# 3. Area Shading Transparan Pengelompokan Klaster (Convex Bounding Bubble)
# Klaster 1: P1(2,1), P2(3,1.5), P3(4,2)
ctx.save()
p1_px, p1_py = to_pixel(2, 1.0)
p3_px, p3_py = to_pixel(4, 2.0)
# Lingkari klaster 1 dengan kapsul/elips halus
ctx.set_source_rgba(0.12, 0.53, 0.90, 0.10) # Soft Blue fill
ctx.arc(to_pixel(3.0, 1.5)[0], to_pixel(3.0, 1.5)[1], 1.7 * SCALE, 0, 2 * math.pi)
ctx.fill_preserve()
ctx.set_source_rgba(0.12, 0.53, 0.90, 0.40) # Soft Blue stroke
ctx.set_line_width(1.5)
ctx.set_dash([4.0, 4.0])
ctx.stroke()
ctx.restore()

# Klaster 2: P4(12,8), P5(14,9), P6(15,10)
ctx.save()
ctx.set_source_rgba(0.90, 0.22, 0.21, 0.10) # Soft Red/Orange fill
ctx.arc(to_pixel(13.67, 9.0)[0], to_pixel(13.67, 9.0)[1], 2.2 * SCALE, 0, 2 * math.pi)
ctx.fill_preserve()
ctx.set_source_rgba(0.90, 0.22, 0.21, 0.40) # Soft Red stroke
ctx.set_line_width(1.5)
ctx.set_dash([4.0, 4.0])
ctx.stroke()
ctx.restore()

# 4. Sumbu Utama Kartesius (X dan Y)
ctx.set_source_rgb(0.15, 0.20, 0.25) # Dark Charcoal
ctx.set_line_width(2.0)

# Sumbu X
ctx.move_to(ORIGIN_X, ORIGIN_Y)
ctx.line_to(ORIGIN_X + PLOT_WIDTH + 25, ORIGIN_Y)
ctx.stroke()

# Panah Sumbu X
arrow_x = ORIGIN_X + PLOT_WIDTH + 25
ctx.move_to(arrow_x, ORIGIN_Y)
ctx.line_to(arrow_x - 10, ORIGIN_Y - 5)
ctx.line_to(arrow_x - 10, ORIGIN_Y + 5)
ctx.close_path()
ctx.fill()

# Sumbu Y
ctx.move_to(ORIGIN_X, ORIGIN_Y)
ctx.line_to(ORIGIN_X, MARGIN_TOP - 20)
ctx.stroke()

# Panah Sumbu Y
arrow_y = MARGIN_TOP - 20
ctx.move_to(ORIGIN_X, arrow_y)
ctx.line_to(ORIGIN_X - 5, arrow_y + 10)
ctx.line_to(ORIGIN_X + 5, arrow_y + 10)
ctx.close_path()
ctx.fill()

# 5. Ticks & Angka Koordinat (Interval Tepat 1 Unit untuk Kedua Sumbu)
ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
ctx.set_font_size(12.0)

# Sumbu X (0 s/d 16, interval 1)
for x_val in range(X_MIN, X_MAX + 1):
    px, _ = to_pixel(x_val, 0)
    # Garis Tick
    ctx.set_source_rgb(0.2, 0.25, 0.3)
    ctx.set_line_width(1.5)
    ctx.move_to(px, ORIGIN_Y)
    ctx.line_to(px, ORIGIN_Y + 6)
    ctx.stroke()
    
    # Label Angka
    txt = str(x_val)
    extents = ctx.text_extents(txt)
    ctx.move_to(px - extents.width / 2, ORIGIN_Y + 22)
    ctx.show_text(txt)

# Sumbu Y (0 s/d 12, interval 1)
for y_val in range(Y_MIN, Y_MAX + 1):
    _, py = to_pixel(0, y_val)
    # Garis Tick
    ctx.set_source_rgb(0.2, 0.25, 0.3)
    ctx.set_line_width(1.5)
    ctx.move_to(ORIGIN_X, py)
    ctx.line_to(ORIGIN_X - 6, py)
    ctx.stroke()
    
    # Label Angka
    txt = str(y_val)
    extents = ctx.text_extents(txt)
    ctx.move_to(ORIGIN_X - 12 - extents.width, py + extents.height / 2)
    ctx.show_text(txt)

# 6. Label Sumbu
# Sumbu X Label
ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
ctx.set_font_size(13.0)
ctx.set_source_rgb(0.1, 0.15, 0.2)
x_title = "Jumlah Kunjungan Pelanggan (kali/bulan) — Sumbu X₁"
ext = ctx.text_extents(x_title)
ctx.move_to(ORIGIN_X + (PLOT_WIDTH - ext.width) / 2, ORIGIN_Y + 52)
ctx.show_text(x_title)

# Sumbu Y Label (Dirotasi 90 derajat vertikal)
ctx.save()
y_title = "Total Belanja Ternormalisasi (Ratusan Ribu Rp) — Sumbu X₂"
ext_y = ctx.text_extents(y_title)
ctx.translate(ORIGIN_X - 58, MARGIN_TOP + (PLOT_HEIGHT + ext_y.width) / 2)
ctx.rotate(-math.pi / 2)
ctx.move_to(0, 0)
ctx.show_text(y_title)
ctx.restore()

# 7. Judul Grafik & Subtitle
ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
ctx.set_font_size(17.0)
ctx.set_source_rgb(0.08, 0.12, 0.18)
title_text = "DIAGRAM KARTESIUS 2D PERILAKU PELANGGAN & HASIL K-MEANS"
ctx.move_to(ORIGIN_X, 42)
ctx.show_text(title_text)

ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
ctx.set_font_size(12.5)
ctx.set_source_rgb(0.35, 0.40, 0.45)
sub_text = "Dataset Minimarket (N=6, K=2) — Skala Sumbu Konsisten 1 : 1 (Jarak Tiap Titik Sumbu X & Y = 1 Unit)"
ctx.move_to(ORIGIN_X, 64)
ctx.show_text(sub_text)

# 8. Legend Box (Keterangan di Kanan Atas)
LEGEND_X = ORIGIN_X + PLOT_WIDTH - 340
LEGEND_Y = 16
LEGEND_W = 340
LEGEND_H = 80

# Background Legend
ctx.set_source_rgba(0.97, 0.98, 0.99, 0.95)
ctx.rectangle(LEGEND_X, LEGEND_Y, LEGEND_W, LEGEND_H)
ctx.fill_preserve()
ctx.set_source_rgb(0.80, 0.84, 0.88)
ctx.set_line_width(1.0)
ctx.stroke()

# Item 1: Klaster 1
ctx.set_source_rgb(0.12, 0.53, 0.90) # Blue
ctx.arc(LEGEND_X + 20, LEGEND_Y + 22, 6.5, 0, 2 * math.pi)
ctx.fill()
ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
ctx.set_font_size(11.5)
ctx.set_source_rgb(0.15, 0.20, 0.25)
ctx.move_to(LEGEND_X + 35, LEGEND_Y + 26)
ctx.show_text("Klaster 1 : P1, P2, P3 (Ekonomis/Rendah)")

# Item 2: Klaster 2
ctx.set_source_rgb(0.90, 0.22, 0.21) # Red
ctx.arc(LEGEND_X + 20, LEGEND_Y + 45, 6.5, 0, 2 * math.pi)
ctx.fill()
ctx.move_to(LEGEND_X + 35, LEGEND_Y + 49)
ctx.show_text("Klaster 2 : P4, P5, P6 (Loyal/Tinggi)")

# Item 3: Centroid Akhir
def draw_star(context, cx, cy, r_outer, r_inner, num_points=5):
    context.save()
    angle = -math.pi / 2
    step = math.pi / num_points
    context.move_to(cx + r_outer * math.cos(angle), cy + r_outer * math.sin(angle))
    for i in range(num_points * 2):
        r = r_outer if i % 2 == 0 else r_inner
        angle += step
        context.line_to(cx + r * math.cos(angle), cy + r * math.sin(angle))
    context.close_path()
    context.restore()

ctx.save()
draw_star(ctx, LEGEND_X + 20, LEGEND_Y + 66, 8.0, 3.5)
ctx.set_source_rgb(0.98, 0.65, 0.05) # Amber Gold
ctx.fill_preserve()
ctx.set_source_rgb(0.70, 0.40, 0.0)
ctx.set_line_width(1.0)
ctx.stroke()
ctx.restore()

ctx.move_to(LEGEND_X + 35, LEGEND_Y + 70)
ctx.show_text("Centroid Akhir : C1 (3,0; 1,5), C2 (13,67; 9,0)")

# 9. Plot Titik Data Objek Pelanggan
points = [
    # (id, x, y, cluster, label_dx, label_dy)
    ("P1", 2, 1.0, 1, -12, 22),
    ("P2", 3, 1.5, 1, -65, -12), # digeser agar tidak tabrakan dengan C1
    ("P3", 4, 2.0, 1, 14, -10),
    ("P4", 12, 8.0, 2, -72, -12),
    ("P5", 14, 9.0, 2, 14, 20),
    ("P6", 15, 10.0, 2, 14, -10)
]

for pid, px_val, py_val, clus, ldx, ldy in points:
    px, py = to_pixel(px_val, py_val)
    
    # Lingkaran Titik
    ctx.save()
    if clus == 1:
        ctx.set_source_rgb(0.12, 0.53, 0.90) # Blue
    else:
        ctx.set_source_rgb(0.90, 0.22, 0.21) # Red
        
    ctx.arc(px, py, 7.5, 0, 2 * math.pi)
    ctx.fill_preserve()
    ctx.set_source_rgb(1.0, 1.0, 1.0)
    ctx.set_line_width(2.0)
    ctx.stroke()
    ctx.restore()
    
    # Teks Label Koordinat
    ctx.save()
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(12.0)
    if clus == 1:
        ctx.set_source_rgb(0.08, 0.38, 0.70)
    else:
        ctx.set_source_rgb(0.75, 0.15, 0.15)
        
    coord_str = f"{pid}({px_val}; {py_val:.1f})"
    ctx.move_to(px + ldx, py + ldy)
    ctx.show_text(coord_str)
    ctx.restore()

# 10. Plot Centroid Akhir (C1 dan C2)
centroids = [
    # (id, x, y, label_dx, label_dy)
    ("C1", 3.0, 1.5, 16, -18),
    ("C2", 41.0 / 3.0, 9.0, -80, -22)
]

for cid, cx_val, cy_val, ldx, ldy in centroids:
    cpx, cpy = to_pixel(cx_val, cy_val)
    
    # Simbol Bintang Centroid
    ctx.save()
    draw_star(ctx, cpx, cpy, 12.0, 5.5)
    ctx.set_source_rgb(0.98, 0.65, 0.05) # Amber Gold
    ctx.fill_preserve()
    ctx.set_source_rgb(0.20, 0.15, 0.05)
    ctx.set_line_width(1.5)
    ctx.stroke()
    ctx.restore()
    
    # Label Centroid
    ctx.save()
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(12.5)
    ctx.set_source_rgb(0.85, 0.45, 0.0)
    c_str = f"{cid} ({cx_val:.2f}; {cy_val:.1f})" if cid == "C2" else f"{cid} ({cx_val:.1f}; {cy_val:.1f})"
    ctx.move_to(cpx + ldx, cpy + ldy)
    ctx.show_text(c_str)
    ctx.restore()

# Simpan ke PNG
output_path = "Week_12/images/grafik_koordinat_pelanggan_kmeans.png"
surface.write_to_png(output_path)
print(f"Berhasil menghasilkan visualisasi presisi di: {output_path}")
