from .base import Command

class ViewEventsCommand(Command):
    def __init__(self, api_client):
        self.api_client = api_client

    def execute(self):
        try:
            response = self.api_client.get("http://localhost:8000/events")
            events = response.json()
            if not events:
                return "Belum ada event."
            return "\n".join([f"- {e['title']} di {e['location']} pada {e['date']}" for e in events])
        except Exception as e:
            return f"Gagal mengambil daftar event: {e}"