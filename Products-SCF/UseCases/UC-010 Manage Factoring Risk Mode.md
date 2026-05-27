# UC-010: Manage Factoring Risk Mode

## Summary

Platform assigns and displays factoring risk mode so supplier, investor, and platform understand who bears default, fraud, dilution, and documentation risk.

## Primary Actor

Platform

## Supporting Actors

Supplier, Investor, Buyer

## Priority

P1

## Preconditions

- Invoice is accepted or under financing evaluation.
- Buyer and supplier profile data is available.

## Main Flow

1. Platform evaluates invoice evidence, buyer rating, supplier history, maturity, and concentration.
2. Platform assigns risk mode.
3. Platform displays supplier exposure and investor exposure.
4. Supplier confirms representations/warranties or recourse obligations.
5. Investor reviews risk mode before funding.

## Risk Modes

- Full recourse.
- Partial recourse.
- Representation and warranty recourse.
- Non-recourse.
- Reserve-backed non-recourse.
- Workout/special servicing.

## Business Rules

- MVP default is representation-and-warranty recourse.
- Non-recourse requires stronger buyer score and clean accepted payable.
- Disputed and overdue invoices cannot use normal factoring risk mode.

## Acceptance Criteria

- Every financeable invoice has risk mode.
- Supplier and investor can see obligations.
- Funding cannot proceed without risk disclosure.

