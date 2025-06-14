from memory_profiler import profile
from event_api.cli.handlers import event_handler

@profile
def test_tambah_event():
    event_handler.tambah_event()

if __name__ == "__main__":
    test_tambah_event()