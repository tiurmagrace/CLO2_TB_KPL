def tampilkan_event(event):
    print("=" * 40)
    print(f"Event   : {event.title}")
    print(f"Lokasi  : {event.location}")
    print(f"Tanggal : {event.date}\n")
    print("Peserta:")
    if event.participants:
        for p in event.participants:
            print(f"- {p.name:<8} | {p.status.value}")
    else:
        print("- (belum ada peserta)")
    hadir = sum(1 for p in event.participants if p.status.name == "ATTENDING")
    tidak = sum(1 for p in event.participants if p.status.name == "NOT_ATTENDING")
    print(f"\nTotal peserta: {len(event.participants)}")
    print(f"Hadir        : {hadir}")
    print(f"Tidak Hadir  : {tidak}")
