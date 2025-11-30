import turtle
import winsound  # 윈도우 전용 소리 라이브러리
import time

# 1. 스크린 설정
screen = turtle.Screen()
screen.title("코딩크루 터틀 피아노 - '비행기'")
screen.bgcolor("black")
screen.setup(width=700, height=400)
screen.tracer(0)  # 애니메이션을 수동으로 제어

# 2. 음계 및 악보 설정
# '도레미파솔' 5개 건반만 사용
key_data = {
    'C': (-100, "white"),
    'D': (-50, "white"),
    'E': (0, "white"),
    'F': (50, "white"),
    'G': (100, "white"),
}

# 4옥타브 기준 주파수 (Hz)
notes_freq = {
    'C': 261,
    'D': 294,
    'E': 329,
    'F': 349,
    'G': 392,
    'R': 0,
}

# '비행기' 동요 악보 (음이름, 박자)
# '비행기' 동요 악보 (음이름, 박자)
# 미레도레 미미미~ 버전
song = [
    ('E', 2), ('D', 0.5), ('C', 0.5), ('D', 1), ('E', 1), ('E', 1), ('E', 1), ('R', 1),  # 미~레도레 미 미 미
    ('D', 1), ('D', 1), ('D', 1), ('R', 1), ('E', 1), ('G', 1), ('G', 1), ('R', 1),      # 레 레 레 / 미 솔 솔
    ('E', 2), ('D', 0.5), ('C', 0.5), ('D', 1), ('E', 1), ('E', 1), ('E', 1), ('R', 1),  # 미~레도레 미 미 미
    ('D', 1), ('D', 1), ('E', 1), ('D', 1), ('C', 2), ('R', 2),                          # 레 레 미 레 도~
]

# 한 박자 길이 (밀리초, ms)
beat_ms = 400

# 3. 건반 그리기
key_turtles = {}  # 각 건반의 터틀 객체를 저장할 딕셔너리

for note, (x_pos, color) in key_data.items():
    key = turtle.Turtle()
    key.shape("square")
    # 터틀의 기본 크기 20px을 기준으로 
    # 세로 6배(120px), 가로 2배(40px)로 정사각형을 변형
    key.shapesize(stretch_wid=6, stretch_len=2) 
    key.color(color)
    key.penup()
    key.goto(x_pos, 0)
    
    # 건반에 음이름 표시
    key.goto(x_pos, -80) # 건반 아래쪽으로 이동
    key.color("white")
    key.write(note, align="center", font=("Arial", 16, "normal"))
    key.goto(x_pos, 0) # 원래 위치로 복귀
    key.color(color)   # 원래 색상으로 복귀
    
    key_turtles[note] = key

# 제목 표시
title_turtle = turtle.Turtle()
title_turtle.hideturtle()
title_turtle.color("white")
title_turtle.penup()
title_turtle.goto(0, 150)
title_turtle.write("스페이스바를 눌러 연주를 시작하세요", align="center", font=("Arial", 20, "bold"))

screen.update()  # 건반과 제목을 화면에 그림

# 4. 키 누름/뗌 함수
"""건반을 누른 것처럼 색상을 변경합니다."""
def press_key(note):
    if note in key_turtles:
        key_turtles[note].color("gray")  # 누른 키는 회색으로

"""건반을 뗀 것처럼 색상을 원래대로 복원합니다."""
def release_key(note):
    if note in key_turtles:
        key_turtles[note].color(key_data[note][1]) # 원래 색(흰색)으로

# 5. 연주 시작
def play_song():
    title_turtle.clear()
    title_turtle.write("♪ 연주 중...", align="center", font=("Arial", 24, "bold"))
    screen.update()

    for note, duration in song:
        if note == 'R':  # 'R'은 쉼표(Rest)
            time.sleep(beat_ms * duration / 1000)
            continue

        if note in key_turtles:
            freq = notes_freq[note]      # 주파수
            dur = int(beat_ms * duration) # 소리 길이 (ms)
            
            # 1. 건반 누름 (시각)
            press_key(note)
            screen.update()  # 화면 즉시 업데이트
            
            # 2. 소리 재생 (청각)
            # winsound.Beep은 해당 시간(dur)만큼 프로그램 실행을 멈추고 소리를 재생
            winsound.Beep(freq, dur) 
            
            # 3. 건반 뗌 (시각)
            release_key(note)
            screen.update()  # 화면 즉시 업데이트

    #연주가 끝나면 안내글씨 표현
    title_turtle.clear()
    title_turtle.write("스페이스바를 눌러 연주를 시작하세요", align="center", font=("Arial", 20, "bold"))
    screen.update()

#키보드 이벤트 설정    
screen.listen()
screen.onkeypress(play_song, "space")

turtle.done()