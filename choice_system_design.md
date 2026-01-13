# Choose Your Own Adventure - 선택지 시스템 설계

## 게임 플로우 구조

### 공통 도입부 (4개 장면)
- scene_01: 긴급 호출
- scene_02: 현장 도착
- scene_03: 사건 브리핑
- scene_04: 연구실 입장

### 첫 번째 분기점 (scene_05)
**분기 선택지:**

**선택 A**: "과학적 분석에 집중한다"
→ Detective Path로 이동

**선택 B**: "숨겨진 배경을 조사한다"
→ Conspiracy Path로 이동

**선택 C**: "관련자들의 심리를 파악한다"
→ Human Drama Path로 이동

---

## 🕵️ Detective Path 선택지 시스템

### Detective 중간 분기 (detective_06)
**선택 D1**: "물리적 증거를 더 수집한다"
→ detective_07~09 (증거 수집 집중)

**선택 D2**: "심리적 압박으로 자백을 받는다"
→ detective_10~12 (심문 집중)

### Detective 최종 분기 (detective_13)
**선택 D3**: "법정에서 완벽한 증거로 승리한다"
→ detective_14~15 (법정 승리 엔딩)

---

## 🎭 Conspiracy Path 선택지 시스템

### Conspiracy 중간 분기 (conspiracy_06)
**선택 C1**: "정부 연결고리를 추적한다"
→ conspiracy_07~09 (정부 음모 추적)

**선택 C2**: "기업 네트워크를 조사한다"
→ conspiracy_10~12 (기업 부패 추적)

### Conspiracy 최종 분기 (conspiracy_13)
**선택 C3**: "언론에 모든 것을 폭로한다"
→ conspiracy_14~15 (영웅적 폭로 엔딩)

---

## 💔 Human Drama Path 선택지 시스템

### Drama 중간 분기 (drama_06)
**선택 H1**: "유지민의 과거를 깊이 파본다"
→ drama_07~09 (감정적 탐구)

**선택 H2**: "한기태와의 관계를 중재한다"
→ drama_10~12 (관계 회복 집중)

### Drama 최종 분기 (drama_13)
**선택 H3**: "치유와 용서를 선택한다"
→ drama_14~15 (인간적 구원 엔딩)

---

## JavaScript 분기 로직

```javascript
// 게임 상태 관리
let currentPath = 'common'; // common, detective, conspiracy, drama
let pathProgress = 0;

// 분기 선택 처리
function handleChoice(choiceType, choiceValue) {
    switch(choiceType) {
        case 'initial_branch':
            if (choiceValue === 'detective') {
                currentPath = 'detective';
                showScene('detective_01');
            } else if (choiceValue === 'conspiracy') {
                currentPath = 'conspiracy';
                showScene('conspiracy_01');
            } else if (choiceValue === 'drama') {
                currentPath = 'drama';
                showScene('drama_01');
            }
            break;

        case 'detective_branch':
            // Detective 중간 분기 로직
            break;

        case 'conspiracy_branch':
            // Conspiracy 중간 분기 로직
            break;

        case 'drama_branch':
            // Drama 중간 분기 로직
            break;
    }
}

// 씬별 선택지 정의
const choicePoints = {
    'scene_05': {
        type: 'initial_branch',
        choices: [
            { text: "🔬 과학적 분석에 집중한다", value: 'detective' },
            { text: "🕵️ 숨겨진 배경을 조사한다", value: 'conspiracy' },
            { text: "💭 관련자들의 심리를 파악한다", value: 'drama' }
        ]
    },
    'detective_06': {
        type: 'detective_branch',
        choices: [
            { text: "증거를 더 수집한다", value: 'evidence' },
            { text: "심리적 압박을 가한다", value: 'interrogation' }
        ]
    }
    // ... 추가 분기점들
};
```

---

## 엔딩 타이틀

### 🕵️ Detective Endings
- **"논리의 승리"** - 과학적 방법으로 완벽한 해결
- **"정의의 실현"** - 법정에서의 최종 승리

### 🎭 Conspiracy Endings
- **"진실의 폭로"** - 거대한 음모를 세상에 알림
- **"영웅의 대가"** - 진실을 밝혔지만 위험에 처함

### 💔 Drama Endings
- **"마음의 치유"** - 모든 인물이 평화를 찾음
- **"용서의 힘"** - 법보다 인간애가 승리

---

## 리플레이 시스템

각 엔딩 후 다른 경로 선택 옵션 제공:
- "다른 접근 방식으로 다시 시작"
- "다른 엔딩 보기"
- "처음부터 다시"