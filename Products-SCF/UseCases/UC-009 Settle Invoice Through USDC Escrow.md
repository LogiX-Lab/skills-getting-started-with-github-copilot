# UC-009: Settle Invoice Through USDC Escrow

## Summary

Platform executes USDC escrow settlement: investor funds invoice, supplier receives advance, buyer repays at maturity, and escrow distributes principal, yield, fees, and residuals.

## Primary Actor

Platform / Escrow

## Supporting Actors

Investor, Supplier, Buyer

## Priority

P0

## Preconditions

- Invoice status is `FACTORED`.
- Escrow terms are defined.
- Wallets or ledger accounts exist.

## Main Flow

1. Investor deposits funding amount into escrow.
2. Escrow sends advance amount to supplier.
3. Escrow holds retention or reserve if applicable.
4. Buyer pays accepted value at maturity.
5. Escrow distributes principal and yield to investor.
6. Escrow releases residual or retention to supplier after fees/loss adjustments.
7. Platform records settlement ledger.
8. Invoice status becomes `SETTLED`.

## Alternative Flows

- Buyer pays late.
- Buyer pays partial amount.
- Buyer defaults.
- Dispute window delays retention release.

## Business Rules

- Settlement ledger must separate advance, principal, yield, fees, reserve, retention, and residual.
- USDC is preferred MVP settlement currency.
- Late payment triggers delinquency workflow.

## Acceptance Criteria

- Supplier receives advance.
- Investor receives principal plus yield.
- Supplier receives residual where applicable.
- Invoice reaches `SETTLED`.

