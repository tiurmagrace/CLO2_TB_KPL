from core.event_manager import *
from lib.utils import tampilkan_event

if __name__ == "__main__":
    while True:
        print("\n=== CLI EVENT PLANNER ===")
        print("1. Tambah Event")
        print("2. Tambah Peserta ke Event")
        print("3. Atur RSVP")
        print("4. Lihat Semua Event")
        print("5. Export Data ke File")
        print("6. Keluar")

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
            print("Terima kasih! Sampai jumpa.")
            break

        else:
            print("Pilihan tidak valid!")
