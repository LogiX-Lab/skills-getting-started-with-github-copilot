# SCF Key Points: Research and Product Analysis

## 1. Research Basis

This note extends the key product questions for the Smart Finux SCF platform using trade finance and stablecoin settlement references.

Reference anchors:

- Global Supply Chain Finance Forum: payables finance is centered on buyer-approved payables; the key financing trigger is buyer approval or an unconditional payment instruction.
- ICC Academy: payable financing typically involves a financier purchasing a buyer-approved invoice at a discount, with pricing based on the buyer's creditworthiness.
- IFC / World Bank: technology-enabled SCF can improve SME access to working capital by using transactional data, automation, and risk profiling.
- BIS / CPMI: stablecoins may help address some cross-border payment frictions, but benefits must be evaluated alongside regulatory, settlement, governance, and financial stability risks.

Product interpretation:

```
The platform should not treat every invoice as financeable.
The platform should treat invoice financeability as a state reached through evidence, buyer validation, risk allocation, and settlement readiness.
```

## 2. Extensibility

### Analysis

The platform should be designed as a configurable SCF operating layer, not as a single hard-coded factoring workflow. SCF products vary by market, buyer maturity, supplier sophistication, financing provider, legal jurisdiction, payment rail, and invoice evidence quality.

The strongest architecture is a state-machine-based platform where invoice mode, financing mode, payment mode, risk mode, and settlement mode are configurable dimensions.

### Core Extensibility Dimensions

| Dimension | Options | Product implication |
| --- | --- | --- |
| Invoice mode | Supplier-issued, buyer-created/self-billing | Controls who can create invoice records. |
| Invoice intake | Manual entry, ERP import, API, CSV/XML/EDI, PDF extraction | Controls how invoice data enters the platform. |
| Factoring mode | Recourse, partial recourse, non-recourse, reserve-backed | Controls risk allocation and pricing. |
| Payment mode | Stablecoin, fiat, hybrid | Controls settlement, reconciliation, FX, and compliance workflow. |
| Risk model | Buyer-led, supplier-aligned, collateral-backed, reserve-backed | Controls credit approval and investor protection. |
| Funding source | Single investor, pool, marketplace, buyer-funded dynamic discounting | Controls capital allocation and yield calculation. |
| Jurisdiction | Local rules for receivable assignment, tax, KYC/KYB, digital signatures | Controls documentation and legal enforceability. |

### Product Requirements

- Use configurable workflow states instead of one fixed invoice lifecycle.
- Store invoice origin, invoice mode, intake channel, risk mode, and payment mode as explicit fields.
- Support new risk policies without rewriting the invoice engine.
- Support structured invoice data as the source of truth, with PDFs as optional evidence unless policy requires them.
- Preserve audit trail across all workflow changes, especially invoice correction, dispute, assignment, and settlement.

### Open Decisions

- Should configurations be stored at relationship, contract, purchase order, or invoice level?
- Which dimensions must be fixed before invoice creation?
- Which dimensions can be changed before financing?
- Which dimensions become immutable once an invoice is financed?

## 3. Risk Model: Supplier Alignment

### Analysis

Traditional payables finance often relies primarily on the buyer's credit risk once the buyer has approved the payable. That is powerful for SMEs because they can access cheaper funding based on the anchor buyer's credit profile rather than their own balance sheet.

However, the platform still needs to manage seller-side risks:

- Invoice fraud.
- Duplicate financing.
- Dilution through credit notes, returns, quality claims, or rebates.
- Incorrect beneficiary.
- Supplier dispute after buyer-created invoice.
- Supplier collusion with buyer-side users.

Supplier alignment means the supplier remains economically accountable for risks caused by the supplier or by invoice quality, even if buyer credit risk is transferred to investors.

### Supplier Alignment Models

| Model | Description | Best fit |
| --- | --- | --- |
| No supplier recourse after buyer acceptance | Supplier has no payment obligation if buyer defaults, except for fraud or representation breach. | Strong buyer, clean approved payable, institutional-grade program. |
| Representation and warranty recourse | Supplier remains liable for fraud, invalid invoice, duplicate assignment, or commercial dilution. | Default model for buyer-approved invoices. |
| Partial first-loss supplier reserve | Supplier provides reserve/collateral covering a fixed percentage of loss. | Medium-risk buyers or early platform phase. |
| Conditional advance loan | Advance is structured as conditional financing; supplier repays if buyer default conditions occur. | Higher-risk invoices, unaccepted or partially verified invoices. |
| Dynamic supplier risk score | Supplier exposure varies by historical dispute rate, dilution rate, and invoice quality. | Mature platform with enough data. |

### Proposed Platform Position

For MVP, supplier alignment should not make every supplier responsible for all buyer defaults. That may reduce adoption and weaken the value proposition of SCF.

A more balanced design:

- Buyer credit/default risk belongs primarily to investor/factor after buyer acceptance.
- Supplier remains responsible for invoice validity, duplicate financing, fraud, wrong beneficiary, and post-acceptance dilution caused by supplier-side issues.
- Additional supplier collateral or recourse can be required only for higher-risk invoices, weaker buyers, or unaccepted/matched-only invoices.

### Product Rules

- Every financed invoice should include supplier representations and warranties.
- Supplier recourse should be explicit and visible before financing.
- Supplier collateral should be configurable by invoice risk tier.
- Buyer default should trigger the agreed risk mode, not a hidden platform assumption.
- Collateral release should occur only after buyer settlement, investor repayment, and dispute window completion.

## 4. Payment Mode

### Analysis

The platform should support stablecoin and fiat payment modes because trade finance users will have different treasury, regulatory, and accounting constraints.

Stablecoin settlement is useful for programmable escrow, near-real-time settlement, cross-border availability, and transparent on-chain payment status. But stablecoin usage introduces issuer, redemption, chain, wallet, compliance, and jurisdictional risks. The platform should therefore support stablecoin as an optional settlement rail, not as the only business logic.

### Payment Modes

| Payment mode | Description | Best fit | Key risk |
| --- | --- | --- | --- |
| Stablecoin-only | Funding, escrow, and settlement occur in USDC or another regulated stablecoin. | Digital-native, cross-border, programmable settlement. | Stablecoin issuer, wallet, chain, and regulatory risk. |
| Fiat-only | Funding and settlement occur through bank rails. | Regulated buyers, traditional treasury teams, local-market deployments. | Slower settlement, banking cutoffs, reconciliation complexity. |
| Hybrid: fiat invoice, stablecoin settlement | Invoice is denominated in fiat, but settlement occurs in stablecoin at a defined conversion rule. | Cross-border supplier payments and stable-value accounting. | FX timing, conversion spread, accounting treatment. |
| Hybrid: stablecoin funding, fiat payout | Investor funds in stablecoin; supplier receives fiat through off-ramp. | Suppliers not ready to hold stablecoins. | Off-ramp liquidity, fees, compliance. |
| Hybrid: fiat buyer payment, stablecoin investor repayment | Buyer pays fiat; platform converts to stablecoin for investor repayment. | Traditional buyers with digital investors. | Conversion and settlement timing risk. |

### Product Requirements

- Store invoice currency separately from settlement currency.
- Store FX rate source, rate timestamp, spread, and conversion party when invoice and settlement currencies differ.
- Support stablecoin escrow only after wallet, chain, KYC/KYB, and sanctions checks are complete.
- Provide payment status across both fiat and on-chain rails.
- Preserve accounting records for invoice amount, advance amount, discount fee, reserve, retention, and final settlement.

### Open Decisions

- Should MVP support only USDC settlement, or allow fiat-denominated invoices settled in USDC?
- Which party owns FX risk between invoice acceptance and settlement?
- Should stablecoin settlement be mandatory for investor funding, buyer repayment, or both?
- Which chains and wallets are approved for production use?

## 5. Mode of Invoice Factoring

### Analysis

Invoice factoring mode should be determined by invoice evidence quality and risk allocation, not only by user preference. A seller-issued invoice can pass through several states before it becomes a strong receivable.

The key product distinction:

```
Seller-issued invoice = payment request.
Buyer-accepted invoice = confirmed payable / Due Value.
Financeable receivable = buyer-accepted payable plus valid assignment, risk mode, and settlement instructions.
```

### Seller-Issued Invoice Types

| Invoice type | Description | Financeability | Key risk |
| --- | --- | --- | --- |
| Draft invoice | Seller-created invoice not submitted to buyer. | Not financeable. | No buyer awareness or payable confirmation. |
| Submitted invoice | Seller issued invoice, buyer has not reviewed it. | Not financeable for MVP. | Invoice may be disputed, duplicated, or unsupported. |
| Evidence-linked invoice | Invoice references PO, contract, delivery, or service approval. | Potentially financeable only with recourse in advanced version. | Evidence does not equal buyer obligation. |
| Matched invoice | System matches invoice against PO, receipt, and tolerance rules. | Potentially financeable with restrictions. | Buyer has not necessarily committed to pay. |
| Buyer-accepted invoice | Buyer confirms amount, due date, beneficiary, and payable obligation. | Strongly financeable. | Main risk becomes buyer credit/default risk. |
| Partially accepted invoice | Buyer accepts only part of invoice amount. | Financeable only for accepted portion. | Remaining balance is disputed. |
| Adjusted invoice | Invoice corrected through credit memo, debit memo, or revised invoice. | Financeable only after buyer accepts latest version. | Duplicate/version risk. |
| Disputed invoice | Buyer rejects or requests correction. | Not financeable. | Commercial value is unresolved. |
| Overdue invoice | Due date has passed without payment. | Not normal factoring; route to workout. | Default or payment stress. |

### Factoring Risk Modes

| Risk mode | Supplier exposure | Investor exposure | Typical use |
| --- | --- | --- | --- |
| Full recourse | Supplier repays if buyer does not pay. | Lower exposure. | Early-stage invoices, weaker buyers, or incomplete evidence. |
| Partial recourse | Supplier covers a defined first-loss layer. | Moderate exposure. | Medium-risk accepted invoices or new supplier history. |
| Representation and warranty recourse | Supplier covers fraud, invalidity, duplicate assignment, dilution, and document breach. | Buyer credit risk mostly remains with investor. | Default for buyer-accepted payables. |
| Non-recourse | Investor/factor assumes buyer non-payment risk, subject to exclusions. | Higher exposure. | Strong buyer, clean accepted payable, proven payment history. |
| Reserve-backed non-recourse | Losses are covered by reserve pool, insurance, buyer collateral, or supplier collateral. | Reduced by structural protection. | Larger invoices, institutional investors, cross-border flows. |
| Workout/special servicing | Financing is no longer standard factoring; collection or restructuring process begins. | Case-specific. | Overdue or distressed invoices. |

### Applying Risk Mode by Invoice Type

| Invoice type | Recommended mode | Reason |
| --- | --- | --- |
| Draft invoice | Block financing | No external claim has been made. |
| Submitted invoice | Block for MVP; possible full recourse later | Buyer has not accepted the payable. |
| Evidence-linked invoice | Full recourse only, advanced version | Evidence improves confidence but does not remove dispute risk. |
| Matched invoice | Full or partial recourse, advanced version | Matching lowers operational risk but buyer obligation may still be missing. |
| Buyer-accepted invoice | Representation/warranty recourse, non-recourse, or reserve-backed non-recourse | Buyer acceptance creates the strongest financeable asset. |
| Partially accepted invoice | Finance accepted amount only | Disputed amount must be excluded from funding base. |
| Adjusted invoice | Same as latest accepted state | Only current accepted version can be financed. |
| Disputed invoice | Block financing | Unresolved commercial value. |
| Overdue invoice | Workout/special servicing | Payment failure changes the product from financing to collection. |

### Product Requirements

- Financing should be blocked unless invoice status and risk mode are compatible.
- MVP should only finance buyer-accepted invoices.
- Non-recourse should require buyer acceptance, buyer risk score, concentration limit, maturity limit, and clean dispute history.
- Recourse and partial recourse should be available for higher-risk deals, but obligations must be clearly disclosed.
- The platform should tokenize or register only the financeable accepted amount, not the raw submitted amount.
- Adjustments must create version history and invalidate financing eligibility for prior versions.
- Partial acceptance should split invoice balances into accepted, disputed, and cancelled portions.

## 6. Buyer-Created Invoice

### Analysis

Buyer-created invoice mode is better described as self-billing, reverse invoicing, or evaluated receipt settlement. It should not be treated as a convenience feature where any buyer can create invoices. It is a negotiated commercial mode where the buyer's system becomes the source of invoice calculation.

This can reduce dispute risk because the invoice is generated from buyer-verified delivery, PO, contract, usage, or milestone data. But it also shifts responsibility to the buyer's data and controls.

### When Buyer-Created Invoice Mode Makes Sense

| Use case | Reason |
| --- | --- |
| Buyer controls measurement | Buyer has verified quantity, usage, meter, logistics, or delivery data. |
| Contract pricing is formula-based | Invoice amount can be calculated from agreed rules. |
| High-volume recurring settlement | Manual supplier invoicing creates avoidable reconciliation burden. |
| Evaluated receipt settlement | Buyer pays based on goods receipt and PO without waiting for supplier invoice. |
| Supplier pre-authorizes self-billing | Supplier accepts buyer-generated invoice records under agreed terms. |

### Controls

- Self-billing must require an invoice mode agreement.
- Supplier should review and accept buyer-created invoices unless pre-authorization exists.
- Buyer-created invoices must link to PO, receipt, contract, or usage evidence.
- The platform should record whether supplier acceptance is explicit, pre-authorized, or waived by contract.
- Buyer-created invoice financing should follow the same risk mode rules after acceptance.

### Product Requirement

Buyer-created invoice mode should be implemented as a separate invoice origin:

```
invoiceOrigin = SELF_BILLED
invoiceModeAgreement = required
supplierAcceptance = explicit | pre_authorized | not_required_by_contract
```

## 7. Yield Model

### Analysis

Investor yield in this SCF platform is primarily a receivables discount yield. Investors provide early liquidity to suppliers and receive repayment from the buyer or escrow at maturity. Yield should reflect time, risk, fees, reserve requirements, and payment mode.

The platform should avoid presenting yield as a simple static percentage. A 2 percent discount over 30 days and a 2 percent discount over 90 days are not economically equivalent. The investor view should show both invoice discount and annualized equivalent yield.

### Yield Drivers

| Driver | Impact |
| --- | --- |
| Buyer credit risk | Stronger buyer lowers required yield. |
| Invoice status | Buyer-accepted invoices lower risk than submitted or matched invoices. |
| Recourse mode | More supplier recourse lowers investor risk and yield. |
| Maturity | Longer tenor increases time risk and annualization impact. |
| Concentration | High exposure to one buyer, supplier, sector, or region increases required yield. |
| Currency/payment rail | Stablecoin, fiat, and hybrid settlement have different operational and liquidity risks. |
| Reserve/collateral | Reserve-backed deals may lower yield by reducing loss severity. |
| Dispute and dilution history | Higher dispute rate increases required yield or blocks financing. |

### Yield Metrics

| Metric | Formula / meaning |
| --- | --- |
| Invoice face value | Amount due from buyer at maturity. |
| Advance amount | Amount paid early to supplier. |
| Discount fee | Face value minus advance amount, net of reserve rules. |
| Simple discount rate | Discount fee / face value. |
| Annualized yield | Simple return adjusted for invoice tenor. |
| Expected loss-adjusted yield | Gross yield minus expected default/dilution/operational loss. |
| Net investor yield | Investor yield after platform fees, reserves, and settlement costs. |

### Product Requirements

- Show simple discount, annualized yield, expected loss-adjusted yield, and net yield.
- Show what risk mode the yield assumes.
- Show whether yield is based on buyer credit, supplier recourse, collateral, reserve pool, or insurance.
- Separate realized yield from expected yield.
- Keep a settlement ledger for principal, discount, fees, reserve release, and loss events.

## 8. Recommended MVP Decisions

For MVP, the product should keep risk logic strict and transparent:

1. Supplier-issued invoice is the default invoice mode.
2. Buyer-created invoice is allowed only where self-billing is explicitly configured.
3. Structured invoice data is the source of truth; PDF is supporting evidence.
4. Only buyer-accepted invoices are financeable.
5. Default risk mode is representation-and-warranty recourse against supplier plus buyer credit risk taken by investor/factor.
6. Non-recourse is available only for approved buyers and clean accepted payables.
7. Stablecoin settlement can be supported, but fiat/hybrid accounting fields must remain explicit.
8. Yield display must show both simple discount and annualized investor return.

## 9. Open Research Questions

- Which receivable assignment or perfection rules apply in the first target jurisdiction?
- Is the platform acting as marketplace, agent, factor, lender, or technology provider?
- Which party legally owns the receivable after financing?
- Should non-recourse be offered by default, or only to institutional investors?
- Should stablecoin settlement be limited to USDC on approved networks for MVP?
- Should supplier collateral be required for all SMEs or only risk-tiered cases?
- How should disputes after buyer acceptance be handled: reserve offset, supplier warranty claim, or investor loss?
- What accounting treatment should buyer and supplier use for financed invoices under target accounting standards?

## Appendix: Research Resources

### Supply Chain Finance and Factoring

- Global Supply Chain Finance Forum, **Payables Finance**  
  https://supplychainfinanceforum.org/techniques/payables-finance/index.html

- ICC Academy, **Open Account Trade Finance Products: Supply Chain Finance, Factoring, Forfaiting, and Export Financing**  
  https://academy.iccwbo.org/trade-finance/article/open-account-trade-finance-products/

- IFC / World Bank Group, **Technology-Enabled Supply Chain Finance for Small and Medium Enterprises is a Major Growth Opportunity for Banks**  
  https://documents.worldbank.org/curated/en/104991502947116592/pdf/118730-BRI-EMCompass-Note-39-Supply-Chain-Financing-PUBLIC.pdf

### Stablecoin Settlement and Regulation

- BIS CPMI, **Considerations for the Use of Stablecoin Arrangements in Cross-Border Payments**  
  https://www.bis.org/cpmi/publ/d220.htm

- BIS Financial Stability Institute, **Stablecoins: Regulatory Responses to Their Promise of Stability**  
  https://www.bis.org/fsi/publ/insights57.htm
