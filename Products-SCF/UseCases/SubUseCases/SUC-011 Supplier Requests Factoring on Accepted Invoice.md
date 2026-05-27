# SUC-011: Supplier Requests Factoring on Accepted Invoice

Parent use case: UC-007  
Target sprint: Sprint 2.2  
Priority: P0

## Objective

Allow supplier to request early payment for accepted invoice value.

## Steps

1. Supplier opens accepted invoices.
2. Supplier selects invoice.
3. Platform shows accepted value, maturity, risk mode, advance estimate, and fee.
4. Supplier confirms request.
5. Platform sets status to `FACTORING_REQUESTED`.

## Acceptance Criteria

- Only accepted invoices can be requested.
- Supplier sees risk/recourse terms.
- Invoice appears in investor marketplace.

