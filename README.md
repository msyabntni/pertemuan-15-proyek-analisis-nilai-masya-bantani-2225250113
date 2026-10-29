# Analisis Nilai Siswa - Proyek Akhir Pertemuan 15

| **Keterangan** | **Data** |
|---|---|
| **Nama** | Masya Bantani |
| **NIM** | 2225250113 |
| **Kelas** | 3-E |
| **Jurusan** | Pendidikan Matematika |

## Deskripsi

Program Python berbasis menu untuk menganalisis sekumpulan nilai siswa. Pengguna sasaran adalah guru atau calon guru matematika yang ingin melihat ringkasan nilai kelas dengan cepat, yaitu rata-rata, median, nilai tertinggi dan terendah, serta jumlah siswa yang lulus.

## Fitur

- Input nilai manual dengan validasi (harus angka 0-100, koma desimal diterima).
- Membaca nilai dari file teks; baris tidak valid dilewati dengan pesan, file yang tidak ada ditangani tanpa program berhenti.
- Ringkasan statistik: jumlah, rata-rata, median, minimum, maksimum, jumlah dan persentase lulus (batas lulus 60).
- Menyimpan ringkasan ke `data/hasil_analisis.txt` (mode append, riwayat tidak tertimpa).
- Aman untuk data kosong.

## Persyaratan

- Python 3.x (tanpa library tambahan)

## Cara Menjalankan

```
git clone https://github.com/USERNAME/pertemuan-15-proyek-analisis-nilai-2225250075.git
cd pertemuan-15-proyek-analisis-nilai-2225250075
python3 main.py
```

Di Windows, gunakan `python main.py` bila `python3` tidak dikenali. Untuk mencoba cepat, pilih menu 2 (baca `data/contoh_data.txt`), lalu menu 3 untuk melihat ringkasan.

Menjalankan seluruh test case:

```
python3 tests/test_proyek.py
```

## Struktur Folder

```
pertemuan-15-proyek-analisis-nilai-2225250113/
|-- README.md
|-- .gitignore
|-- main.py                  (menu utama)
|-- src/
|   |-- __init__.py
|   |-- input_data.py        (input, validasi, baca file)
|   |-- proses.py            (statistik dan kelulusan)
|   `-- output.py            (tampilan dan simpan hasil)
|-- data/
|   `-- contoh_data.txt      (data contoh 8 nilai)
|-- tests/
|   |-- test_case.md         (tabel test case dan hasil)
|   `-- test_proyek.py       (menjalankan 15 test case)
`-- docs/
    |-- bug_log.md           (catatan bug dan perbaikan)
    `-- bukti_bug/proses_versi_awal.py
```

## Test Case

Ada 15 test case yang mencakup kondisi normal, boundary, invalid, kosong, dan file. Tabel lengkap ada di [tests/test_case.md](tests/test_case.md). Cuplikan:

| ID | Fitur | Input | Expected | Actual Awal | Actual Akhir | Status Akhir |
|---|---|---|---|---|---|---|
| TC01 | Rata-rata | `[70, 80, 90]` | 80.0 | 80.0 | 80.0 | PASS |
| TC02 | Kelulusan | `60` | True | False | True | PASS |
| TC04 | Rata-rata | `[]` | 0 | ZeroDivisionError | 0 | PASS |
| TC05 | Validasi | `'abc'` | ValueError | ValueError | ValueError | PASS |
| TC12 | Ringkasan | `[]` | (0, None, None) | ZeroDivisionError | (0, None, None) | PASS |
| TC13 | Ringkasan | `contoh_data.txt` | 6 lulus, rata-rata 72.5 | 5 lulus | 6 lulus | PASS |

Hasil awal 11/15 PASS. Setelah tiga bug diperbaiki, hasil akhir 15/15 PASS tanpa regresi.

## Bug yang Ditemukan

| ID | Ringkasan | Status |
|---|---|---|
| BUG-01 | Rata-rata data kosong menyebabkan `ZeroDivisionError` | Closed |
| BUG-02 | Operator `>` pada kelulusan membuat nilai 60 tidak lulus | Closed |
| BUG-03 | `min`/`max`/persentase tidak aman untuk data kosong | Closed |

Detail penyebab dan perbaikan ada di [docs/bug_log.md](docs/bug_log.md).

## Known Issues

- Data hanya tersimpan selama program berjalan; ringkasan baru tersimpan permanen bila memilih menu 4.
- Batas lulus masih tetap 60 (konstanta `BATAS_LULUS` di `src/proses.py`) dan belum bisa diubah dari menu.
- Menu 2 hanya membaca `data/contoh_data.txt`.

## Anggota dan Kontribusi

| Nama | NIM | Kontribusi |
|---|---|---|
| Masya Bantani | 2225250113 | Perancangan, implementasi, pengujian, debugging, dan dokumentasi |

## Referensi/Bantuan

- Dokumentasi resmi Python 3 dan VS Code.
- Think Python (Downey, 2015).
- Bantuan AI untuk menyusun struktur proyek, contoh kode, dan dokumentasi. Algoritma, fungsi utama, test case, dan bug yang diperbaiki sudah saya baca dan pahami.
