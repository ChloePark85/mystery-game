#!/bin/bash

# 0의 집행 - GitHub Pages 배포 스크립트

echo "🎮 0의 집행 - GitHub Pages 배포 준비"
echo "=================================="

# 1. index.html 생성 (메인 게임 파일)
echo "📁 index.html 생성 중..."
cp enhanced_game_vn_cyoa_full.html index.html
echo "✅ index.html 생성 완료"

# 2. Git 초기화 (이미 있으면 건너뛰기)
if [ ! -d ".git" ]; then
    echo "🔧 Git 초기화 중..."
    git init
    git branch -M main
    echo "✅ Git 초기화 완료"
fi

# 3. 파일 추가 및 커밋
echo "📦 파일 추가 및 커밋 중..."
git add .
git commit -m "0의 집행 - Choose Your Own Adventure 게임 배포"

echo "🚀 배포 준비 완료!"
echo ""
echo "📋 다음 단계:"
echo "1. GitHub에서 새 저장소 생성 (예: mystery-game)"
echo "2. 아래 명령어 실행:"
echo "   git remote add origin https://github.com/YOUR_USERNAME/mystery-game.git"
echo "   git push -u origin main"
echo "3. GitHub → Settings → Pages → Source: main branch"
echo "4. 5-10분 후 https://YOUR_USERNAME.github.io/mystery-game/ 접속"
echo ""
echo "💡 팁: 이미지 51개를 game/images/scenes/ 폴더에 넣는 것을 잊지 마세요!"