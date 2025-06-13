from .base import Command
import json

class ExportDataCommand(Command):
    def __init__(self, api_client):
        self.api_client = api_client

    def execute(self):
        try:
            response = self.api_client.get("http://localhost:8000/events")
            with open("exported_events.json", "w", encoding="utf-8") as f:
                json.dump(response.json(), f, indent=2, ensure_ascii=False)
            return "Data berhasil diekspor ke exported_events.json"
        except Exception as e:
            return f"Gagal mengekspor data: {e}"