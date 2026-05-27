# SUC-015: Buyer Repays and Escrow Distributes Settlement

Parent use case: UC-009  
Target sprint: Sprint 3.2  
Priority: P0

## Objective

Settle a factored invoice at maturity.

## Steps

1. Buyer pays accepted value.
2. Escrow receives repayment.
3. Escrow pays investor principal and yield.
4. Escrow releases supplier residual or retention after fees.
5. Platform sets invoice status to `SETTLED`.

## Acceptance Criteria

- Investor receives principal plus yield.
- Supplier residual is calculated and recorded.
- Settlement ledger balances.

