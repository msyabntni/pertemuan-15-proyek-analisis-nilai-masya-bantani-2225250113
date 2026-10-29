"""Versi awal src/proses.py (memuat bug BUG-01, BUG-02, BUG-03).
Disimpan sebagai bukti proses debugging. Tidak dipakai oleh program."""

BATAS_LULUS = 60


def hitung_rata_rata(nilai):
    return sum(nilai) / len(nilai)


def cek_lulus(nilai, batas=BATAS_LULUS):
    return nilai > batas


def hitung_median(nilai):
    if not nilai:
        return None
    urut = sorted(nilai)
    n = len(urut)
    tengah = n // 2
    if n % 2 == 1:
        return urut[tengah]
    return (urut[tengah - 1] + urut[tengah]) / 2


def ringkasan(nilai, batas=BATAS_LULUS):
    jumlah = len(nilai)
    lulus = sum(1 for x in nilai if cek_lulus(x, batas))
    return {
        "jumlah": jumlah,
        "rata_rata": round(hitung_rata_rata(nilai), 2),
        "median": hitung_median(nilai),
        "minimum": min(nilai),
        "maksimum": max(nilai),
        "lulus": lulus,
        "tidak_lulus": jumlah - lulus,
        "persen_lulus": round(lulus / jumlah * 100, 1),
    }
