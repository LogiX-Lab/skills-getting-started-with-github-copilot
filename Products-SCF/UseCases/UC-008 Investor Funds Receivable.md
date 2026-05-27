# UC-008: Investor Funds Receivable

## Summary

Investor reviews an accepted receivable and funds it based on risk, maturity, yield, and settlement terms.

## Primary Actor

Investor

## Supporting Actors

Supplier, Platform, Escrow

## Priority

P0

## Preconditions

- Invoice status is `FACTORING_REQUESTED`.
- Investor is onboarded and wallet/funding source is ready.
- Risk and yield details are available.

## Main Flow

1. Investor opens marketplace.
2. Investor filters by buyer, supplier, maturity, yield, amount, and risk mode.
3. Investor opens invoice detail.
4. Platform displays accepted value, buyer profile, supplier profile, evidence summary, risk mode, simple discount, annualized yield, reserve, and settlement currency.
5. Investor confirms funding.
6. Platform locks/funds escrow.
7. Invoice status becomes `FACTORED`.

## Alternative Flows

- Investor rejects opportunity.
- Funding fails due to insufficient balance.
- Credit ceiling or concentration limit blocks funding.

## Business Rules

- Investor funds accepted value only.
- Yield assumptions must be visible.
- Risk mode must be visible before funding.

## Acceptance Criteria

- Investor can fund a valid receivable.
- Funding creates escrow or ledger entry.
- Invoice moves to `FACTORED`.

