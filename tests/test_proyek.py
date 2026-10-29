"""Menjalankan seluruh test case proyek.
Cara: python3 tests/test_proyek.py   (dijalankan dari folder utama proyek)"""
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.input_data import baca_dari_file, parse_nilai
from src.output import simpan_hasil
from src.proses import cek_lulus, hitung_median, hitung_rata_rata, ringkasan

FOLDER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTOH = os.path.join(FOLDER, "data", "contoh_data.txt")


def file_sementara(isi):
    f = tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8")
    f.write(isi)
    f.close()
    return f.name


def uji_file_tidak_ada():
    nilai, pesan = baca_dari_file("tidak_ada.txt")
    return (len(nilai), len(pesan))


def uji_file_ada_baris_rusak():
    nilai, pesan = baca_dari_file(file_sementara("80\nabc\n70\n"))
    return (len(nilai), len(pesan))


def uji_simpan_append():
    nama = os.path.join(tempfile.mkdtemp(), "hasil.txt")
    simpan_hasil(ringkasan([70, 80]), nama)
    simpan_hasil(ringkasan([60]), nama)
    with open(nama, encoding="utf-8") as f:
        return f.read().count("RINGKASAN NILAI")


def uji_ringkasan_kosong():
    r = ringkasan([])
    return (r["jumlah"], r["minimum"], r["maksimum"])


def uji_ringkasan_contoh():
    r = ringkasan(baca_dari_file(CONTOH)[0])
    return (r["lulus"], r["rata_rata"])


def uji_file_contoh():
    return len(baca_dari_file(CONTOH)[0])


def coba(fungsi):
    try:
        return fungsi()
    except Exception as e:
        return type(e).__name__


TESTS = [
    ("TC01", "Rata-rata", "[70, 80, 90]", lambda: hitung_rata_rata([70, 80, 90]), 80.0),
    ("TC02", "Kelulusan", "60 (batas)", lambda: cek_lulus(60), True),
    ("TC03", "Kelulusan", "59", lambda: cek_lulus(59), False),
    ("TC04", "Rata-rata", "[] (kosong)", lambda: hitung_rata_rata([]), 0),
    ("TC05", "Validasi", "'abc'", lambda: parse_nilai("abc"), "ValueError"),
    ("TC06", "Validasi", "'120'", lambda: parse_nilai("120"), "ValueError"),
    ("TC07", "Validasi", "'-1'", lambda: parse_nilai("-1"), "ValueError"),
    ("TC08", "Validasi", "'85,5'", lambda: parse_nilai("85,5"), 85.5),
    ("TC09", "File", "file tidak ada", uji_file_tidak_ada, (0, 1)),
    ("TC10", "File", "contoh_data.txt", uji_file_contoh, 8),
    ("TC11", "Median", "[80, 60, 90, 70]", lambda: hitung_median([80, 60, 90, 70]), 75.0),
    ("TC12", "Ringkasan", "[] (kosong)", uji_ringkasan_kosong, (0, None, None)),
    ("TC13", "Ringkasan", "contoh_data.txt", uji_ringkasan_contoh, (6, 72.5)),
    ("TC14", "File", "baris rusak 'abc'", uji_file_ada_baris_rusak, (2, 1)),
    ("TC15", "Simpan", "2x simpan (append)", uji_simpan_append, 2),
]

if __name__ == "__main__":
    gagal = 0
    print(f"{'ID':<5}{'Fitur':<11}{'Input':<22}{'Expected':<18}{'Actual':<18}Status")
    for kode, fitur, masukan, fungsi, harapan in TESTS:
        hasil = coba(fungsi)
        ok = hasil == harapan
        gagal += not ok
        print(f"{kode:<5}{fitur:<11}{masukan:<22}{str(harapan):<18}{str(hasil):<18}{'PASS' if ok else 'FAIL'}")
    print(f"\nRingkasan: {len(TESTS) - gagal}/{len(TESTS)} PASS")
    sys.exit(1 if gagal else 0)
