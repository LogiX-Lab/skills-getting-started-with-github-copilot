# UC-014: Build Verifiable Payment Profile

## Summary

Platform builds buyer and supplier profiles from invoice validation, funding, settlement, dispute, dilution, and default history.

## Primary Actor

Platform

## Supporting Actors

Supplier, Buyer, Investor

## Priority

P1

## Preconditions

- Invoice events are recorded.
- Settlement ledger exists.
- Buyer and supplier entities exist.

## Main Flow

1. Platform records invoice creation and acceptance events.
2. Platform records disputes, corrections, rejections, and partial acceptances.
3. Platform records factoring request and funding events.
4. Platform records repayment, settlement, late payment, or delinquency.
5. Platform updates buyer and supplier profile metrics.
6. Platform exposes profile summary to marketplace and dashboards.

## Profile Metrics

| Actor | Metrics |
| --- | --- |
| Buyer | On-time payment rate, late payments, defaults, outstanding financed exposure, credit ceiling usage. |
| Supplier | Dispute rate, correction rate, dilution rate, duplicate attempts, successful settlements. |
| Investor | Funded volume, realized yield, delinquency exposure, portfolio concentration. |

## Business Rules

- Profile changes must be event-based and auditable.
- Buyer late/default status affects future financeability.
- Supplier dispute/dilution history affects risk mode and yield.

## Acceptance Criteria

- On-time settlement improves profile history.
- Delinquency degrades buyer status.
- Marketplace can show basic buyer and supplier risk signals.

