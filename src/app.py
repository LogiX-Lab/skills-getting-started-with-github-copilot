"""
Supply Chain Finance Portal API.

A simple FastAPI application that allows suppliers, buyers, and investors
to collaborate on financing opportunities.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(
    title="Supply Chain Finance Portal API",
    description="API for listing and joining supply chain finance opportunities",
)

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory financing opportunity database
opportunities = {
    "PO-2026-001": {
        "description": "Early payment program for electronics component supply",
        "buyer": "Northwind Retail",
        "supplier": "Vertex Components",
        "invoice_amount": 250000,
        "discount_rate": 1.8,
        "max_participants": 6,
        "participants": [
            {"email": "ops@vertexcomponents.com", "role": "supplier"},
            {"email": "treasury@northwind.com", "role": "buyer"},
            {"email": "credit@fundbridge.com", "role": "investor"},
        ],
    },
    "PO-2026-002": {
        "description": "Dynamic discounting for seasonal apparel procurement",
        "buyer": "BlueWave Stores",
        "supplier": "Sunrise Textiles",
        "invoice_amount": 180000,
        "discount_rate": 2.1,
        "max_participants": 6,
        "participants": [
            {"email": "finance@sunrisetextiles.com", "role": "supplier"},
            {"email": "payables@bluewave.com", "role": "buyer"},
        ],
    },
    "PO-2026-003": {
        "description": "Inventory-backed financing for logistics equipment",
        "buyer": "TransitHub Logistics",
        "supplier": "Atlas Equipment",
        "invoice_amount": 320000,
        "discount_rate": 1.5,
        "max_participants": 6,
        "participants": [
            {"email": "sales@atlashardware.com", "role": "supplier"},
            {"email": "procurement@transithub.com", "role": "buyer"},
        ],
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/opportunities")
def get_opportunities():
    return opportunities


@app.post("/opportunities/{opportunity_name}/join")
def join_opportunity(opportunity_name: str, email: str, role: str):
    """Join an opportunity as supplier, buyer, or investor."""
    # Validate opportunity exists
    if opportunity_name not in opportunities:
        raise HTTPException(status_code=404, detail="Opportunity not found")

    normalized_role = role.strip().lower()
    if normalized_role not in {"supplier", "buyer", "investor"}:
        raise HTTPException(status_code=400, detail="Role must be supplier, buyer, or investor")

    # Get the specific opportunity
    opportunity = opportunities[opportunity_name]

    # Ensure unique participants and basic capacity control
    if any(participant["email"] == email for participant in opportunity["participants"]):
        raise HTTPException(status_code=400, detail="Participant already joined this opportunity")
    if len(opportunity["participants"]) >= opportunity["max_participants"]:
        raise HTTPException(status_code=400, detail="Opportunity is already full")

    opportunity["participants"].append({"email": email, "role": normalized_role})
    return {"message": f"{role.title()} {email} joined {opportunity_name}"}
