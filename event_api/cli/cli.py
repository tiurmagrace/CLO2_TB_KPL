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

def konversi_tanggal(tanggal_input: str) -> str:
    hari, bulan_str, tahun = tanggal_input.split()
    bulan_map = {b: i+1 for i, b in enumerate(["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"])}
    return f"{tahun}-{bulan_map[bulan_str]:02d}-{int(hari):02d}"

def tambah_data(endpoint_key, fields, valid_map={}):
    data = {}
    for f in fields:
        val = input(f"{f.capitalize()}: ").strip()
        data[f] = valid(val, valid_map[f], f + " tidak valid") if f in valid_map else val
    if endpoint_key == "events":
        data["date"] = konversi_tanggal(data["date"])
        data["participants"] = []
    response = requests.post(API_ENDPOINTS[endpoint_key], json=data)
    print("\u2705 Data berhasil ditambahkan!" if response.status_code == 201 else tampilkan_api_error(response))

def lihat_data(endpoint_key, headers, keys):
    response = requests.get(API_ENDPOINTS[endpoint_key])
    if response.status_code == 200:
        items = response.json()
        if not items: return print("\u26A0\ufe0f Belum ada data!")
        print(tabulate([[i+1]+[item.get(k,"") for k in keys] for i,item in enumerate(items)], headers=["No"]+headers, tablefmt="grid"))
    else: tampilkan_api_error(response)

def export_data():
    response = requests.get(API_ENDPOINTS["export"])
    if response.status_code == 200:
        folder = r"C:\Users\USER\Documents\CLO2_TB_KPL\event_api\cli"
        filename = os.path.join(folder, "export_events.json")
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(response.json(), f, indent=4, ensure_ascii=False)
        print(f"✅ Data berhasil diekspor ke folder '{folder}' dengan nama file: {filename}")
    else:
        tampilkan_api_error(response)