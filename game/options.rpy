## 0의 집행 (Execution of Zero) - Ren'Py 설정 파일

define config.name = _("0의 집행")
define gui.show_name = True

define config.version = "1.0"

define gui.about = _p("""
SF 하드보일드 데이터 추리 게임

스마트 맨션에서 벌어진 의문의 사고사.
AI와 로그 데이터를 통해 진실을 밝혀내세요.
""")

define build.name = "execution_of_zero"

define config.has_sound = True
define config.has_music = True
define config.has_voice = False

define config.enter_transition = dissolve
define config.exit_transition = dissolve

define config.intra_transition = dissolve

define config.after_load_transition = None

define config.end_game_transition = None

define config.window = "auto"

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

default preferences.text_cps = 0

default preferences.afm_time = 15

define config.save_directory = "execution_of_zero-1584543946"

define config.window_icon = "gui/window_icon.png"

init python:
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    build.documentation('*.html')
    build.documentation('*.txt')