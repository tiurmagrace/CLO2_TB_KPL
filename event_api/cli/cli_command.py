import re
import requests
from commands import (
    AddEventCommand, ViewEventsCommand, ExportDataCommand,
    AddParticipantCommand, SetRSVPCommand
)

def parse_command(text):
    text = text.lower()
    if m := re.search(r'tambah event (.*?) di (.*?) tanggal (.*)', text):
        return AddEventCommand(requests, {
            'title': m[1], 'location': m[2], 'date': format_date(m[3])
        })
    if re.search(r'(lihat|tampilkan|show) event', text):
        return ViewEventsCommand(requests)
    if re.search(r'(export|ekspor) data', text):
        return ExportDataCommand(requests)
    if m := re.search(r'tambah peserta (.*?) ke event (.*)', text):
        return AddParticipantCommand(requests, {
            'name': m[1], 'event_name': m[2]
        })
    if m := re.search(r'atur rsvp (.*?) (hadir|tidak hadir) untuk event (.*)', text):
        return SetRSVPCommand(requests, {
            'name': m[1], 'status': 'ya' if 'hadir' in m[2] else 'tidak', 'event_name': m[3]
        })
    return None

def format_date(date_str):
    bulan = {
        'januari': '01', 'februari': '02', 'maret': '03', 'april': '04', 'mei': '05', 'juni': '06',
        'juli': '07', 'agustus': '08', 'september': '09', 'oktober': '10', 'november': '11', 'desember': '12'
    }
    if m := re.search(r'(\d{1,2})\s+(\w+)\s+(\d{4})', date_str):
        return f"{m[3]}-{bulan.get(m[2], '01')}-{int(m[1]):02d}"
    return date_str

def main():
    print("📋 CLI - Command Pattern Only")
    while True:
        try:
            text = input("\n📝 Ketik perintahmu: ").strip()
            command = parse_command(text)
            if command:
                result = command.execute()
                print(f"✅ {result}")
            else:
                print("❌ Perintah tidak dikenali.")
        except KeyboardInterrupt:
            print("\n👋 Terima kasih, sampai jumpa!")
            break

if __name__ == '__main__':
    main()
