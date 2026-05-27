# SUC-017: Update Verifiable Payment Profile

Parent use case: UC-014  
Target sprint: Sprint 3.2 / Sprint 4.1  
Priority: P1

## Objective

Update buyer and supplier profiles based on settlement events.

## Steps

1. Platform receives settlement event.
2. Platform classifies event as on-time, late, default, disputed, or adjusted.
3. Platform updates buyer payment history.
4. Platform updates supplier dispute/dilution history.
5. Platform exposes profile summary in marketplace.

## Acceptance Criteria

- On-time settlement updates buyer profile positively.
- Delinquency updates buyer profile negatively.
- Supplier dispute history can be tracked.

