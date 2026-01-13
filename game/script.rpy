## 0의 집행 (Execution of Zero) - 메인 스크립트

# 캐릭터 정의
define j = Character("진", color="#c8ffc8")  # 주인공 - 데이터 포렌식 전문가
define y = Character("유지민", color="#ffb3b3")  # 조교 - 용의자
define h = Character("한기태", color="#b3d9ff")  # 투자자 - 용의자
define noah = Character("AI 노아", color="#d4af37")  # 홈 AI
define police = Character("경찰", color="#cccccc")

# 게임 상태 변수
default current_phase = 0  # 0: 현장조사, 1: 심문, 2: 추리
default evidence_collected = []  # 수집한 증거
default suspicion = {"yujimin": 0, "hankitae": 0, "noah": 0}
default investigation_points = 0

# 증거 클래스
init python:
    class Evidence:
        def __init__(self, name, description, log_data, timestamp=""):
            self.name = name
            self.description = description
            self.log_data = log_data
            self.timestamp = timestamp

    # 주요 증거 정의
    robot_arm_log = Evidence(
        "로봇 팔 작동 로그",
        "사망 추정 시각에 로봇 팔은 전원 OFF 상태였다.",
        "21:00 - Robot Arm System: SHUTDOWN SEQUENCE INITIATED"
    )

    audio_log = Evidence(
        "오디오 센서 로그",
        "21:00경 연구실에서 음성 데이터가 기록되지 않았다.",
        "21:00 - Audio Sensor: 0 bytes recorded"
    )

    power_consumption = Evidence(
        "전력 사용량 로그",
        "21:00에 블라인드와 공기청정기가 최대 출력으로 작동했다.",
        "21:00 - Smart Blind: MAX POWER / Air Purifier: MAX POWER"
    )

    smartwatch_data = Evidence(
        "스마트워치 생체 데이터",
        "강박사의 심박수가 20:55에 급격히 상승했다.",
        "20:55 - Heart Rate: 45 → 120 BPM"
    )

# 게임 시작
label start:
    scene black with fade

    "2024년 3월 15일, 오후 11시 30분."
    "서울 강남구 소재 초호화 스마트 맨션 '아르카디아'."

    scene bg_mansion_exterior with fade

    "모든 것이 IoT로 연결된 이 집에서, 불가능한 일이 벌어졌다."

    j "데이터는 거짓말을 하지 않는다. 하지만 데이터를 해석하는 인간은 거짓말을 한다."

    scene bg_entrance with fade

    police "진 탐정님, 현장은 이쪽입니다. 피해자는 강박사... 천재 로봇 공학자였죠."
    police "지하 연구실에서 자신이 개발한 로봇 팔에 목이 눌려 사망했습니다."

    j "사고사로 보고 있습니까?"

    police "그렇습니다. AI 시스템의 오작동으로 추정되고... 이상한 점은 로봇이 전원이 꺼진 상태였다는 겁니다."

    j "전원이 꺼진 기계가 사람을 죽였다... 흥미롭군요."

    # 현장 조사 시작
    call scene_investigation

    # 심문 단계
    call interrogation_phase

    # 추리 및 해결
    call deduction_phase

    return

# 현장 조사
label scene_investigation:
    $ current_phase = 0

    scene bg_lab_dark with fade

    "지하 2층 연구실. 공기는 멸균실처럼 차갑고, 피비린내 대신 기계유 냄새가 감돈다."
    "시체는 이미 치워졌고, 거대한 산업용 로봇 팔만이 덩그러니 서 있다."

    j "범죄 현장에서 가장 중요한 건 첫인상이 아니라 마지막 데이터다."

    menu investigation_menu:
        "무엇을 조사할까?"

        "로봇 팔 검사":
            jump examine_robot_arm

        "제어 패널 확인":
            jump examine_control_panel

        "연구실 환경 조사":
            jump examine_environment

        "조사 완료":
            if investigation_points >= 3:
                jump investigation_complete
            else:
                j "아직 충분히 조사하지 못했다. 뭔가 빠뜨린 게 있을 것이다."
                jump investigation_menu

label examine_robot_arm:
    $ investigation_points += 1

    "거대한 로봇 팔을 자세히 살펴본다. 6축 다관절 구조의 정밀한 기계다."

    j "유압 실린더가 차갑다. 작동한 지 꽤 오래된 것 같다."
    j "관절 부분에... 섬유 조각이 끼어있다. 넥타이 재질 같은데."

    $ evidence_collected.append("robot_arm_fiber")

    "로봇 팔 관절에서 섬유 조각을 발견했다."

    jump investigation_menu

label examine_control_panel:
    $ investigation_points += 1

    "제어 패널의 디스플레이가 여전히 켜져 있다. 로그 기록을 확인해보자."

    j "마지막 접속 기록... 어제 오후 6시. 그 이후로는 활동 로그가 없다."
    j "하지만 21시 정각에 'SHUTDOWN SEQUENCE' 기록이 있다."

    $ evidence_collected.append(robot_arm_log)

    "로봇 팔의 종료 시퀀스 로그를 발견했다."

    jump investigation_menu

label examine_environment:
    $ investigation_points += 1

    "연구실 전체를 둘러본다. 모든 것이 정리정돈되어 있고, 다른 실험 장비들은 정상적으로 작동하고 있다."

    j "블라인드가 완전히 내려와 있다. 평소에도 이랬을까?"
    j "공기청정기가 최대 출력으로 돌아가고 있다. 무엇을 정화하려고?"

    $ evidence_collected.append(power_consumption)

    "퇴근 시간대 전력 사용 패턴이 이상하다."

    jump investigation_menu

label investigation_complete:
    j "죽음은 결과다. 하지만 이 현장에는 원인이 결여되어 있다."
    j "전원이 꺼진 기계가 사람을 죽였다는 것... 물리 법칙을 거스르는 일이다."
    j "하지만 데이터는 명확하다. 뭔가 다른 각도로 접근해야 한다."

    return

# 심문 단계
label interrogation_phase:
    $ current_phase = 1

    scene bg_living_room with fade

    police "용의자들을 거실에 모았습니다. 사건 당일 집에 있었던 사람들이죠."

    j "좋습니다. 한 명씩 이야기를 들어보죠."

    menu interrogation_choice:
        "누구부터 심문할까?"

        "유지민 (조교)":
            call interrogate_yujimin

        "한기태 (투자자)":
            call interrogate_hankitae

        "AI 노아에게 질문":
            call interrogate_noah

        "심문 완료":
            if len([x for x in ["yujimin_done", "hankitae_done", "noah_done"] if x in evidence_collected]) >= 3:
                return
            else:
                j "아직 모든 사람의 이야기를 듣지 못했다."
                jump interrogation_choice

label interrogate_yujimin:
    show yujimin nervous at center with dissolve

    j "유지민 씨. 당신은 강박사의 제자라고 들었습니다."

    y "네... 2년째 조교로 일하고 있어요. 교수님은... 정말 좋은 분이셨어요."

    j "사건 당일, 몇 시에 집을 나갔습니까?"

    y "8시 50분쯤요. 로그에도 남아있을 거예요. 현관 센서가 다 기록하거든요."

    j "나가기 직전에 강박사님과 대화를 나누었나요?"

    y "네. 9시에 교수님이 '커피 머신 돌려놔'라고 말씀하시는 걸 들었어요."
    y "그래서 교수님이 살아계신다고 생각했는데..."

    $ suspicion["yujimin"] += 1

    j "흥미롭군요. 다시 이야기해보겠습니다."

    $ evidence_collected.append("yujimin_done")
    hide yujimin

    jump interrogation_choice

label interrogate_hankitae:
    show hankitae confident at center with dissolve

    j "한기태 씨. 당신은 강박사와 어떤 관계입니까?"

    h "투자자입니다. 그의 로봇 기술을 상용화하려고 논의 중이었죠."

    j "사건 당일에는 왜 여기에?"

    h "계약 조건 때문에 만나기로 했습니다. 하지만... 좀 언성이 높아졌죠."
    h "그는 기술을 공개하기 싫어했고, 저는 투자금 회수를 원했으니까요."

    j "다툼 후에는 어디 계셨습니까?"

    h "거실에서 술이나 마시고 있었습니다. 기계 따위는 모르거든요."

    $ suspicion["hankitae"] += 1

    j "그 시간에 지하에서 무슨 일이 벌어지는지 알고 계셨습니까?"

    h "전혀요. 관심도 없었고요."

    $ evidence_collected.append("hankitae_done")
    hide hankitae

    jump interrogation_choice

label interrogate_noah:
    show screen tablet_ui

    noah "안녕하세요, 진 탐정님. 저는 이 집의 관리 AI 노아입니다."

    j "노아, 21시경 집안 상황을 보고해주세요."

    noah "21시 정각 기준으로 거실의 소음 데시벨은 40dB로 평온했습니다."
    noah "로봇 연구실의 전력 사용량은 0입니다."
    noah "그러나 스마트 블라인드와 공기청정기가 퇴근 모드로 인해 최대 출력으로 작동했습니다."

    $ evidence_collected.append(audio_log)

    j "퇴근 모드? 자세히 설명해주세요."

    noah "매일 21시에 실행되는 자동 루틴입니다. 조명을 끄고, 블라인드를 내리고, 모든 기기를 대기 상태로 전환합니다."
    noah "강박사님이 직접 프로그래밍하신 시퀀스입니다."

    $ suspicion["noah"] += 1

    j "로봇 팔도 이 루틴에 포함됩니까?"

    noah "네. 로봇 팔은 초기화 자세로 복귀한 후 전원을 차단합니다."

    $ evidence_collected.append("noah_done")
    hide screen tablet_ui

    jump interrogation_choice

# 추리 단계
label deduction_phase:
    $ current_phase = 2

    scene bg_lab_dark with fade

    j "이제 퍼즐의 조각들을 맞춰볼 시간입니다."
    j "죽음의 시각은 21시. 로봇 팔의 전원은 OFF. 하지만 누군가는 거짓말을 하고 있다."

    call screen evidence_review

    j "데이터 다이브를 시작합니다."

    # 모순 찾기 게임
    menu contradiction_1:
        "첫 번째 모순을 찾아보자."

        "유지민의 증언과 오디오 로그":
            j "유지민은 21시에 강박사의 목소리를 들었다고 했습니다."
            j "하지만 오디오 센서는 그 시간 음성 데이터 0바이트를 기록했습니다."
            $ investigation_points += 2
            jump contradiction_2

        "한기태의 알리바이":
            j "한기태는 거실에서 술을 마시고 있었다고 합니다. 하지만 이것만으로는 부족합니다."
            jump contradiction_1

        "AI의 시스템 로그":
            j "노아의 로그는 정확해 보입니다. 다른 모순을 찾아야 합니다."
            jump contradiction_1

label contradiction_2:
    menu contradiction_choice_2:
        "두 번째 모순을 찾아보자."

        "스마트워치 심박수 데이터":
            if smartwatch_data in evidence_collected:
                j "강박사의 스마트워치 데이터를 확인했습니다."
                j "20:55에 심박수가 급격히 상승했습니다. 45에서 120으로."
                j "유지민이 나간 건 20:50. 그럼 누가 강박사를 위협했을까요?"
                $ investigation_points += 2
                jump final_deduction
            else:
                j "아직 중요한 증거가 부족합니다."
                jump contradiction_2

        "퇴근 모드 시스템":
            j "퇴근 모드... 이것이 핵심일까요? 더 생각해봅시다."
            jump contradiction_2

label final_deduction:
    scene bg_lab_bright with flash

    j "이제 모든 것이 명확해졌습니다."

    show yujimin shocked at center with dissolve

    j "유지민 씨. 당신이 범인입니다."

    y "뭐라고요?! 말도 안 돼요! 저는 8시 50분에 나갔어요!"

    j "맞습니다. 하지만 나가기 전에 당신은 함정을 설치했습니다."
    j "강박사의 넥타이를 로봇 팔의 관절 틈에 끼워둔 것입니다."

    y "그... 그건..."

    j "21시 퇴근 모드가 실행되면, 로봇 팔은 초기화 자세로 이동합니다."
    j "전원이 켜져서 공격한 게 아닙니다. 전원이 꺼지면서 중력에 의해 팔이 떨어진 겁니다."
    j "그 무게만으로도 목에 걸린 넥타이가 조여질 수 있습니다."

    y "아니에요! 저는 정말 모른다구요!"

    j "당신은 시스템의 허점을 이용했습니다. '종료' 프로세스는 '공격' 로그에 남지 않습니다."
    j "하지만 한 가지 계산 실수가 있었습니다."

    show screen evidence_final

    j "강박사는 당신이 함정을 설치하는 걸 눈치챘습니다."
    j "20:55, 심박수 급상승. 죽음에 대한 공포가 아니라 배신에 대한 분노였습니다."

    y "!!!"

    j "그리고 21시. 당신이 만든 기계적 운명이 실행되었습니다."
    j "완벽한 계획이었지만... 데이터는 모든 것을 기억하고 있었습니다."

    hide yujimin with dissolve

    scene black with fade

    "사건은 해결되었다."
    "하지만 진에게는 찜찜함이 남았다."
    "기계는 명령받은 대로 작동했을 뿐이다."
    "살인을 저지른 것은 인간의 계산된 악의였다."

    "데이터는 거짓말을 하지 않는다."
    "거짓말을 하는 것은 언제나 인간이다."

    centered "END"

    return

# 화면 정의들
screen tablet_ui():
    frame:
        xalign 0.95
        yalign 0.05
        xsize 200
        ysize 100

        vbox:
            text "NOAH System" size 16 color "#d4af37"
            text "Status: ONLINE" size 12 color "#00ff00"

screen evidence_review():
    frame:
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 400

        vbox:
            text "수집한 증거" size 24 xalign 0.5
            null height 20

            for evidence in evidence_collected:
                if isinstance(evidence, str):
                    text "• [evidence]" size 16
                else:
                    text "• [evidence.name]" size 16

            null height 30
            textbutton "닫기" action Return()

screen evidence_final():
    frame:
        xalign 0.5
        yalign 0.8
        xsize 500
        ysize 100

        text "스마트워치 생체 데이터: 20:55 심박수 급상승" size 14 xalign 0.5

    timer 3.0 action Hide("evidence_final")