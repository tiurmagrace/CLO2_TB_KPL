from .base import Command

class AddEventCommand(Command):
    def __init__(self, api_client, event_data):
        self.api_client = api_client
        self.event_data = event_data

    def execute(self):
        try:
            response = self.api_client.post("http://localhost:8000/events", json=self.event_data)
            return response.json().get("message", "Event berhasil ditambahkan.")
        except Exception as e:
            return f"Gagal menambahkan event: {e}"