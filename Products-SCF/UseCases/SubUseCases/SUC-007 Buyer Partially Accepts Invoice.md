# SUC-007: Buyer Partially Accepts Invoice

Parent use case: UC-004  
Target sprint: Sprint 1.2  
Priority: P1

## Objective

Allow buyer to accept only part of an invoice and exclude disputed balance from financing.

## Steps

1. Buyer enters accepted amount.
2. Buyer enters reason for unaccepted balance.
3. Platform stores accepted and disputed portions.
4. Platform sets status to `PARTIALLY_ACCEPTED`.

## Acceptance Criteria

- Accepted value can be less than face value.
- Disputed balance is not financeable.
- Reason is stored in audit trail.

