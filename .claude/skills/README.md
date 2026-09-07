# 등록된 스킬

## HyperFrames (발표자료 기본 도구)

`hyperframes` 계열 스킬은 HTML/CSS 로 슬라이드와 영상을 만드는 오픈소스 프레임워크입니다.
**이 저장소에서 발표자료(슬라이드, 덱, 프레젠테이션)를 만들 때는 이 스킬을 우선으로 씁니다.**

| 스킬 | 언제 쓰나 |
|---|---|
| `hyperframes` | **입구.** 영상·애니메이션·발표자료 요청이면 여기부터 읽고 라우팅 |
| `slideshow` | 발표자료·피치덱·인터랙티브 덱 (실행 가능한 덱이 결과물) |
| `hyperframes-core` | 컴포지션 작성 규약 (clip, track, `data-*`, 결정성) |
| `hyperframes-cli` | `scaffold` / `check` / `present` / `render` 등 CLI |
| `hyperframes-keyframes` | 키프레임·타임라인 |
| `hyperframes-animation` | 애니메이션 규칙·블루프린트·전환 |

### 출처와 갱신

- 출처: <https://github.com/heygen-com/hyperframes> (`skills/` 디렉터리)
- 벤더링한 커밋: `0d5d3f3eb3aecd9fd64954d2767d3d64e97e58fc`
- 라이선스: Apache-2.0 — 전문은 `LICENSE-hyperframes`
- 갱신 방법: 위 저장소를 clone 한 뒤 `skills/<이름>` 을 이 디렉터리로 다시 복사하고, 이 문서의 커밋 해시를 갱신합니다. (CLI 를 쓸 수 있으면 `npx hyperframes skills update <이름>` 도 같은 일을 합니다.)

여기에는 발표자료에 필요한 6개만 담았습니다. 캡션·음악·PR 영상 등 다른 워크플로가 필요하면 위 저장소에서 해당 스킬 폴더를 같은 방식으로 추가하면 됩니다.
