# Sbbagi / 스빡이 Hermes Profile

SPEC(성균관대학교 창업동아리, SKKU Prep Entrepreneurs' Club) 운영 보조용 Hermes Agent 프로필을 다른 컴퓨터에서도 재현하기 위한 저장소입니다.

이 저장소는 **스빡이의 재사용 가능한 설정/스크립트/메모 템플릿만** 담습니다. OAuth 토큰, API 키, Discord 토큰, Gmail 토큰, 로그, 세션 DB, 메일 첨부파일, 개인정보 문서는 절대 커밋하지 않습니다.

## 포함된 것

- `profiles/sbbagi/config.yaml` — 스빡이 Hermes 프로필용 기본 설정 템플릿
- `profiles/sbbagi/SOUL.md` — 스빡이 기본 페르소나/응답 스타일
- `profiles/sbbagi/memories/USER.md` — 스빡이/SPEC 역할과 사용자 선호 메모
- `profiles/sbbagi/memories/MEMORY.md` — 운영상 재사용 가능한 주의사항(credential 제외)
- `profiles/sbbagi/skills/` — 현재 sbbagi 프로필의 활성 Hermes skills 사본(캐시/아카이브 제외)
- `profiles/sbbagi/scripts/gmail_spec_watchdog.py` — Gmail 새 메일 Discord 알림용 script-only watchdog
- `cron/gmail_spec_watchdog.template.json` — cron job 설정 참고 템플릿
- `scripts/install_profile.sh` — 새 컴퓨터에 프로필/래퍼 설치
- `artifacts/local-bin-spbaki.sh` — 이전에 보존된 `spbaki` wrapper 원본
- `forensics/preservation-report.md` — 기존 보존 리포트

## 새 컴퓨터에 설치

### 1. Hermes Agent 설치

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

설치 후 터미널을 새로 열거나 PATH를 갱신하세요.

### 2. 이 저장소 클론

```bash
git clone https://github.com/skku-spec/Sbbagi.git
cd Sbbagi
```

### 3. 스빡이 프로필 설치

기본 프로필명은 현재 운영 중인 `sbbagi`입니다.

```bash
bash scripts/install_profile.sh
```

다른 프로필명으로 설치하려면:

```bash
bash scripts/install_profile.sh sbbagi
```

설치되면 `~/.local/bin/sbbagi` 래퍼가 생성됩니다.

```bash
sbbagi
# 또는
hermes -p sbbagi
```

## 필수 후속 설정

이 저장소에는 보안상 credential이 없습니다. 새 컴퓨터마다 아래를 다시 해야 합니다.

### 모델/OAuth 설정

```bash
hermes -p sbbagi setup
# 또는
hermes -p sbbagi model
```

현재 템플릿은 `openai-codex / gpt-5.5`를 기본값으로 둡니다. 실제 사용 가능한 provider/model은 새 환경의 인증 상태에 맞게 바꾸세요.

### Discord Gateway 설정

Discord에서 스빡이를 쓰려면 새 컴퓨터에서 gateway를 설정해야 합니다.

```bash
hermes -p sbbagi gateway setup
hermes -p sbbagi gateway run
```

상시 실행하려면 Hermes 공식 docs의 gateway service 설치 방식을 따르세요.

### Gmail OAuth 설정

Gmail watchdog은 다음 파일이 필요합니다.

```text
~/.hermes/profiles/sbbagi/google_token.json
```

Google OAuth client secret/token은 개인 credential이므로 이 저장소에 없습니다. Hermes Google Workspace skill 또는 별도 OAuth flow로 새 환경에서 다시 발급하세요.

필요 패키지:

```bash
python -m pip install --user google-auth google-api-python-client google-auth-oauthlib
```

watchdog 단독 테스트:

```bash
HERMES_PROFILE_HOME="$HOME/.hermes/profiles/sbbagi" \
python "$HOME/.hermes/profiles/sbbagi/scripts/gmail_spec_watchdog.py"
```

첫 실행은 기존 메일을 seen 처리하고 조용히 종료합니다. 이후 새 메일이 오면 알림 텍스트를 출력합니다.

## Gmail Watchdog Cron 등록

Hermes cron은 스크립트 파일명이 profile scripts 디렉터리 기준 상대경로여야 합니다.

```bash
hermes -p sbbagi cron create 'every 5m' \
  --script gmail_spec_watchdog.py \
  --no-agent \
  --deliver origin
```

동작 방식:

- 5분마다 Gmail API만 호출합니다.
- LLM을 호출하지 않는 `no_agent=true` 방식이라 토큰을 쓰지 않습니다.
- 새 메일이 없으면 아무 메시지도 보내지 않습니다.
- 발신자 주소를 고정하지 않고 모든 incoming sender를 감지합니다.
- `sent`, `drafts`, `trash`, `spam`은 제외합니다.
- 첨부 원문은 Discord에 올리지 않고 파일명만 표시합니다.
- 주민등록번호/긴 숫자 등은 본문 미리보기에서 자동 마스킹합니다.

필터를 바꾸고 싶으면 환경변수로 Gmail query를 지정할 수 있습니다.

```bash
export SBBAGI_GMAIL_QUERY='in:inbox newer_than:7d -in:spam -in:trash'
```

## 절대 커밋하면 안 되는 것

`.gitignore`에도 막아두었지만, 아래는 수동으로도 절대 올리지 마세요.

- `.env`
- `auth.json`
- `google_token.json`
- `google_client_secret.json`
- Discord bot token / Google OAuth secret / API keys
- `state.db*`, `sessions/`, `logs/`, `cron/output/`
- Gmail 원문, 첨부파일, 신분증, 통장사본, 주민등록번호, 계좌번호 등 개인정보 문서

## 현재 운영 메모

- Assistant 이름/역할: “스빡이”, SPEC 운영 보조
- SPEC = SKKU Prep Entrepreneurs' Club, 성균관대 창업동아리
- RISE 업무 담당자 이름은 오혜진이 맞고 “오해진”이 아님
- Gmail에서 이미 보낸 메일을 삭제해도 상대방 받은편지함에서 회수되는 것은 아님

## 기존 보존 리포트

이 저장소는 원래 macOS 로컬에 남아 있던 `spbaki` wrapper만 보존하는 목적이었습니다. 현재는 실제 운영 중인 Hermes profile 템플릿과 Gmail watchdog 스크립트를 추가했습니다. 기존 보존 내용은 `forensics/preservation-report.md`를 참고하세요.
