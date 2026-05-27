# SUC-003: Submit Supplier Invoice to Buyer Review

Parent use case: UC-002  
Target sprint: Sprint 1.1  
Priority: P0

## Objective

Move a supplier-created invoice into the buyer review queue.

## Steps

1. Supplier submits completed invoice.
2. Platform sets status to `SUPPLIER_ISSUED`.
3. Platform links buyer workspace.
4. Platform sets buyer-facing status to `PENDING_BUYER_REVIEW`.
5. Buyer receives notification or queue entry.

## Acceptance Criteria

- Buyer can see submitted invoice.
- Supplier can see invoice review status.
- Invoice is not financeable at this stage.

