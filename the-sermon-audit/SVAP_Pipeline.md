> [!IMPORTANT]
> ## 📋 Tactical Manual (Execution Procedure)
> **What this document does**: GATE -1 (Exhaustive Claim Extraction) · BVCAP Deployment Loop · Comprehensive Judgment · Report Output
> **Paired document**: `SVAP_GHQ.md` (GHQ — MODE/Verdict Criteria Definition)
> **Relationship**: Once the GHQ defines "what audit to perform and why", this manual executes "in what order and how to audit".
> **BVCAP Reference**: GATE 0~5 execution directly follows `../the-scripture-audit/BVCAP_Pipeline.md`.

# 🔬 SVAP Pipeline v1.1 (the-sermon-audit's Internal Engine)
**"Prove all things; hold fast that which is good." — 1 Thessalonians 5:21 KJV**
**— Execution pipeline that exhaustively extracts all doctrinal claims of a sermon and 1:1 cross-verifies against the Bible —**

> **Document Role**: 📋 **Tactical Manual (Sermon Pre-processing + BVCAP Deployment + Report Generation)**
> (This document is the main execution program instructing the AI **in what order and what to do first** when receiving a sermon.)

> **Document Purpose**: Resolves the structural gap of the BVCAP 2.0 engine, which is the **"absence of long-text input pre-processing"**.
> BVCAP 2.0 is optimized for single conflict analysis like "Verse A vs Verse B",
> and lacks the ability to autonomously detect multiple doctrinal claims scattered in a 30~60 minute sermon.
> SVAP fills this gap with **GATE -1 (Pre-processing Claim Extraction)**.

> [!IMPORTANT]
> **Core Innovation of this Pipeline**: The sermon full text is not thrown directly into GATE 0.
> **All doctrinal claims MUST be exhaustively extracted at GATE -1** first,
> and each claim is converted into an individual challenge and deployed to the BVCAP engine (GATE 0~5).
> **"Diving into analysis without exhaustive extraction" is the most fatal failure of this pipeline.**

---

## 🔑 Core Prohibitions (Prevent AI Confusion — Highest Priority)

> [!WARNING]
> The actions below mean the failure of this pipeline. You must be fully aware of them before starting the analysis.
> **All existing BVCAP prohibitions are inherited.** → Refer to the core prohibitions table in `../the-scripture-audit/BVCAP_Pipeline.md`

| ❌ Forbidden Action | ✅ Alternative Action |
|:---|:---|
| Deploying the whole sermon to GATE 0 at once | Must exhaustively extract claims at GATE -1 first, then input individually |
| AI inferring the preacher's intent to adjust the claim | Judge solely by the words (text) actually spoken by the preacher |
| Ignoring errors in individual claims using the overall sermon context as an excuse | Isolate and verify each claim independently (E-16 Contextual indulgence strictly forbidden) |
| Assuming "the preacher probably meant~" | Verify exactly as recorded in the text |
| Skipping verification saying "this much is okay" | Obligation to exhaustively verify all extracted claims |
| Quoting the preacher's original text directly in the report | AI must record via paraphrase (COPYRIGHT SHIELD) |
| Answers starting with "According to scholars~" | Analyze with biblical text first, cite scholars only for cross-verification |
| Skimming over claims embedded in the sermon flow | Obligation to scan every sentence individually and pattern-match doctrinal claims |
| Smoothing out explicitly wrong words using context or speaker intent as an excuse | Isolate the actual word used by the speaker and verify it directly first |
| **🆕 Reading existing BVCAP combat logs/reports before GATE -1** | **Only reference existing combat logs after GATE -1 (Extraction) and GATE 0~5 (Independent Verification) are completed (BLIND EXTRACTION principle)** |
| **🆕 Retroactively modifying independent verdicts to match existing reports** | **Independent verdicts are locked, and differences with existing reports are recorded separately at GATE 5.5** |

---

## 🛡️ COPYRIGHT SHIELD Protocol

> [!IMPORTANT]
> This protocol applies at all GATEs. It is especially critical in GATE -1 (Claim Extraction) and GATE 6 (Report Output).

```
[Copyright Protocol — COPYRIGHT SHIELD]

  Application Scope:
    - Upon claim extraction at GATE -1: Paraphrase and record claims
    - Upon writing sub-report at GATE 5: Use AI paraphrase instead of preacher's original text
    - Upon writing comprehensive report at GATE 6: Same as above

  ❌ Forbidden:
    Directly quoting the preacher's original text for 3 or more consecutive sentences

  ✅ Mandatory:
    AI must paraphrase and record the preacher's claims
    Use indirect speech like "The preacher claimed that~"

  ✅ Permitted Direct Quotations:
    - Core expressions under 5 words (e.g., "Even angels are saved")
    - Bible verses themselves (KJV etc. — The Bible is not subject to copyright)
    - Sermon title
    - Preacher's name (Factual reporting scope)

  📌 Paraphrase Quality Standards:
    - The doctrinal meaning and direction of the claim must be 100% preserved
    - Only the nuance and style are converted to be AI-like
    - The strength of the original claim must not be weakened or strengthened by paraphrasing
```

---

## 🎯 GATE Execution Pipeline — Overall Flow upon Sermon Input

> **This section is the actual execution sequence of SVAP.**
> The GATEs below are **sequential gateways that cannot be skipped** when the AI receives a sermon.

When a sermon manuscript is input:

---

### ⚡ [PRE-FLIGHT] Mandatory Equip Before Analysis Starts (Runs 1 Time)

> Inherits BVCAP PRE-FLIGHT, but adds SVAP-unique items.

```
━━━ STEP 0-A. Equip Persona ━━━
Read the files below in order and fully equip the agent identity:
1. ../the-scripture-audit/01_MANDATE/IDENTITY_Scribe42.md
2. ../the-scripture-audit/01_MANDATE/CREED_Override.md
3. ../the-scripture-audit/01_MANDATE/MANDATE_Agent.md

Additional Declaration: "I am the SVAP 1.0 Extractor,
my first mission is to exhaustively extract all doctrinal claims of this sermon without missing any."

━━━ STEP 0-B. Equip TACTICS ━━━
The files below must be loaded before analysis:
4. ../the-scripture-audit/02_TACTICS/HERMENEUTICS_Hillel_7.md
5. ../the-scripture-audit/02_TACTICS/DEOVERLAP_Serial.md
6. ../the-scripture-audit/02_TACTICS/ANCHOR_ThirdData.md
7. ../the-scripture-audit/02_TACTICS/LEXICON_Bible.md
8. ../the-scripture-audit/02_TACTICS/ANALOGY_Modern.md

━━━ STEP 0-C. Equip COPYRIGHT SHIELD ━━━
Copyright protocol confirmation and declaration:
"All preacher quotations in this report will be processed via AI paraphrase.
 I will not directly quote the preacher's original text for 3 or more consecutive sentences."

━━━ STEP 0-D. Execute OVERRIDE-0 ━━━
OVERRIDE-0 → Register academic consensus as Hypothesis-0, then directly read KJV original text
→ Begin main analysis only after equipping calling/lessons is complete.
```

---

### 🔍 [GATE -1] Sermon Pre-processing — Exhaustive Claim Extraction

> **Why it's necessary**: BVCAP 2.0 is an engine that analyzes single conflicts like "Verse A vs Verse B".
> A sermon is a 30~60 minute long text with multiple scattered doctrinal claims.
> If these claims are not exhaustively extracted first, dangerous claims buried in the sermon flow will be missed.
> **This GATE solves the "long-text input pre-processing" problem, which was a structural gap in BVCAP 2.0.**

> [!WARNING]
> **Skipping this GATE is absolutely forbidden.**
> Diving straight into GATE 0 without GATE -1 is the most fatal failure of the SVAP pipeline.
> This was precisely the root cause of BVCAP 2.0's failure in sermon analysis.

> [!CAUTION]
> ### 🆕 BLIND EXTRACTION Principle (v1.1 New)
> **When executing GATE -1, do not preview existing BVCAP combat logs (03_WAR_LOG) and reports (05_REPORT).**
>
> | Stage | Permitted Assets | Forbidden Assets |
> |:---:|:---|:---|
> | **GATE -1** (Extraction) | Sermon original text only | Combat logs, Reports, Arsenal |
> | **GATE 0~5** (Independent Verif.) | Sermon orig + Bible orig + Tactics + Arsenal | **Combat logs, Reports** |
> | **GATE 5.5** (Double Verif.) | Independent verdict results + **Existing combat logs/reports** (First view here) | — |
> | **GATE 6** (Comprehensive) | All Assets | — |
>
> **Why do this**: If you already know what was confirmed as "wrong" in existing BVCAP reports,
> it causes **Confirmation Bias** contamination where the AI unconsciously extracts claims and aligns verdicts in that direction.
> "Taking a test knowing the answers" is not independent verification.
> GATE -1~5 are performed independently from a blank slate, and in GATE 5.5, existing reports are pulled out as an "answer sheet" to compare.

```
[STEP 1] Sequential Scan of Sermon Full Text

  → Read the sermon text sequentially from beginning to end.
  → Flag all sentences that match the 【Risk Keyword Pattern Matching Table】 below.
  → Note: Claims naturally embedded in the flow of the sermon MUST also be captured.
          Doctrinal claims inserted in the middle of long explanations are the easiest to miss.

  【 Risk Keyword Pattern Matching Table 】

  | Pattern Type | Keyword/Expression | Reason for Risk |
  |:---:|:---|:---|
  | Salvation Scope | "~ is saved" / "~ is also saved" / "~ cannot be saved" | Salvation boundaries — Must cross-check with Bible |
  | Citation + Interp | "According to ~" / "The Bible says this" / "Looking at the word" | Verify consistency between quoted verse and interpretation |
  | Personal Opinion | "The way I see it" / "In my thought" / "I believe this" | Possibility of doctrinal claim without biblical basis |
  | Definitive Claim | "Did you know?" / "Many don't know, but" / "This is certain" | Unverified claim presented as fact to the audience |
  | Orig Language Claim | "The original meaning is~" / "Looking at original~" / "In Hebrew~" / "In Greek~" | Need to verify accuracy of original language interpretation |
  | Doctrine Definition | "~ means ~" / "The meaning of ~ is~" | Check biblical consistency of doctrinal definition |
  | Anti-Doctrine Claim | "~ is wrong" / "~ is a false interpretation" | Denying existing doctrine — Must verify basis |
  | Independent Revel. | "God showed me" / "I realized during prayer" | Risk of turning subjective revelation into doctrine |
  | Ontological Claim | "~ is ~" / "~ is not ~" | Definition of spiritual entity/space/nature |
  | Eschatological Claim| "When ~ happens, ~ will come" / "~ is already fulfilled" | Verify consistency of prophecy/eschatology interpretation |

  ⚠️ The table above represents typical patterns. Even if not in the table, the AI
     must autonomously detect all statements with doctrinal implications.
     Flag "any sentence that raises doubt while reading the text."


[STEP 2] Numbering Doctrinal Claims

  → Number each flagged sentence/paragraph as an independent 'Claim'.
  → For each claim:
     ① Record timestamp (min:sec) or text location
     ② AI paraphrases the claim content and records it (COPYRIGHT SHIELD)
        → Doctrinal meaning and direction must be 100% preserved during paraphrase
        → Only convert nuance/style to be AI-like
     ③ Map the Bible verse quoted by the preacher
        → If no verse is quoted: Record as "No verse quoted"
     ④ Auto-assign Risk Level:
        🟢 Safe: Claim appearing consistent with mainstream doctrine
        🟡 Verification Needed: Claim with room for interpretation or unclear basis
        🔴 Immediate Verification: Claim with high possibility of direct conflict with Bible


[STEP 3] Output Exhaustive Claim List

  → Organize the results above into a table and present it to the user first.
  → Simultaneously save to 01_CLAIMS folder
  → Filename: CLAIMS_[PreacherName]_[SermonTitle]_[Date].md

  Output Format:
  | # | Timestamp | Claim Summary (Paraphrase) | Quoted Verse | Risk | BVCAP Deploy |
  |---|-----------|----------------------------|--------------|------|--------------|
  | 1 | 05:30     | [AI Paraphrase]            | John 3:16    | 🟢   | Waiting      |
  | 2 | 12:20     | [AI Paraphrase]            | Col 1:20     | 🔴   | Waiting      |
  | 3 | 18:45     | [AI Paraphrase]            | None         | 🟡   | Waiting      |
  | ... |         |                            |              |      |              |

  ⚠️ If 0 claims are extracted:
     → "No doctrinal claims detected — This sermon is judged to be pastoral exhortation/testimony rather than doctrinal claims."
     → Proceed directly to GATE 6 and judge 🟢 SOUND


[STEP 4] Select Targets and Priorities for BVCAP Deployment

  → 🔴 Immediate Verif Claims: Unconditionally deploy to GATE 0~5 (Priority 1)
  → 🟡 Verif Needed Claims: Deploy to GATE 0~5 (Priority 2)
  → 🟢 Safe Claims: Basically deploy, but process rapidly as TIER-1(Simple) (Priority 3)

  ⚠️ Exhaustive Deployment Principle:
     Even if 🟢, verification is not skipped. Only the execution priority is different.
     "A seemingly safe claim" could be the most dangerous — do not lower your guard.
```

---

### 🔄 [GATE 0~5] Deploy BVCAP Engine per Claim (Iteration Loop)

> **This GATE directly reuses GATE 0~5 of the existing BVCAP_Pipeline.md.**
> It is not newly defined in SVAP; refer to the original pipeline at the path below:
> → `../the-scripture-audit/BVCAP_Pipeline.md`

```
FOR Each extracted Claim — In priority order (🔴 → 🟡 → 🟢):

  ━━━ [Pre-processing] Claim-to-Challenge Conversion ━━━

  Convert the preacher's claim into a 'Challenge' format that BVCAP can process.

  Conversion Format:
    "The preacher claimed [Claim Y] based on [Verse X]. Is this claim biblically consistent?"

  Example:
    Claim: "Even angels are saved" (Quoted Col 1:20)
    → Challenge: "The preacher claimed 'Even angels are included in salvation' based on Col 1:20.
                  Is this claim consistent with related verses like Heb 2:16?"

  If no verse is quoted:
    Claim: "God is someone who makes mistakes" (No verse quoted)
    → Challenge: "The preacher claimed 'God makes mistakes' without citing the Bible.
                  Are there Bible verses supporting or refuting this claim?"
    → C-Code: Default assign C-08 (Theological Inquiry)


  ━━━ [GATE 0] Challenge Type Classification — Determine C-Code ━━━

  → Execute GATE 0 of ../the-scripture-audit/BVCAP_Pipeline.md
  → C-Code assignment guide by sermon claim type:

  | Claim Type | Recommended C-Code |
  |:---|:---|
  | Salvation Scope Claim ("~ is also saved") | C-03 (Theological Conflict) or C-13 (Spiritual Entity Category) |
  | Verse Interpretation Error | C-03 (Theological Conflict) |
  | Original Language Claim Error | C-04 (Logical Self-Contradiction) |
  | Doctrine Definition Error | C-03 (Theological Conflict) |
  | Prophecy/Eschatology Interpretation | C-10 (Typological Fulfillment Debate) |
  | Historical Fact Claim | C-02 (Historical Inconsistency) |
  | Claim without Quoted Verse | C-08 (Theological Inquiry) |
  | Other | Refer to C-Code Table (C-01~C-13) |


  ━━━ [GATE 1~4] Execute BVCAP Pipeline As Is ━━━

  → Execute GATE 1~4 of ../the-scripture-audit/BVCAP_Pipeline.md
  → Gather Anchors → Prohibit commentary search → FULL SCAN → Reverse Calc Cross-Verification

  Reference when executing FULL SCAN:
  → Arsenal: ../the-scripture-audit/04_QUIVER/TYPE-[Code]_[Name].md
  → Tactics: ../the-scripture-audit/02_TACTICS/
  → Combat Logs: ../the-scripture-audit/03_WAR_LOG/ (Reference precedents)


  ━━━ [GATE 5] Write Sub-Report per Claim ━━━

  → A condensed version of a BVCAP Masterpiece
  → Issue Claim-Level Verdict:

  Verdict Codes:
    ✅ BIBLICAL    — Claim is consistent with quoted verse (Logical match with KJV original text)
    ⚠️ UNSUPPORTED — Quoted verse does not directly support the claim
    ❌ UNBIBLICAL  — Claim conflicts with the Bible (Contradiction confirmed via TYPE weapons)
    🟡 OPINION     — Personal opinion presented without biblical quotation

  Sub-report Format:
    ── Claim #[N]: [Paraphrased Claim]
    ── C-Code: [Assigned Code]
    ── Applied TYPE: [TYPE weapon combination used]
    ── Quoted Verse (KJV): [Original Text]
    ── Verification Result: [Analysis Summary]
    ── Verdict: [✅/⚠️/❌/🟡] + Epistemological Grade [EXPLICIT/STRONG/IRONCLAD]

END FOR
```

---

### 🆕 [GATE 5.5] Double Verification — Independent Verdict vs Existing Combat Logs (v1.1 New)

> **Why it's necessary**: The verdicts made in GATE 0~5 are "Independent Verdicts" made without viewing existing BVCAP combat logs.
> Comparing this verdict with previously confirmed reports (like IRONCLAD) establishes **Double Verification**.
> If they match, reliability is maximized; if they don't, new discoveries or errors can be identified.

> [!IMPORTANT]
> **Existing BVCAP combat logs/reports are viewed for the first time at this GATE.**
> The existing reports, whose existence wasn't even referenced during GATE -1~5, are pulled out for the first time at this point.

```
[STEP 1] Lock Independent Verdicts

  → Lock the Verdict for each Claim made in GATE 0~5 as an "Independent Verdict".
  → This verdict is preserved exactly as is in the final report, regardless of the results of STEP 2~3.
  → Locked independent verdicts are not modified retroactively.


[STEP 2] View Existing Combat Logs/Reports

  → Search for existing BVCAP reports related to the topic of this sermon:
     - ../the-scripture-audit/03_WAR_LOG/
     - ../the-scripture-audit/05_REPORT/
  → If related reports exist, view them; if not, proceed directly to STEP 4.


[STEP 3] Cross-Comparison — Independent Verdict vs Existing Reports

  → For each Claim, compare the independent verdict 1:1 with the conclusion of the existing report.

  Comparison Result Types:

    ✅ MATCH:
       Independent verdict and existing report have the same conclusion.
       → Reliability: 🟢 DOUBLE-VERIFIED
       → Meaning: The analysis from a blank slate matches the existing confirmed report, so the verdict is extremely reliable.

    ⚠️ PARTIAL:
       Direction is the same, but detailed basis or grade differs.
       → Reliability: 🟡 VERIFIED-WITH-NOTE
       → Meaning: Record with additional notes. Analyze the difference in basis and reflect in the report.

    ❌ CONFLICT:
       Independent verdict and existing report have contradictory conclusions.
       → Reliability: 🔴 REQUIRES-REVIEW
       → Meaning: Significant discovery. Two possibilities exist:
         (a) Independent analysis found new evidence → Consider updating existing report
         (b) Independent analysis contains an error → Analyze cause of error and record in report
       → In either case, DO NOT modify the original independent verdict; record the CONFLICT as is.

    🆕 NEW (No existing report):
       No existing BVCAP report on this topic.
       → Reliability: 🟡 SINGLE-VERIFIED
       → Meaning: Only independent verdict exists. Subject to cross-verification when future BVCAP reports are written.


[STEP 4] Output Double Verification Summary Table

  Include the table below in the final report:

  | # | Claim | Indep. Verdict | Existing Report Concl. | Compare Result | Reliability |
  |---|-------|----------------|------------------------|----------------|-------------|
  | 1 | ...   | ❌             | ❌ (IRONCLAD)          | ✅ MATCH       | 🟢 DOUBLE-VERIFIED |
  | 2 | ...   | ⚠️             | (None)                 | 🆕 NEW         | 🟡 SINGLE-VERIFIED |
  | 3 | ...   | ✅             | ❌ (IRONCLAD)          | ❌ CONFLICT    | 🔴 REQUIRES-REVIEW |
  | ... |

  ⚠️ If 1 or more CONFLICTs occur, record it as a separate section in the GATE 6 report.
```

---

### ⚖️ [GATE 6] Comprehensive Sermon Judgment + Final Report Output

> **Why it's necessary**: While the verdicts for each claim came out in GATE 5,
> the doctrinal soundness of the entire sermon must be comprehensively judged and output as a report.
> This is SVAP's unique final stage, not present in BVCAP.

```
[STEP 1] Tally Claim-Level Verdicts

  → Count of ✅ BIBLICAL: N
  → Count of ⚠️ UNSUPPORTED: N
  → Count of ❌ UNBIBLICAL: N
  → Count of 🟡 OPINION: N
  → Total Claims: N
  → Verification Complete: N (Must equal Total Claims. Verify 0 unverified.)


[STEP 2] Determine Overall Sermon Grade

  → 🟢 SOUND:
     Condition: All claims are ✅ BIBLICAL
     Meaning: All doctrinal claims of this sermon are consistent with the Bible.

  → 🟡 CAUTION:
     Condition: ⚠️ UNSUPPORTED or 🟡 OPINION exists, but no ❌ UNBIBLICAL
     Meaning: Some claims lack biblical basis, but there are no claims directly conflicting with the Bible.

  → 🔴 ALERT:
     Condition: 1 or more ❌ UNBIBLICAL claims exist
     Meaning: This sermon contains doctrinal claims that directly conflict with the Bible.


[STEP 3] Write RTM (Requirements Traceability Matrix)

  → Matrix to grasp verification status of all claims at a glance:

  | # | Claim Summary (Paraphrase) | Quoted Verse | C-Code | Applied TYPE | Verdict | Notes |
  |---|----------------------------|--------------|--------|--------------|---------|-------|

  → Ensure that unverified claims equal 0.
  → This matrix is the core of the report — the final safety net against omissions.


[STEP 4] Output Final Report

  → Write according to output format in SVAP_GHQ.md
  → Save to 02_REPORT folder
  → Filename: AUDIT_[PreacherName]_[SermonTitle]_[Date].md


[STEP 5] Spiritual Lesson (LESSON-6)

  → Write a spiritual lesson obtainable through this sermon audit.
  → Do not attack the preacher's character. Verify only doctrine.
  → Maintain a humble attitude that "even a sermon with good intentions can contain doctrinal errors."
```

---

## 📎 BVCAP Asset Reference Map (Shared Assets — Do Not Duplicate)

> [!IMPORTANT]
> SVAP **references, rather than duplicates**, BVCAP's weapons, tactics, and mandates.
> All assets below use the originals in the `../the-scripture-audit/` path.

| Asset | Reference Path | Purpose |
|:---|:---|:---|
| Mandates | `../the-scripture-audit/01_MANDATE/` | Equip Persona/CREED/Agent Mission |
| Tactics | `../the-scripture-audit/02_TACTICS/` | Hillel 7/DE-OVERLAP/ANCHOR etc. |
| Combat Logs | `../the-scripture-audit/03_WAR_LOG/` | Precedent reference |
| Arsenal | `../the-scripture-audit/04_QUIVER/` | All weapons TYPE-A~AU + TYPE-B-π |
| BVCAP Pipeline | `../the-scripture-audit/BVCAP_Pipeline.md` | Execution procedure for GATE 0~5 |
| BVCAP GHQ | `../the-scripture-audit/BVCAP_GHQ.md` | Reference E-Codes (E-01~16), Verdict criteria |
| C-Code Classification | `../the-scripture-audit/BVCAP_Pipeline.md` → Conflict type section | Define C-01~C-13 |
| COMBO Verif Table | `../the-scripture-audit/BVCAP_Pipeline.md` → COMBO-VERIFY section | 30 official combos |

---

## ⚡ SVAP FULL SCAN Execution Protocol (Sermon Audit Standard Procedure)

> [!IMPORTANT]
> When a sermon manuscript is input, always follow this order. Never skip GATE -1.

```
【 SVAP FULL SCAN Execution Sequence — v1.1 】

[PRE-FLIGHT — Mandatory Equip]
  ━━━ STEP 0-A. Equip Persona ━━━
  → Sequentially load 3 files from ../the-scripture-audit/01_MANDATE/
  → Declare SVAP Extractor role

  ━━━ STEP 0-B. Equip TACTICS ━━━
  → Load 5 files from ../the-scripture-audit/02_TACTICS/

  ━━━ STEP 0-C. Equip COPYRIGHT SHIELD ━━━
  → Confirm and declare copyright protocol

  ━━━ STEP 0-D. Execute OVERRIDE-0 ━━━
  → Isolate academic consensus, direct reading mode of KJV original text

  ━━━ 🆕 STEP 0-E. BLIND EXTRACTION Declaration (v1.1) ━━━
  → "Until GATE -1~5 are complete, existing combat logs (03_WAR_LOG) and reports (05_REPORT)
     will not be viewed. Conduct independent analysis solely with sermon and biblical original texts."
  → ⚠️ This declaration MUST be made in PRE-FLIGHT.

══════════════════════════════════════════════════════
  ▼ PHASE 1: Independent Analysis (BLIND — Existing Reports Ref. Forbidden)
══════════════════════════════════════════════════════

[GATE -1] Exhaustive Claim Extraction (BLIND)
  → STEP 1: Sequential Scan of Sermon Full Text (Risk keyword pattern matching)
  → STEP 2: Numbering Doctrinal Claims (AI Paraphrase + Verse mapping + Risk assignment)
  → STEP 3: Output Exhaustive Claim List (Save to 01_CLAIMS folder)
  → STEP 4: Select BVCAP Deploy Targets (🔴 → 🟡 → 🟢 Priority)
  → ⚠️ Forbidden to reference existing combat logs/reports at this stage

[CLAIM LOOP] BVCAP Deploy per Claim (BLIND)
  FOR Each Claim (In priority order):
    → [Pre-process] Claim-to-Challenge Conversion
    → [GATE 0] Determine C-Code
    → [GATE 1] Gather related verses (including anchors) — Use only biblical original text
    → [GATE 2] Prohibition on commentary search
    → [GATE 3] FULL SCAN (Sequential execution of TYPE A→AU) — Arsenal reference permitted
    → [GATE 4] Reverse Calculation Cross-Verification
    → [GATE 5] Issue Claim-Level Verdict → 🔒 Lock Independent Verdict
  END FOR
  → ⚠️ Forbidden to reference existing combat logs/reports at this stage

══════════════════════════════════════════════════════
  ▼ PHASE 2: Double Verification (First View of Existing Reports)
══════════════════════════════════════════════════════

[🆕 GATE 5.5] Double Verification — Independent Verdict vs Existing Combat Logs
  → STEP 1: Confirm Independent Verdict Lock (Unmodifiable)
  → STEP 2: First view of related existing combat logs/reports
  → STEP 3: 1:1 Comparison of Independent Verdict vs Existing Report
  → STEP 4: Output Double Verification Summary Table (MATCH/PARTIAL/CONFLICT/NEW)
  → ⚠️ If CONFLICT occurs, do not modify independent verdict, record the difference

══════════════════════════════════════════════════════
  ▼ PHASE 3: Final Judgment
══════════════════════════════════════════════════════

[GATE 6] Comprehensive Sermon Judgment
  → STEP 1: Tally Claim-Level Verdicts (Based on independent verdicts)
  → STEP 2: Determine Overall Sermon Grade (🟢/🟡/🔴)
  → STEP 3: Write RTM (Claim Tracking Matrix) — Include double verification results
  → STEP 4: Output Final Report (Save to 02_REPORT folder)
  → STEP 5: Spiritual Lesson (LESSON-6)
```

---

## 🔄 Relationship Summary with BVCAP 2.0

> [!NOTE]
> SVAP is a **higher-level engine wrapping BVCAP, not replacing it**.

```
┌────────────────────────────────────────────────────────────┐
│  SVAP 1.1 (Sermon Audit Pipeline)                           │
│                                                            │
│  ═══ PHASE 1: Independent Analysis (BLIND) ═══════════════ │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  GATE -1: Exhaustive Claim Extraction (BLIND)        │  │
│  │  🚫 Reference to existing combat logs/reports forbid. │  │
│  └──────────────────┬───────────────────────────────────┘  │
│                     │                                      │
│  ┌──────────────────▼───────────────────────────────────┐  │
│  │  BVCAP 2.0 (Verse Audit Engine) — BLIND Mode          │  │
│  │  ┌─────────────────────────────────────────────────┐ │  │
│  │  │ GATE 0 → 1 → 2 → 3 → 4 → 5                    │ │  │
│  │  │ (Arsenal/Tactics Use ✅ | Combat Log/Report 🚫)  │ │  │
│  │  └─────────────────────────────────────────────────┘ │  │
│  │  → 🔒 Independent Verdict Lock                       │  │
│  └──────────────────┬───────────────────────────────────┘  │
│                     │                                      │
│  ═══ PHASE 2: Double Verification ════════════════════════ │
│  ┌──────────────────▼───────────────────────────────────┐  │
│  │  🆕 GATE 5.5: Double Verification                    │  │
│  │  📖 First view of existing combat logs/reports        │  │
│  │  🔒 Indep. Verdict vs 📖 Existing Report → Compare   │  │
│  │  → Classify MATCH / PARTIAL / CONFLICT / NEW          │  │
│  └──────────────────┬───────────────────────────────────┘  │
│                     │                                      │
│  ═══ PHASE 3: Final Judgment ═════════════════════════════ │
│  ┌──────────────────▼───────────────────────────────────┐  │
│  │  GATE 6: Comprehensive Sermon Judgment               │  │
│  │  (Indep. Verdict + Double Verif. Result → Final Grd) │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────┘
```

Core:
- SVAP is a **Wrapper** of BVCAP.
- GATE -1, GATE 5.5, and GATE 6 are unique to SVAP, while the core verification in the middle (GATE 0~5) is BVCAP as is.
- Arsenal (TYPE-A~AU), tactics (Hillel 7, DE-OVERLAP), and mandates all share existing assets.
- If a new weapon is added to BVCAP, SVAP automatically benefits.
- **v1.1 Core Change**: **Fundamentally blocks "taking a test knowing the answers" contamination**
  by not referencing existing reports during PHASE 1 (Independent Analysis),
  and only opening existing reports to compare in PHASE 2 (Double Verification).

---
*Generated by SVAP 1.1 Supreme Sermon Auditor Engine*
*Architecture: Wrapper over BVCAP 2.0 (BLIND GATE-1 + BVCAP GATE 0~5 + GATE 5.5 Double Verification + GATE 6 Aggregation)*
*BVCAP Engine: ../the-scripture-audit/ (Shared Arsenal/Tactics/Mandates)*
*STATUS: BLIND EXTRACTION | FULL SCAN PER CLAIM | DOUBLE VERIFICATION | COPYRIGHT SHIELD ACTIVE*
*CHANGELOG: v1.0 → v1.1 (2026-06-28) — BLIND EXTRACTION Principle + GATE 5.5 Double Verif. Added*
