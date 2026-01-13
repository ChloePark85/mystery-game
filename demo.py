#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
0의 집행 (Execution of Zero)
SF 하드보일드 데이터 추리 게임 - 자동 실행 데모
"""

import time
import sys

def type_text(text, delay=0.02):
    """타이핑 효과"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def demo():
    print("=" * 60)
    print("                    0의 집행")
    print("              (Execution of Zero)")
    print("=" * 60)
    print()

    type_text("2024년 3월 15일, 오후 11시 30분.")
    type_text("서울 강남구 소재 초호화 스마트 맨션 '아르카디아'.")
    type_text("모든 것이 IoT로 연결된 이 집에서, 불가능한 일이 벌어졌다.")
    print()

    type_text("[진] 데이터는 거짓말을 하지 않는다.")
    type_text("     하지만 데이터를 해석하는 인간은 거짓말을 한다.")
    print()

    type_text("[경찰] 진 탐정님, 현장은 이쪽입니다.")
    type_text("       피해자는 강박사... 천재 로봇 공학자였죠.")
    type_text("       지하 연구실에서 자신이 개발한 로봇 팔에")
    type_text("       목이 눌려 사망했습니다.")
    print()

    time.sleep(1)
    print("\n" + "=" * 60)
    print("                    현장 조사")
    print("=" * 60)

    type_text("지하 2층 연구실.")
    type_text("공기는 멸균실처럼 차갑고, 피비린내 대신 기계유 냄새가 감돈다.")
    type_text("시체는 이미 치워졌고, 거대한 산업용 로봇 팔만이 덩그러니 서 있다.")
    print()

    type_text("[진] 범죄 현장에서 가장 중요한 건")
    type_text("     첫인상이 아니라 마지막 데이터다.")
    print()

    type_text(">>> 로봇 팔을 검사한다...")
    time.sleep(1)

    type_text("[진] 유압 실린더가 차갑다. 작동한 지 꽤 오래된 것 같다.")
    type_text("     관절 부분에... 섬유 조각이 끼어있다. 넥타이 재질 같은데.")
    print()
    print("🔍 증거 발견: 로봇 팔 관절의 섬유 조각")
    print()

    type_text(">>> 제어 패널을 확인한다...")
    time.sleep(1)

    type_text("[진] 마지막 접속 기록... 어제 오후 6시.")
    type_text("     그 이후로는 활동 로그가 없다.")
    type_text("     하지만 21시 정각에 'SHUTDOWN SEQUENCE' 기록이 있다.")
    print()
    print("🔍 증거 발견: 로봇 팔 종료 시퀀스 로그")
    print()

    time.sleep(1)
    print("\n" + "=" * 60)
    print("                     심문")
    print("=" * 60)

    type_text("💭 유지민(조교)과의 대화:")
    print()
    type_text("[유지민] 저는 8시 50분에 집을 나갔어요.")
    type_text("         9시에 교수님이 '커피 머신 돌려놔'라고")
    type_text("         말씀하시는 걸 들었어요.")
    print()

    type_text("🤖 AI 노아와의 대화:")
    print()
    type_text("[AI 노아] 21시 정각 기준으로")
    type_text("          거실의 소음 데시벨은 40dB로 평온했습니다.")
    type_text("          로봇 연구실의 전력 사용량은 0입니다.")
    type_text("          오디오 센서 기록: 0 bytes")
    print()
    print("🔍 증거 발견: 21시 오디오 센서 로그")
    print()

    time.sleep(1)
    print("\n" + "=" * 60)
    print("                    추리")
    print("=" * 60)

    type_text("[진] 첫 번째 모순을 발견했습니다.")
    type_text("     유지민은 21시에 강박사의 목소리를 들었다고 했습니다.")
    type_text("     하지만 오디오 센서는 그 시간 음성 데이터 0바이트를 기록했습니다.")
    print()

    type_text("     추가로, 강박사의 스마트워치 데이터를 확인했습니다.")
    type_text("     20:55에 심박수가 45에서 120으로 급격히 상승했습니다.")
    print()
    print("🔍 추가 증거: 20:55 심박수 급상승")
    print()

    time.sleep(1)
    print("\n" + "=" * 60)
    print("                   진실 폭로")
    print("=" * 60)

    type_text("[진] 유지민 씨. 당신이 범인입니다.")
    print()
    type_text("     당신은 나가기 전에 함정을 설치했습니다.")
    type_text("     강박사의 넥타이를 로봇 팔의 관절 틈에 끼워둔 것입니다.")
    print()

    type_text("     21시 퇴근 모드가 실행되면, 로봇 팔은 초기화 자세로 이동합니다.")
    type_text("     전원이 켜져서 공격한 게 아닙니다.")
    type_text("     전원이 꺼지면서 중력에 의해 팔이 떨어진 겁니다.")
    print()

    type_text("     강박사는 당신의 함정을 눈치챘습니다.")
    type_text("     20:55 심박수 급상승이 그 증거입니다.")
    type_text("     배신에 대한 분노와 죽음에 대한 공포였습니다.")
    print()

    type_text("     완벽한 계획이었지만...")
    type_text("     데이터는 모든 것을 기억하고 있었습니다.")
    print()

    time.sleep(2)
    print("\n" + "=" * 60)
    print("                    END")
    print("=" * 60)

    type_text("사건은 해결되었다.")
    type_text("하지만 진에게는 찜찜함이 남았다.")
    type_text("기계는 명령받은 대로 작동했을 뿐이다.")
    type_text("살인을 저지른 것은 인간의 계산된 악의였다.")
    print()

    type_text("데이터는 거짓말을 하지 않는다.")
    type_text("거짓말을 하는 것은 언제나 인간이다.")
    print()

    print("\n🎮 게임 완료!")
    print("\n📁 Ren'Py 버전은 game/ 폴더에 있습니다.")
    print("   Ren'Py 런처로 실행할 수 있습니다.")

if __name__ == "__main__":
    print("Starting 0의 집행 (Execution of Zero) - Demo...")
    time.sleep(1)
    demo()