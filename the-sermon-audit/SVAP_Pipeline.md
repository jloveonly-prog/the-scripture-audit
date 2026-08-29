<!-- doc_no: 20260829_0208 | ver: 20260829_0942 -->
> [!IMPORTANT]
> ## 📋 The Tactical Manual (Pipeline — Execution Procedure)
> **What This Document Does**: GATE -1 (full extraction of doctrinal claims) · the BVCAP input loop · comprehensive judgment · report output
> **Companion Document**: `SVAP_GHQ.md` (GHQ — defines MODE/verdict criteria)
> **Relationship**: once GHQ defines "what to audit and why," this manual executes "in what order and how to audit."
> **BVCAP Reference**: the execution of GATE 0-5 follows `../the-scripture-audit/BVCAP_Pipeline.md` exactly as-is.

# 🔬 SVAP Pipeline v1.3 (the internal engine of the-sermon-audit)
**"Prove all things; hold fast that which is good." — 1 Thessalonians 5:21 KJV**
**— an execution pipeline that fully extracts every doctrinal claim from a sermon and verifies each one 1:1 against Scripture —**

> **Document Role**: 📋 **the Tactical Manual (sermon pre-processing + BVCAP input + report generation)**
> (This document is the main execution program instructing the AI **in what order, and what to do first**, upon receiving a sermon.)

> **Document Purpose**: it resolves the structural void of the BVCAP 2.0 engine, which lacks **"long-text input pre-processing."**
> BVCAP 2.0 is optimized for single-conflict analysis ("Verse A vs. Verse B"),
> but it has no autonomous capability to detect multiple doctrinal claims scattered throughout a 30-60 minute sermon.
> SVAP fills this void with **GATE -1 (Pre-processing Claim Extraction).**

> [!IMPORTANT]
> **The core innovation of this pipeline**: the entire text of a sermon is never cast directly into GATE 0.
> It must always first pass through **GATE -1, which fully extracts every doctrinal claim**,
> converting each claim into an individual Challenge before feeding it into the BVCAP engine (GATE 0-5).
> **"Diving into analysis without full extraction" is this pipeline's most fatal failure.**

---

## 🔑 Core Prohibitions (Preventing AI Confusion — Equip First and Foremost)

> [!WARNING]
> The actions below constitute a failure of this pipeline. Internalize them fully before beginning analysis.
> **All of BVCAP's existing prohibitions are inherited in full** → see the Core Prohibitions table in `../the-scripture-audit/BVCAP_Pipeline.md`

| ❌ Prohibited Action | ✅ Substitute Action |
|:---|:---|
| feeding the entire sermon into GATE 0 all at once | always fully extract claims in GATE -1 first, then feed them in individually |
| the AI inferring the preacher's intent and correcting the claim | judge using only the words (the text) the preacher actually said |
| ignoring an individual claim's error under the excuse of the sermon's overall context | verify each claim in isolation, independently (strictly prohibit E-16, the contextual pardon) |
| assuming "the preacher probably meant ~" | verify exactly as recorded in the text |
| letting something pass as "this much is fine" without verification | a duty to fully verify every extracted claim |
| quoting the preacher's original words verbatim in the report | the AI paraphrases and records them (COPYRIGHT SHIELD) |
| an answer beginning with "according to scholars ~" | first analyze with the biblical text, and cite scholars only for cross-verification |
| skimming past a claim embedded within the flow of the sermon | scan every sentence individually; a duty to pattern-match for doctrinal claims |
| smoothing over a manifestly wrong word under the excuse of context or speaker intent | isolate the very word the speaker used, as-is, for primary verification |
| **🆕 reading existing BVCAP war-log records/reports before GATE -1** | **reference existing war-log records only after GATE -1 (extraction) and GATE 0-5 (independent verification) are complete (the BLIND EXTRACTION principle)** |
| **🆕 retroactively adjusting an independent verdict to match an existing report** | **the independent verdict is locked; any difference from an existing report is recorded separately at GATE 5.5** |

---

## 🛡️ COPYRIGHT SHIELD (the Copyright Protection Protocol)

> [!IMPORTANT]
> This protocol applies at every GATE. It is especially central at GATE -1 (claim extraction) and GATE 6 (report output).

```
[The Copyright Protocol — COPYRIGHT SHIELD]

  Scope of Application:
    - at GATE -1 claim extraction: record the claim in paraphrase
    - at GATE 5 sub-report writing: use an AI paraphrase in place of the
      preacher's original words
    - at GATE 6 comprehensive report writing: the same

  ❌ Prohibited:
    directly quoting 3 or more consecutive sentences of the preacher's
    original words

  ✅ Mandatory:
    the AI paraphrases the preacher's claim when recording it
    use indirect speech in the form "the preacher claimed that ~"

  ✅ Permitted Direct Quotation:
    - a core phrase of 5 words or fewer (e.g., "even angels are saved")
    - the biblical text itself (KJV, etc. — Scripture is not subject to
      copyright)
    - the sermon's title
    - the preacher's name (within the scope of factual reporting)

  📌 Standards for Paraphrase Quality:
    - the doctrinal meaning and the direction of the claim in the
      original must be preserved 100%
    - only the tone or style is converted into AI phrasing
    - the paraphrase must not weaken or strengthen the intensity of the
      original claim
```

---

## 🎯 The GATE Execution Pipeline — the Full Flow Upon Sermon Input

> **This section is SVAP's actual execution order.**
> The GATEs below are **sequential checkpoints the AI cannot skip** upon receiving a sermon.

Once the sermon manuscript is entered:

---

### ⚡ [PRE-FLIGHT] Mandatory Equipping Before Analysis Begins (Executed Once)

> Inherits BVCAP's PRE-FLIGHT, adding SVAP-specific items.

```
━━━ STEP 0-A. Equip Persona ━━━
Read the following files in order and fully equip the agent identity:
1. ../the-scripture-audit/01_MANDATE/IDENTITY_Scribe42.md
2. ../the-scripture-audit/01_MANDATE/CREED_Override.md
3. ../the-scripture-audit/01_MANDATE/MANDATE_Agent.md

Additional Declaration: "As the SVAP 1.0 Extractor, my first mission is
to extract, without exception, every doctrinal claim in this sermon."

━━━ STEP 0-B. Equip Tactics (TACTICS) ━━━
The following files must be loaded before analysis:
4. ../the-scripture-audit/02_TACTICS/HERMENEUTICS_Hillel_7.md
5. ../the-scripture-audit/02_TACTICS/DEOVERLAP_Serial.md
6. ../the-scripture-audit/02_TACTICS/ANCHOR_ThirdData.md
7. ../the-scripture-audit/02_TACTICS/LEXICON_Bible.md
8. ../the-scripture-audit/02_TACTICS/ANALOGY_Modern.md
9. ../the-scripture-audit/02_TACTICS/TACTIC_Auto_Grill.md
   (actually triggered at GATE 3, but included in the 9 equipping-proof
   items of STEP 0-F, so it is loaded here together)

━━━ STEP 0-C. Equip COPYRIGHT SHIELD ━━━
Confirm and declare the copyright protocol:
"Every citation of the preacher in this report is processed as an
 AI paraphrase. No 3+ consecutive sentences of the preacher's original
 words are directly quoted."

━━━ STEP 0-D. Execute OVERRIDE-0 ━━━
OVERRIDE-0 → register the mainstream academic view as Hypothesis-0, then
read the KJV original text directly
→ begin this analysis only after equipping is complete.

━━━ 🆕 STEP 0-F. Output the Equipping-Proof Checklist (New 2026-08-17, Mandatory) ━━━

  > Why this is needed: STEP 0-A~0-D only said "read this," with **no
  > output proving it was read.**
  > As a result, it was undetectable when analysis proceeded without ever
  > opening the referenced documents, and a case was observed in which an
  > audit was actually conducted, adopting a theological-system label as
  > grounding for the verdict, without having seen `CREED_Override.md`'s
  > C-4 (prohibition of theological-system labels).
  > **Inheritance by reference is not inheritance in practice.**
  > This rule extends to PRE-FLIGHT the pattern from `CREED_Override.md`
  > OVERRIDE-2, item 4 (prohibition of self-certifying one's own
  > statement) — "do not merely answer with a conclusion; present
  > item-by-item grounds."

  → **Before** entering GATE -1, output the table below. A summary
  answer of the form "yes, I've read them all" is prohibited.

  | # | Document | Equipped | One clause from that document directly applied to this audit |
  |:-:|:---|:--:|:---|
  | 1 | IDENTITY_Scribe42.md | ☐ | (e.g., the separation of the audit tier from the witness tier) |
  | 2 | CREED_Override.md | ☐ | **C-4 detailed implementation instruction — prohibition of theological-system labels** ← mandatory entry |
  | 3 | MANDATE_Agent.md | ☐ | |
  | 4 | HERMENEUTICS_Hillel_7.md | ☐ | |
  | 5 | DEOVERLAP_Serial.md | ☐ | |
  | 6 | ANCHOR_ThirdData.md | ☐ | **ANCHOR-1P, 6th order, ⓪ sweeping adjacent verses** ← mandatory entry |
  | 7 | LEXICON_Bible.md | ☐ | |
  | 8 | ANALOGY_Modern.md | ☐ | |
  | 9 | TACTIC_Auto_Grill.md | ☐ | |
  | 10 | **00_THESCRIPTURE/README.md** | ☐ | **KJV 1769 Cambridge, incl. italics / Korean KSKJB** ← mandatory entry |

  🚨 a document whose 4th column cannot be filled is **treated as not
     equipped.** Listing filenames alone is not proof of equipping.

━━━ 🆕 STEP 0-G. Confirm Existence of the Scripture Corpus (New 2026-08-19, Mandatory) ━━━

  Not a declaration but an **execution**:

     ls "../the-scripture-audit/00_THESCRIPTURE/"

  | File | Purpose | If Present | If Absent |
  |:---|:---|:---|:---|
  | `KJV_1769.txt` | **the sole authoritative English text for verdicts** — quotation, grammar, and italics all included | used as the authoritative text | `[Full Scan: memory-based]` 🟡 |
  | `KJV_1769_search.txt` | a search-oriented derivative of `KJV_1769.txt` (for full surveys, frequency, silence) | **every full scan hinges on this** | ditto |
  | `TheScripture_ko_en_search.json` | **Korean citation ⒜ (priority 1)** | use the KSKJB text | ⒝ live lookup → on failure, ⒞ LLM translation (see below) |

  🚨 **declaring from memory without searching, when the file is
     available, is a procedural violation.**
  🚨 substitute only when the file is absent; for English, `[Full Scan:
     memory-based]` 🟡 cannot be used as the sole grounding for a
     STRONG/IRONCLAD rating.
  🚨 the report must always include the **Scripture-source block** (the
     output format in `SVAP_GHQ.md`) at its end.

  ── the sole authoritative English text is `KJV_1769.txt` alone (2026-08-19) ──
  Reason: it is the only file that simultaneously satisfies both italics
  `[ ]` preservation and searchability.
  `KJV_1769_search.txt` is merely its search-oriented derivative, not a
  separate standard.
  Detailed grounds: `../the-scripture-audit/00_THESCRIPTURE/README.md`,
  "Why We Narrowed to a Single File"

  ⚠️ Acquiring the Korean Text — 3 Stages (Revised 2026-08-19):

  ⒜ a local file exists → cite `TheScripture_ko_en_search.json` (KSKJB)
    directly.

  ⒝ no local file → a live lookup on `kingjamesbiblekorea.com` (priority 2)
    · on a successful lookup, use **the identical copyright notation as
      ⒜** (KSKJB, CC BY-NC-ND 4.0) + note the date of the lookup.
    · where possible, look it up via raw HTML parsing (the
      `fetch_kjv_ko.py` method). Tools of the WebFetch type have the
      model summarize/reconstruct the page on return, so they do not
      guarantee character-for-character fidelity.
    · 🚨 this path is **the KSKJB original text, not LLM translation
      (⒞)** — do not mislabel it as `[Korean: LLM translation]`.

  ⒞ both ⒜ and ⒝ fail (a clone environment + no site access, etc.) — the
    fallback:
    · **the model translates the KJV English directly into Korean
      itself.** The principle of literal translation applies — the
      moment a paraphrase is made to favor the argument, it ceases to be
      an audit and becomes advocacy.
    · change the source notation to **[Korean: LLM translation]**:
        Korean Scripture citation: the Korean scriptural text in this
        report is a direct translation of the KJV English, not a
        citation of any specific Korean version (Standard King James,
        the Authorized Version, the Korean King James, etc.).
    · 🚨 **do not label it as a KSKJB citation** — attributing a source
      that was not actually used is a false notation.
    · 🚨 **a Korean translation is never grounds for a verdict.** The
      verdict is always based on the KJV English (CREED C-1).
    · if needed, a local file can be generated (about 10 minutes) via
      `../the-scripture-audit/00_THESCRIPTURE/fetch_kjv_ko.py`.
```

---

### 🔍 [GATE -1] Sermon Pre-processing — Full Extraction of Doctrinal Claims (Claim Extraction)

> **Why this is needed**: BVCAP 2.0 is an engine that analyzes a single collision, "Verse A vs. Verse B."
> A sermon is a long text, 30-60 minutes in length, with multiple doctrinal claims scattered throughout.
> Unless these claims are fully extracted first, a dangerous claim buried within the flow of the sermon will be missed.
> **This GATE resolves the "long-text input pre-processing" problem that was BVCAP 2.0's structural void.**

> [!WARNING]
> **Skipping this GATE is absolutely prohibited.**
> Proceeding directly to GATE 0 without GATE -1 is the SVAP pipeline's most fatal failure.
> This was precisely the root cause of BVCAP 2.0's failure at sermon analysis.

> [!CAUTION]
> ### 🆕 The BLIND EXTRACTION Principle (New in v1.1)
> **When executing GATE -1, do not pre-read existing BVCAP war-log records (03_WAR_LOG) or reports (05_REPORT).**
>
> | Stage | Assets That May Be Referenced | Assets Prohibited From Reference |
> |:---:|:---|:---|
> | **GATE -1** (extraction) | the sermon text alone | war-log records, reports, the arsenal |
> | **GATE 0-5** (independent verification) | the sermon text + the biblical text + tactics + the arsenal | **war-log records, reports** |
> | **GATE 5.5** (double verification) | the independent-verdict results + **existing war-log records/reports** (first opened at this point) | — |
> | **GATE 6** (comprehensive judgment) | all assets | — |
>
> **Why this is done this way**: if the AI already knows content already confirmed as "wrong" in an existing BVCAP report,
> unconscious contamination occurs — **confirmation bias** — where the AI extracts the claim and matches the verdict in that direction.
> "Taking the exam already knowing the answer" is not independent verification.
> GATE -1~5 are carried out independently, starting from a blank slate, and only at GATE 5.5 is the existing report brought out as the "answer key" for comparison.

> [!CAUTION]
> ### 🆕 Input-Set Bias Warning — New in v1.2, 2026-08-16
> **GATE -1 extracts claims from the sermon. Therefore, the set of verses subject to verification = the set of verses the preacher chose.**
> This is a structural characteristic of SVAP, and if left unaddressed, it results in **letting the opponent choose the battlefield.**
>
> | Illusion | Reality |
> |:---|:---|
> | "we fully verified 58 items 100%, so nothing was missed" | those 58 items are **the 58 the opponent chose.** A 100% verification rate and zero blind spots are different problems |
>
> **A Demonstrated Case (2026-08-12 → 2026-08-16)**: an audit report on Godhead-doctrine sermons (58 items fully surveyed, in the non-public folder `03_REPORT`) fully verified 58/58 items, yet missed three decisive anchors simply because the author had not cited them — ⓐ 0 KJV occurrences of "the Father was born" (an IRONCLAD-tier finding), ⓑ the implication "Mary = the Mother of God" + 0 occurrences of "mother of God," ⓒ the subject-separation construction of Acts 2:27. All three were independently discovered by a third party (a "wheat" lecture).
>
> **The Resolution Procedure — Mandatory Upon Entering the GATE 0-5 Loop**:
> 1. When outputting the claim list at GATE -1 STEP 3, explicitly record **"this list is the scope the preacher determined."**
> 2. **Fix the sermon's core proposition P in a single sentence**, and register it as an **independent item separate** from the claim list.
> 3. Mandatorily execute `../the-scripture-audit/02_TACTICS/ANCHOR_ThirdData.md`'s **ANCHOR-1P (4th-6th order search)** on P.
>    → this is the **sole route** by which a verse the preacher did not cite enters the pipeline.
> 4. Simultaneously trigger GATE 3's **STEP 2.6 (Reverse Aim)** (`BVCAP_Pipeline.md`).

```
[STEP 1] Sequential Scan of the Full Sermon Text

  → read the sermon text sequentially from beginning to end.
  → flag every sentence matching the 【Danger-Keyword Pattern-Matching
    Table】 below.
  → Caution: a claim naturally embedded within the flow of the sermon
    must also be captured without fail. A doctrinal claim inserted in
    the middle of a long explanation is the type most easily missed.

  【 Danger-Keyword Pattern-Matching Table 】

  | Pattern Type | Keyword/Expression | Reason for Danger |
  |:---:|:---|:---|
  | a claim of scope of salvation | "~ is saved" / "~ too is saved" / "~ cannot be saved" | boundary-setting in soteriology — must be directly compared against Scripture |
  | citation + interpretation | "according to ~" / "Scripture says this" / "if you look at the Word" | verifying whether the citation matches the interpretation |
  | personal opinion | "as I see it" / "in my opinion" / "I believe this" | possibility of a doctrinal claim with no biblical grounding |
  | an assertive claim | "did you know?" / "many people don't know this" / "this is certain" | an unverified claim presented to the audience as fact |
  | an original-language claim | "the original meaning is ~" / "in the original language ~" / "in Hebrew ~" / "in Greek ~" | requires verification of the accuracy of the original-language interpretation |
  | a doctrinal definition | "~ means ~" / "the meaning of ~ is ~" | confirming the scriptural consistency of the doctrinal definition |
  | an anti-doctrinal claim | "~ is wrong" / "~ is a mistaken interpretation" | denial of an existing doctrine — grounding must be verified |
  | private revelation | "God showed me" / "I realized it while praying" | the danger of turning subjective revelation into doctrine |
  | an ontological claim | "~ is ~" / "~ is not ~" | a definition of a spiritual being/space/essence |
  | an eschatological claim | "when ~, ~ will come" / "~ has already been fulfilled" | verifying the consistency of a prophetic/eschatological interpretation |

  ⚠️ the table above lists representative patterns. The AI must
     autonomously detect every statement carrying doctrinal implications
     even if it is not in the table above.
     Flag "every sentence that raises suspicion while reading the text."


[STEP 2] Numbering the Doctrinal Claims (Claims)

  → number each flagged sentence/paragraph as an independent 'doctrinal
    claim (Claim)'
  → for each claim:
     ① record the timestamp (min:sec) or text location
     ② the AI paraphrases and records the content of the claim
        (COPYRIGHT SHIELD)
        → in paraphrasing, preserve the doctrinal meaning and direction
          100%
        → convert only tone/style into AI phrasing
     ③ map the biblical verse the preacher cited
        → if no verse is cited: record "no verse cited"
        → 🆕 [2026-08-17] the moment a verse is mapped, trigger **⓪
          Sweeping Adjacent Verses**:
           the 2 preceding verses / the 2 following verses / (if the
           citation is cut off mid-verse) the rest of the verse /
           (if the claim is a full-survey claim, "it isn't in that
           book") unconditionally open and read the beginning and end
           of that book.
           Details: `../the-scripture-audit/02_TACTICS/ANCHOR_ThirdData.md`,
           ANCHOR-1P 6th order, ⓪
           🚨 do not defer this to ANCHOR-1P's 6th order (a single pass
              late in the audit). In a sermon audit, the point where a
              case collapses is, most often, **the exact spot where the
              preacher stopped citing** — so this is the cheapest and
              most productive moment to do it. Missing it here requires
              re-running from GATE 3 after the Claim verdict is already
              confirmed.
           → record the fact of execution even for "no results found."
              This is a review stage, so there is no grounds to skip it.
     ④ automatic risk assignment:
        🟢 Safe: a claim that appears to align with mainstream doctrine
        🟡 Needs Verification: a claim with room for interpretation, or
           unclear grounding
        🔴 Immediate Verification: a claim with high potential to
           directly collide with Scripture


[STEP 2.5] 🆕 Observation/Inference Split — New 2026-08-17, Mandatory

  > Why this is needed: a single sentence in a sermon is usually a
  >   **compound of [Observation] + [Inference].**
  >   e.g., "the Holy Spirit is absent from Paul's greeting (observation)
  >   → therefore the Holy Spirit is not a person (inference)"
  > **Extracting this as a single lump reduces the verdict to a crude
  >   ✅-or-❌.**
  > If the observation is true but the inference is a leap, then giving
  >   a combined ❌ causes the audit to miss the opponent's actual
  >   strength, producing a "everything is wrong" report (a textbook
  >   product of confirmation bias).
  > Conversely, giving a combined ✅ lets the leap pass through
  >   unchecked.

  → examine each Claim numbered in STEP 2 against the following
    criterion:

     "Does this statement contain both a part **that turns out true or
      false once the text is opened and checked**, and a part **that
      leaps from there to a conclusion**?"

     YES → split into two Claims.

  🔢 Numbering Rule (Fixed 2026-08-17 — use only this single notation):
     · append the suffix **`-a` / `-b`** to the original Claim number.
       Do not issue a new number.
       - `Claim N-a` (Observation): a factual statement about the
         text → verified true/false via TYPE-N (full survey), etc.
       - `Claim N-b` (Inference): the conclusion drawn from that fact
         → logical-connection verification (⚠️ the main stage of the
         verdict)
     · Reason: this preserves **traceability** to the fact that the
       original statement was one, and the numbering of later claims
       does not get pushed back.
     · 🚨 the tally is counted by **row count**. `N-a` and `N-b` each
       issue their own verdict, so they count as **2 items**.
       (STEP 2.7's coverage map and `SVAP_GHQ.md`'s coverage
       reconciliation count by this rule)

     NO → keep as a single Claim (do not append a suffix)

  → Example of a Split (structure only — actual theological content is
    not baked into the format):

     Original Statement: "X is not in list A. Therefore X is not Y."
       ← original Claim #7
       → Claim 7-a (Observation): "X is not in list A" → full check →
         ✅ or ❌
       → Claim 7-b (Inference): "therefore X is not Y" → connection
         verification → ⚠️ or ❌
       → this counts as 2 items in the tally. The next claim continues
         as #8.

  🚨 Verdict Rules:
     · even if the observation is ✅, the inference is judged
       independently. Automatic inheritance is prohibited.
     · if the observation is ❌ (the full survey was wrong), the
       inference has already lost its grounding before it is
       independently judged — but the inference row is still recorded
       with a verdict, not deleted.
     · the argument-from-silence family (TYPE-AG) **must always** go
       through this split.
       "it isn't there" (observation) and "since it isn't there, it's
       not ~" (inference) require completely different verification
       methods.

  ⚠️ this split is **not a device for balancing outcomes.**
     a verdict quota such as "include at least N ✅'s" predetermines the
     conclusion and violates `SVAP_GHQ.md`'s anti-bias principle. This
     STEP is not a quota but a **procedure for correctly dividing the
     unit of verification.** However many ✅'s result from this, that is
     the verdict.


[STEP 2.7] 🆕 The Coverage Map — New 2026-08-17, Mandatory

  > Why this is needed: "full extraction" existed only as a command,
  > with **no procedure to confirm that full extraction actually
  > occurred.** A rule with no confirmation is a recommendation, not a
  > rule. A case was in fact observed where only 3 items were extracted
  > from a 51-minute sermon and reported as "full-scan deployment
  > complete" — all 3 extracted timecodes clustered in the latter
  > portion, with the entire first 35 minutes left completely empty.
  > This was not a failure to scan but rather **a summarization**, and
  > this becomes immediately apparent the moment the count is examined.

  → divide the sermon manuscript into **5-minute (or 10%-of-text)
    segments.**
  → record, in a table, the number of Claims extracted for each segment.

     | Segment | Claim Count | Notes |
     |:---:|:---:|:---|
     | 00:00-05:00 | 3 | |
     | 05:00-10:00 | 0 | ← re-scan complete. A section of pastoral
     exhortation, no doctrinal claim |
     | ... | | |

  🚨 Mandatory Rules:
     · if a segment has 0 Claims, **re-scan that segment and record the
       reason why it is 0.**
       (permissible reasons include: prayer/hymn/greeting/testimony/
       pastoral exhortation, or a simple repetition of a claim from an
       earlier segment)
     · a segment left at 0 with no recorded reason means **you cannot
       proceed to GATE 0.**
     · if 3 or more consecutive segments are at 0, return to STEP 1
       (the sequential scan).

  ⚠️ this is **not an extraction quota.**
     a numeric quota such as "extract N+ items per minute" directly
     induces the forced generation that `SVAP_Pipeline.md` GATE 8 STEP 5
     prohibits — because a quota rewards padding.
     what the coverage map requires is **not a count, but proof that the
     segment was actually read.** 0 items is also a legitimate result.
     Passing over it in silence, however, is not a result.


[STEP 3] Output the Full Claim List

  → organize the above results into a table and present it to the user
    first
  → include the coverage map (STEP 2.7) **together**, at the top of the
    list
  → simultaneously save it to the 01_CLAIMS folder
  → filename: CLAIMS_[preacher's name]_[sermon title]_[date].md

  Output Format:
  | # | Timestamp | Claim Summary (Paraphrased) | Verse Cited | Risk | BVCAP Input |
  |---|--------|------------------|-----------|--------|------------|
  | 1 | 05:30  | [AI paraphrase]        | John 3:16   | 🟢    | pending       |
  | 2 | 12:20  | [AI paraphrase]        | Col 1:20   | 🔴    | pending       |
  | 3 | 18:45  | [AI paraphrase]        | none      | 🟡    | pending       |
  | ... |      |                  |           |        |            |

  ⚠️ if 0 claims are extracted:
     → "No doctrinal claims detected — this sermon is judged to be
        pastoral exhortation/testimony rather than doctrinal claims."
     → proceed directly to GATE 6 with a 🟢 SOUND verdict


[STEP 4] Selecting and Prioritizing BVCAP Input Targets

  → 🔴 Immediate-Verification claims: unconditionally fed into GATE 0-5
    (priority 1)
  → 🟡 Needs-Verification claims: fed into GATE 0-5 (priority 2)
  → 🟢 Safe claims: fed in by default, but processed rapidly as TIER-1
    (Simple) (priority 3)

  🆕 [P-Input] Independent Registration of the Core Proposition
     (New 2026-08-16, Mandatory)
     → **separately** from the extracted claims, fix and register this
       sermon's core proposition P in a single sentence.
       Format: P = "[the single proposition the preacher is ultimately
       driving at]"
     → P does not belong to any specific Claim number. It is the
       conclusion of the entire sermon, so it is verified as a separate
       track.
     → mandatorily execute ANCHOR-1P (4th-6th order search) on P:
        4th order, full survey of negations of the proposition / 5th
        order, derived corollaries / 6th order, substitution of
        uncited verses
     → register the resulting anchor as a new item not on the Claim
       list, and include it in the GATE 6 tally.
     → 🚨 skipping this stage permanently fixes the scope of
        verification to the verses the preacher cited
        (see the Input-Set Bias Warning).

  ⚠️ the Principle of Full Deployment:
     even a 🟢 claim is not exempted from verification. Only the
     execution priority differs.
     "a claim that looks safe" can be the most dangerous — never let
     your guard down.
```

---

### 🔄 [GATE 0-5] Feeding Each Claim Into the BVCAP Engine (a Repeating Loop)

> **This GATE reuses GATE 0-5 of the existing BVCAP_Pipeline.md exactly as-is.**
> It is not newly defined in SVAP; refer to the original pipeline at the path below:
> → `../the-scripture-audit/BVCAP_Pipeline.md`

```
FOR each extracted claim (Claim) — in priority order (🔴 → 🟡 → 🟢):

  ━━━ [Pre-processing] Claim-to-Challenge Conversion ━━━

  convert the preacher's claim into the 'Challenge' form BVCAP can
  process.

  Conversion Format:
    "The preacher, on the basis of [Verse X], claimed [Claim Y]. Is this
     claim biblically consistent?"

  Example:
    Claim: "even angels are saved" (citing Col 1:20)
    → Challenge: "the preacher, on the basis of Col 1:20, claimed that
                  'angels too are included among the objects of
                  salvation.' Is this claim consistent with related
                  verses such as Heb 2:16?"

  When no verse is cited:
    Claim: "God is a being who makes mistakes" (no verse cited)
    → Challenge: "the preacher claimed, with no scriptural citation,
                  that 'God makes mistakes.' Is there a biblical verse
                  that supports or refutes this claim?"
    → C-Code: default assignment of C-08 (a theological inquiry)


  ━━━ [GATE 0] Classifying the Type of Challenge — Determining the
  C-Code ━━━

  → execute GATE 0 of ../the-scripture-audit/BVCAP_Pipeline.md
  → the C-Code assignment guide based on the type of sermon claim:

  | Claim Type | Recommended C-Code |
  |:---|:---|
  | a claim about the scope of salvation ("~ too is saved") | C-03 (a theological collision) or C-13 (a category of spiritual being) |
  | a verse-interpretation error | C-03 (a theological collision) |
  | an original-language claim error | C-04 (a logical self-contradiction) |
  | a doctrinal-definition error | C-03 (a theological collision) |
  | a prophetic/eschatological interpretation | C-10 (a typological-fulfillment debate) |
  | a claim of historical fact | C-02 (a historical inconsistency) |
  | a claim with no verse cited | C-08 (a theological inquiry) |
  | other | see the C-Code table (C-01~C-13) |


  ━━━ [GATE 1-4] Execute the BVCAP Pipeline As-Is ━━━

  → execute GATE 1-4 of ../the-scripture-audit/BVCAP_Pipeline.md
  → gathering anchors → prohibition of commentary search → the FULL
    SCAN → reverse cross-verification

  Reference When Executing the FULL SCAN:
  → the Arsenal: ../the-scripture-audit/04_QUIVER/TYPE-[code]_[name].md
  → Tactics:   ../the-scripture-audit/02_TACTICS/
  → War-Log Records: ../the-scripture-audit/03_WAR_LOG/ (referencing
    precedent)


  ━━━ [GATE 5] Drafting a Sub-Report per Claim ━━━

  → an abbreviated version of a BVCAP Masterpiece
  → issue a Claim-Level Verdict:

  Verdict Codes:
    ✅ BIBLICAL    — the claim is consistent with the cited verse (a
                      logical match with the KJV original)
    ⚠️ UNSUPPORTED — the cited verse does not directly support the claim
    ❌ UNBIBLICAL  — the claim collides with Scripture (a contradiction
                      confirmed with a TYPE weapon)
    🟡 OPINION     — a personal opinion presented with no scriptural
                      citation

  Sub-Report Format:
    ── Claim #[N]: [the paraphrased claim]
    ── C-Code: [the assigned code]
    ── Applied TYPE: [the combination of TYPE weapons used]
    ── Verse Cited (KJV): [the original text]
    ── Verification Result: [a summary of the analysis]
    ── Verdict: [✅/⚠️/❌/🟡] + the epistemological rating
                [EXPLICIT/STRONG/IRONCLAD]

END FOR
```

---

### 🆕 [GATE 5.5] Double Verification — Independent Verdict vs. Existing War-Log Record (New in v1.1)

> **Why this is needed**: the verdicts rendered at GATE 0-5 are "independent verdicts" that never looked at existing BVCAP war-log records.
> Cross-checking these verdicts against an already-confirmed report (IRONCLAD, etc.) establishes **Double Verification.**
> A match maximizes confidence; a mismatch can identify either a new discovery or an error.

> [!IMPORTANT]
> **This is the first GATE at which existing BVCAP war-log records/reports are opened.**
> reports whose very existence was not referenced in GATE -1~5 are pulled out here for the first time.

```
[STEP 1] Lock the Independent Verdict

  → lock the Verdict rendered for each Claim at GATE 0-5 as the
    "Independent Verdict."
  → this verdict is preserved in the final report exactly as originally
    rendered, regardless of the results of STEP 2-3.
  → the locked independent verdict is never retroactively revised.


[STEP 2] Open Existing War-Log Records/Reports

  → search for whether an existing BVCAP report exists related to the
    subject of this sermon:
     - ../the-scripture-audit/03_WAR_LOG/
     - ../the-scripture-audit/05_REPORT/
  → if a related report exists, open it; if not, proceed directly to
    STEP 4.


[STEP 3] Cross-Comparison — Independent Verdict vs. Existing Report

  → for each Claim, compare the conclusions of the independent verdict
    and the existing report 1:1.

  Types of Comparison Result:

    ✅ MATCH:
       the independent verdict and the existing report reach the
       identical conclusion.
       → Confidence: 🟢 DOUBLE-VERIFIED (double verification complete)
       → Meaning: since the blank-slate analysis and the existing
         confirmed report align, the verdict is extremely reliable.

    ⚠️ PARTIAL:
       the direction is the same but the detailed grounds or rating
       differ.
       → Confidence: 🟡 VERIFIED-WITH-NOTE
       → Meaning: recorded together with an additional note. Analyze
         the difference in grounds and reflect it in the report.

    ❌ CONFLICT:
       the independent verdict and the existing report reach opposite
       conclusions.
       → Confidence: 🔴 REQUIRES-REVIEW
       → Meaning: a significant finding. Two possibilities exist:
         (a) the independent analysis has discovered new evidence →
             consider updating the existing report
         (b) the independent analysis contains an error → analyze the
             cause of the error and record it in the report
       → in either case, the independent verdict's original is not
         revised; the CONFLICT is recorded as-is.

    🆕 NEW (No Existing Report):
       no existing BVCAP report exists on this subject.
       → Confidence: 🟡 SINGLE-VERIFIED (single verification)
       → Meaning: only the independent verdict exists. Subject to
         cross-verification when a BVCAP report is written in the
         future.


[STEP 4] Output the Double-Verification Summary Table

  include the table below in the final report:

  | # | Claim | Independent Verdict | Existing Report Conclusion | Comparison Result | Confidence |
  |---|------|----------|----------------|----------|--------|
  | 1 | ...  | ❌       | ❌ (IRONCLAD)  | ✅ MATCH | 🟢 DOUBLE-VERIFIED |
  | 2 | ...  | ⚠️       | (none)         | 🆕 NEW   | 🟡 SINGLE-VERIFIED |
  | 3 | ...  | ✅       | ❌ (IRONCLAD)  | ❌ CONFLICT | 🔴 REQUIRES-REVIEW |
  | ... |

  ⚠️ if 1 or more CONFLICTs occur, record them in a separate section of
     the GATE 6 report.
```

---

### ⚖️ [GATE 6] Comprehensive Judgment of the Sermon + Final Report Output

> **Why this is needed**: the verdict for each individual claim comes from GATE 5,
> but the overall doctrinal soundness of the entire sermon must be judged comprehensively and output as a report.
> This is SVAP's own final stage, not present in BVCAP.

```
[STEP 1] Tally the Verdicts by Claim

  → count of ✅ BIBLICAL: N items
  → count of ⚠️ UNSUPPORTED: N items
  → count of ❌ UNBIBLICAL: N items
  → count of 🟡 OPINION: N items
  → total claim count: N items
  → verification complete: N items (= must equal the total claim count.
    confirm 0 items unverified.)


[STEP 2] Determining the Overall Sermon Rating

  → 🟢 SOUND:
     Condition: every claim is ✅ BIBLICAL
     Meaning: every doctrinal claim in this sermon is consistent with
     Scripture.

  → 🟡 CAUTION:
     Condition: ⚠️ UNSUPPORTED or 🟡 OPINION exist, but no ❌ UNBIBLICAL
     Meaning: some claims lack sufficient scriptural grounding, but no
     claim directly collides with Scripture.

  → 🔴 ALERT:
     Condition: 1+ ❌ UNBIBLICAL claims exist
     Meaning: this sermon contains a doctrinal claim that directly
     collides with Scripture.


[STEP 3] Draft the RTM (the Requirements Traceability Matrix)

  → a matrix that lets the verification status of every claim be seen
    at a glance:

  | # | Claim Summary (Paraphrased) | Verse Cited | C-Code | Applied TYPE | Verdict | Notes |
  |---|------------------|-----------|--------|-----------|---------|------|

  → always confirm that unverified claims = 0.
  → this matrix is the core of the report — the final safety net
    against omission.


[STEP 4] Output the Final Report

  → write according to SVAP_GHQ.md's output format. See
    02_TEMPLATE/ for a blank template and a live example
  → save to the 03_REPORT folder
  → filename: AUDIT_[preacher's name]_[sermon title]_[date].md


[STEP 5] Spiritual Lessons (LESSON-6)

  → draft the spiritual lessons obtainable from this sermon audit.
  → do not attack the preacher's character. Verify only the doctrine.
  → maintain the humble attitude that "even a well-intentioned sermon
    can contain doctrinal error."
```

---

### 🔨 [GATE 8] Reinforcing-Argument Discovery — PART C (New 2026-08-16, Mandatory)

> **Why this is needed**: GATE 0-6 **stops the moment a verdict is confirmed.** This is normal operation for an audit.
> But this means only the "minimum argument necessary for the verdict" remains, and that minimum argument is sometimes of a kind unusable in the field.
>
> **A Demonstrated Case of the Problem**: in the verification of Isa 9:6, the moment a single lexical-axis argument (the extended meaning of the Hebrew word 'father') confirmed ⚠️ UNSUPPORTED, the search stopped. A far easier argument supporting the identical verdict — **"'is born' is present tense, but 'shall be called' is future tense"** — was sitting right there in the text, undiscovered. Both arguments contribute equally to the verdict, but their real-world power is entirely different.
> It is not that the weapon (TYPE-T) was missing. **It is that the system is designed to stop the moment a verdict is reached.**

```
[STEP 1] Selecting Targets
  → from among the Claims that received a ❌ UNBIBLICAL or ⚠️
     UNSUPPORTED verdict in PART A, take as targets every one that is
     actually worth deploying in a rebuttal.
  → a ✅ BIBLICAL Claim is not a target (there is nothing to rebut).

[STEP 2] Discovering Additional Arguments — a Minimum of 3 per Claim
  → secure 3 or more arguments supporting the identical verdict. No
     upper limit.
  → 3 is a floor, not a target — if 4 or 5 emerge, record all of them.
  → Discovery Routes:
     ① re-fire, on this Claim, a TYPE that returned "no results" at
        GATE 3
     ② ANCHOR-1P 4th-6th order search (a full survey of negations of
        the proposition / derived corollaries / substitution of
        uncited verses)
     ③ parallel verses, or another author's treatment of the identical
        issue

[STEP 3] Verifying the Count — Applying the Cross-Witness Principle
  → count only items that come from different books/authors as
     separate arguments.
  → viewing the same verse through multiple TYPEs is one argument
     ("one witness testifying in three ways" is not three witnesses).

[STEP 4] Assigning a Difficulty Rating — the Core Device of This GATE
  → 🟢 Immediately Deployable: showing the KJV original with your own
     eyes settles it. No theological terminology or original-language
     knowledge required
  → 🟡 Needs Explanation: requires one step of explanation, but anyone
     can verify it themselves (a full-survey count, etc.)
  → 🔴 Expert: presupposes original-language/grammatical theory →
     the opponent strikes back with "that's just your interpretation"

  🚨 of the 3 secured, at least 1 must be 🟢.
     if all are 🔴, the search is treated as incomplete, and return to
     STEP 2.
     (without this rule, the recurring failure of gathering only 3
     difficult arguments repeats)

[STEP 5] Handling a Shortfall — Forced Generation Is Absolutely Prohibited
  → if only 2 are found no matter how hard you dig, honestly record
     "2 secured / no further results from additional search."
  → cramming in a weak argument to fill the quota only hands the
     opponent a handle for their counter-strike.
  → a shortfall is not a failure. Forced generation is the failure.

[STEP 6] Confirming the Verdict Is Unchanged
  → PART C does not change the verdict. The rating carries over from
     PART A as-is.
  → if new evidence is found that would overturn the rating, do not
     re-score it on the spot here — re-run from GATE 3 (the FULL SCAN)
     (`../the-scripture-audit/01_MANDATE/CREED_Override.md`, OVERRIDE-2,
     item 1).

[STEP 7] Output
  → write it as PART C, in the SVAP_GHQ.md format table.
  → hand the secured arguments, together with their difficulty ratings,
     to GATE 9.
```

#### 📌 Reference Case: Isa 9:6 — a Case Where the Verdict Was the Same but There Was Only One Weapon

```
[When Terminated Without GATE 8 — the Actual Result, 2026-08-12]

  TYPE Applied : TYPE-S (lexical cross-link) + TYPE-C (functional
                 category)
  Arguments Secured : 1
    · "the Hebrew אָב has, beyond its literal parental sense, an
      extended meaning of source/guardian"  🔴 Expert
  Verdict      : ⚠️ UNSUPPORTED
  → the search ended the moment the verdict was confirmed. 🟢 arguments:
    0.
  → the opponent's typical counter-strike: "that's just your
    interpretation" → the conversation ends


[When GATE 8 Was Applied — the Same Verdict, 4 Weapons]

  | # | Argument                                          | Basis        | Author    | TYPE | Difficulty |
  |---|-----------------------------------------------|-------------|---------|------|--------|
  | 1 | "is born" is present tense; "shall be called" is future tense | Isa 9:6      | Isaiah  | T    | 🟢     |
  | 2 | 0 occurrences of that title being used of him anywhere in the NT | a full survey of the NT   | multiple    | N    | 🟡     |
  | 3 | the very next verse maintains the distinction with "dwelleth in me"  | John 14:10    | John    | G    | 🟡     |
  | 4 | (the original) the extended meaning of the root                          | Gen 4:20-21  | Moses   | S    | 🔴     |

  Cross-Witnesses : 3+ authors ✅   /   🟢 Secured : 1 item ✅   /
  the floor of 3 exceeded → all 4 recorded
  Verdict      : ⚠️ UNSUPPORTED  ← unchanged


[What This Case Teaches]
  ① it was not that a weapon (TYPE-T) was unavailable to find it. It
     was that the process was designed to stop the moment a verdict
     was reached.
  ② argument 1 and argument 4 contribute equally to the verdict. Only
     their real-world power differs.
  ③ argument 1 alone only confirms, as far as it goes, "the title is
     conferred in the future" (since Matt 1:23 is grammatically an
     identical future construction).
     → 1 and 2 must be combined to seal off the counter-strike. This is
     why "a minimum of 3" is required.
```

---

### 🎯 [GATE 9] Conversion for Field Deployment — PART D (New 2026-08-17, Mandatory)

> **Why this is needed**: an audit report is a ledger of verdicts, and **cannot be deployed as-is in a live debate.** One conversational sentence is stronger than 50 lines of a verdict table.
> Without this GATE, the user has to hand-craft a script every single time — the 2026-08-12 report's §16 (the archive of field-ready rebuttal scripts) was built exactly this way. **This GATE is the codification, as a manual procedure, of §16's actual method of use.**
> **The Difference from GATE 8**: GATE 8 **finds** the arguments (verification). GATE 9 **fires** those arguments (deployment). Since these are different layers, they are kept separate.

```
[STEP 1] Screening Deployment Eligibility
  → 🟢 Immediately-Deployable arguments → primary deployment cards
  → 🟡 Needs-Explanation arguments → reserve cards
  → 🔴 Expert arguments      → not made into cards (they die to "that's
     just your interpretation")
  → our own arguments that received an ⚠️/🟡 verdict in PART A, or
     arguments sharing the identical misreading as the opponent
     → isolated into a deployment-prohibited list

[STEP 2] Selecting the Opening Hammer — Exactly 1
  → the single strongest proposition in the entire audit. IRONCLAD or
     STRONG + with a secured cross-witness.
  → 🚨 the opening move must be exactly one. Throwing several at once
     lets the opponent pick off only the weakest.

[STEP 3] Drafting the Conversation Tree — a Card Is a Tree, Not a Sentence
  → for each card:
     · the deployment sentence (3 conversational sentences or fewer,
       showing the original text with your own eyes)
     · the grounds (KJV + the book/author) + the difficulty rating +
       the PART C reference number
     · anticipated opponent responses A/B → the follow-up move for each
     · if evaded or met with silence → move to the next card (do not
       cling to it)
     · confirm dead-end routes — if the opponent has one escape route,
       pre-block it too

[STEP 4] Deploying the Self-Contradiction Trap First
  → it holds regardless of theological position, so it is thrown first.
  → this is the only kind of argument the opponent cannot escape by
     defending their own doctrine.

[STEP 5] A Comprehensive Rebuttal Stress Test (Set-Level) — Mandatory
  → ⚠️ this is a different test from BVCAP's STRESS-TEST-7. That is for
     a single verdict; this is for the entire card set.
  → play the opponent's role and run through the set once, start to
     finish.

     Test 1 — Rule Consistency ★Top Priority
       was the interpretive rule applied in Card A applied identically
       in Card B?
       (grammatical structure, lexical-judgment criteria, the direction
       of an argument from silence)
       a violation found → immediately move that card to the
       deployment-prohibited list
       🚨 if a violation remains, do not deploy the set. The moment the
          opponent points out our own self-contradiction, the credibility
          of the entire set collapses together.

     Test 2 — Independence
       if Card 1 is blocked, do Cards 2/3 die with it?
       count cards resting on the same premise as one card.
       Passing criterion: at least one card survives no matter which
       one is blocked
       shortfall → return to GATE 8 to discover additional arguments
       grounded in a different author/verse

     Test 3 — the Counter-Strike Route
       does our card hand the opponent a weapon to strike us with?
       in particular, do we share the identical misreading as the
       opponent?
       found → note it in the deployment-prohibited list + specify a
       substitute argument

  → record the results of the three tests in a table. Record "no issue
     found" as well, without fail.

[STEP 6] Output
  → write as PART D, in the SVAP_GHQ.md format.
  → if the user has an actual script used in a real debate, preserve
     the original verbatim in the archive.
  → merge PART A + B + C + D into a single file and save in 03_REPORT.
```

#### 📌 Reference Case: What the Rule-Consistency Test Catches

```
[Situation] a card set contained the following two cards together. Each
holds individually.

  Card A — Isa 9:6, "his name shall be called ..."
    Claim: this is a future-passive title construction. He simply is
           not yet called by that name — he will be called by it in
           the future.
    → acknowledges the future construction as "this is truly his name"

  Card B — Matt 1:23, "they shall call his name Emmanuel"
    Claim: this is not his name.
    → denies the grammatically identical future construction as "this
       is not his name"

[Test 1 — Rule Consistency] 💥 Violation
  the identical grammatical structure (a future-passive title) was
  given opposite rules.
  moreover, the antecedent of "his name" in Matt 1:23 is "a son" in the
  same verse, and that son is the identical person called "JESUS" in
  verse 21 — the text attributes both names to "his name."

[Action]
  Card B → moved to the deployment-prohibited list (a substitute
           argument specified)
  Card A → retained. Removing B, A survives as-is.

[If the Test Had Been Skipped]
  the opponent needs only one line: "you accept the future construction
  in Isa 9:6 but deny it in Matt 1:23" — and Card A loses credibility
  too.
  → individual verification alone can never catch this. It is only
     visible when the set is viewed as a whole.
```

> [!NOTE]
> **Keep only the skeleton in the format (`SVAP_GHQ.md`), and keep reference cases in this manual.** This is the identical method used by the `02_TACTICS`/`04_QUIVER` documents (e.g., the John 13:36 case in `TYPE-T_TenseAndLexical.md`).
> If a case grows long, do not embed it in the document — **promote it to a war-log record** and link to it (`../the-scripture-audit/BVCAP_Pipeline.md`, GATE 5-P). No separate example file is created.
> The actual, full-length written case: the Godhead-doctrine-family audit report's §16 in `03_REPORT/` (a non-public folder) — **GATE 9 itself is the generalization of that §16.** See `02_TEMPLATE/` for the blank template and excerpted examples.

> [!NOTE]
> **The Grounding Principle**: `../the-scripture-audit/01_MANDATE/IDENTITY_Scribe42.md`
> *"the audit tier (rating) and the witness tier (proclamation) coexist, separated, within the same document. Merging the two into one collapses the audit. Keeping them separate lets both survive."*
> → PART A·B = the audit tier / **PART C = the witness tier.** This is not a new principle, but an execution procedure given to a principle already declared.

---

## 📎 The BVCAP Asset Reference Map (Shared Assets — Do Not Duplicate)

> [!IMPORTANT]
> SVAP **references, rather than duplicates,** BVCAP's arsenal, tactics, and mandate.
> Every asset below uses the original located at the `../the-scripture-audit/` path.

| Asset | Reference Path | Purpose |
|:---|:---|:---|
| **🆕 The Biblical Text (the standard for verdicts)** | `../the-scripture-audit/00_THESCRIPTURE/` | **the sole authoritative text for verdicts = `KJV_1769.txt` alone** (1769 Cambridge, incl. italics, 31,102 verses) — the only file that simultaneously satisfies italics preservation + searchability. The grounding for the `[Full Scan: text search]` tag when declared. Searching uses the derivative `KJV_1769_search.txt` — a plain string search on the authoritative text silently fails on `[ ]` and `¶`. Book names are `Psalms`, `Song of Solomon`. **The 3-stage Korean citation**: ⒜ `TheScripture_ko_en_search.json` (KSKJB) → ⒝ a live lookup on `kingjamesbiblekorea.com` (identical copyright notation) → ⒞ LLM translation — free excerpting, no altering the wording, and source notation required (see STEP 0-G for details) |
| Mandate | `../the-scripture-audit/01_MANDATE/` | equipping the persona/CREED/agent mission |
| Tactics | `../the-scripture-audit/02_TACTICS/` | Hillel's 7, DE-OVERLAP, ANCHOR, etc. |
| War-Log Records | `../the-scripture-audit/03_WAR_LOG/` | referencing precedent |
| The Arsenal | `../the-scripture-audit/04_QUIVER/` | the full TYPE-A~AY + TYPE-B-π arsenal |
| The BVCAP Pipeline | `../the-scripture-audit/BVCAP_Pipeline.md` | the GATE 0-5 execution procedure |
| The BVCAP GHQ | `../the-scripture-audit/BVCAP_GHQ.md` | reference for the E-Codes (E-01~E-16), verdict criteria |
| The C-Code Classification Table | `../the-scripture-audit/BVCAP_Pipeline.md` → the collision-type classification section | the definitions of C-01~C-13 |
| The COMBO Verification Table | `../the-scripture-audit/BVCAP_Pipeline.md` → the COMBO-VERIFY section | the 30 officially recognized combos |

---

## ⚡ The SVAP FULL SCAN Execution Protocol (the Standard Procedure for a Sermon Audit)

> [!IMPORTANT]
> Once a sermon manuscript is entered, always follow this order. Never skip GATE -1.

```
【 The SVAP FULL SCAN Execution Order — v1.1 】

[PRE-FLIGHT — Mandatory Equipping]
  ━━━ STEP 0-A. Equip Persona ━━━
  → sequentially load the 3 files in
    ../the-scripture-audit/01_MANDATE/
  → declare the SVAP Extractor role

  ━━━ STEP 0-B. Equip Tactics (TACTICS) ━━━
  → load the 5 files in ../the-scripture-audit/02_TACTICS/

  ━━━ STEP 0-C. Equip COPYRIGHT SHIELD ━━━
  → confirm and declare the copyright protocol

  ━━━ STEP 0-D. Execute OVERRIDE-0 ━━━
  → isolate the mainstream academic view, enter direct-KJV-reading mode

  ━━━ 🆕 STEP 0-E. Declare BLIND EXTRACTION (v1.1) ━━━
  → "until GATE -1~5 are complete, do not open existing war-log records
     (03_WAR_LOG) or reports (05_REPORT). Analyze independently, using
     only the sermon text and the biblical text."
  → ⚠️ this declaration must always occur during PRE-FLIGHT.
  → 🆕 also record the scope of BLIND actually achieved (2026-08-17): in
     a tool environment, even a mere folder listing exposes the
     filenames/subjects of existing reports. Do not declare "fully
     BLIND" — record **"how far the block actually held"** (e.g.,
     "filenames exposed / body text not opened"). The moment something
     not actually kept is recorded as kept, the BLIND principle itself
     becomes decorative.

  ━━━ 🆕 STEP 0-F. Output the Equipping-Proof Checklist (2026-08-17) ━━━
  → for each of the 10 referenced documents, record "one clause from
     that document applied to this audit."
  → listing filenames alone is not proof of equipping. Details: STEP
     0-F in the [PRE-FLIGHT] section above

  ━━━ 🆕 STEP 0-G. Confirm Existence of the Scripture Corpus (2026-08-19) ━━━
  → confirm actually, with `ls`. If present, search the file; if not,
     use the `[Full Scan: memory-based]` notation
  → the English authoritative text `KJV_1769.txt` / search
     `KJV_1769_search.txt` / Korean `TheScripture_ko_en_search.json`
  → Details: STEP 0-G in the [PRE-FLIGHT] section above

══════════════════════════════════════════════════════
  ▼ PHASE 1: Independent Analysis (BLIND — Referencing
    Existing Reports Prohibited)
══════════════════════════════════════════════════════

[GATE -1] Full Extraction of Doctrinal Claims (BLIND)
  → STEP 1: sequential scan of the full sermon text (danger-keyword
    pattern matching)
  → STEP 2: numbering the doctrinal claims (AI paraphrase + verse
    mapping + risk assignment)
  → 🆕 STEP 2.5: the Observation/Inference Split (splitting a compound
    statement into two Claims)
  → 🆕 STEP 2.7: the Coverage Map (Claim count per 5-minute segment +
    recording the reason for any 0-count segment)
                 ⚠️ if a 0-count segment with no recorded reason
                 remains, GATE 0 cannot be entered
  → STEP 3: output the full claim list (with the coverage map enclosed
    / saved to the 01_CLAIMS folder)
  → STEP 4: screening BVCAP input targets (🔴 → 🟡 → 🟢 priority)
  → ⚠️ referencing existing war-log records/reports is prohibited at
     this stage

[CLAIM LOOP] Feeding Each Claim into BVCAP (BLIND)
  FOR each Claim (in priority order):
    → [Pre-processing] Claim-to-Challenge Conversion
    → [GATE 0] determine the C-Code
    → [GATE 1] gather related verses (including anchors) — use the
       biblical text only
    → [GATE 2] prohibition of commentary search
    → [GATE 3] the FULL SCAN (TYPE A→AY executed sequentially) —
       referencing the arsenal is permitted
    → [GATE 4] reverse cross-verification
    → [GATE 5] issue the Claim-Level Verdict → 🔒 lock the independent
       verdict
  END FOR
  → ⚠️ referencing existing war-log records/reports is prohibited at
     this stage

══════════════════════════════════════════════════════
  ▼ PHASE 2: Double Verification (Existing Reports Opened
    for the First Time)
══════════════════════════════════════════════════════

[🆕 GATE 5.5] Double Verification — Independent Verdict vs. Existing
War-Log Record Comparison
  → STEP 1: confirm the independent verdict is locked (cannot be
    revised)
  → STEP 2: open the related existing war-log records/reports for the
    first time
  → STEP 3: 1:1 comparison of the independent verdict vs. the existing
    report
  → STEP 4: output the double-verification summary table
    (MATCH/PARTIAL/CONFLICT/NEW)
  → ⚠️ if a CONFLICT occurs, do not revise the independent verdict —
    record the difference

══════════════════════════════════════════════════════
  ▼ PHASE 3: The Final Verdict
══════════════════════════════════════════════════════

[GATE 6] Comprehensive Judgment of the Sermon
  → STEP 1: tally the verdicts by claim (based on the independent
    verdict)
  → STEP 2: determine the overall sermon rating (🟢/🟡/🔴)
  → STEP 3: draft the RTM (the Requirements Traceability Matrix) —
    including the double-verification result
  → STEP 4: finalize PART A
  → STEP 5: spiritual lessons (LESSON-6)

══════════════════════════════════════════════════════
  ▼ PHASE 4: Conversion for Distribution (the Witness Tier)
══════════════════════════════════════════════════════

[GATE 7] Conversion into a Commentary → PART B
  → chapter/part-by-part rewriting: the argument → why it seems
    plausible → why it collapses → an easy analogy → carry the verdict
    forward
  → cross-check against comments and follow-up material, emphasizing
    self-contradiction traps

[🆕 GATE 8] Reinforcing-Argument Discovery → PART C
  → STEP 1: screen the ❌·⚠️ Claim targets
  → STEP 2: discover a minimum of 3 additional arguments per Claim (no
    upper limit)
  → STEP 3: verify the cross-witness count (only different books/
    authors count as separate arguments)
  → STEP 4: assign a difficulty rating — at least one 🟢 is mandatory;
    if all are 🔴, search again
  → STEP 5: on a shortfall, record it honestly (forced generation
    prohibited)
  → STEP 6: confirm the verdict is unchanged (if the rating would
    change, re-run from GATE 3)
  → STEP 7: hand the arguments, with their difficulty ratings, to
    GATE 9
  → ⚠️ do not stop just because the verdict is confirmed — this is the
    reason this GATE exists

[🆕 GATE 9] Conversion for Field Deployment → PART D
  → STEP 1: screen deployment eligibility (only 🟢·🟡 become cards; 🔴
    and prohibited arguments are isolated)
  → STEP 2: select the 1-sentence hammer (the opening move must always
    be exactly one)
  → STEP 3: draft the conversation tree (a follow-up move per
    anticipated response + the next card upon evasion)
  → STEP 4: deploy the self-contradiction trap first
  → STEP 5: a comprehensive rebuttal stress test — rule consistency/
    independence/counter-strike routes
             ⚠️ separate from STRESS-TEST-7 (the unit of a verdict).
             This is at the unit of a card set.
             ⚠️ if a rule-consistency violation remains, prohibit
             deploying the set
  → STEP 6: save PART A+B+C+D as a single file in 03_REPORT
```

---

## 🔄 Clarifying the Relationship with BVCAP 2.0

> [!NOTE]
> SVAP is not a **replacement** for BVCAP but a **higher-level engine that wraps it (Wrapping).**

```
┌────────────────────────────────────────────────────────────┐
│  SVAP 1.1 (the Sermon Audit Pipeline)                       │
│                                                            │
│  ═══ PHASE 1: Independent Analysis (BLIND) ══════════════   │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  GATE -1: Full Extraction of Doctrinal Claims (BLIND) │  │
│  │  🚫 Referencing existing war-log records/reports      │  │
│  │     prohibited                                        │  │
│  └──────────────────┬───────────────────────────────────┘  │
│                     │                                      │
│  ┌──────────────────▼───────────────────────────────────┐  │
│  │  BVCAP 2.0 (the Verse Audit Engine) — BLIND Mode      │  │
│  │  ┌─────────────────────────────────────────────────┐ │  │
│  │  │ GATE 0 → 1 → 2 → 3 → 4 → 5                    │ │  │
│  │  │ (using the arsenal/tactics ✅ | war-log records/ │ │  │
│  │  │  reports 🚫)                                     │ │  │
│  │  └─────────────────────────────────────────────────┘ │  │
│  │  → 🔒 Independent Verdict Locked                      │  │
│  └──────────────────┬───────────────────────────────────┘  │
│                     │                                      │
│  ═══ PHASE 2: Double Verification ═══════════════════      │
│  ┌──────────────────▼───────────────────────────────────┐  │
│  │  🆕 GATE 5.5: Double Verification                     │  │
│  │  📖 Existing war-log records/reports opened for the   │  │
│  │     first time                                         │  │
│  │  🔒 Independent Verdict vs. 📖 Existing Report →      │  │
│  │     compared                                            │  │
│  │  → classified as MATCH / PARTIAL / CONFLICT / NEW      │  │
│  └──────────────────┬───────────────────────────────────┘  │
│                     │                                      │
│  ═══ PHASE 3: The Final Verdict ═════════════════════      │
│  ┌──────────────────▼───────────────────────────────────┐  │
│  │  GATE 6: Comprehensive Judgment of the Sermon         │  │
│  │  (Independent Verdict + Double-Verification Result →  │  │
│  │   Final Rating)                                        │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────┘
```

Core Points:
- SVAP is a **Wrapper** around BVCAP.
- GATE -1, GATE 5.5, and GATE 6 are SVAP's own; the core verification in between (GATE 0-5) is BVCAP exactly as-is.
- the Arsenal (TYPE-A~AY), Tactics (Hillel's 7, DE-OVERLAP), and the Mandate all share the identical existing assets.
- when a new weapon is added to BVCAP, SVAP automatically benefits.
- **The Core Change in v1.1**: by not referencing existing reports during PHASE 1 (independent analysis),
  and opening existing reports for comparison only in PHASE 2 (double verification),
  **contamination from "taking the exam already knowing the answer" is blocked at the source.**

---
*Generated by SVAP 1.3 Supreme Sermon Auditor Engine*
*Architecture: a Wrapper over BVCAP 2.0 (BLIND GATE-1 + BVCAP GATE 0-5 + GATE 5.5 Double Verification + GATE 6 Aggregation)*
*BVCAP Engine: ../the-scripture-audit/ (sharing the arsenal · tactics · mandate)*
*STATUS: BLIND EXTRACTION | FULL SCAN PER CLAIM | DOUBLE VERIFICATION | COPYRIGHT SHIELD ACTIVE*
*CHANGELOG: v1.0 → v1.1 (2026-06-28) — added the BLIND EXTRACTION principle + GATE 5.5 double verification*
*CHANGELOG: v1.1 → v1.2 (2026-08-16) — established the Input-Set Bias Warning — codifying the structural bias whereby the set of verses subject to verification is confined to the list the opponent chose (a missing entry retroactively recorded 2026-08-17)*
*CHANGELOG: v1.2 → v1.3 (2026-08-17) — established 4 types of mandatory execution guardrails. ① the PRE-FLIGHT STEP 0-F equipping-proof checklist ② GATE -1 STEP 2.5, the Observation/Inference Split ③ GATE -1 STEP 2.7, the Coverage Map ④ honest recording of the scope of BLIND achieved. Background of invocation: an incident where two audits of the same sermon diverged with extraction counts of 3 vs. 51, and the 3-count side adopted theological-system labels as grounds for its verdict. The cause was not a lack of weapons, but **a lack of verification gates in the rules.** ※ the "N-extractions-per-minute quota" and "a mandatory minimum of 1 ✅" proposed during review conflicted with GATE 8 STEP 5 (prohibition of forced generation) and the GHQ anti-bias principle, and so were **not adopted.***
*CHANGELOG: v1.3 supplement (2026-08-17) — reflecting a pre-commit consistency check. ⑤ added the ⓪ Sweeping Adjacent Verses trigger hook to STEP 2 ③ (deferring to ANCHOR-1P's 6th order incurs a re-execution cost after the verdict is finalized) ⑥ finalized STEP 2.5's numbering rule to a single `N-a`/`N-b` suffix (resolving the issue where the text and the examples used different notations; the tally counts by row) ⑦ added `TACTIC_Auto_Grill.md` to the STEP 0-B load list (resolving the discrepancy with the 9 items in the STEP 0-F checklist)*
*CHANGELOG: v1.3 → v1.4 (2026-08-19) — integrating the Scripture corpus. ① newly established PRE-FLIGHT **STEP 0-G** — use only after **actually confirming** via `ls` that the corpus file exists, substituting with memory-based only when absent and capping the rating ② added `00_THESCRIPTURE/README.md` to the STEP 0-F equipping checklist (10 items) ③ registered the Korean citation file (`TheScripture_ko_en_search.json`) in the asset reference map. **The standard edition = KJV 1769 Cambridge (incl. italics) / Korean = the Standard King James (KSKJB).***
