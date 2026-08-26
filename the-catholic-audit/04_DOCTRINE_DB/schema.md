# Doctrine Card Schema

> All doctrine cards follow this format as independent .md files.

---

## Field Definitions

| Field | Type | Required | Description |
|:---|:---|:---:|:---|
| `id` | string | ✅ | Unique Identifier (e.g., CCC-1257, TRENT-S06-C09) |
| `title` | string | ✅ | Doctrine Title |
| `source` | string | ✅ | Source Document |
| `section` | string | ✅ | Article/Canon Number |
| `authority` | enum | ✅ | De Fide / Sententia Certa / Sententia Communis / Opinió / Pastoral |
| `anathema` | bool | ✅ | Is there an Anathema clause? |
| `year` | int | ✅ | Year promulgated |
| `text_ko` | string | ✅ | Core content summary |
| `text_la` | string | | Latin original text |
| `tags` | list | ✅ | Topic tags |
| `claims` | list | ✅ | Propositions this doctrine claims |
| `negates` | list | ✅ | Propositions this doctrine negates |
| `collisions` | list | | Colliding doctrine card IDs |

## Doctrine Card Template
```markdown
# [ID] — [Title]

| Field | Content |
|:---|:---|
| **ID** | |
| **Source** | |
| **Article** | |
| **Dogmatic Tier** | |
| **Anathema** | |
| **Year** | |

## Original Text (Summary)
> 

## Tags
` `, ` `

## Claims
1. 
2. 

## Negates
1. 
2. 

## Related Collisions
- → [COL-000]
