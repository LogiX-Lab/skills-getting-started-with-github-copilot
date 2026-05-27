# UC-002: Supplier Creates Supplier-Issued Invoice

## Summary

Supplier creates a structured supplier-issued invoice after delivery or service completion. PDF upload is optional, not required.

## Primary Actor

Supplier

## Supporting Actors

Buyer, Platform

## Priority

P0

## Preconditions

- Supplier is onboarded.
- Buyer exists or can be invited.
- Invoice mode is `SUPPLIER_ISSUED`.
- Supplier has invoice creation permission.

## Main Flow

1. Supplier opens invoice creation.
2. Supplier selects buyer.
3. Supplier enters invoice number, amount, currency, issue date, maturity date, PO reference, delivery reference, and line items.
4. Supplier optionally attaches PDF or supporting evidence.
5. Platform validates required fields.
6. Platform creates invoice with status `SUPPLIER_ISSUED`.
7. Platform sends invoice to buyer review queue as `PENDING_BUYER_REVIEW`.

## Alternative Flows

- Supplier imports invoice data from ERP/AP/AR through API, CSV, XML, or EDI.
- Supplier saves incomplete invoice as draft.
- Platform blocks invoice if required legal identifiers are missing.

## Business Rules

- Structured invoice data is the source of truth.
- PDF is supporting evidence unless a document-first policy applies.
- Supplier-issued invoice is not financeable until buyer acceptance.

## Acceptance Criteria

- Supplier can create invoice without uploading PDF.
- Invoice enters buyer review queue.
- Invoice status is tracked.

