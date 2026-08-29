---
id: "catholic-report-153"
title_ko: "📁 CVCAP 마스터피스 보고서 인덱스"
title_en: "📁 CVCAP Masterpiece Report Index"
file_ko: "REPORT_INDEX.md"
file_en: "REPORT_INDEX.md"
category: "report"
status: "translated"
source: "KO"
updated: "2026-08-27"
---
# 📁 CVCAP Masterpiece Report Index
## — Document Court (Catholic Internal Documents Only) Record of Findings —

> **STATUS**: CVCAP 3.0 automation pipeline running | **Engine**: CVCAP 3.0 (single-track internal documents + automation layer)
> **Operation Goal**: Confirm the internal collapse (Implosion) of Catholic Magisterium and infallibility
> **Last Updated**: 2026-07-21 (removed phantom cards + full-layer integrity check passed 22/22 — scripts/verify_pipeline.py)

---

## 🆕 Currently Active Outputs (CVCAP 3.0 — Automated Detection Based on 04_DOCTRINE_DB)

> Below are the **currently active reports**, automatically indexed by `scripts/conflict_detector.py` from the input of
> `04_DOCTRINE_DB/` (71 doctrine cards, duplicates cleaned up) and compiled comprehensively by a human.

| Output | Location | Content | Status |
|:---|:---|:---|:---:|
| Comprehensive Audit Report | [REPORT_Catholic_Magisterium_Internal_Collisions_Comprehensive_Audit.md](./REPORT_Catholic_Magisterium_Internal_Collisions_Comprehensive_Audit.md) | **16 major contradictions** individually verified (soteriology, infallibility, sacramental theology, Mariology, ethical doctrine, etc.) | ✅ Latest |
| Automated Detection Candidates (Embedding) | [auto_conflict_results.csv](./auto_conflict_results.csv) | **2,154 candidates** (unconfirmed) that passed Sentence-Transformers similarity ≥0.60 + the cross-claim filter | ✅ Latest |
| Automated Detection Excluded Cases (Transparency Disclosure) | [auto_conflict_excluded_self_negation.csv](./auto_conflict_excluded_self_negation.csv) | **1,760 cases** excluded as false positives (same position) — includes a list of 34 manually verified exclusion pairs | ✅ Latest |
| Combo Filter Tagging | [cvcap_combo_results.csv](./cvcap_combo_results.csv) | **626 cases** simultaneously flagged by CVCAP 3.0's multiple filters (keyword tagging — unconfirmed candidates) | ✅ Latest |
| LLM Secondary Review (YES only) | [llm_verified_conflicts.csv](./llm_verified_conflicts.csv) | `scripts/llm_judge.py` — headless review via the claude CLI (no API key required). **✅ Full review of all candidates complete** (cumulative YES: 55 cases — all manually re-verified) | ✅ Complete |
| Full LLM Review Log | [llm_judge_full_log.csv](./llm_judge_full_log.csv) | All rulings (YES/NO) + rationale. **0** candidates remain unreviewed. To resume after adding new cards: `python scripts/llm_judge.py next 200` | ✅ Complete |
| Collision Network Visualization | [conflict_network.html](./conflict_network.html) | Interactive Vis.js graph — **top 150** by similarity (open in Chrome) | ✅ Latest |
| Confirmed Collision Cards | [`../05_COLLISION_CARDS/confirmed/`](../05_COLLISION_CARDS/confirmed/) | COL-001~014, fully verified by hand (009~014 are newly discovered cards that passed the 3-stage process of automated detection → LLM review → source-text comparison: EENS Chapter 3 + the self-negation of the same-sex blessing + the reversal on religious freedom + the practical contradiction of Canon 844) | ✅ Latest |
| Candidate Cards | [`../05_COLLISION_CARDS/candidates/`](../05_COLLISION_CARDS/candidates/) | Empty — CAND-001 was promoted to COL-014 after passing the OODA promotion hearing on 2026-07-21 | ✅ Processing complete |
| Combo Cards (Confirmed) | [`../05_COLLISION_CARDS/combos/`](../05_COLLISION_CARDS/combos/) | COMBO-01~05 — chain-collapse cards for Mariology, infallibility, soteriology, purgatory/indulgences, and the same-sex blessing | ✅ Latest |
| Zero-Day Scan Candidates | [`../06_ZERO_DAY/scan_targets.md`](../06_ZERO_DAY/scan_targets.md) | Priority search targets for the future (e.g., Fiducia Supplicans) | 🔄 In progress |

> ⚠️ **Detector Limitations Notice (Trust Tiers)**:
> ① Embedding similarity cannot fully distinguish 'topical proximity' from 'logical contradiction,' so all
> 2,154 items in `auto_conflict_results.csv` are **"first-pass candidates requiring theological re-review by a human/LLM."**
> ② The 626 items in `cvcap_combo_results.csv` are **keyword-filter hit counts**, not a count of confirmed contradictions.
> ③ For final confirmed judgments, trust **only individually verified cards**, such as the 16 major contradictions in `REPORT_Catholic_Magisterium_Internal_Collisions_Comprehensive_Audit.md`,
> `05_COLLISION_CARDS/confirmed/`, and `combos/`.
> ④ In the early char n-gram era, 57% of 49 automated candidates turned out to be false positives (confirmed by source-text comparison), and
> in accordance with that lesson, 8 duplicate cards pointing to the same document were removed from the database on 2026-07-07 (80→71 cards; one additional phantom card for the schema.md template was also removed).

---

## ⚔️ Linked Reports from the Scripture Court (BVCAP — a Separate Engine)

> CVCAP 3.0 verifies **only** Catholicism's internal documents. Verification of the same doctrines against the **original text of Scripture** is
> handled by `../../the-scripture-audit/` (BVCAP), and the reports below are the **targets for final content merging**.
> When both sides confirm collapse, a 🔴 CHECKMATE is declared in the merged report (→ see the integrated interface `CVCAP_GHQ.md`).

> Location: `../../the-scripture-audit/05_REPORT/catholic/`

| # | Filename | Topic | Core Strike Point | Status |
|:---:|:---|:---|:---|:---:|
| 1 | [REPORT_Why_Catholics_Cannot_Confess_Jesus_as_Savior.md](../../the-scripture-audit/05_REPORT/catholic/REPORT_Why_Catholics_Cannot_Confess_Jesus_as_Savior.md) | The core question of soteriology | The "yes/no" trap — Catholic soteriology collapses whichever answer is chosen | ✅ Complete |
| 2 | [REPORT_Why_Catholics_Cannot_Confess_Jesus_as_Savior_NotebookLM.md](../../the-scripture-audit/05_REPORT/catholic/REPORT_Why_Catholics_Cannot_Confess_Jesus_as_Savior_NotebookLM.md) | Soteriology (for video) | Video-script-optimized version of the document above | ✅ Video-ready |
| 3 | [REPORT_Catholic_3_Major_Escape_Routes_Blockaded_SolaScriptura.md](../../the-scripture-audit/05_REPORT/catholic/REPORT_Catholic_3_Major_Escape_Routes_Blockaded_SolaScriptura.md) | Sola Scriptura | Complete blocking of the three great Catholic escape routes: Scripture+Tradition dual authority / ex cathedra / preemptive salvation | ✅ Complete |
| 4 | [REPORT_PapalPrimacy_PeterRock_Audit.md](../../the-scripture-audit/05_REPORT/catholic/REPORT_PapalPrimacy_PeterRock_Audit.md) | Papal primacy | Matthew 16:18 — is "the rock" Peter? Distinguishing the original Greek Petros vs. Petra | ✅ Complete |
| 5 | [REPORT_Mary_Immaculate_Assumption_Audit.md](../../the-scripture-audit/05_REPORT/catholic/REPORT_Mary_Immaculate_Assumption_Audit.md) | Marian dogma | The decisive blow of Luke 2:22's purification rite / complete absence of scriptural basis | ✅ Complete |
| 6 | [REPORT_ApostolicSuccession_Tradition_Audit.md](../../the-scripture-audit/05_REPORT/catholic/REPORT_ApostolicSuccession_Tradition_Audit.md) | Apostolic succession | Proof of historical rupture / collapse of the timeline for Peter as Bishop of Rome | ✅ Complete |
| 7 | [REPORT_Catholic_IntercessionOfSaints_Audit.md](../../the-scripture-audit/05_REPORT/catholic/REPORT_Catholic_IntercessionOfSaints_Audit.md) | Intercession of the saints | 1 Timothy 2:5 "one mediator" — the structural impossibility of the intercession of saints | ✅ Complete |
| 8 | [REPORT_Infant_Baptism_Dilemma_7_Sacraments_Collapse.md](../../the-scripture-audit/05_REPORT/catholic/REPORT_Infant_Baptism_Dilemma_7_Sacraments_Collapse.md) | Infant baptism / the Seven Sacraments | Inducing a chain collapse of the Seven Sacraments through the infant-baptism dilemma | ✅ Core weapon |
| 9 | [[F+E+G+N+P+I+T+S]_Peter_Calvary_Martyrdom.md](../../the-scripture-audit/05_REPORT/catholic/[F+E+G+N+P+I+T+S]_Peter_Calvary_Martyrdom.md) | Peter's site of martyrdom | Historical forensics — verifying the theory of Peter's martyrdom in Rome | ✅ Complete |
| 10 | [REPORT_1_John_Comma.md](../../the-scripture-audit/05_REPORT/catholic/REPORT_1_John_Comma.md) | The Johannine Comma | Suspected Vulgate manuscript tampering — textual-critical forensics of the Trinity passage | ✅ Complete |
| 11 | [REPORT_WINE_Wine_Liquor_Wrath_Original_Language_Forensics.md](../../the-scripture-audit/05_REPORT/catholic/REPORT_WINE_Wine_Liquor_Wrath_Original_Language_Forensics.md) | Communion wine | Transubstantiation vs. original-language scriptural forensics | ✅ Complete |
| 12 | [REPORT_CatholicApocrypha_ScriptAnalysis.md](../../the-scripture-audit/05_REPORT/catholic/REPORT_CatholicApocrypha_ScriptAnalysis.md) | The Apocrypha | Dismantling the claim of canonicity for the Apocrypha | ✅ Complete |

> Catholic-specific scriptural weapon cards: [`../03_QUIVER/CATHOLIC_TARGETED_WEAPONS.md`](../03_QUIVER/CATHOLIC_TARGETED_WEAPONS.md) (under the jurisdiction of the Scripture Court/BVCAP — reserved for the merge stage)

---

## 🗄️ Live-Combat Record Archive (CVCAP 1.0 Era, 2026-07-05) — For Historical Reference

> Records of live comment-section debates from **before** the automation pipeline was introduced. Still valid as reference material for real-world rhetoric and argumentation patterns.

| # | Filename | Combat Type | Outcome | Lesson |
|:---:|:---|:---|:---:|:---|
| 1 | [Catholic_Comments.md](../../the-scripture-audit/05_REPORT/catholic/Catholic_Comments.md) | Live comment-section combat | Record | For analyzing real-world patterns |
| 2 | [catholic_round_2.md](../../the-scripture-audit/05_REPORT/catholic/catholic_round_2.md) | Transubstantiation / patristic debate | ⚠️ Took a hit | John 6:63 was not used — later stockpiled as BVCAP weapon card A |
| 3 | [Catholic_Court.md](../../the-scripture-audit/05_REPORT/catholic/Catholic_Court.md) | Mock trial | Analysis | For reference on argument structure |
| 4 | [Catholic_Apologetics.md](../../the-scripture-audit/05_REPORT/catholic/Catholic_Apologetics.md) | Apologetics record | Analysis | For understanding defense patterns |

### 🎯 Core Standing Weapons (Verified from Combat Records)
- **The condemnation of Honorius I** (a Document Court nuclear weapon) → `03_QUIVER/QVCAP_WEAPONS.md`, Collapse Card 1
- **The reverse cherry-picking of Augustine** (patristic court) → `03_QUIVER/QVCAP_WEAPONS.md`, Collapse Card 6
- **The identical Greek word sarx in John 6:63** (Scripture Court — under BVCAP jurisdiction) → `CATHOLIC_TARGETED_WEAPONS.md`, Card A

---

## 📢 Public Content Strategy

| Content | Based on Document | Format | Purpose |
|:---|:---|:---:|:---|
| **"Why Catholicism Cannot Confess Jesus as Savior"** | BVCAP REPORT_Why_Catholics_Cannot_Confess_Jesus_as_Savior_NotebookLM.md | Video | Grab viewer attention with a core question |
| **"The Infant Baptism Dilemma and the Collapse of the Seven Sacraments"** | BVCAP REPORT_Infant_Baptism_Dilemma_7_Sacraments_Collapse.md | Video | Shake the entire structure of Catholic sacramental theology |
| **"Why the Pope Cannot Be Infallible"** | CVCAP catholic_error_report Parts 7, 10 | Document/Video | Declare the internal collapse of infallibility |
| **"The 16 Great Contradictions Series"** | CVCAP catholic_error_report Parts 1-16 | Series | Fully disclose the internal documents' self-contradictions |

---

*Generated by CVCAP 3.0 — Document Court Record of Findings*
*First written: 2026-07-05 | Last revised: 2026-07-21 (full review complete + integrity self-check introduced)*
