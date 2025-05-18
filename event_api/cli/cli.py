def main():
    tampilkan_banner()
    if not login(): return print("\u274C Login gagal!")
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        tampilkan_banner()
        print("\n=== MENU UTAMA ===")
        print("\n--- Manajemen Event ---")
        for i in range(1, 6): print(f"{i}. {ENTITY[str(i)][0]}")
        print("\n--- Manajemen Klien & Vendor ---")
        for i in range(6, 10): print(f"{i}. {ENTITY[str(i)][0]}")
        print("\n--- Manajemen Staff ---")
        for i in range(10, 12): print(f"{i}. {ENTITY[str(i)][0]}")
        print("\n--- Manajemen Inventaris ---")
        for i in range(12, 14): print(f"{i}. {ENTITY[str(i)][0]}")
        print("\n--- Manajemen Keuangan ---")
        for i in range(14, 16): print(f"{i}. {ENTITY[str(i)][0]}")
        print("\n--- Lainnya ---")
        print("16. Keluar")

        pilih = input("\nPilih menu: ").strip()
        if pilih in ENTITY:
            try:
                ENTITY[pilih][1]()
            except Exception as e:
                print(f"\u274C Terjadi kesalahan: {e}")
            input("\nTekan Enter untuk kembali ke menu...")
        else:
            print("\u26A0\ufe0f Pilihan tidak valid!")
            input("\nTekan Enter untuk lanjut...")

if _name_ == "_main_":
    main()