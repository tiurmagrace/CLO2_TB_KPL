from core.event_manager import *
from core.management import (
    tambah_klien, tambah_vendor, tambah_staff, 
    tambah_inventaris, tambah_keuangan, laporan_keuangan
)
from lib.utils import tampilkan_event

# --- fungsi login ---
def login():
    admin_username = "admin"
    admin_password = "1234"

    print("=== LOGIN ADMIN ===")
    username = input("Username: ")
    password = input("Password: ")

    if username == admin_username and password == admin_password:
        print("\nLogin berhasil!\n")
        return True
    else:
        print("\nUsername atau password salah. Akses ditolak.\n")
        return False

# --- program utama ---
if __name__ == "__main__":
    if not login():
        exit()

    while True:
        print("\n=== CLI EVENT ORGANIZER ===")
        print("1. Tambah Event")
        print("2. Tambah Peserta ke Event")
        print("3. Atur RSVP")
        print("4. Lihat Semua Event")
        print("5. Export Data ke File")
        print("6. Tambah Klien")
        print("7. Tambah Vendor")
        print("8. Tambah Staff")
        print("9. Tambah Inventaris")
        print("10. Tambah Catatan Keuangan")
        print("11. Lihat Laporan Keuangan")
        print("12. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            title = input("Judul Event: ")
            location = input("Lokasi      : ")
            date = input("Tanggal     : ")
            event = tambah_event(title, location, date)
            print("\nEvent berhasil ditambahkan!")
            print(f"Judul   : {event.title}")
            print(f"Lokasi  : {event.location}")
            print(f"Tanggal : {event.date}")
            print("Peserta : (belum ada peserta)")

        elif pilih == "2":
            if not events:
                print("Belum ada event.")
                continue
            for i, e in enumerate(events):
                print(f"[{i+1}] {e.title}")
            idx = int(input("Pilih nomor event: ")) - 1
            name = input("Nama Peserta: ")
            tambah_peserta(idx, name)
            print(f"Peserta {name} berhasil ditambahkan ke event '{events[idx].title}'.")

        elif pilih == "3":
            if not events:
                print("Belum ada event.")
                continue
            for i, e in enumerate(events):
                print(f"[{i+1}] {e.title}")
            idx = int(input("\nPilih event: ")) - 1
            if not events[idx].participants:
                print("Belum ada peserta.")
                continue
            for p in events[idx].participants:
                print(f"- {p.name:<8} | Status: {p.status.value}")
            nama = input("\nMasukkan nama peserta: ")
            konfirmasi = input("Konfirmasi kehadiran? (ya/tidak): ")
            if atur_rsvp(idx, nama, konfirmasi):
                print("Status berhasil diperbarui!")
            else:
                print("Peserta tidak ditemukan.")

        elif pilih == "4":
            if not events:
                print("Belum ada event.")
                continue
            for e in events:
                tampilkan_event(e)

        elif pilih == "5":
            file = export_data()
            print(f"\nSemua data berhasil diekspor ke file:\n./{file}")

        elif pilih == "6":
            name = input("Nama Klien : ")
            contact = input("Kontak     : ")
            address = input("Alamat     : ")
            klien = tambah_klien(name, contact, address)
            print(f"Klien '{klien.name}' berhasil ditambahkan.")

        elif pilih == "7":
            name = input("Nama Vendor : ")
            service = input("Layanan     : ")
            contact = input("Kontak      : ")
            vendor = tambah_vendor(name, service, contact)
            print(f"Vendor '{vendor.name}' berhasil ditambahkan.")

        elif pilih == "8":
            name = input("Nama Staff : ")
            role = input("Peran      : ")
            staff = tambah_staff(name, role)
            print(f"Staff '{staff.name}' berhasil ditambahkan.")

        elif pilih == "9":
            name = input("Nama Barang Inventaris: ")
            item = tambah_inventaris(name)
            print(f"Inventaris '{item.name}' berhasil ditambahkan.")

        elif pilih == "10":
            description = input("Deskripsi   : ")
            amount = float(input("Jumlah (Rp) : "))
            tipe = input("Tipe (Income/Expense): ").lower()
            record = tambah_keuangan(description, amount, tipe)
            print(f"Catatan keuangan '{record.description}' berhasil ditambahkan.")

        elif pilih == "11":
            laporan_keuangan()

        elif pilih == "12":
            print("Terima kasih! Sampai jumpa.")
            break

        else:
            print("Pilihan tidak valid!")