# SUC-010: Block Exact Duplicate Registration

Parent use case: UC-005  
Target sprint: Sprint 2.1  
Priority: P0

## Objective

Prevent the same accepted receivable from being registered or financed twice.

## Steps

1. Platform generates invoice hash.
2. Platform checks accepted invoice registry.
3. If hash exists, platform blocks registration.
4. Platform records duplicate attempt.
5. User sees clear error.

## Acceptance Criteria

- Exact duplicate cannot enter financeable registry.
- Duplicate attempt is auditable.
- Existing invoice can be referenced by authorized user.

