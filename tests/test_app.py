import copy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture(autouse=True)
def reset_opportunities():
    original = copy.deepcopy(app_module.opportunities)
    yield
    app_module.opportunities = original


def test_get_opportunities_returns_supply_chain_data():
    client = TestClient(app_module.app)

    response = client.get("/opportunities")

    assert response.status_code == 200
    body = response.json()
    assert "PO-2026-001" in body
    assert body["PO-2026-001"]["buyer"] == "Northwind Retail"
    assert body["PO-2026-001"]["supplier"] == "Vertex Components"


def test_join_opportunity_accepts_valid_participant():
    client = TestClient(app_module.app)

    response = client.post(
        "/opportunities/PO-2026-002/join",
        params={"email": "new.investor@capital.com", "role": "investor"},
    )

    assert response.status_code == 200
    assert "joined PO-2026-002" in response.json()["message"]
    participants = app_module.opportunities["PO-2026-002"]["participants"]
    assert {"email": "new.investor@capital.com", "role": "investor"} in participants


def test_join_opportunity_rejects_invalid_role():
    client = TestClient(app_module.app)

    response = client.post(
        "/opportunities/PO-2026-001/join",
        params={"email": "user@company.com", "role": "auditor"},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Role must be supplier, buyer, or investor"


def test_join_opportunity_rejects_duplicate_email():
    client = TestClient(app_module.app)

    response = client.post(
        "/opportunities/PO-2026-001/join",
        params={"email": "ops@vertexcomponents.com", "role": "supplier"},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Participant already joined this opportunity"
