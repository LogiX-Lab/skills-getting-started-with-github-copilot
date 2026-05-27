# UC-003: Buyer Imports or Uploads Supplier Invoice

## Summary

Buyer imports supplier-issued invoice data from buyer ERP/AP systems or uploads a supplier invoice PDF for extraction and review.

## Primary Actor

Buyer

## Supporting Actors

Supplier, Platform

## Priority

P1

## Preconditions

- Buyer is onboarded.
- Supplier relationship exists or can be matched.
- Invoice mode is `SUPPLIER_ISSUED`.

## Main Flow

1. Buyer opens invoice intake.
2. Buyer selects import method: ERP/AP import, API payload, CSV/XML/EDI, or PDF upload.
3. Platform parses structured data or extracts fields from PDF.
4. Buyer reviews extracted/imported fields.
5. Platform links invoice to supplier, PO, delivery reference, and buyer workspace.
6. Platform sets status to `PENDING_BUYER_REVIEW`.

## Alternative Flows

- If supplier is unknown, platform routes invoice to matching queue.
- If PDF extraction is incomplete, buyer manually confirms fields.
- If the invoice already exists, platform routes to duplicate review.

## Business Rules

- Buyer upload is an intake channel, not an invoice mode.
- PDF upload is required only for the PDF-upload channel.
- Structured invoice data must be confirmed before validation.

## Acceptance Criteria

- Buyer can import invoice without PDF.
- Buyer can upload PDF and confirm extracted fields.
- Invoice can proceed to validation.

