#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
0의 집행 (Execution of Zero)
SF 하드보일드 데이터 추리 게임 - 텍스트 버전
"""

import sys
import time

class Game:
    def __init__(self):
        self.current_phase = 0
        self.evidence_collected = []
        self.suspicion = {"yujimin": 0, "hankitae": 0, "noah": 0}
        self.investigation_points = 0

        # 증거 정의
        self.evidences = {
            "robot_arm_fiber": "로봇 팔 관절에서 발견된 넥타이 섬유",
            "robot_arm_log": "21:00 - Robot Arm: SHUTDOWN SEQUENCE",
            "power_consumption": "21:00 - 블라인드/공기청정기 최대 출력",
            "audio_log": "21:00 - 오디오 센서: 0 bytes",
            "smartwatch_data": "20:55 - 심박수: 45 → 120 BPM"
        }

    def clear_screen(self):
        print("\n" * 50)

    def type_text(self, text, delay=0.03):
        """타이핑 효과"""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

    def wait_for_input(self, prompt=">>> Enter를 눌러 계속... "):
        input(prompt)

    def show_menu(self, title, options):
        """메뉴 표시"""
        print(f"\n=== {title} ===")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        while True:
            try:
                choice = int(input("선택하세요: ")) - 1
                if 0 <= choice < len(options):
                    return choice
                else:
                    print("잘못된 선택입니다.")
            except ValueError:
                print("숫자를 입력해주세요.")

    def intro(self):
        self.clear_screen()
        print("="*60)
        print("                    0의 집행")
        print("              (Execution of Zero)")
        print("="*60)
        print()

        self.type_text("2024년 3월 15일, 오후 11시 30분.")
        self.type_text("서울 강남구 소재 초호화 스마트 맨션 '아르카디아'.")
        self.type_text("모든 것이 IoT로 연결된 이 집에서, 불가능한 일이 벌어졌다.")
        print()

        self.type_text("[진] 데이터는 거짓말을 하지 않는다.")
        self.type_text("     하지만 데이터를 해석하는 인간은 거짓말을 한다.")
        print()

        self.type_text("[경찰] 진 탐정님, 현장은 이쪽입니다.")
        self.type_text("       피해자는 강박사... 천재 로봇 공학자였죠.")
        self.type_text("       지하 연구실에서 자신이 개발한 로봇 팔에")
        self.type_text("       목이 눌려 사망했습니다.")
        print()

        self.type_text("[진] 사고사로 보고 있습니까?")
        print()

        self.type_text("[경찰] 그렇습니다. AI 시스템의 오작동으로 추정되고...")
        self.type_text("       이상한 점은 로봇이 전원이 꺼진 상태였다는 겁니다.")
        print()

        self.type_text("[진] 전원이 꺼진 기계가 사람을 죽였다... 흥미롭군요.")

        self.wait_for_input()

    def scene_investigation(self):
        self.clear_screen()
        print("=" * 60)
        print("                    현장 조사")
        print("=" * 60)

        self.type_text("지하 2층 연구실.")
        self.type_text("공기는 멸균실처럼 차갑고, 피비린내 대신 기계유 냄새가 감돈다.")
        self.type_text("시체는 이미 치워졌고, 거대한 산업용 로봇 팔만이 덩그러니 서 있다.")
        print()

        self.type_text("[진] 범죄 현장에서 가장 중요한 건")
        self.type_text("     첫인상이 아니라 마지막 데이터다.")
        print()

        while self.investigation_points < 3:
            options = [
                "로봇 팔 검사",
                "제어 패널 확인",
                "연구실 환경 조사"
            ]

            if self.investigation_points >= 3:
                options.append("조사 완료")

            choice = self.show_menu("무엇을 조사할까?", options)

            if choice == 0:  # 로봇 팔 검사
                self.investigate_robot_arm()
            elif choice == 1:  # 제어 패널
                self.investigate_control_panel()
            elif choice == 2:  # 환경 조사
                self.investigate_environment()
            elif choice == 3 and self.investigation_points >= 3:
                break

        self.type_text("[진] 죽음은 결과다. 하지만 이 현장에는 원인이 결여되어 있다.")
        self.type_text("     전원이 꺼진 기계가 사람을 죽였다는 것...")
        self.type_text("     물리 법칙을 거스르는 일이다.")
        self.wait_for_input()

    def investigate_robot_arm(self):
        if "robot_arm_fiber" not in self.evidence_collected:
            self.investigation_points += 1
            print()
            self.type_text("거대한 로봇 팔을 자세히 살펴본다.")
            self.type_text("6축 다관절 구조의 정밀한 기계다.")
            print()
            self.type_text("[진] 유압 실린더가 차갑다. 작동한 지 꽤 오래된 것 같다.")
            self.type_text("     관절 부분에... 섬유 조각이 끼어있다.")
            self.type_text("     넥타이 재질 같은데.")
            print()
            self.evidence_collected.append("robot_arm_fiber")
            print("🔍 증거 발견: 로봇 팔 관절의 섬유 조각")
        else:
            print("이미 충분히 조사했다.")
        self.wait_for_input()

    def investigate_control_panel(self):
        if "robot_arm_log" not in self.evidence_collected:
            self.investigation_points += 1
            print()
            self.type_text("제어 패널의 디스플레이가 여전히 켜져 있다.")
            print()
            self.type_text("[진] 마지막 접속 기록... 어제 오후 6시.")
            self.type_text("     그 이후로는 활동 로그가 없다.")
            self.type_text("     하지만 21시 정각에 'SHUTDOWN SEQUENCE' 기록이 있다.")
            print()
            self.evidence_collected.append("robot_arm_log")
            print("🔍 증거 발견: 로봇 팔 종료 시퀀스 로그")
        else:
            print("이미 충분히 조사했다.")
        self.wait_for_input()

    def investigate_environment(self):
        if "power_consumption" not in self.evidence_collected:
            self.investigation_points += 1
            print()
            self.type_text("연구실 전체를 둘러본다.")
            self.type_text("모든 것이 정리정돈되어 있고, 다른 실험 장비들은 정상적으로 작동한다.")
            print()
            self.type_text("[진] 블라인드가 완전히 내려와 있다. 평소에도 이랬을까?")
            self.type_text("     공기청정기가 최대 출력으로 돌아가고 있다.")
            self.type_text("     무엇을 정화하려고?")
            print()
            self.evidence_collected.append("power_consumption")
            print("🔍 증거 발견: 21시 전력 사용 패턴 이상")
        else:
            print("이미 충분히 조사했다.")
        self.wait_for_input()

    def interrogation_phase(self):
        self.clear_screen()
        print("=" * 60)
        print("                     심문")
        print("=" * 60)

        interrogated = []

        while len(interrogated) < 3:
            suspects = []
            if "yujimin" not in interrogated:
                suspects.append("유지민 (조교)")
            if "hankitae" not in interrogated:
                suspects.append("한기태 (투자자)")
            if "noah" not in interrogated:
                suspects.append("AI 노아에게 질문")

            choice = self.show_menu("누구를 심문할까?", suspects)

            if choice == 0 and "yujimin" not in interrogated:
                self.interrogate_yujimin()
                interrogated.append("yujimin")
            elif choice == 1 and "hankitae" not in interrogated:
                self.interrogate_hankitae()
                interrogated.append("hankitae")
            elif choice == 2 and "noah" not in interrogated:
                self.interrogate_noah()
                interrogated.append("noah")

    def interrogate_yujimin(self):
        self.clear_screen()
        print("💭 유지민과의 대화")
        print("-" * 30)

        self.type_text("[진] 유지민 씨. 당신은 강박사의 제자라고 들었습니다.")
        print()
        self.type_text("[유지민] 네... 2년째 조교로 일하고 있어요.")
        self.type_text("         교수님은... 정말 좋은 분이셨어요.")
        print()
        self.type_text("[진] 사건 당일, 몇 시에 집을 나갔습니까?")
        print()
        self.type_text("[유지민] 8시 50분쯤요. 로그에도 남아있을 거예요.")
        self.type_text("         현관 센서가 다 기록하거든요.")
        print()
        self.type_text("[진] 나가기 직전에 강박사님과 대화를 나누었나요?")
        print()
        self.type_text("[유지민] 네. 9시에 교수님이 '커피 머신 돌려놔'라고")
        self.type_text("         말씀하시는 걸 들었어요.")
        self.type_text("         그래서 교수님이 살아계신다고 생각했는데...")
        print()

        self.suspicion["yujimin"] += 1
        self.wait_for_input()

    def interrogate_hankitae(self):
        self.clear_screen()
        print("💼 한기태와의 대화")
        print("-" * 30)

        self.type_text("[진] 한기태 씨. 당신은 강박사와 어떤 관계입니까?")
        print()
        self.type_text("[한기태] 투자자입니다. 그의 로봇 기술을 상용화하려고")
        self.type_text("         논의 중이었죠.")
        print()
        self.type_text("[진] 사건 당일에는 왜 여기에?")
        print()
        self.type_text("[한기태] 계약 조건 때문에 만나기로 했습니다.")
        self.type_text("         하지만... 좀 언성이 높아졌죠.")
        self.type_text("         그는 기술을 공개하기 싫어했고,")
        self.type_text("         저는 투자금 회수를 원했으니까요.")
        print()
        self.type_text("[진] 다툼 후에는 어디 계셨습니까?")
        print()
        self.type_text("[한기태] 거실에서 술이나 마시고 있었습니다.")
        self.type_text("         기계 따위는 모르거든요.")
        print()

        self.wait_for_input()

    def interrogate_noah(self):
        self.clear_screen()
        print("🤖 AI 노아와의 대화")
        print("-" * 30)

        self.type_text("[AI 노아] 안녕하세요, 진 탐정님.")
        self.type_text("          저는 이 집의 관리 AI 노아입니다.")
        print()
        self.type_text("[진] 노아, 21시경 집안 상황을 보고해주세요.")
        print()
        self.type_text("[AI 노아] 21시 정각 기준으로")
        self.type_text("          거실의 소음 데시벨은 40dB로 평온했습니다.")
        self.type_text("          로봇 연구실의 전력 사용량은 0입니다.")
        self.type_text("          그러나 스마트 블라인드와 공기청정기가")
        self.type_text("          퇴근 모드로 인해 최대 출력으로 작동했습니다.")
        print()

        self.evidence_collected.append("audio_log")
        print("🔍 증거 추가: 21시 오디오 센서 로그")

        self.type_text("[진] 퇴근 모드? 자세히 설명해주세요.")
        print()
        self.type_text("[AI 노아] 매일 21시에 실행되는 자동 루틴입니다.")
        self.type_text("          조명을 끄고, 블라인드를 내리고,")
        self.type_text("          모든 기기를 대기 상태로 전환합니다.")
        self.type_text("          강박사님이 직접 프로그래밍하신 시퀀스입니다.")
        print()
        self.type_text("[진] 로봇 팔도 이 루틴에 포함됩니까?")
        print()
        self.type_text("[AI 노아] 네. 로봇 팔은 초기화 자세로 복귀한 후")
        self.type_text("          전원을 차단합니다.")
        print()

        self.wait_for_input()

    def deduction_phase(self):
        self.clear_screen()
        print("=" * 60)
        print("                    추리")
        print("=" * 60)

        self.type_text("[진] 이제 퍼즐의 조각들을 맞춰볼 시간입니다.")
        self.type_text("     죽음의 시각은 21시. 로봇 팔의 전원은 OFF.")
        self.type_text("     하지만 누군가는 거짓말을 하고 있다.")
        print()

        # 모순 찾기 1
        print("🔍 첫 번째 모순을 찾아보자.")
        options = [
            "유지민의 증언과 오디오 로그",
            "한기태의 알리바이",
            "AI의 시스템 로그"
        ]

        choice = self.show_menu("어떤 모순인가?", options)

        if choice == 0:  # 정답
            print()
            self.type_text("[진] 유지민은 21시에 강박사의 목소리를 들었다고 했습니다.")
            self.type_text("     하지만 오디오 센서는 그 시간 음성 데이터")
            self.type_text("     0바이트를 기록했습니다.")
            print()

            # 스마트워치 데이터 추가
            self.evidence_collected.append("smartwatch_data")
            print("🔍 추가 증거 발견: 강박사의 스마트워치 생체 데이터")

            self.type_text("[진] 강박사의 스마트워치 데이터를 확인했습니다.")
            self.type_text("     20:55에 심박수가 급격히 상승했습니다.")
            self.type_text("     45에서 120으로.")
            self.type_text("     유지민이 나간 건 20:50. 그럼 누가 강박사를 위협했을까요?")

        else:
            print("\n다른 각도로 접근해봅시다...")

        self.wait_for_input()
        self.final_revelation()

    def final_revelation(self):
        self.clear_screen()
        print("=" * 60)
        print("                   진실 폭로")
        print("=" * 60)

        self.type_text("[진] 이제 모든 것이 명확해졌습니다.")
        print()
        self.type_text("     유지민 씨. 당신이 범인입니다.")
        print()
        self.type_text("[유지민] 뭐라고요?! 말도 안 돼요!")
        self.type_text("         저는 8시 50분에 나갔어요!")
        print()
        self.type_text("[진] 맞습니다. 하지만 나가기 전에 당신은 함정을 설치했습니다.")
        self.type_text("     강박사의 넥타이를 로봇 팔의 관절 틈에 끼워둔 것입니다.")
        print()
        self.type_text("[유지민] 그... 그건...")
        print()
        self.type_text("[진] 21시 퇴근 모드가 실행되면, 로봇 팔은 초기화 자세로 이동합니다.")
        self.type_text("     전원이 켜져서 공격한 게 아닙니다.")
        self.type_text("     전원이 꺼지면서 중력에 의해 팔이 떨어진 겁니다.")
        self.type_text("     그 무게만으로도 목에 걸린 넥타이가 조여질 수 있습니다.")
        print()
        self.type_text("[진] 당신은 시스템의 허점을 이용했습니다.")
        self.type_text("     '종료' 프로세스는 '공격' 로그에 남지 않습니다.")
        self.type_text("     하지만 한 가지 계산 실수가 있었습니다.")
        print()
        self.type_text("     강박사는 당신이 함정을 설치하는 걸 눈치챘습니다.")
        self.type_text("     20:55, 심박수 급상승.")
        self.type_text("     죽음에 대한 공포가 아니라 배신에 대한 분노였습니다.")
        print()
        self.type_text("[진] 그리고 21시. 당신이 만든 기계적 운명이 실행되었습니다.")
        self.type_text("     완벽한 계획이었지만...")
        self.type_text("     데이터는 모든 것을 기억하고 있었습니다.")
        print()

        self.wait_for_input()

        self.clear_screen()
        print("=" * 60)
        print("                    END")
        print("=" * 60)

        self.type_text("사건은 해결되었다.")
        self.type_text("하지만 진에게는 찜찜함이 남았다.")
        self.type_text("기계는 명령받은 대로 작동했을 뿐이다.")
        self.type_text("살인을 저지른 것은 인간의 계산된 악의였다.")
        print()
        self.type_text("데이터는 거짓말을 하지 않는다.")
        self.type_text("거짓말을 하는 것은 언제나 인간이다.")
        print()

        print("게임 종료")

    def show_evidence(self):
        """수집한 증거 표시"""
        if not self.evidence_collected:
            print("\n수집한 증거가 없습니다.")
            return

        print("\n📋 수집한 증거:")
        print("-" * 40)
        for evidence in self.evidence_collected:
            if evidence in self.evidences:
                print(f"• {self.evidences[evidence]}")
            else:
                print(f"• {evidence}")

    def run(self):
        """게임 메인 루프"""
        self.intro()
        self.scene_investigation()
        self.interrogation_phase()
        self.deduction_phase()

if __name__ == "__main__":
    print("Starting 0의 집행 (Execution of Zero)...")
    time.sleep(1)

    game = Game()
    game.run()