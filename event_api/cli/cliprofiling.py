import time
from getpass import getpass
from memory_profiler import profile
from event_api.cli.config import ADMIN
from event_api.cli.handlers import (
    event_handler,
    client_handler,
    vendor_handler,
    staff_handler,
    inventory_handler,
    finance_handler,
    export_handler,
)

ENTITY = {
    "1": ("Tambah Event", event_handler.tambah_event),
    "2": ("Tambah Peserta", event_handler.tambah_peserta),
    "3": ("Atur RSVP", event_handler.atur_rsvp),
    "4": ("Lihat Events", event_handler.lihat_events),
    "5": ("Export Data", export_handler.export_data),
    "6": ("Tambah Klien", client_handler.tambah_client),
    "7": ("Lihat Daftar Klien", client_handler.lihat_clients),
    "8": ("Tambah Vendor", vendor_handler.tambah_vendor),
    "9": ("Lihat Daftar Vendor", vendor_handler.lihat_vendors),
    "10": ("Tambah Staff", staff_handler.tambah_staff),
    "11": ("Lihat Daftar Staff", staff_handler.lihat_staff),
    "12": ("Tambah Inventaris", inventory_handler.tambah_inventaris),
    "13": ("Lihat Daftar Inventaris", inventory_handler.lihat_inventaris),
    "14": (
        "Tambah Catatan Keuangan",
        finance_handler.tambah_catatan_keuangan,
    ),
    "15": (
        "Lihat Laporan Keuangan",
        finance_handler.lihat_laporan_keuangan,
    ),
    "16": (
        "Keluar",
        lambda: print("Terima kasih telah menggunakan CLI Event Organizer!"),
    ),
}


def tampilkan_banner():
    """Menampilkan banner aplikasi."""
    print("\033c", end="")  # ANSI escape code untuk membersihkan terminal
    print("""
    =====================================
    =        EVENT ORGANIZER CLI        =
    =====================================
    """)


def login():
    """Menangani proses login pengguna."""
    print("\n===== LOGIN EVENT ORGANIZER CLI =====")
    username = input("Username: ")
    password = getpass("Password: ")

    return username == ADMIN["username"] and password == ADMIN["password"]


@profile
def main():
    """Fungsi utama untuk menjalankan aplikasi CLI."""
    start = time.perf_counter()
    tampilkan_banner()

    if not login():
        print("Login gagal!")
        return

    while True:
        tampilkan_banner()

        print("\n=== MENU UTAMA ===")

        print("\n--- Manajemen Event ---")
        for i in range(1, 6):
            print(f"{i}. {ENTITY[str(i)][0]}")

        print("\n--- Manajemen Klien & Vendor ---")
        for i in range(6, 10):
            print(f"{i}. {ENTITY[str(i)][0]}")

        print("\n--- Manajemen Staff ---")
        for i in range(10, 12):
            print(f"{i}. {ENTITY[str(i)][0]}")

        print("\n--- Manajemen Inventaris ---")
        for i in range(12, 14):
            print(f"{i}. {ENTITY[str(i)][0]}")

        print("\n--- Manajemen Keuangan ---")
        for i in range(14, 16):
            print(f"{i}. {ENTITY[str(i)][0]}")

        print("\n--- Lainnya ---")
        print("16. Keluar")

        pilih = input("\nPilih menu: ").strip()

        if pilih == "16":
            ENTITY["16"][1]()
            break

        if pilih in ENTITY:
            try:
                ENTITY[pilih][1]()
            except Exception as e:
                print(f"Terjadi kesalahan: {e}")

            input("\nTekan Enter untuk kembali ke menu...")
        else:
            print("⚠ Pilihan tidak valid!")
            input("\nTekan Enter untuk lanjut...")

    end = time.perf_counter()
    print(f"\n✅ Total waktu eksekusi: {end - start:.2f} detik")


if __name__ == "__main__":
    main = profile(main)
    main()
