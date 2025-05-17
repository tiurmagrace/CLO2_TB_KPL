from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Event Organizer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"], 
    allow_headers=["*"],
)

from routers import (
    event_router, client_router, vendor_router,
    staff_router, inventory_router, finance_router,
    export_router
)

app.include_router(event_router.router, prefix="/events", tags=["Events"])
app.include_router(client_router.router, prefix="/clients", tags=["Clients"])
app.include_router(vendor_router.router, prefix="/vendors", tags=["Vendors"])
app.include_router(staff_router.router, prefix="/staff", tags=["Staff"])
app.include_router(inventory_router.router, prefix="/inventory", tags=["Inventory"])
app.include_router(finance_router.router, prefix="/finance", tags=["Finance"])
app.include_router(export_router.router, prefix="/export", tags=["Export"])

@app.get("/")
def root():
    return {"message": "Welcome to Event Organizer API"}