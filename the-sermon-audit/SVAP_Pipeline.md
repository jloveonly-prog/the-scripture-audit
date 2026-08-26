<!--
TranslationID: [002]
Category: sermon_audit
Language: en
Status: completed
TranslatedDate: 2026-08-26
SourceFile: D:\01.TheScriptureAudit_ko\the-sermon-audit\SVAP_Pipeline.md
-->

> [!IMPORTANT]
> ## 📋 Tactical Manual (Execution Procedure)
> **What this document doth**: GATE -1 (Exhaustive extraction of doctrinal claims) · BVCAP input loop · Comprehensive judgment · Report generation
> **Companion document**: `SVAP_GHQ.md` (General Headquarters — defineth MODE and judgment criteria)
> **Relationship**: When the headquarters defineth "what to audit and wherefore," this manual executeth "in what order and how to audit."
> **BVCAP Reference**: The execution of GATE 0~5 strictly followeth `../the-scripture-audit/BVCAP_Pipeline.md`.

# 🔬 SVAP Pipeline v1.3 (the-sermon-audit Internal Engine)
**"Prove all things; hold fast that which is good." — 1 Thessalonians 5:21 KJV**
**— The execution pipeline that exhaustively extracteth all doctrinal claims from a sermon and strictly verifieth them 1:1 against the Scripture —**

> **Document Role**: 📋 **Tactical Manual (Sermon Pre-processing + BVCAP Input + Report Generation)**
> (This document is the main execution program that instructeth the AI on **what order and what to do first** when receiving a sermon.)

> **Document Purpose**: It resolveth the structural void of the BVCAP 2.0 engine, which lacketh **"long-text input pre-processing."**
> BVCAP 2.0 is optimized for single conflict analysis ("Verse A vs. Verse B"),
> but it hath no autonomous capability to detect multiple doctrinal claims scattered throughout a 30~60 minute sermon.
> SVAP filleth this void with **GATE -1 (Pre-processing Claim Extraction)**.

> [!IMPORTANT]
> **The core innovation of this pipeline**: The entire sermon is NEVER cast directly into GATE 0.
> It must absolutely pass through **GATE -1 to exhaustively extract all doctrinal claims**,
> converting each claim into an individual Challenge before casting it into the BVCAP engine (GATE 0~5).
> **"Entering analysis without e
<truncated 60949 bytes>
arning newly established — Codified the structural bias where the verification target set is limited to the list chosen by the adversary (Omitted history retroactively recorded on 2026-08-17)*
*CHANGELOG: v1.2 → v1.3 (2026-08-17) — 4 types of execution Guardrails newly established. ① PRE-FLIGHT STEP 0-F Equipping Proof Checklist ② GATE -1 STEP 2.5 Observation–Inference Split ③ GATE -1 STEP 2.7 Coverage Map ④ Honest recording of BLIND achievement scope. Background of invocation: An incident where two audits on the same sermon diverged with extraction counts of 3 vs 51, and the 3-count side adopted theological system labels for judgment grounds. The cause was not a lack of weapons, but **a lack of verification gates in the rules**. ※ The proposed "N extraction quota per minute" and "Mandatory minimum 1 ✅" during review conflicted with GATE 8 STEP 5 (Prohibition of forced generation) and the GHQ bias prohibition principle, and were thus **not adopted.***
*CHANGELOG: v1.3 Supplement (2026-08-17) — Reflected pre-commit coherence check. ⑤ Added ⓪ Sweeping Adjacent Verses invocation hook to STEP 2 ③ (Delaying to ANCHOR-1P 6th order incureth re-execution costs after judgment is finalized) ⑥ Finalized STEP 2.5 numbering rule to single `N-a`/`N-b` suffix (Resolved the issue of text and examples using different notation, tallying based on row count) ⑦ Added `TACTIC_Auto_Grill.md` to STEP 0-B load list (Resolved discrepancy with the 9 items in STEP 0-F checklist)*
*CHANGELOG: v1.3 -> v1.4 (2026-08-19) — Scripture Corpus Integration. ① PRE-FLIGHT **STEP 0-G Newly Established** — Use after **actual verification** of corpus file existence via `ls`, substituting with memory-based only when absent and capping the grade ② Added `00_THESCRIPTURE/README.md` to STEP 0-F equipping checklist (10 items) ③ Registered Korean citation file (`TheScripture_ko_en_search.json`) in asset reference map. **Standard Edition = KJV 1769 Cambridge (incl. italics) / Korean = Standard King James (KSKJB)**.*