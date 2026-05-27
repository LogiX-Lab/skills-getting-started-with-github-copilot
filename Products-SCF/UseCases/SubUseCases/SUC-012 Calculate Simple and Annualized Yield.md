# SUC-012: Calculate Simple and Annualized Yield

Parent use case: UC-012  
Target sprint: Sprint 2.2  
Priority: P0

## Objective

Show investor the economic return of funding an invoice.

## Calculations

- `discountFee = acceptedValue - advanceAmount`
- `simpleDiscountRate = discountFee / acceptedValue`
- `annualizedYield = simpleDiscountRate * (365 / tenorDays)`

## Acceptance Criteria

- Simple discount rate is displayed.
- Annualized yield is displayed.
- Yield references accepted value and maturity date.

