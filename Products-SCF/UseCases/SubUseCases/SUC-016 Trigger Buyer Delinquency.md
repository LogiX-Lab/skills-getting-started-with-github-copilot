# SUC-016: Trigger Buyer Delinquency

Parent use case: UC-011  
Target sprint: Sprint 4.1  
Priority: P0

## Objective

Mark buyer and invoice delinquent when repayment is missing after grace period.

## Trigger

```text
escrowReceived < requiredSettlementAmount
and currentTime > maturityDate + gracePeriod
```

## Steps

1. Platform checks maturity deadline.
2. Platform compares received amount with required amount.
3. Platform sets invoice status to `DELINQUENT`.
4. Platform freezes new financing for buyer.
5. Platform notifies parties.

## Acceptance Criteria

- Late payment triggers delinquency.
- Buyer financing is frozen.
- Delinquency is visible in profile.

