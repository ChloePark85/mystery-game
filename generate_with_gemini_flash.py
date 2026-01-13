#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
0의 집행 - Gemini 2.5 Flash Image를 사용한 이미지 생성
"""

import requests
import json
import time
import os
import base64
from pathlib import Path

# API 설정
API_KEY = "AIzaSyA1enVShSIIkEE_HHaxS-EAuc2hsNlGvgk"
MODEL_NAME = "gemini-2.5-flash-image"

# 이미지 저장 폴더 생성
os.makedirs("game/images/scenes", exist_ok=True)

# 첫 5개 장면만 테스트로 생성
test_scenes = [
    {
        "scene": "01_emergency_call",
        "title": "긴급 호출",
        "prompt": "Dark detective office at night in Seoul, Korean detective at desk with computer screens glowing, phone ringing, noir cyberpunk atmosphere, professional investigator workspace, moody blue lighting, digital forensics equipment, urban Korean setting, digital art style"
    },
    {
        "scene": "02_mansion_exterior",
        "title": "현장 도착",
        "prompt": "Ultra-modern smart home mansion exterior at night in Seoul, sleek glass and steel architecture, Korean cityscape background, police cars with flashing red and blue lights, high-tech building with LED accents, cyberpunk noir atmosphere, futuristic residential building, digital art style"
    },
    {
        "scene": "03_police_briefing",
        "title": "사건 브리핑",
        "prompt": "Police briefing scene outside Korean smart mansion, Korean police officers in uniform, detective in dark suit, crime scene yellow tape, professional consultation, Seoul urban night setting, serious law enforcement atmosphere, digital art style"
    },
    {
        "scene": "04_lab_entrance",
        "title": "연구실 입장",
        "prompt": "Underground laboratory entrance in Korea, sterile white walls, modern elevator doors opening, cold blue fluorescent lighting, high-tech research facility corridor, clean minimalist design, scientific atmosphere, cyberpunk aesthetic, digital art style"
    },
    {
        "scene": "05_lab_overview",
        "title": "연구실 전체 관찰",
        "prompt": "Pristine sterile research laboratory interior, perfectly organized scientific equipment, large industrial robotic arm in center, white walls and metallic surfaces, advanced scientific instruments, crime scene but clean, cold LED lighting, digital art style"
    }
]

def generate_image_with_gemini_flash(prompt, scene_name):
    """Gemini 2.5 Flash Image를 사용하여 이미지 생성"""

    # AI Studio 문서에 따른 올바른 엔드포인트
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent?key={API_KEY}"

    headers = {
        'Content-Type': 'application/json'
    }

    # 프롬프트 향상
    enhanced_prompt = f"Create a high-quality digital art image: {prompt}. Style: cyberpunk noir, professional illustration, detailed, atmospheric lighting, 16:9 aspect ratio, Korean setting, cinematic composition"

    payload = {
        "contents": [{
            "parts": [{
                "text": enhanced_prompt
            }]
        }],
        "generationConfig": {
            "temperature": 0.4,
            "topK": 32,
            "topP": 0.95,
            "maxOutputTokens": 8192,
        }
    }

    try:
        print(f"🎨 Generating: {scene_name}")
        print(f"📝 Prompt: {enhanced_prompt[:100]}...")

        response = requests.post(url, headers=headers, json=payload, timeout=60)

        print(f"📊 Status: {response.status_code}")

        if response.status_code == 200:
            result = response.json()

            # 응답 구조 확인
            print(f"🔍 Response keys: {list(result.keys())}")

            if 'candidates' in result and len(result['candidates']) > 0:
                candidate = result['candidates'][0]
                print(f"🔍 Candidate keys: {list(candidate.keys())}")

                # 이미지 데이터 찾기
                if 'content' in candidate:
                    content = candidate['content']
                    if 'parts' in content:
                        for part in content['parts']:
                            print(f"🔍 Part keys: {list(part.keys())}")

                            # 여러 가능한 이미지 데이터 위치 확인
                            if 'inlineData' in part:
                                image_data = part['inlineData']['data']
                                save_image(image_data, scene_name)
                                return True
                            elif 'text' in part and 'base64' in part['text']:
                                # 텍스트로 래핑된 base64 데이터
                                text = part['text']
                                if 'data:image' in text:
                                    base64_data = text.split('base64,')[1] if 'base64,' in text else text
                                    save_image(base64_data, scene_name)
                                    return True

                # 전체 응답 출력 (디버깅용)
                print(f"📄 Full response: {json.dumps(result, indent=2)[:500]}...")

            print(f"⚠️ No image data found in response for {scene_name}")
            return False

        else:
            print(f"❌ API Error: {response.status_code}")
            print(f"Response: {response.text}")
            return False

    except Exception as e:
        print(f"❌ Exception: {str(e)}")
        return False

def save_image(base64_data, scene_name):
    """Base64 이미지 데이터를 파일로 저장"""
    try:
        image_path = f"game/images/scenes/{scene_name}.png"
        with open(image_path, "wb") as f:
            f.write(base64.b64decode(base64_data))
        print(f"💾 Saved: {image_path}")
        return True
    except Exception as e:
        print(f"❌ Save error: {e}")
        return False

def test_model_availability():
    """모델 사용 가능성 테스트"""

    # 모델 정보 확인
    models_url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"

    try:
        response = requests.get(models_url, timeout=10)
        if response.status_code == 200:
            models = response.json()

            print("🔍 Available models:")
            for model in models.get('models', []):
                name = model.get('name', '')
                if 'flash-image' in name or 'imagen' in name:
                    print(f"  - {name}")

                    # 지원되는 메서드 확인
                    methods = model.get('supportedGenerationMethods', [])
                    print(f"    Methods: {methods}")

        else:
            print(f"❌ Models API error: {response.status_code}")

    except Exception as e:
        print(f"❌ Models check error: {e}")

def main():
    print("🎮 Gemini 2.5 Flash Image로 이미지 생성 시작")
    print("=" * 60)

    # 1. 모델 사용 가능성 확인
    test_model_availability()

    print(f"\n🎨 테스트: 첫 {len(test_scenes)}개 장면 생성")

    success_count = 0
    total_count = len(test_scenes)

    for i, scene_data in enumerate(test_scenes, 1):
        print(f"\n📸 Scene {i}/{total_count}: {scene_data['title']}")

        success = generate_image_with_gemini_flash(
            scene_data['prompt'],
            scene_data['scene']
        )

        if success:
            success_count += 1

        # API 제한 고려하여 대기
        if i < total_count:
            print("⏳ Waiting 3 seconds...")
            time.sleep(3)

    print(f"\n✅ 테스트 완료!")
    print(f"📊 성공률: {success_count}/{total_count} ({(success_count/total_count)*100:.1f}%)")

    if success_count > 0:
        print(f"\n📁 생성된 이미지:")
        for scene in test_scenes[:success_count]:
            print(f"  - game/images/scenes/{scene['scene']}.png")

if __name__ == "__main__":
    main()