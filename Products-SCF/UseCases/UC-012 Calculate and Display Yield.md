# UC-012: Calculate and Display Yield

## Summary

Platform calculates deal-level and portfolio-level investor yield for discounted receivables.

## Primary Actor

Investor

## Supporting Actors

Platform, Supplier

## Priority

P0

## Preconditions

- Invoice is accepted and financeable.
- Accepted value and maturity date are known.
- Discount fee or advance amount is defined.

## Main Flow

1. Platform calculates advance amount.
2. Platform calculates discount fee.
3. Platform calculates simple discount rate.
4. Platform calculates annualized yield based on tenor.
5. Platform displays gross yield, expected loss-adjusted yield where available, and net investor yield.
6. Investor reviews yield before funding.
7. Platform records realized yield after settlement.

## Core Metrics

| Metric | Meaning |
| --- | --- |
| Face value | Amount due from buyer at maturity. |
| Accepted value | Buyer-confirmed financeable amount. |
| Advance amount | Early payment to supplier. |
| Discount fee | Investor/platform economic return before allocations. |
| Simple discount rate | Discount fee / accepted value. |
| Annualized yield | Time-adjusted return. |
| Net investor yield | Yield after fees, reserves, and settlement costs. |

## Business Rules

- Yield must show what risk mode it assumes.
- Expected yield must be separated from realized yield.
- Annualized yield must be shown because tenor changes economic meaning.

## Acceptance Criteria

- Investor sees simple discount and annualized yield.
- Settlement updates realized yield.
- Yield detail is tied to invoice and risk mode.

