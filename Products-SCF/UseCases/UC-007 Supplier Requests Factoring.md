# UC-007: Supplier Requests Factoring

## Summary

Supplier requests early payment on a buyer-accepted financeable receivable.

## Primary Actor

Supplier

## Supporting Actors

Platform, Investor

## Priority

P0

## Preconditions

- Invoice status is `ACCEPTED`.
- Duplicate check has passed.
- Financing is allowed.
- Settlement beneficiary is verified.
- Risk mode is assigned.

## Main Flow

1. Supplier opens accepted invoices.
2. Supplier selects invoice.
3. Platform displays accepted value, maturity, risk mode, advance estimate, discount fee, and expected residual.
4. Supplier confirms factoring request.
5. Platform sets status to `FACTORING_REQUESTED`.
6. Invoice appears in investor marketplace.

## Alternative Flows

- Platform blocks request if invoice is disputed, rejected, overdue, duplicate, or non-financeable.
- Supplier cancels factoring request before funding.
- Platform requires additional supplier representation/warranty acceptance.

## Business Rules

- Supplier can request factoring only for accepted value.
- Raw submitted invoice value is not financeable.
- Risk obligations must be disclosed before request.

## Acceptance Criteria

- Supplier can request factoring for accepted invoice.
- Non-financeable invoices cannot be requested.
- Investor marketplace receives valid opportunity.

