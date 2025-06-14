from event_api.cli.utils import konversi_tanggal

def test_konversi_tanggal():
    assert konversi_tanggal("10 Juni 2025") == "2025-06-10"
