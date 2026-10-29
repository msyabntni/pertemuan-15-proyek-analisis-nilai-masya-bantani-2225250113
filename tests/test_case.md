# Test Case - Analisis Nilai Siswa

Dijalankan dengan: `python3 tests/test_proyek.py`

| ID | Fitur | Jenis | Input | Expected | Actual Awal | Status Awal | Actual Akhir | Status Akhir |
|---|---|---|---|---|---|---|---|---|
| TC01 | Rata-rata | Normal | `[70, 80, 90]` | 80.0 | 80.0 | PASS | 80.0 | PASS |
| TC02 | Kelulusan | Boundary | `60` | True | False | FAIL | True | PASS |
| TC03 | Kelulusan | Di bawah batas | `59` | False | False | PASS | False | PASS |
| TC04 | Rata-rata | Kosong | `[]` | 0 | ZeroDivisionError | FAIL | 0 | PASS |
| TC05 | Validasi | Invalid | `'abc'` | ValueError | ValueError | PASS | ValueError | PASS |
| TC06 | Validasi | Invalid | `'120'` | ValueError | ValueError | PASS | ValueError | PASS |
| TC07 | Validasi | Invalid | `'-1'` | ValueError | ValueError | PASS | ValueError | PASS |
| TC08 | Validasi | Normal | `'85,5'` | 85.5 | 85.5 | PASS | 85.5 | PASS |
| TC09 | File | File tidak ada | `tidak_ada.txt` | (0 nilai, 1 pesan) | (0, 1) | PASS | (0, 1) | PASS |
| TC10 | File | Normal | `contoh_data.txt` | 8 nilai | 8 | PASS | 8 | PASS |
| TC11 | Median | Normal (genap) | `[80, 60, 90, 70]` | 75.0 | 75.0 | PASS | 75.0 | PASS |
| TC12 | Ringkasan | Kosong | `[]` | (0, None, None) | ZeroDivisionError | FAIL | (0, None, None) | PASS |
| TC13 | Ringkasan | Data contoh | `contoh_data.txt` | (6 lulus, rata-rata 72.5) | (5, 72.5) | FAIL | (6, 72.5) | PASS |
| TC14 | File | Baris tidak valid | `80, abc, 70` | (2 nilai, 1 pesan) | (2, 1) | PASS | (2, 1) | PASS |
| TC15 | Simpan | Append | 2x simpan | 2 blok ringkasan | 2 | PASS | 2 | PASS |

Hasil awal: 11/15 PASS (4 FAIL). Hasil akhir setelah perbaikan: 15/15 PASS.
Test yang sudah PASS sebelum perbaikan tetap PASS sesudahnya, jadi tidak ada regresi.
