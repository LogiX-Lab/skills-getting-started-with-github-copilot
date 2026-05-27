# SUC-006: Buyer Accepts Full Invoice as Due Value

Parent use case: UC-004  
Target sprint: Sprint 1.2  
Priority: P0

## Objective

Convert supplier Ask Value into buyer-confirmed Due Value.

## Steps

1. Buyer confirms invoice is valid.
2. Buyer accepts full invoice amount.
3. Platform stores `acceptedValue = faceValue`.
4. Platform records buyer confirmation/signature.
5. Platform sets status to `ACCEPTED`.

## Acceptance Criteria

- Accepted value is stored separately from face value.
- Buyer acceptance event is auditable.
- Invoice becomes eligible for financeability checks.

