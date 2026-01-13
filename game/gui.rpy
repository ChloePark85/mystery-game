## GUI 설정 - SF 하드보일드 스타일

# 색상 테마
define gui.accent_color = '#00ff41'  # 매트릭스 그린
define gui.idle_color = '#888888'
define gui.idle_small_color = '#aaaaaa'
define gui.hover_color = '#00ff41'
define gui.selected_color = '#ffffff'
define gui.insensitive_color = '#8888887f'

define gui.muted_color = '#512d44'
define gui.hover_muted_color = '#7a4356'

define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'

# 폰트
define gui.text_font = "DejaVuSans.ttf"
define gui.name_text_font = "DejaVuSans.ttf"
define gui.interface_text_font = "DejaVuSans.ttf"

# 텍스트 크기
define gui.text_size = 22
define gui.name_text_size = 30
define gui.interface_text_size = 18
define gui.label_text_size = 24
define gui.notify_text_size = 16
define gui.title_text_size = 50

# 메인 메뉴
define gui.main_menu_background = "gui/main_menu.png"

# 게임 메뉴
define gui.game_menu_background = "gui/game_menu.png"

# 대화창
define gui.textbox_height = 185
define gui.textbox_yalign = 1.0

define gui.name_xpos = 240
define gui.name_ypos = 0

define gui.namebox_width = None
define gui.namebox_height = None

define gui.namebox_borders = Borders(5, 5, 5, 5)
define gui.namebox_tile = False

define gui.text_xpos = 268
define gui.text_ypos = 50
define gui.text_width = 744
define gui.text_xalign = 0.0

# 버튼
define gui.button_width = None
define gui.button_height = 36

define gui.button_borders = Borders(4, 4, 4, 4)
define gui.button_tile = False

define gui.button_text_font = gui.interface_text_font
define gui.button_text_size = gui.interface_text_size
define gui.button_text_xalign = 0.0

define gui.choice_button_width = 790
define gui.choice_button_height = None

define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(100, 5, 100, 5)

define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5

# 퀵 버튼
define gui.quick_button_borders = Borders(10, 4, 10, 0)
define gui.quick_button_text_size = 14
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

# 설정 화면
define gui.page_button_borders = Borders(10, 4, 10, 4)

define gui.slot_button_width = 276
define gui.slot_button_height = 206
define gui.slot_button_borders = Borders(10, 10, 10, 10)
define gui.slot_button_text_size = 14
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color

# 스타일 정의
style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5

style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")

style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"

# 커스텀 스타일 - 증거 화면
style evidence_frame is empty:
    background "#000000cc"
    padding (20, 20)

style evidence_text:
    color "#00ff41"
    font "DejaVuSans.ttf"
    size 18

# 타임라인 UI 스타일
style timeline_button:
    background "#333333"
    hover_background "#555555"
    selected_background "#00ff41"
    padding (10, 5)

style timeline_text:
    color "#ffffff"
    size 14
    text_align 0.5