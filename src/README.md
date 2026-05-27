# Supply Chain Finance Portal API

A simple FastAPI application that allows suppliers, buyers, and investors to collaborate on supply chain finance opportunities.

## Features

- View all available financing opportunities
- Join an opportunity as supplier, buyer, or investor

## Getting Started

1. Install the dependencies:

   ```
   pip install fastapi uvicorn
   ```

2. Run the application:

   ```
   python app.py
   ```

3. Open your browser and go to:
   - API documentation: http://localhost:8000/docs
   - Alternative documentation: http://localhost:8000/redoc

## API Endpoints

| Method | Endpoint                                                               | Description                                                                  |
| ------ | ---------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| GET    | `/opportunities`                                                       | Get all opportunities with buyer/supplier context and participant data      |
| POST   | `/opportunities/{opportunity_name}/join?email=user@company.com&role=investor` | Join a specific opportunity as supplier, buyer, or investor |

## Data Model

The application uses a simple in-memory data model with meaningful identifiers:

1. **Opportunities** - Uses purchase-order-like ID as identifier:

   - Description
   - Buyer and supplier
   - Invoice amount and discount rate
   - Maximum number of participants allowed
   - List of participants with email and role

2. **Participants** - Uses business email as identifier:
   - Role (`supplier`, `buyer`, or `investor`)

All data is stored in memory, which means data will be reset when the server restarts.
