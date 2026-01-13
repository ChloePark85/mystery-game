#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
0의 집행 - 장면별 이미지 생성기 (Imagen API 사용)
"""

import requests
import json
import time
import os
import base64
from pathlib import Path

# Gemini API 설정
API_KEY = "AIzaSyA1enVShSIIkEE_HHaxS-EAuc2hsNlGvgk"
IMAGE_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-fast-generate-001:generateContent"

# 이미지 저장 폴더 생성
os.makedirs("game/images/scenes", exist_ok=True)

# 각 장면별 이미지 프롬프트 (간결하고 명확하게)
scene_prompts = [
    # Phase 1: 도입부 (1-4)
    {
        "scene": "01_emergency_call",
        "title": "긴급 호출",
        "prompt": "Dark detective office at night, computer screens glowing, phone ringing, noir cyberpunk style, professional workspace"
    },
    {
        "scene": "02_mansion_exterior",
        "title": "현장 도착",
        "prompt": "Modern smart home mansion at night, glass architecture, Seoul cityscape, police cars with flashing lights, cyberpunk aesthetic"
    },
    {
        "scene": "03_police_briefing",
        "title": "사건 브리핑",
        "prompt": "Police briefing outside mansion, Korean officers, detective in dark suit, crime scene tape, professional atmosphere"
    },
    {
        "scene": "04_lab_entrance",
        "title": "연구실 입장",
        "prompt": "Underground laboratory entrance, sterile white walls, elevator opening, cold blue lighting, high-tech facility"
    },

    # Phase 2: 현장 조사 (5-10)
    {
        "scene": "05_lab_overview",
        "title": "연구실 전체 관찰",
        "prompt": "Sterile research laboratory, organized equipment, large robotic arm in center, white walls, scientific instruments"
    },
    {
        "scene": "06_robot_arm_inspection",
        "title": "로봇 팔 정밀 검사",
        "prompt": "Close-up robotic arm joint, magnifying glass, small fabric fibers in metal joints, forensic examination"
    },
    {
        "scene": "07_control_panel",
        "title": "제어 패널 데이터 분석",
        "prompt": "High-tech control panel, multiple screens, 'SHUTDOWN SEQUENCE' on monitor, blue interface, cyberpunk UI"
    },
    {
        "scene": "08_environment_check",
        "title": "주변 기기 상태 확인",
        "prompt": "Smart home devices, motorized blinds, air purifier, power graphs on screens, IoT sensors, automation"
    },
    {
        "scene": "09_evidence_analysis",
        "title": "증거 정리 및 분석",
        "prompt": "Detective with tablet, multiple screens showing analysis, evidence correlation, professional investigation"
    },
    {
        "scene": "10_investigation_complete",
        "title": "현장 조사 완료",
        "prompt": "Detective closing tablet, leaving laboratory, completed investigation, transition scene"
    },

    # Phase 3: 심문 (11-19)
    {
        "scene": "11_living_room",
        "title": "거실로 이동",
        "prompt": "Modern luxury living room, floor-to-ceiling windows, Seoul night view, suspects on sofa, wall screen"
    },
    {
        "scene": "12_yujimin_interview1",
        "title": "유지민 1차 심문",
        "prompt": "Young Korean woman, late 20s, long black hair, white lab coat, nervous expression, sitting interview"
    },
    {
        "scene": "13_hankitae_interview1",
        "title": "한기태 1차 심문",
        "prompt": "Middle-aged Korean businessman, 40s, confident but cold expression, dark suit, modern setting"
    },
    {
        "scene": "14_ai_noah_interface",
        "title": "AI 노아 1차 질문",
        "prompt": "Holographic AI interface, blue digital avatar, 'NOAH SYSTEM' text, futuristic display, data streams"
    },
    {
        "scene": "15_yujimin_interview2",
        "title": "유지민 2차 심문",
        "prompt": "Same Korean woman, now distressed and pale, sweating nervously, hands trembling, guilt in eyes"
    },
    {
        "scene": "16_hankitae_interview2",
        "title": "한기태 2차 심문",
        "prompt": "Same businessman maintaining composure, slightly defensive posture, consistent character design"
    },
    {
        "scene": "17_ai_noah_details",
        "title": "AI 노아 2차 질문",
        "prompt": "Detailed AI interface, system diagrams, automation routines, shutdown sequences, technical visualization"
    },
    {
        "scene": "18_smartwatch_data",
        "title": "스마트워치 데이터 발견",
        "prompt": "Close-up smartwatch display, heart rate spike graph, '45→120 BPM', medical interface, crucial evidence"
    },
    {
        "scene": "19_interrogation_complete",
        "title": "심문 완료",
        "prompt": "Detective reviewing testimonies on tablet, contradiction charts, three suspects background, analysis"
    },

    # Phase 4: 추리 및 해결 (20-25)
    {
        "scene": "20_data_analysis",
        "title": "최종 데이터 분석",
        "prompt": "Multiple screens data analysis, timeline reconstruction, evidence correlation charts, forensic visualization"
    },
    {
        "scene": "21_trick_hypothesis",
        "title": "트릭 추론",
        "prompt": "Technical diagram robotic arm gravity mechanism, physics illustration, necktie in joints, scientific explanation"
    },
    {
        "scene": "22_suspect_identification",
        "title": "범인 지목",
        "prompt": "Detective pointing at female suspect, dramatic confrontation, suspicion meters, climactic moment"
    },
    {
        "scene": "23_truth_revelation",
        "title": "진실 폭로",
        "prompt": "Korean woman shocked guilty expression, tears, hands covering face, emotional breakdown, defeat"
    },
    {
        "scene": "24_case_closed",
        "title": "사건 종결",
        "prompt": "Police car outside mansion, suspect in handcuffs, crime scene resolution, flashing police lights"
    },
    {
        "scene": "25_epilogue",
        "title": "에필로그",
        "prompt": "Detective silhouette against window, Seoul night cityscape, contemplative pose, noir atmosphere, city lights"
    }
]

def generate_image_with_imagen(prompt, scene_name):
    """Imagen API를 사용하여 이미지 생성"""

    headers = {
        'Content-Type': 'application/json'
    }

    # 프롬프트 향상
    enhanced_prompt = f"{prompt}, digital art style, high quality, cyberpunk noir aesthetic, Korean setting, professional illustration, 16:9 aspect ratio, detailed, atmospheric lighting, cinematic composition"

    payload = {
        "contents": [{
            "parts": [{
                "text": enhanced_prompt
            }]
        }],
        "generationConfig": {
            "temperature": 0.4,
            "topK": 32,
            "topP": 1,
            "maxOutputTokens": 8192,
        }
    }

    try:
        print(f"🎨 Generating: {scene_name}")

        response = requests.post(
            f"{IMAGE_API_URL}?key={API_KEY}",
            headers=headers,
            json=payload,
            timeout=60
        )

        if response.status_code == 200:
            result = response.json()
            print(f"✅ Success: {scene_name}")

            # 응답에서 이미지 데이터 추출
            if 'candidates' in result and len(result['candidates']) > 0:
                candidate = result['candidates'][0]
                if 'content' in candidate and 'parts' in candidate['content']:
                    for part in candidate['content']['parts']:
                        if 'inlineData' in part:
                            # Base64 이미지 데이터 저장
                            image_data = part['inlineData']['data']

                            # 이미지 파일로 저장
                            image_path = f"game/images/scenes/{scene_name}.png"
                            with open(image_path, "wb") as f:
                                f.write(base64.b64decode(image_data))

                            print(f"💾 Saved: {image_path}")
                            return True

            print(f"⚠️ No image data in response for {scene_name}")
            return False

        else:
            print(f"❌ API Error for {scene_name}: {response.status_code}")
            print(f"Response: {response.text}")
            return False

    except Exception as e:
        print(f"❌ Error generating {scene_name}: {str(e)}")
        return False

def main():
    print("🎮 0의 집행 - 장면별 이미지 생성 시작")
    print("=" * 60)

    success_count = 0
    total_count = len(scene_prompts)

    for i, scene_data in enumerate(scene_prompts, 1):
        print(f"\n📸 Scene {i:02d}/{total_count:02d}: {scene_data['title']}")

        success = generate_image_with_imagen(
            scene_data['prompt'],
            scene_data['scene']
        )

        if success:
            success_count += 1

        # API 제한을 고려하여 잠시 대기
        if i < total_count:
            print("⏳ Waiting 2 seconds...")
            time.sleep(2)

    print(f"\n✅ 이미지 생성 완료!")
    print(f"📊 성공: {success_count}/{total_count} ({(success_count/total_count)*100:.1f}%)")

    if success_count > 0:
        print(f"\n📁 생성된 이미지들:")
        print(f"  - 저장 위치: game/images/scenes/")
        print(f"  - 파일 형식: scene_XX.png")
        print(f"  - 해상도: 1024x1024 (16:9 비율 고려)")

if __name__ == "__main__":
    main()