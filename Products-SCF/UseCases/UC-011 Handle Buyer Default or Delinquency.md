# UC-011: Handle Buyer Default or Delinquency

## Summary

Platform detects late or missing buyer repayment and triggers delinquency, freeze, notification, and recovery workflows.

## Primary Actor

Platform

## Supporting Actors

Buyer, Supplier, Investor, Platform Operator

## Priority

P1

## Preconditions

- Invoice status is `FACTORED`.
- Maturity date and grace period are defined.
- Expected settlement amount is known.

## Main Flow

1. Platform monitors maturity date.
2. Platform checks escrow or settlement ledger after grace period.
3. If received amount is less than required settlement amount, platform marks invoice `DELINQUENT`.
4. Platform freezes new financing for buyer.
5. Platform updates buyer profile.
6. Platform notifies supplier, investor, buyer, and operator.
7. Platform triggers configured reserve, collateral, or recourse waterfall.

## Default Trigger

```text
if escrowReceived < requiredSettlementAmount
and currentTime > maturityDate + gracePeriod
then status = DELINQUENT
```

## Alternative Flows

- Buyer pays during grace period.
- Buyer makes partial payment.
- Dispute prevents immediate recovery.
- Operator routes case to collection/workout.

## Business Rules

- Default must be programmatic and auditable.
- Delinquent buyers cannot generate new financeable opportunities.
- Recovery follows assigned risk mode.

## Acceptance Criteria

- Late payment triggers delinquency.
- Buyer profile updates.
- New financing is blocked for delinquent buyer.

