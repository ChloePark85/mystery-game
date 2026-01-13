#!/usr/bin/env python3
"""
안전한 이미지 생성 스크립트
API 키는 환경변수나 .env 파일에서 읽어옵니다.
"""

import os
import requests
import json
from typing import Optional

def get_api_key() -> Optional[str]:
    """환경변수나 .env 파일에서 API 키를 안전하게 가져옵니다."""

    # 1. 환경변수에서 확인
    api_key = os.getenv('GOOGLE_API_KEY')
    if api_key:
        return api_key

    # 2. .env 파일에서 확인
    try:
        with open('.env', 'r') as f:
            for line in f:
                if line.startswith('GOOGLE_API_KEY='):
                    return line.split('=', 1)[1].strip()
    except FileNotFoundError:
        pass

    # 3. 직접 입력 요청
    print("API 키를 찾을 수 없습니다.")
    print("다음 중 하나를 선택하세요:")
    print("1. 환경변수 설정: export GOOGLE_API_KEY=your_key")
    print("2. .env 파일 생성: echo 'GOOGLE_API_KEY=your_key' > .env")
    print("3. 지금 직접 입력")

    choice = input("선택 (1/2/3): ")
    if choice == '3':
        api_key = input("API 키 입력: ").strip()

        # .env 파일에 저장할지 물어보기
        save = input(".env 파일에 저장하시겠습니까? (y/n): ").lower()
        if save == 'y':
            with open('.env', 'w') as f:
                f.write(f"GOOGLE_API_KEY={api_key}\n")
            print("✅ .env 파일에 저장되었습니다.")

        return api_key

    return None

def test_api_connection(api_key: str) -> bool:
    """API 연결을 테스트합니다."""

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent?key={api_key}"

    headers = {'Content-Type': 'application/json'}

    payload = {
        "contents": [{
            "parts": [{
                "text": "Hello, just testing the API connection. Please respond with 'OK'."
            }]
        }],
        "generationConfig": {
            "temperature": 0.1,
            "maxOutputTokens": 10,
        }
    }

    try:
        print("🧪 API 연결 테스트 중...")
        response = requests.post(url, headers=headers, json=payload, timeout=30)

        if response.status_code == 200:
            print("✅ API 연결 성공!")
            return True
        else:
            print(f"❌ API 연결 실패: {response.status_code}")
            print(f"응답: {response.text}")
            return False

    except Exception as e:
        print(f"❌ 연결 오류: {e}")
        return False

def generate_image_prompts():
    """이미지 프롬프트를 생성합니다."""

    api_key = get_api_key()
    if not api_key:
        print("❌ API 키를 가져올 수 없습니다.")
        return

    if not test_api_connection(api_key):
        print("❌ API 연결에 실패했습니다.")
        return

    print("\n🎨 이미지 프롬프트 생성을 시작합니다...")
    print("cyoa_image_prompts.md 파일에 이미 51개의 상세한 프롬프트가 준비되어 있습니다.")
    print("해당 프롬프트들을 사용하여 직접 이미지를 생성해주세요.")

if __name__ == "__main__":
    print("🎮 0의 집행 - 이미지 생성 도구")
    print("=" * 50)
    generate_image_prompts()