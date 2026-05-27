# SUC-001: Create Relationship Invoice Mode Setting

Parent use case: UC-001  
Target sprint: Sprint 0.1 / Sprint 1.1  
Priority: P0

## Objective

Store the invoice mode that governs how invoices are created between a buyer and supplier.

## Trigger

Platform operator, buyer admin, or supplier admin configures a trading relationship.

## Steps

1. User selects buyer and supplier relationship.
2. User selects invoice mode.
3. Platform defaults to `SUPPLIER_ISSUED` if no selection exists.
4. Platform records allowed intake channels.
5. Platform saves `invoiceModeAgreementId`.

## Acceptance Criteria

- New invoices can reference `invoiceModeAgreementId`.
- Supplier-issued mode is available by default.
- Self-billing cannot be enabled without explicit authorization.

