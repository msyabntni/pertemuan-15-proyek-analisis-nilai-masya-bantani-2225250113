"""Logika inti: statistik dan kelulusan."""

BATAS_LULUS = 60


def hitung_rata_rata(nilai):
    """Rata-rata list numerik. List kosong menghasilkan 0."""
    if not nilai:
        return 0
    return sum(nilai) / len(nilai)


def cek_lulus(nilai, batas=BATAS_LULUS):
    """True jika nilai mencapai batas (nilai tepat di batas dinyatakan lulus)."""
    return nilai >= batas


def hitung_median(nilai):
    """Median list numerik. List kosong menghasilkan None."""
    if not nilai:
        return None
    urut = sorted(nilai)
    n = len(urut)
    tengah = n // 2
    if n % 2 == 1:
        return urut[tengah]
    return (urut[tengah - 1] + urut[tengah]) / 2


def ringkasan(nilai, batas=BATAS_LULUS):
    """Dictionary ringkasan statistik. Aman untuk list kosong."""
    jumlah = len(nilai)
    lulus = sum(1 for x in nilai if cek_lulus(x, batas))
    return {
        "jumlah": jumlah,
        "rata_rata": round(hitung_rata_rata(nilai), 2),
        "median": hitung_median(nilai),
        "minimum": min(nilai) if nilai else None,
        "maksimum": max(nilai) if nilai else None,
        "lulus": lulus,
        "tidak_lulus": jumlah - lulus,
        "persen_lulus": round(lulus / jumlah * 100, 1) if jumlah else 0,
    }
