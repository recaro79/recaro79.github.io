# 홈페이지 운영 지침 (Claude 작업용)

세무법인 인성 남기원 세무사 홈페이지(recaro79.github.io) 글 게시 작업 지침입니다.
예약 작업으로 새로 시작된 세션은 **이 파일과 `_ops/log.md`를 먼저 읽고** 작업합니다.

## 0. 절대 원칙
- 세법 내용은 절대 틀리면 안 됩니다. 모든 조문은 **법제처 MCP(search_law → get_law_text)** 로 현행 원문과 부칙(적용 시기)을 대조합니다.
- 예규·판례·심판례는 원문으로 확인된 것만 싣습니다. 확인이 안 되면 그 부분을 통째로 뺍니다. 절대 지어내지 않습니다.
- 세액 예시는 반드시 코드(python)로 계산·검산합니다.
- 정부안·국회 심사 단계 내용은 "확정 아님"을 분명히 표시합니다. 뉴스는 실제 기사·보도자료 링크를 출처로 답니다.
- 확인이 안 되는 주제는 건너뛰고 다음 주제로 넘어갑니다.
- 소속은 "세무법인 인성"으로만 씁니다. 직함은 "지점대표세무사". 말투는 공손하고 친근하게, 고객이 알아보기 쉽게 씁니다.
- 연락처: 휴대폰 010-7741-4822 · 이메일 recaro798@gmail.com · 팩스 051-861-9995 · 카카오톡 https://pf.kakao.com/_wdZNX/chat · 주소 부산광역시 연제구 월드컵대로 153 연희빌딩 3층 · 상담 평일 09:00~18:00

## 1. 수정 규칙 (일괄 수정)
무언가를 고치면 관련된 모든 파일을 같이 고칩니다.
- 홈페이지: `index.html`, `column/*.html`, `column/index.html`, `card/index.html`, `contact.vcf`
- 세목별 안내문: 저장소 `recaro79/guide` (yangdo·jeungyeo·sangsok 등 7개)
- 명함: `card/index.html`, `contact.vcf`, QR 명함 이미지 `card/qr-card.png` — 연락처·직함·업무 문구가 바뀌면 `_ops/qrcard/card.html` 문구를 고치고 `python3 _ops/qrcard/build.py` 실행
- CSS를 바꾸면 모든 페이지의 `/assets/style.css?v=` 값을 새로 올립니다.

## 2. 칼럼 + 카드뉴스 게시 절차
1. `_ops/log.md`에서 다음 번호(NN)와 주제를 확인합니다. 상속·증여·양도 위주, 2~3편마다 종합소득세 또는 법인세 1편.
2. 법제처로 조문·부칙 확인 → 사례 세액을 python으로 계산.
3. 칼럼 HTML: 최신 칼럼(`column/` 중 번호가 가장 큰 파일)을 복사해 같은 구조로 작성
   (핵심 3줄 요약 → 카드뉴스 → 질문 인용 → 가상 사례 → 본문 표 → 세액 비교표 → 체크리스트 → 준비 자료 → 상담 안내 → 태그).
   파일명 `column/NN-영문-슬러그.html`, title/description/og/canonical 모두 교체.
4. 카드뉴스 7장: `_ops/cardnews/template.html`을 복사해 문구만 바꾸고
   `python3 _ops/cardnews/render.py <html절대경로> <출력접두어>` → PNG 7장 → JPG(quality 86)로 `assets/cardnews/NN/1~7.jpg`.
   썸네일 `assets/img/colNN-thumb.jpg`(720×720, 1번 카드 상단 정사각 크롭).
   렌더 전에 template 폴더의 profile.jpg, qr.png가 HTML과 같은 폴더에 있어야 합니다.
5. `index.html`과 `column/index.html`의 `<!-- COLUMNS:START -->` 바로 아래에 카드 추가.
6. `sitemap.xml`에 URL 추가.
7. 모바일(390px) 화면에서 가로 넘침이 없는지 Playwright로 확인.
8. 커밋·푸시 후 `_ops/log.md`에 기록.

## 3. 세법 개정 소식 갱신 (월요일 작업)
- `index.html`의 `<!-- NEWS:START -->`~`<!-- NEWS:END -->`: 최신 소식을 맨 위에 추가, 7~8개만 유지.
  태그: 시행(class nw g / t-g), 국회 심사(nw a / t-a), 정부안(nw b / t-b).
- `<!-- TIMELINE:START -->`~`END`: 2026년 세법개정안 진행 단계와 "최종 확인" 날짜 갱신. 본회의 의결·공포되면 단계 표시를 바꾸고, 공포된 법률은 법제처에서 확인 후 "시행/시행예정"으로 표기.
- `<!-- SCHEDULE:START -->`~`END`: 지난 일정은 자동으로 숨겨지지만, 앞으로 3~4개월 일정이 늘 5개 이상 있도록 추가. 요일은 python으로 계산, 기한이 토·일·공휴일이면 다음 날(국세기본법 제5조).
- 섹션 머리의 "● YYYY.MM.DD. 확인" 날짜 갱신.
- 개정세법 칼럼 1편(+카드뉴스) 작성: 가장 영향이 큰 개정 사항을 고객 눈높이로 설명.

## 4. 커밋
- 작성자: recaro79 <recaro798@gmail.com>
- 저장소가 없으면 add_repo로 recaro79/recaro79.github.io (push 권한)를 붙이고 clone 합니다.
