# SUC-008: Buyer Disputes, Rejects, or Holds Invoice

Parent use case: UC-004  
Target sprint: Sprint 1.2  
Priority: P0

## Objective

Support non-acceptance decisions in buyer invoice review.

## Steps

1. Buyer chooses dispute, reject, or hold.
2. Buyer provides reason.
3. Platform updates status.
4. Supplier can view the decision and reason.

## Acceptance Criteria

- `DISPUTED`, `REJECTED`, and hold states are supported.
- Non-accepted invoice cannot be financed.
- Supplier receives actionable reason.

