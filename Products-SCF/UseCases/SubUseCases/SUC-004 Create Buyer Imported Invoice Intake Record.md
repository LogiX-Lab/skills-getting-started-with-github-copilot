# SUC-004: Create Buyer Imported Invoice Intake Record

Parent use case: UC-003  
Target sprint: Sprint 1.1  
Priority: P1

## Objective

Support buyer-side invoice intake from ERP/AP data or uploaded supplier PDF placeholder.

## Steps

1. Buyer chooses import/upload intake.
2. Buyer enters or confirms structured invoice fields.
3. Platform marks intake channel as `BUYER_ERP`, `BUYER_UPLOAD`, or equivalent.
4. Platform routes invoice to buyer review.

## Acceptance Criteria

- Buyer can create intake record without full ERP automation.
- Intake channel is stored.
- Invoice can proceed to validation.

