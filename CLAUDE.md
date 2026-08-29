# CLAUDE.md

이 파일은 Claude Code가 이 디렉토리에서 작업할 때 항상 따라야 하는 규칙을 담습니다.

## Backup 폴더 정책 (생태계 공통 규칙)

- `backup/` 폴더 및 그 하위의 모든 파일/폴더는 **git으로 절대 커밋하지 않는다.**
  - `.gitignore`에 `**/backup/` 규칙이 있는지 먼저 확인하고 없으면 추가한다.
- `backup/` 하위 내용은 **어떤 공개 채널(웹사이트, 배포, Keep 등)에도 절대 노출하지 않는다.**
- 공개하고 싶은 문서는 애초에 `backup/`에 두지 않는다.
- 이 정책은 `D:\00.TheScriptureMaster` 생태계(00~06, 99) 전체에 공통 적용된다.

## 이 디렉토리 (01.TheScriptureAudit — EN)

- QVCAP 감사 엔진(영문판). `the-scripture-audit`, `the-catholic-audit`, `the-sermon-audit` 세 하위 유닛을 포함.
- 이 저장소는 `01.TheScriptureAudit_ko`(한글판)의 번역본입니다. **한글판이 원본(source of truth)**이며, 여기는 번역 이관 대상입니다.
- 검증 완료된 `REPORT` 폴더의 문서만 `02.TheScriptureSynagogue`로 이관됩니다. 이 저장소에서 `04.TheScriptureKeep`으로 직접 배포하지 않습니다.
