#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
0의 집행 - 장면별 이미지 생성기
Gemini API를 사용하여 각 장면에 맞는 이미지 생성
"""

import requests
import json
import time
import os
from pathlib import Path

# Gemini API 설정
GEMINI_API_KEY = "AIzaSyA1enVShSIIkEE_HHaxS-EAuc2hsNlGvgk"
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro-vision:generateContent"

# 이미지 저장 폴더 생성
os.makedirs("game/images/scenes", exist_ok=True)

# 각 장면별 이미지 프롬프트
scene_prompts = [
    # Phase 1: 도입부 (1-4)
    {
        "scene": "01_emergency_call",
        "title": "긴급 호출",
        "prompt": "Dark detective office at night in Seoul, computer screens glowing, phone ringing, noir atmosphere, cyberpunk aesthetic, digital forensics equipment, moody lighting, professional investigator workspace, digital art style"
    },
    {
        "scene": "02_mansion_exterior",
        "title": "현장 도착",
        "prompt": "Ultra-modern smart home mansion exterior at night, glass and steel architecture, Seoul cityscape, police cars with flashing lights, high-tech building with LED accents, cyberpunk noir atmosphere, futuristic residential building, digital art style"
    },
    {
        "scene": "03_police_briefing",
        "title": "사건 브리핑",
        "prompt": "Police briefing scene outside smart mansion, Korean police officers in uniform, detective in dark suit, crime scene tape, professional consultation, urban night setting, serious atmosphere, digital art style"
    },
    {
        "scene": "04_lab_entrance",
        "title": "연구실 입장",
        "prompt": "Underground laboratory entrance, sterile white walls, elevator doors opening, cold blue lighting, high-tech research facility, clean minimalist design, scientific atmosphere, cyberpunk aesthetic, digital art style"
    },

    # Phase 2: 현장 조사 (5-10)
    {
        "scene": "05_lab_overview",
        "title": "연구실 전체 관찰",
        "prompt": "Sterile research laboratory interior, organized equipment, large industrial robotic arm in center, white walls, metallic surfaces, scientific instruments, clean and pristine crime scene, cold lighting, digital art style"
    },
    {
        "scene": "06_robot_arm_inspection",
        "title": "로봇 팔 정밀 검사",
        "prompt": "Close-up of industrial robotic arm joint, magnifying glass examining mechanical parts, small black fabric fibers caught in metal joints, forensic examination, detailed mechanical components, evidence discovery, digital art style"
    },
    {
        "scene": "07_control_panel",
        "title": "제어 패널 데이터 분석",
        "prompt": "High-tech control panel with multiple screens, 'SHUTDOWN SEQUENCE' displayed on monitor, timestamp '21:00', blue glowing interface, data logs and system information, cyberpunk UI design, digital art style"
    },
    {
        "scene": "08_environment_check",
        "title": "주변 기기 상태 확인",
        "prompt": "Smart home automation devices, motorized blinds, air purifier, power consumption graphs on screens, IoT sensors, automated systems, high-tech environmental controls, data visualization, digital art style"
    },
    {
        "scene": "09_evidence_analysis",
        "title": "증거 정리 및 분석",
        "prompt": "Detective examining tablet with evidence photos and data, multiple screens showing forensic analysis, organized evidence layout, professional investigation setup, data correlation, digital forensics, digital art style"
    },
    {
        "scene": "10_investigation_complete",
        "title": "현장 조사 완료",
        "prompt": "Detective closing tablet and preparing to leave laboratory, final evidence collection, transition from crime scene to interrogation phase, professional demeanor, completed investigation, digital art style"
    },

    # Phase 3: 심문 (11-19)
    {
        "scene": "11_living_room",
        "title": "거실로 이동",
        "prompt": "Modern luxury smart home living room, floor-to-ceiling windows with Seoul night view, minimalist furniture, two suspects sitting on sofa, large wall screen, contemporary interior design, digital art style"
    },
    {
        "scene": "12_yujimin_interview1",
        "title": "유지민 1차 심문",
        "prompt": "Young Korean woman in her late 20s, long black hair, white lab coat, nervous anxious expression, sitting across from interviewer, consistent character design, realistic proportions, digital art style"
    },
    {
        "scene": "13_hankitae_interview1",
        "title": "한기태 1차 심문",
        "prompt": "Middle-aged Korean businessman in his 40s, confident but cold expression, dark business suit, sitting in modern living room, professional appearance, consistent character design, digital art style"
    },
    {
        "scene": "14_ai_noah_interface",
        "title": "AI 노아 1차 질문",
        "prompt": "Holographic AI interface on wall screen, blue digital avatar projection, 'NOAH SYSTEM' text, futuristic hologram display, smart home control center, glowing data streams, cyberpunk aesthetic, digital art style"
    },
    {
        "scene": "15_yujimin_interview2",
        "title": "유지민 2차 심문",
        "prompt": "Same young Korean woman from earlier, now more distressed and pale, sweating nervously, hands trembling, guilt and fear in eyes, consistent character design, psychological pressure, digital art style"
    },
    {
        "scene": "16_hankitae_interview2",
        "title": "한기태 2차 심문",
        "prompt": "Same middle-aged businessman, maintaining composure but slightly defensive posture, consistent character from earlier scene, same business suit and facial features, digital art style"
    },
    {
        "scene": "17_ai_noah_details",
        "title": "AI 노아 2차 질문",
        "prompt": "Detailed AI interface showing system diagrams, automated home routines, shutdown sequences, technical data visualization, smart home automation flowcharts, cyberpunk interface design, digital art style"
    },
    {
        "scene": "18_smartwatch_data",
        "title": "스마트워치 데이터 발견",
        "prompt": "Close-up of smartwatch display showing heart rate spike graph, timeline from 20:55, dramatic data visualization, numbers '45 BPM → 120 BPM', medical monitoring interface, crucial evidence, digital art style"
    },
    {
        "scene": "19_interrogation_complete",
        "title": "심문 완료",
        "prompt": "Detective reviewing all testimonies and evidence on tablet, multiple contradiction charts, data correlation analysis, three suspects in background, investigation synthesis, digital art style"
    },

    # Phase 4: 추리 및 해결 (20-25)
    {
        "scene": "20_data_analysis",
        "title": "최종 데이터 분석",
        "prompt": "Comprehensive data analysis on multiple screens, timeline reconstruction, evidence correlation charts, forensic data visualization, systematic investigation results, professional analysis, digital art style"
    },
    {
        "scene": "21_trick_hypothesis",
        "title": "트릭 추론",
        "prompt": "Technical diagram showing robotic arm gravity mechanism, physics illustration of shutdown sequence, necktie caught in mechanical joints, scientific explanation of murder method, forensic reconstruction, digital art style"
    },
    {
        "scene": "22_suspect_identification",
        "title": "범인 지목",
        "prompt": "Detective pointing accusingly at female suspect, dramatic confrontation scene, suspicion meters showing evidence against each suspect, climactic moment of truth, digital art style"
    },
    {
        "scene": "23_truth_revelation",
        "title": "진실 폭로",
        "prompt": "Same young Korean woman from earlier interviews, now with shocked guilty expression, tears in eyes, hands covering face in defeat, emotional breakdown, consistent character design, digital art style"
    },
    {
        "scene": "24_case_closed",
        "title": "사건 종결",
        "prompt": "Police car outside smart mansion, suspect in handcuffs being led away, crime scene resolution, justice served, urban night setting with flashing police lights, digital art style"
    },
    {
        "scene": "25_epilogue",
        "title": "에필로그",
        "prompt": "Detective silhouette against large window overlooking Seoul night cityscape, contemplative pose, noir atmosphere, city lights reflecting, philosophical mood, cyberpunk city background, digital art style"
    }
]

def generate_image_with_gemini(prompt, scene_name):
    """Gemini API를 사용하여 이미지 생성"""

    headers = {
        'Content-Type': 'application/json'
    }

    # Gemini는 텍스트 생성만 지원하므로, 대신 DALL-E나 Midjourney 스타일의 상세 프롬프트를 생성
    detailed_prompt = f"""
    Create a detailed image prompt for: {prompt}

    Style requirements:
    - Digital art style with high quality rendering
    - Cyberpunk noir aesthetic
    - Korean setting (Seoul)
    - Professional crime investigation theme
    - Consistent character designs
    - Moody atmospheric lighting
    - 16:9 aspect ratio suitable for game interface

    Technical specifications:
    - High resolution (1920x1080)
    - Sharp details for UI integration
    - Appropriate contrast for text overlay
    - Professional illustration quality
    """

    payload = {
        "contents": [{
            "parts": [{
                "text": detailed_prompt
            }]
        }],
        "generationConfig": {
            "temperature": 0.7,
            "topK": 40,
            "topP": 0.95,
            "maxOutputTokens": 1024,
        }
    }

    try:
        response = requests.post(
            f"{GEMINI_API_URL}?key={GEMINI_API_KEY}",
            headers=headers,
            json=payload,
            timeout=30
        )

        if response.status_code == 200:
            result = response.json()
            if 'candidates' in result and len(result['candidates']) > 0:
                generated_text = result['candidates'][0]['parts'][0]['text']
                print(f"✅ Generated prompt for {scene_name}")
                return generated_text
            else:
                print(f"❌ No content generated for {scene_name}")
                return None
        else:
            print(f"❌ API Error for {scene_name}: {response.status_code}")
            print(f"Response: {response.text}")
            return None

    except Exception as e:
        print(f"❌ Error generating {scene_name}: {str(e)}")
        return None

def save_prompts_for_external_generation():
    """외부 이미지 생성 도구용 프롬프트 파일 생성"""

    print("🎨 외부 이미지 생성을 위한 프롬프트 파일 생성 중...")

    with open("game/images/image_prompts.txt", "w", encoding="utf-8") as f:
        f.write("0의 집행 (Execution of Zero) - 장면별 이미지 생성 프롬프트\n")
        f.write("=" * 80 + "\n\n")

        for i, scene_data in enumerate(scene_prompts, 1):
            f.write(f"Scene {i:02d}: {scene_data['title']}\n")
            f.write(f"파일명: {scene_data['scene']}.png\n")
            f.write(f"프롬프트: {scene_data['prompt']}\n")
            f.write("-" * 80 + "\n\n")

    print(f"✅ 프롬프트 파일 저장 완료: game/images/image_prompts.txt")

    # JSON 형태로도 저장
    with open("game/images/scene_prompts.json", "w", encoding="utf-8") as f:
        json.dump(scene_prompts, f, ensure_ascii=False, indent=2)

    print(f"✅ JSON 프롬프트 파일 저장 완료: game/images/scene_prompts.json")

def main():
    print("🎮 0의 집행 - 장면별 이미지 생성 시작")
    print("=" * 60)

    # Gemini API는 이미지 생성을 직접 지원하지 않으므로
    # 상세한 프롬프트를 생성하여 외부 도구에서 사용할 수 있게 함

    print("📝 Gemini API로 향상된 프롬프트 생성 중...")

    enhanced_prompts = []

    for i, scene_data in enumerate(scene_prompts, 1):
        print(f"\n🎨 Scene {i:02d}: {scene_data['title']}")

        # Gemini로 프롬프트 향상
        enhanced_prompt = generate_image_with_gemini(
            scene_data['prompt'],
            scene_data['scene']
        )

        if enhanced_prompt:
            enhanced_prompts.append({
                **scene_data,
                'enhanced_prompt': enhanced_prompt
            })
        else:
            enhanced_prompts.append(scene_data)

        # API 호출 제한 고려하여 잠시 대기
        time.sleep(1)

    # 향상된 프롬프트 저장
    with open("game/images/enhanced_prompts.json", "w", encoding="utf-8") as f:
        json.dump(enhanced_prompts, f, ensure_ascii=False, indent=2)

    # 기본 프롬프트도 저장
    save_prompts_for_external_generation()

    print(f"\n✅ 총 {len(scene_prompts)}개 장면의 이미지 프롬프트 생성 완료!")
    print("\n📁 생성된 파일들:")
    print("  - game/images/image_prompts.txt (텍스트 형태)")
    print("  - game/images/scene_prompts.json (기본 JSON)")
    print("  - game/images/enhanced_prompts.json (Gemini 향상 JSON)")

    print("\n🎨 이미지 생성 방법:")
    print("  1. DALL-E, Midjourney, 또는 Stable Diffusion 사용")
    print("  2. 각 프롬프트를 복사하여 이미지 생성")
    print("  3. 생성된 이미지를 game/images/scenes/ 폴더에 저장")
    print("  4. 파일명은 scene_01.png, scene_02.png 형식으로 저장")

if __name__ == "__main__":
    main()