# Event Organizer API

## Deskripsi Proyek

Event Organizer API adalah sebuah sistem berbasis **FastAPI** yang dirancang untuk mengelola berbagai data terkait penyelenggaraan acara, seperti informasi event, peserta, klien, staf, vendor, inventaris, dan keuangan. Sistem ini juga memungkinkan ekspor data acara ke dalam format JSON.
API ini dikembangkan dengan menerapkan pendekatan **Table-driven Construction Pattern**, yang membantu menjaga struktur kode agar tetap modular, konsisten, dan mudah untuk dikembangkan lebih lanjut.

## Fitur Utama

- Manajemen Event (buat event, tambah peserta, update RSVP)
- Manajemen Klien, Vendor, dan Staf
- Inventaris perlengkapan acara
- Pencatatan Keuangan (pemasukan dan pengeluaran)
- Ekspor data Event
- Validasi data otomatis dengan Pydantic
- Penanganan status RSVP menggunakan Enum

## Table-driven Construction Pattern

**Table-driven Construction** adalah metode pemrograman di mana:
- **Logika program dikendalikan oleh struktur data (tabel)**, bukan pernyataan kondisional panjang.
- Struktur ini memudahkan pengelolaan aturan dan mempercepat pengembangan.
- Pendekatan ini meminimalisasi hardcoding dan memudahkan testing.

Penerapan dalam proyek ini:
1. **Model data** dibuat menggunakan `Pydantic` untuk validasi otomatis.
2. **Enum** digunakan untuk mengatur nilai yang valid (seperti `RSVPStatus`, `FinanceType`, `Confirmation`).
3. Data disimpan sementara dalam **struktur data Python (List)** sebagai representasi tabel.
4. **Router FastAPI** diatur dengan pola endpoint yang konsisten dan modular.
5. **Prefix dan tags** digunakan untuk pengelompokan endpoint dalam dokumentasi.

### Struktur Proyek
event_api/
├── models/           # Model data dengan validasi Pydantic
├── routers/          # API Endpoints dengan FastAPI Router
├── services/         # Business logic services
├── utils/            # Fungsi dan utilitas pendukung
└── main.py           # Aplikasi utama dan router registration

### Kontributor
- Nama: Tiurma Grace Angelina Sihaloho - 2311104042
- Bagian yang Dikerjakan: FastAPI dan Table-driven Construction

### Instalasi dan Menjalankan

1. Pastikan Python 3.8+ terinstall lebih baru telah terpasang.
2. Buat dan aktifkan virtual environment Python:
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # Linux/Mac
   python3 -m venv .venv
   source .venv/bin/activate

2. Install dependensi:
pip install fastapi uvicorn
pip install fastapi "pydantic>=2.0" uvicorn
pip install tabulate

3. Jalankan server FastAPI:
uvicorn main:app --reload

4. Akses dokumentasi API di browser:
Dokumentasi Swagger: http://127.0.0.1:8000/docs

Dokumentasi ReDoc: http://127.0.0.1:8000/redoc


**Daftar Endpoint**

| No | Endpoint                          | Method       |Fungsi                                        |
| 1  | `/events/`                        | `POST`       | Membuat event baru                           |
| 2  | `/events/`                        | `GET`        | Menampilkan semua event                      |
| 3  | `/events/{event_id}/participants` | `POST`       | Menambahkan peserta ke event                 |
| 4  | `/events/{event_id}/rsvp`         | `PUT`        | Mengubah status RSVP peserta                 |
| 5  | `/clients/`                       | `POST`       | Menambahkan client baru                      |
| 6  | `/clients/`                       | `GET`        | Menampilkan semua client                     |
| 7  | `/export/events`                  | `GET`        | Mengekspor data semua event dalam format JSON|
| 8  | `/finance/`                       | `POST`       | Menambahkan catatan keuangan                 |
| 9  | `/finance/`                       | `GET`        | Menampilkan semua catatan keuangan           |
| 10 | `/finance/summary`                | `GET`        | Ringkasan pemasukan, pengeluaran, dan saldo  |
| 11 | `/vendors/`                       | `POST`       | Menambahkan vendor baru                      |
| 12 | `/vendors/`                       | `GET`        | Menampilkan semua vendor                     |
| 13 | `/staffs/`                        | `POST`       | Menambahkan staff baru                       |
| 14 | `/staffs/`                        | `GET`        | Menampilkan semua staff                      |
| 15 | `/inventories/`                   | `POST & GET` | Menambahkan dan menampilkan item inventaris  |
