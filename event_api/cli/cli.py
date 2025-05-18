import os, re, json, requests
from datetime import datetime
from getpass import getpass
from typing import List, Dict, Any
from tabulate import tabulate

API_BASE_URL = "http://127.0.0.1:8000"
API_ENDPOINTS = {
    "events": f"{API_BASE_URL}/events/",
    "clients": f"{API_BASE_URL}/clients/",
    "vendors": f"{API_BASE_URL}/vendors/",
    "staff": f"{API_BASE_URL}/staff/",
    "inventory": f"{API_BASE_URL}/inventory/",
    "finance": f"{API_BASE_URL}/finance/",
    "export": f"{API_BASE_URL}/export/events"
}

ADMIN = {"username": "admin", "password": "1234"}
POLA = {
    "tanggal": r"^(0[1-9]|[12][0-9]|3[01])\s(Januari|Februari|Maret|April|Mei|Juni|Juli|Agustus|September|Oktober|November|Desember)\s\d{4}$",
    "kontak": r"^08\d{10}$"
}

def format_rupiah(angka):
    return f"Rp {int(angka):,}".replace(",", ".")

def valid(val, pola, err):
    return val if re.match(pola, val.strip()) else valid(input(f"{err}. Coba lagi: "), pola, err)

def iangka(msg, min_v, max_v):
    val = input(msg).strip()
    return int(val) if val.isdigit() and min_v <= int(val) <= max_v else iangka(f"Masukkan angka {min_v}-{max_v}: ", min_v, max_v)