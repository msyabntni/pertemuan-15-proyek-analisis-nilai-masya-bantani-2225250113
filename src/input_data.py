"""Pengambilan dan validasi data nilai."""

NILAI_MIN = 0
NILAI_MAKS = 100


def parse_nilai(teks):
    """Mengubah teks menjadi angka dalam rentang 0-100.

    Koma desimal diterima (85,5). Melempar ValueError jika bukan angka
    atau berada di luar rentang.
    """
    teks = teks.strip().replace(",", ".")
    try:
        nilai = float(teks)
    except ValueError:
        raise ValueError(f"'{teks}' bukan angka")
    if not NILAI_MIN <= nilai <= NILAI_MAKS:
        raise ValueError(f"nilai {teks} di luar rentang {NILAI_MIN}-{NILAI_MAKS}")
    return nilai


def baca_dari_file(nama_file):
    """Membaca nilai dari file teks (satu nilai per baris).

    Mengembalikan (daftar_nilai, daftar_pesan). Baris kosong diabaikan,
    baris tidak valid dilewati dengan pesan, dan file yang tidak ada
    ditangani tanpa membuat program berhenti.
    """
    nilai, pesan = [], []
    try:
        with open(nama_file, encoding="utf-8") as f:
            for no, baris in enumerate(f, start=1):
                if not baris.strip():
                    continue
                try:
                    nilai.append(parse_nilai(baris))
                except ValueError as e:
                    pesan.append(f"Baris {no} dilewati: {e}")
    except FileNotFoundError:
        pesan.append(f"File tidak ditemukan: {nama_file}")
    return nilai, pesan


def minta_nilai():
    """Meminta nilai dari pengguna satu per satu sampai mengetik 'selesai'."""
    nilai = []
    print("Masukkan nilai (0-100) satu per satu. Ketik 'selesai' untuk berhenti.")
    while True:
        try:
            teks = input(f"Nilai ke-{len(nilai) + 1}: ")
        except EOFError:
            break
        if teks.strip().lower() == "selesai":
            break
        try:
            nilai.append(parse_nilai(teks))
        except ValueError as e:
            print("Input tidak valid:", e)
    return nilai
