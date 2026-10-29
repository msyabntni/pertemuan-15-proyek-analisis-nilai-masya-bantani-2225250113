"""Tampilan dan penyimpanan hasil."""
import os


def format_ringkasan(r):
    """Mengubah dictionary ringkasan menjadi teks siap tampil."""
    if r["jumlah"] == 0:
        return "RINGKASAN NILAI\nBelum ada data nilai."
    return (
        "RINGKASAN NILAI\n"
        f"Jumlah data   : {r['jumlah']}\n"
        f"Rata-rata     : {r['rata_rata']}\n"
        f"Median        : {r['median']}\n"
        f"Minimum       : {r['minimum']}\n"
        f"Maksimum      : {r['maksimum']}\n"
        f"Lulus         : {r['lulus']} ({r['persen_lulus']}%)\n"
        f"Tidak lulus   : {r['tidak_lulus']}"
    )


def tampilkan(r):
    print(format_ringkasan(r))


def simpan_hasil(r, nama_file):
    """Menambahkan ringkasan ke file (mode append agar riwayat tidak hilang)."""
    folder = os.path.dirname(nama_file)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(nama_file, "a", encoding="utf-8") as f:
        f.write(format_ringkasan(r) + "\n\n")
    return nama_file
