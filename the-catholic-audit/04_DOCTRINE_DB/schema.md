---
id: "catholic-doctrine_db-031"
title_ko: "교리 카드 스키마 (Doctrine Card Schema)"
title_en: "Doctrine Card Schema"
file_ko: "schema.md"
file_en: "schema.md"
category: "doctrine_db"
status: "translated"
source: "KO"
updated: "2026-08-27"
---
# Doctrine Card Schema

> Every doctrine card follows this format. Each card is an independent .md file.

---

## Field Definitions

| Field | Type | Required | Description |
|:---|:---|:---:|:---|
| `id` | string | ✅ | Unique identifier (e.g., CCC-1257, TRENT-S06-C09) |
| `title` | string | ✅ | Doctrine title |
| `source` | string | ✅ | Source document name |
| `section` | string | ✅ | Paragraph/Canon number |
| `authority` | enum | ✅ | De Fide / Sententia Certa / Sententia Communis / Opinio / Pastoral |
| `anathema` | bool | ✅ | Whether an anathema clause is present |
| `year` | int | ✅ | Year of enactment/promulgation |
| `text_ko` | string | ✅ | Core content (Korean summary) |
| `text_la` | string | | Latin original text (if available) |
| `tags` | list | ✅ | Subject tags |
| `claims` | list | ✅ | Propositions this doctrine asserts |
| `negates` | list | ✅ | Propositions this doctrine denies |
| `collisions` | list | | IDs of other doctrine cards that collide with this one |

## Tag System

### Subject Tags
soteriology, sacramental_theology, ecclesiology, papal_theology, mariology, eschatology,
baptism, eucharist, confession, confirmation, marriage, holy_orders, anointing_of_the_sick,
grace, merit, justification, sanctification, purgatory, indulgences, limbo,
infallibility, primacy, magisterium, councils, tradition, revelation

### Logic Tags
necessary, prohibited, permitted, conditional, absolute, ordinary, pastoral

### Doctrinal-Rank Tags
de_fide, sententia_certa, sententia_communis, opinio, pastoral

## Doctrine Card Template

```markdown
# [ID] — [Title]

| Field | Content |
|:---|:---|
| **ID** | |
| **Source** | |
| **Paragraph** | |
| **Doctrinal Rank** | |
| **Anathema** | |
| **Year** | |

## Original Text (Summary)
> 

## Tags
``, ``

## Claims
1. 
2. 

## Negates
1. 
2. 

## Related Collisions
- → [COL-000]
```
