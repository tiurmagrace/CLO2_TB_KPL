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