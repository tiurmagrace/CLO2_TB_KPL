from .base import Command

class AddParticipantCommand(Command):
    def __init__(self, api_client, participant_data):
        self.api_client = api_client
        self.participant_data = participant_data

    def execute(self):
        try:
            response = self.api_client.post("http://localhost:8000/participants", json=self.participant_data)
            return response.json().get("message", "Peserta berhasil ditambahkan.")
        except Exception as e:
            return f"Gagal menambahkan peserta: {e}"