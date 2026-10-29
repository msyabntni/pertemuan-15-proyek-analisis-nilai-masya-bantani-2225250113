"""Analisis Nilai Siswa - program utama (menu)."""
import os

from src.input_data import baca_dari_file, minta_nilai
from src.output import simpan_hasil, tampilkan
from src.proses import ringkasan

FOLDER = os.path.dirname(os.path.abspath(__file__))
FILE_CONTOH = os.path.join(FOLDER, "data", "contoh_data.txt")
FILE_HASIL = os.path.join(FOLDER, "data", "hasil_analisis.txt")

MENU = """
=== ANALISIS NILAI SISWA ===
1. Input nilai manual
2. Baca nilai dari file (data/contoh_data.txt)
3. Tampilkan ringkasan
4. Simpan ringkasan ke file
5. Keluar"""


def main():
    nilai = []
    while True:
        print(MENU)
        try:
            pilihan = input("Pilih menu (1-5): ").strip()
        except EOFError:
            break
        if pilihan == "1":
            nilai = minta_nilai()
            print(f"{len(nilai)} nilai tersimpan.")
        elif pilihan == "2":
            nilai, pesan = baca_dari_file(FILE_CONTOH)
            for p in pesan:
                print(p)
            print(f"{len(nilai)} nilai berhasil dibaca.")
        elif pilihan == "3":
            tampilkan(ringkasan(nilai))
        elif pilihan == "4":
            print("Tersimpan di:", simpan_hasil(ringkasan(nilai), FILE_HASIL))
        elif pilihan == "5":
            print("Terima kasih.")
            break
        else:
            print("Pilihan tidak valid, masukkan angka 1-5.")


if __name__ == "__main__":
    main()
