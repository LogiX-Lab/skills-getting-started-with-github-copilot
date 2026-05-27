# SUC-009: Generate Deterministic Invoice Hash

Parent use case: UC-005  
Target sprint: Sprint 2.1  
Priority: P0

## Objective

Create a stable unique hash for accepted invoice registration.

## Hash Inputs

- `supplierTaxId`
- `buyerTaxId`
- `invoiceNumber`
- `purchaseOrderId`
- `deliveryReference`
- `acceptedValue`
- `maturityDate`

## Acceptance Criteria

- Same normalized input produces same hash.
- Hash is generated only when required fields are present.
- Hash is stored on accepted invoice record.

