# UC-001: Configure Invoice Mode Agreement

## Summary

Buyer and supplier define which invoice mode applies to their commercial relationship before invoices enter the Verity lifecycle.

## Primary Actor

Buyer / Supplier

## Supporting Actors

Platform Operator

## Priority

P0

## Preconditions

- Buyer and supplier organizations exist.
- Commercial relationship, contract, or purchase order exists.
- User has permission to configure relationship settings.

## Main Flow

1. User opens supplier-buyer relationship settings.
2. User selects invoice mode: `SUPPLIER_ISSUED` or `SELF_BILLING`.
3. User selects allowed intake channels: manual entry, ERP import, API, CSV/XML/EDI, or PDF upload.
4. User defines whether supplier acceptance is required for self-billing.
5. User defines whether PDF evidence is optional or required.
6. Platform saves the mode agreement.
7. Future invoices inherit the configured mode unless an authorized exception is created.

## Alternative Flows

- If no invoice mode exists, platform defaults to `SUPPLIER_ISSUED`.
- If self-billing is selected, platform requires explicit authorization.
- If a user lacks permission, platform blocks changes.

## Business Rules

- Supplier-issued invoice is the default mode.
- Buyer-created invoice requires self-billing authorization.
- Invoice mode may be stored at relationship, contract, PO, or invoice level.
- Financeability still requires buyer acceptance regardless of mode.

## Acceptance Criteria

- User can configure invoice mode for a buyer-supplier relationship.
- Platform blocks unauthorized self-billing.
- Invoice records store `invoiceModeAgreementId`.

