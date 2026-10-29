# Bug Log

| ID | Gejala | Test | Lokasi | Penyebab | Perbaikan | Status |
|---|---|---|---|---|---|---|
| BUG-01 | Rata-rata list kosong menghasilkan `ZeroDivisionError` | TC04, TC12 | `src/proses.py`, `hitung_rata_rata` | Pembagian dengan `len(nilai)` = 0 tanpa pemeriksaan | Tambah `if not nilai: return 0` | Closed |
| BUG-02 | Nilai 60 dinyatakan tidak lulus; jumlah lulus pada data contoh 5, seharusnya 6 | TC02, TC13 | `src/proses.py`, `cek_lulus` | Operator `>` mengecualikan nilai tepat di batas | `>` diganti `>=` | Closed |
| BUG-03 | `ringkasan([])` melempar `ValueError` pada `min()`, dan pembagian nol pada `persen_lulus` | TC12 | `src/proses.py`, `ringkasan` | `min`, `max`, dan persentase tidak memeriksa data kosong. Bug ini baru terlihat setelah BUG-01 diperbaiki karena sebelumnya tertutup oleh `ZeroDivisionError`. | `min(nilai) if nilai else None`, `max(...)` serupa, dan persentase 0 jika `jumlah` = 0 | Closed |

Versi awal `proses.py` disimpan di `docs/bukti_bug/proses_versi_awal.py`.
Perbaikan dilakukan dengan perubahan minimal pada `src/proses.py`, lalu seluruh test case dijalankan ulang (15/15 PASS).
