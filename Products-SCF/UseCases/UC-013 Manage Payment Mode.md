# UC-013: Manage Payment Mode

## Summary

Platform supports stablecoin, fiat, and hybrid payment modes for funding, advance, repayment, and settlement.

## Primary Actor

Buyer / Supplier / Investor

## Supporting Actors

Platform, Settlement Infrastructure

## Priority

P2

## Preconditions

- Parties have approved settlement identities.
- Payment mode policy exists for relationship or invoice.

## Main Flow

1. User selects or reviews payment mode.
2. Platform stores invoice currency and settlement currency separately.
3. Platform verifies wallet, bank account, or off-ramp requirements.
4. Platform records FX source and conversion owner when currencies differ.
5. Platform executes settlement through selected rail.
6. Platform records payment reference, transaction hash, or bank reference.

## Payment Modes

- Stablecoin-only.
- Fiat-only.
- Fiat invoice with stablecoin settlement.
- Stablecoin funding with fiat supplier payout.
- Fiat buyer payment with stablecoin investor repayment.

## Business Rules

- USDC is preferred MVP demo rail.
- Fiat and hybrid modes require explicit accounting fields.
- Chain, wallet, FX, and conversion metadata must be auditable.

## Acceptance Criteria

- Invoice stores invoice currency and settlement currency.
- Payment references are recorded.
- Hybrid mode can be modeled even if not fully automated in MVP.

