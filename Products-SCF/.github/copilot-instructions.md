# Copilot instructions for this repository

## Current repository status

This repository is currently a **planning/specification workspace** for **Verity**, not a runnable application repository yet. There are no checked-in package manifests, build scripts, test runners, or lint configs at the repository root or below it, so there are currently **no repository-defined build, test, or lint commands to run**, and therefore no single-test command either.

When future sessions add executable code, update this file with the real commands from the committed toolchain rather than inventing placeholder workflows.

## High-level architecture

The repository follows a documented planning pipeline rather than a code-first architecture:

```text
Ideation -> Use Cases -> Roadmap of Impl Plan
```

- `Ideation/` contains the product thesis, value-resolution model, frontend TRD, risk analysis, and Round002 product specification.
- `UseCases/` converts that product model into actor-centered behavior, business rules, statuses, and acceptance criteria.
- `ImplPlan/` turns selected use cases into phased MVP delivery work.
- `DesignofSite/TemplateOfSite/Theme/` holds alternate marketing-site design systems; treat these as design-token sources, not implementation code.

The product itself is an on-chain supply-chain-finance platform with four major layers that are described across the docs:

1. **Persona-specific application surfaces**: supplier, buyer, and investor portals plus public marketing pages.
2. **Workflow/state layer**: invoice intake, buyer validation, financeability checks, factoring request, funding, escrow settlement, delinquency handling, and verifiable profile updates.
3. **Settlement/integration layer**: Circle Programmable Wallets, USDC settlement, Circle CCTP/Bridge Kit, and Arc network assumptions.
4. **Data + contract layer**: an `InvoiceRegistry`, a `FactoringEscrow`, and a `VerifiableProfile`, with off-chain storage for profiles, invoice metadata, and audit history.

If you are implementing code from these docs, keep the MVP sequence intact:

1. Supplier creates structured invoice data.
2. Buyer validates and accepts it as payable.
3. Platform computes deterministic `invoiceHash` and blocks duplicates.
4. Supplier requests factoring on accepted value.
5. Investor funds the receivable.
6. Escrow advances supplier funds and later distributes settlement.

## Key repository conventions

### Preserve document traceability

This repo treats product decisions as traceable artifacts. New implementation notes, schemas, or future code should stay aligned with the chain:

- ideation/product spec -> use case -> sub-use case -> implementation roadmap

Do not introduce flows that contradict the documented use cases without updating the upstream product docs as well.

### Verity is a **Due Value** financing platform, not an invoice-upload product

The core thesis is consistent across the product spec, use cases, and roadmap:

- only **buyer-accepted Due Value** is financeable
- supplier-submitted invoice data alone is **not** financeable
- accepted value, not raw face value, is the financing basis

Any future code, schemas, or UI should preserve that distinction.

### Structured invoice data is the workflow source of truth

For MVP behavior:

- structured invoice fields drive the workflow
- PDF upload is optional supporting evidence unless a document-first policy is explicitly being modeled
- buyer acceptance, matching, and risk state determine financeability

Do not make PDF/OCR the primary workflow path unless the docs are being intentionally revised.

### Keep the documented invoice lifecycle and terminology consistent

The specs rely on explicit status names and value-state terminology. Reuse the existing terms instead of inventing near-synonyms.

Common statuses and state terms already used across the docs include:

- `SUPPLIER_ISSUED`
- `PENDING_BUYER_REVIEW`
- `MATCHED`
- `DISPUTED`
- `REJECTED`
- `PARTIALLY_ACCEPTED`
- `ACCEPTED`
- `FACTORING_REQUESTED`
- `FACTORED`
- `DELINQUENT`
- `SETTLED`

The larger value model also matters: `ASK_VALUE` must pass matching and buyer acceptance before it becomes `DUE_VALUE`.

### Default invoice mode and risk mode are already defined

- Default invoice mode is `SUPPLIER_ISSUED` unless an explicit agreement enables self-billing.
- MVP default risk mode is **representation-and-warranty recourse**.
- Funding flows must disclose risk mode, supplier obligations, and investor-visible yield assumptions before funding proceeds.

### Anti-duplicate logic is a first-class product rule

Duplicate prevention is not an optional optimization. Future implementations should preserve:

- deterministic `invoiceHash`
- registration of accepted receivables only
- auditable blocking of exact duplicates
- version/history handling for adjusted invoices

The stronger recommended hash inputs are documented in `UseCases/UC-005 Prevent Duplicate Invoice Financing.md`; prefer those documented business identifiers over simplified demo-only hashes.

### Auditability and profile updates are part of the domain model

This product expects important events to remain auditable: buyer acceptance, factoring request, funding, settlement, delinquency, and profile changes. If future code adds persistence, event history should be modeled as a first-class concern, not an afterthought.

### Public-site design work should follow a chosen theme, not a blend

`DesignofSite/TemplateOfSite/Theme/` contains separate design analyses (`framer` and `wise`). If implementing marketing UI, choose one theme for a surface and follow its tokens, spacing, typography, and color rules consistently instead of mixing both systems.
