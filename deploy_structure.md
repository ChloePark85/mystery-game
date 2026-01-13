# 배포용 파일 구조

## 필수 파일들

```
mystery-game/
├── index.html                           # 메인 게임 (enhanced_game_vn_cyoa_full.html을 복사)
├── README.md                           # 게임 설명
├── game/
│   └── images/
│       └── scenes/
│           ├── scene_01.png            # 공통 장면들
│           ├── scene_02.png
│           ├── scene_03.png
│           ├── scene_04.png
│           ├── detective_01.png        # Detective 경로 (15개)
│           ├── detective_02.png
│           │   ... (detective_15.png까지)
│           ├── conspiracy_01.png       # Conspiracy 경로 (15개)
│           ├── conspiracy_02.png
│           │   ... (conspiracy_15.png까지)
│           ├── drama_01.png           # Drama 경로 (15개)
│           ├── drama_02.png
│           │   ... (drama_15.png까지)
│           ├── choice_detective.png    # 선택지 이미지들
│           ├── choice_conspiracy.png
│           ├── choice_drama.png
│           ├── branch_split.png
│           ├── evidence_analysis.png
│           └── final_revelation.png
└── docs/                              # 개발 문서들 (선택사항)
    ├── story_redesign_plan.md
    ├── cyoa_image_prompts.md
    └── choice_system_design.md
```

## 배포 전 체크리스트

✅ enhanced_game_vn_cyoa_full.html → index.html로 복사
✅ 모든 이미지 파일 생성 및 배치 (총 51개)
✅ 이미지 경로 확인 (game/images/scenes/)
✅ 브라우저에서 로컬 테스트
✅ 모바일 반응형 테스트
✅ README.md 작성

## 빠른 배포 명령어

### GitHub Pages
```bash
cp enhanced_game_vn_cyoa_full.html index.html
git add .
git commit -m "게임 배포 준비"
git push origin main
```

### Netlify
1. 폴더를 zip으로 압축
2. netlify.com에서 드래그 앤 드롭

### 로컬 테스트
```bash
python serve.py
```