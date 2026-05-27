# UC-006: Buyer Creates Self-Billed Invoice

## Summary

Buyer creates an invoice-like payable under an authorized self-billing or reverse-invoicing agreement.

## Primary Actor

Buyer

## Supporting Actors

Supplier, Platform

## Priority

P2

## Preconditions

- Invoice mode agreement allows `SELF_BILLING`.
- Buyer has verified delivery, usage, contract, or receipt data.
- Supplier review is required unless pre-authorized.

## Main Flow

1. Buyer opens self-billing creation.
2. Platform verifies self-billing authorization.
3. Buyer selects supplier and source documents.
4. Buyer creates invoice-like payable from PO, receipt, contract, usage, or milestone data.
5. Platform submits invoice to supplier review or checks pre-authorization.
6. Supplier accepts, or pre-authorization satisfies review.
7. Buyer signs payable obligation.
8. Platform registers invoice as `ACCEPTED`.

## Alternative Flows

- Supplier disputes buyer-created invoice.
- Platform blocks self-billing if no mode agreement exists.
- Buyer cancels draft before supplier review.

## Business Rules

- Self-billing is a negotiated invoice mode, not a buyer upload path.
- Supplier acceptance must be explicit, pre-authorized, or contractually waived.
- Same financeability rules apply after acceptance.

## Acceptance Criteria

- Buyer cannot self-bill without authorization.
- Supplier review/pre-authorization is recorded.
- Accepted self-billed invoice can become financeable.

