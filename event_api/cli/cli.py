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

def ijumlah():
    try:
        j = float(input("Jumlah (Rp): ").replace('.', '').replace(',', ''))
        return j if j > 0 else ijumlah()
    except:
        print("Format jumlah tidak valid!")
        return ijumlah()
    
def konversi_tanggal(tanggal_input: str) -> str:
    hari, bulan_str, tahun = tanggal_input.split()
    bulan_map = {b: i+1 for i, b in enumerate(["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"])}
    return f"{tahun}-{bulan_map[bulan_str]:02d}-{int(hari):02d}"

def tampilkan_api_error(response):
    print(f"\n[ERROR] Status Code: {response.status_code}")
    try: print(f"Detail: {response.json().get('detail', 'Tidak ada detail')}")
    except: print(f"Response: {response.text}")

def ambil_daftar_events():
    response = requests.get(API_ENDPOINTS["events"])
    return response.json() if response.status_code == 200 else []

def ipilih(items):
    if not items:
        return -1
    for i, item in enumerate(items):
        print(f"[{i+1}] {item}")
    return iangka("\nPilih nomor: ", 1, len(items)) - 1