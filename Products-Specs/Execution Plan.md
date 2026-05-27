# Verity Product Specs Optimization & Execution Plan

## 1. Scope and Objective

This execution plan transforms the existing source specifications in `Products-SCF/` into a focused, MVP-first delivery path with clearer priorities, acceptance gates, and implementation sequencing.

**Source baseline**
- `Products-SCF/Ideation/Round002/Product Specifications.md`
- `Products-SCF/UseCases/README.md`
- `Products-SCF/ImplPlan/MVP Implementation Roadmap.md`

## 2. Optimization Decisions

1. **MVP-first reduction**: prioritize only the end-to-end supplier-issued invoice flow before expansion use cases.
2. **Single financeability rule**: only buyer-accepted invoices (`DUE_VALUE` / `ACCEPTED`) can be financed.
3. **Traceability by use case ID**: every sprint item must map to UC IDs for auditability.
4. **Risk baseline simplification**: default to representation-and-warranty recourse for MVP.
5. **Settlement baseline simplification**: standardize MVP settlement to USDC escrow path.

## 3. Execution Roadmap

### Phase 0 — Foundation Alignment (Sprint 0)

**Goal**: freeze MVP decisions and technical baseline.

Deliverables:
- finalized state machine and invoice lifecycle
- deterministic invoice-hash input specification
- core entities and schema draft
- architecture and Circle integration approach

### Phase 1 — Invoice Truth to Due Value (Sprints 1-2)

**Goal**: establish financeable invoice quality.

Mapped use cases: UC-001, UC-002, UC-003, UC-004

Deliverables:
- supplier structured invoice creation (no PDF required)
- buyer review/match/accept-dispute-reject-hold workflow
- accepted amount separation from face amount
- auditable buyer acceptance event

### Phase 2 — Factoring Enablement (Sprints 3-4)

**Goal**: convert accepted invoices into investable opportunities.

Mapped use cases: UC-005, UC-007, UC-008, UC-010, UC-012

Deliverables:
- deterministic hash and duplicate financing prevention
- financeability checks and risk-mode assignment
- supplier factoring request flow
- investor opportunity board and funding action
- discount + annualized yield calculator

### Phase 3 — Settlement Completion (Sprints 5-6)

**Goal**: complete value movement and ledger closure.

Mapped use cases: UC-009, UC-014

Deliverables:
- USDC escrow disbursement flow (advance, settlement, residuals)
- settlement ledger events and profile updates
- maturity payment closure and `SETTLED` transition

### Phase 4 — Hardening and Demo Readiness (Sprints 7-8)

**Goal**: increase reliability and prepare final demo/release package.

Mapped use cases: UC-011 + regression on core UCs

Deliverables:
- delinquency/default handling baseline
- end-to-end UAT script for supplier/buyer/investor
- demo runbook and release checklist

## 4. Execution Governance

For each sprint, enforce:

- **Entry criteria**: dependencies complete and scope frozen.
- **Exit criteria**: acceptance criteria pass for mapped UCs.
- **Artifacts**: updated workflow diagrams, API contracts, and decision log.
- **Risks**: weekly review of duplicate financing, buyer default, and settlement failure scenarios.

## 5. MVP Acceptance Gate

MVP is complete only when all conditions pass:

1. Supplier can create invoice data and submit for review.
2. Buyer can validate and accept invoice into financeable state.
3. Duplicate accepted invoice financing is blocked.
4. Supplier can request factoring and investor can fund.
5. USDC settlement completes and transitions invoice to `SETTLED`.
6. Yield and payout values are auditable from system records.

## 6. Post-MVP Backlog (Explicitly Deferred)

- UC-006 Buyer self-billing automation
- UC-013 full hybrid/fiat payment-mode automation
- advanced underwriting and insurance integrations
- secondary market capabilities
