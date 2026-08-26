> [!IMPORTANT]
> ## 🧠 Automation Engine Spec (Automation Layer)
> **What this document does**: Doctrine DB automatic conflict detection · Logical filters · Combo engine · Conflict severity definition
> **Companion documents**: `CVCAP_GHQ.md` (HQ — Strategy/Verdict criteria) · `CVCAP_Pipeline.md` (Tactical manual — OODA execution procedure)
> **Relationship**: The HQ determines "what to strike and why," this automation engine "mechanically unearths strike candidates," and the tactical manual "verifies the candidates in court."

# 🧠 CVCAP 3.0 Methodology (The Ultimate Theological Logic Verification Algorithm)
## Catholic Vault & Conciliar Audit Pipeline — Automation Engine Spec

> **Version**: v3.0
> **Status**: Active
> **Target**: Catholic internal documents only (CCC · Councils · Papal declarations · Canon Law · CDF documents)
> **Scriptural Verification**: Not handled by this engine — `../the-scripture-audit/` (BVCAP) handles it separately, and the two reports are merged at the final output stage.

---

## 📜 Version History

| Version | Method | Limitation → Reason for Next Version |
|:---:|:---|:---|
| **1.0** | Manual verification | Speed limits, only handles known conflicts |
| **2.0** | Doctrine DB structure + A→Not-A auto-detect + Hermeneutical rupture, Modus Tollens, Reductio ad absurdum, Practical contradiction filters | Mostly surface conflicts — couldn't catch the 'mindset itself' of defense logic |
| **3.0** | Inherits all 2.0 + 4 Meta logic filters (Moving goalposts, Retorsion, False dichotomy, Argument from silence) + Combo engine + LLM secondary judge | (Current) |

---

## 1. Overview

CVCAP 1.0 was a 1-dimensional formal logic filter detecting only explicit text conflicts (A vs Not A).
CVCAP 2.0 caught surface absurdities through 'hermeneutical rupture, modus tollens, reductio ad absurdum, and practical contradictions'.
**CVCAP 3.0** goes a step further, absorbing advanced forensic logic weapons to completely shut down the **'deception and logical fallacy of the mindset itself'** used by the Catholic Magisterium to defend itself, acting as the Ironclad filter.

---

## 2. Automatic Conflict Discovery Pipeline (Zero-day Discovery Pipeline)

### Step 1: Proposition Extraction
Extract `claims[]` and `negates[]` from each doctrine card in `04_DOCTRINE_DB/`.

### Step 2: Cross-Reference
- Check if Card A's `claims[]` semantically matches Card B's `negates[]`.
- Execute: `scripts/conflict_detector.py` → `07_REPORT/auto_conflict_results.csv`

### Step 3: LLM Secondary Precision Judge (LLM-as-a-Judge)
- Embedding similarity cannot distinguish 'topic proximity' from 'logical contradiction', so LLM re-judges candidates in theological context.
- Execution: `scripts/llm_judge.py` or `cvcap-judge` agent.

### Step 4: Combo Detection (2~4 stages)
- Execute: `scripts/run_cvcap_combos.py` → `07_REPORT/cvcap_combo_results.csv`

### Step 5: Conflict Card Registration
Save verified conflicts in `05_COLLISION_CARDS/confirmed/` and `05_COLLISION_CARDS/combos/`.

---

## 3. Collision Severity Levels

| Level | Description | Destructive Power |
|:---:|:---|:---|
| **5** | De Fide vs De Fide — Absolute dogma contradiction | ☢️ Nuke |
| **4** | De Fide vs Council document | 💣 High Explosive |
| **3** | CCC vs CCC internal conflict | 🔥 Grenade |
| **2** | Canon Law vs CCC | 🔫 Bullet |
| **1** | Recent Papal document vs Past dogma tension | 🔍 Probe |

---

## 4. Core Logical Filters

### 🔴 Filter 1: Reductio ad absurdum
* Finds structures where assuming a doctrine is true leads to an absurd conclusion against other Catholic doctrines or historical facts.

### 🔵 Filter 2: Hermeneutical Rupture
* Exposes the historical deception of subtly accepting previously condemned heretical doctrines by just changing the 'words and nuances' today.

### 🟡 Filter 3: Modus Tollens
* Finds logical cracks where an "absolute necessity" collapses in the face of physical impossibility, negating its divine origin.

### 🟣 Filter 4: Action-vs-Doctrine Discrepancy
* Detects hypocrisy where the text defends a principle, but pastoral practice allows the 'essential evil' that the principle condemns.

### 🟠 Filter 5: Moving Goalposts [New 3.0]
* Exposes the trick of subtly shrinking or altering the definition or scope of a doctrine when it hits a logical/historical limit (e.g., Limbo, Papal Infallibility conditions).

### 🟢 Filter 6: Retorsion (Boomerang Argument) [New 3.0]
* Takes the logical premise used by the opponent to defend the Magisterium and applies it to their own system, causing self-contradiction.

### 🟤 Filter 7: False Dichotomy [New 3.0]
* Destroys the false frame of "either A (infallible Catholic) or B (chaos)" by presenting a third option.

### ⚫ Filter 8: First Mention & Argument from Silence [New 3.0]
* Contrasts the absolute silence in early documents (1st-3rd century Fathers) with the 'first appearance' of a doctrine to confirm it as a later invention rather than a 'development' (e.g., Assumption of Mary).

---

## 5. Priority Scan Targets (Zero-day Goldmines)
> → See `06_ZERO_DAY/scan_targets.md` (Fiducia Supplicans, Amoris Laetitia, Limbo, Fratelli Tutti, etc.)

---

## 6. Application Guidelines (For Subagents)
CVCAP 3.0 is a Meta logic analyzer beyond text collision. You must thoroughly dissect whether the defense logic falls into the post-apologetic tricks caught by filters 5-8. Ensure findings go through the OODA court procedure in `CVCAP_Pipeline.md`.
