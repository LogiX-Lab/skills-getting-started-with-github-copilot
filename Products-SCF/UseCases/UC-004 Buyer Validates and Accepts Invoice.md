# UC-004: Buyer Validates and Accepts Invoice

## Summary

Buyer validates supplier-issued invoice against PO, receipt, contract, delivery, tax, and tolerance rules, then accepts or disputes the payable.

## Primary Actor

Buyer

## Supporting Actors

Supplier, Platform

## Priority

P0

## Preconditions

- Invoice status is `PENDING_BUYER_REVIEW`.
- Buyer has permission to review payables.
- Supplier and buyer relationship is active.

## Main Flow

1. Buyer opens invoice review queue.
2. Buyer selects invoice.
3. Platform displays invoice details and evidence.
4. Buyer reviews PO, receipt, delivery reference, contract terms, tax, discounts, maturity date, and beneficiary.
5. Buyer confirms accepted value.
6. Buyer signs or confirms payable obligation.
7. Platform updates status to `ACCEPTED`.
8. Platform records accepted value and audit trail.

## Alternative Flows

- Buyer disputes invoice and provides reason.
- Buyer rejects invoice.
- Buyer holds invoice for internal approval.
- Buyer partially accepts invoice and marks remaining balance disputed.

## Business Rules

- `ASK_VALUE` must become `DUE_VALUE` before financing.
- Financeable value equals buyer-accepted value, not raw invoice face value.
- Disputed and rejected invoices are not financeable.

## Acceptance Criteria

- Buyer can accept, dispute, reject, hold, or partially accept invoice.
- Accepted invoice records buyer confirmation.
- Only accepted value can become financeable.

