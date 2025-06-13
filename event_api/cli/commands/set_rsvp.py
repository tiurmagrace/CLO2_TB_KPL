from .base import Command

class SetRSVPCommand(Command):
    def __init__(self, api_client, rsvp_data):
        self.api_client = api_client
        self.rsvp_data = rsvp_data

    def execute(self):
        try:
            response = self.api_client.post("http://localhost:8000/rsvp", json=self.rsvp_data)
            return response.json().get("message", "RSVP berhasil disimpan.")
        except Exception as e:
            return f"Gagal mengatur RSVP: {e}"