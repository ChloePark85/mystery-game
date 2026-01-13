#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
0의 집행 (Execution of Zero)
SF 하드보일드 데이터 추리 게임 - 간소화 인터랙티브 버전
"""

import time
import os

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def type_text(text, delay=0.01):
    """빠른 타이핑 효과"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def menu_choice(options):
    print()
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("\n선택하세요: ")) - 1
            if 0 <= choice < len(options):
                return choice
            print("잘못된 선택입니다.")
        except (ValueError, KeyboardInterrupt):
            print("숫자를 입력해주세요.")

def run_game():
    clear_screen()

    print("=" * 60)
    print("                    0의 집행")
    print("              (Execution of Zero)")
    print("=" * 60)
    print()

    type_text("2024년 3월 15일, 오후 11시 30분.")
    type_text("서울 강남구 초호화 스마트 맨션 '아르카디아'.")
    type_text("모든 것이 IoT로 연결된 이 집에서, 불가능한 일이 벌어졌다.")
    print()

    type_text("[진] 데이터는 거짓말을 하지 않는다.")
    type_text("     하지만 데이터를 해석하는 인간은 거짓말을 한다.")
    print()

    input(">>> Enter로 계속...")
    clear_screen()

    # 현장 조사
    print("=" * 60)
    print("                    현장 조사")
    print("=" * 60)

    type_text("지하 2층 연구실.")
    type_text("거대한 산업용 로봇 팔이 덩그러니 서 있다.")
    print()

    evidence = []

    while len(evidence) < 3:
        options = []
        if "로봇팔" not in evidence:
            options.append("로봇 팔 검사")
        if "로그" not in evidence:
            options.append("제어 패널 확인")
        if "환경" not in evidence:
            options.append("연구실 환경 조사")
        if len(evidence) >= 2:
            options.append("조사 완료")

        choice = menu_choice(options)

        if "로봇 팔 검사" in options[choice]:
            print("\n🔍 로봇 팔 관절에서 넥타이 섬유 조각 발견!")
            evidence.append("로봇팔")
        elif "제어 패널 확인" in options[choice]:
            print("\n🔍 21:00 SHUTDOWN SEQUENCE 로그 발견!")
            evidence.append("로그")
        elif "연구실 환경 조사" in options[choice]:
            print("\n🔍 21시에 블라인드/공기청정기 최대 출력 기록!")
            evidence.append("환경")
        elif "조사 완료" in options[choice] and len(evidence) >= 2:
            break

        input("\n>>> Enter로 계속...")

    clear_screen()

    # 심문
    print("=" * 60)
    print("                     심문")
    print("=" * 60)

    type_text("[유지민] 저는 8시 50분에 집을 나갔어요.")
    type_text("         9시에 교수님이 '커피 머신 돌려놔'라고 말씀하시는 걸 들었어요.")
    print()

    type_text("[AI 노아] 21시 정각 오디오 센서 기록: 0 bytes")
    type_text("          아무 음성도 기록되지 않았습니다.")
    print()

    type_text("🔍 모순 발견!")
    print()

    input(">>> Enter로 계속...")
    clear_screen()

    # 추리
    print("=" * 60)
    print("                    추리")
    print("=" * 60)

    type_text("[진] 첫 번째 모순:")
    type_text("     유지민은 9시에 목소리를 들었다고 했지만")
    type_text("     오디오 센서는 0바이트를 기록했습니다.")
    print()

    type_text("     추가 증거: 강박사 스마트워치")
    type_text("     20:55 심박수 45 → 120 급상승!")
    print()

    options = ["유지민이 범인이다", "한기태가 범인이다", "AI가 오작동했다"]
    choice = menu_choice(options)

    clear_screen()

    # 결말
    print("=" * 60)
    print("                   진실 폭로")
    print("=" * 60)

    if choice == 0:  # 정답
        type_text("🎯 정답!")
        print()
        type_text("[진] 유지민 씨, 당신이 범인입니다.")
        print()
        type_text("     트릭의 정체:")
        type_text("     1. 넥타이를 로봇 팔 관절에 끼워둠")
        type_text("     2. 21시 퇴근 모드로 로봇 팔이 초기화 자세로 이동")
        type_text("     3. 전원이 꺼지면서 중력으로 팔이 떨어짐")
        type_text("     4. 그 무게로 넥타이가 조여져 질식사")
        print()
        type_text("     완벽한 계획이었지만...")
        type_text("     데이터는 모든 것을 기억하고 있었습니다.")
    else:
        type_text("❌ 틀렸습니다!")
        print()
        type_text("정답: 유지민이 중력을 이용한 기계적 살인을 저질렀습니다.")

    print()
    print("=" * 60)
    print("                    END")
    print("=" * 60)

    type_text("데이터는 거짓말을 하지 않는다.")
    type_text("거짓말을 하는 것은 언제나 인간이다.")
    print()
    print("🎮 게임 완료!")

if __name__ == "__main__":
    try:
        run_game()
    except KeyboardInterrupt:
        print("\n\n게임을 종료합니다.")