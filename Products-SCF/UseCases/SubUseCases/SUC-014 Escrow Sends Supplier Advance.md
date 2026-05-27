# SUC-014: Escrow Sends Supplier Advance

Parent use case: UC-009  
Target sprint: Sprint 3.1  
Priority: P0

## Objective

Pay supplier advance after investor funds receivable.

## Steps

1. Escrow receives investor funds.
2. Platform calculates advance amount.
3. Platform transfers or records supplier advance.
4. Platform records retention/reserve if applicable.
5. Invoice status becomes `FACTORED`.

## Acceptance Criteria

- Supplier advance is recorded.
- Settlement ledger separates advance and reserve.
- Invoice status updates correctly.

