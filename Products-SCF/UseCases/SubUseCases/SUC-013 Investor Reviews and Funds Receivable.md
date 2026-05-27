# SUC-013: Investor Reviews and Funds Receivable

Parent use case: UC-008  
Target sprint: Sprint 2.2 / Sprint 3.1  
Priority: P0

## Objective

Investor funds a financeable accepted invoice.

## Steps

1. Investor opens marketplace.
2. Investor reviews invoice detail, buyer profile, risk mode, accepted value, maturity, and yield.
3. Investor confirms funding.
4. Platform creates escrow/funding ledger.
5. Invoice moves toward `FACTORED`.

## Acceptance Criteria

- Investor can fund only financeable invoice.
- Funding amount is recorded.
- Invoice status changes after successful funding.

