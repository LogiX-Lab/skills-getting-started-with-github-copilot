# UC-005: Prevent Duplicate Invoice Financing

## Summary

Platform creates a deterministic invoice hash and prevents the same accepted receivable from being financed more than once.

## Primary Actor

Platform

## Supporting Actors

Supplier, Buyer, Investor

## Priority

P0

## Preconditions

- Invoice has been accepted by buyer.
- Required invoice identity fields are available.

## Main Flow

1. Platform normalizes invoice data.
2. Platform creates `invoiceHash`.
3. Platform checks registry for existing hash.
4. If no duplicate exists, platform registers invoice as financeable.
5. Platform stores hash, version, accepted value, buyer, supplier, and maturity date.

## Duplicate Hash Inputs

Recommended inputs:

```text
supplierTaxId
buyerTaxId
invoiceNumber
purchaseOrderId
deliveryReference
acceptedValue
maturityDate
```

## Alternative Flows

- If exact duplicate exists, platform blocks registration.
- If near duplicate is suspected, platform routes to manual review.
- If invoice is adjusted, platform links new version to prior invoice.

## Business Rules

- Duplicate accepted invoice registration is blocked.
- Adjusted invoices must preserve version history.
- Only latest accepted version can be financeable.

## Acceptance Criteria

- Exact duplicate hash cannot be registered.
- Duplicate attempt is auditable.
- Financeable registry contains unique accepted receivables.

