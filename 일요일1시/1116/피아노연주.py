import turtle
import winsound
import time

# 1. 스크린 설정
screen = turtle.Screen()
screen.title("코딩크루 터틀 피아노")
screen.bgcolor("black")
screen.setup(width=700, height=400)
screen.tracer(0)

# 2. 음계 및 악보 설정
key_data = {
    'C': (-100, "white"),
    'D': (-50, "white"),
    'E': (0, "white"),
    'F': (50, "white"),
    'G': (100, "white"),
}

notes_freq = {
    'C': 261,
    'D': 294,
    'E': 329,
    'F': 349,
    'G': 392,
}

# 여러 동요 악보 모음
songs = {
    '1': {
        'title': '떴다 떴다 비행기',
        'notes': [
            ('E', 1), ('D', 1), ('C', 1), ('D', 1), ('E', 1), ('E', 1), ('E', 2), ('R', 0.5),
            ('D', 1), ('D', 1), ('D', 2), ('E', 1), ('G', 1), ('G', 2), ('R', 0.5),
            ('E', 1), ('D', 1), ('C', 1), ('D', 1), ('E', 1), ('E', 1), ('E', 2), ('R', 0.5),
            ('D', 1), ('D', 1), ('E', 1), ('D', 1), ('C', 2),
        ]
    },
    '2': {
        'title': '학교종',
        'notes': [
            ('G', 1), ('G', 1), ('G', 1), ('G', 1), ('E', 1), ('G', 1), ('E', 2), ('R', 0.5),
            ('E', 1), ('D', 1), ('E', 1), ('F', 1), ('D', 2), ('R', 1),
            ('G', 1), ('G', 1), ('G', 1), ('G', 1), ('E', 1), ('G', 1), ('E', 2), ('R', 0.5),
            ('E', 1), ('D', 1), ('E', 1), ('D', 1), ('C', 2),
        ]
    },
    '3': {
        'title': '작은별',
        'notes': [
            ('C', 1), ('C', 1), ('G', 1), ('G', 1), ('E', 1), ('E', 1), ('G', 2), ('R', 0.5),
            ('F', 1), ('F', 1), ('E', 1), ('E', 1), ('D', 1), ('D', 1), ('C', 2), ('R', 0.5),
            ('G', 1), ('G', 1), ('F', 1), ('F', 1), ('E', 1), ('E', 1), ('D', 2), ('R', 0.5),
            ('G', 1), ('G', 1), ('F', 1), ('F', 1), ('E', 1), ('E', 1), ('D', 2),
        ]
    },
    '4': {
        'title': '곰 세 마리',
        'notes': [
            ('C', 1), ('C', 1), ('C', 1), ('C', 1), ('C', 1), ('E', 1), ('G', 2), ('R', 0.5),
            ('E', 1), ('E', 1), ('E', 1), ('E', 1), ('E', 1), ('G', 1), ('C', 2), ('R', 0.5),
            ('G', 1), ('G', 1), ('G', 1), ('G', 1), ('G', 1), ('E', 1), ('C', 2), ('R', 0.5),
            ('G', 1), ('E', 1), ('C', 1), ('G', 1), ('E', 1), ('C', 1),
        ]
    }
}

beat_ms = 400

# 선택된 곡 저장
selected_song = None

# 3. 메뉴 화면 그리기
def draw_menu():
    menu_turtle = turtle.Turtle()
    menu_turtle.hideturtle()
    menu_turtle.color("white")
    menu_turtle.penup()
    
    menu_turtle.goto(0, 100)
    menu_turtle.write("♪ 터틀 피아노 동요 선택 ♪", align="center", font=("Arial", 28, "bold"))
    
    y = 40
    for key, song_info in songs.items():
        menu_turtle.goto(0, y)
        menu_turtle.write(f"{key}. {song_info['title']}", align="center", font=("Arial", 18, "normal"))
        y -= 40
    
    menu_turtle.goto(0, y - 20)
    menu_turtle.write("숫자 키를 눌러주세요", align="center", font=("Arial", 14, "italic"))
    
    screen.update()

# 4. 키 선택 함수
def select_song(key):
    global selected_song
    if key in songs:
        selected_song = key
        screen.clear()
        screen.bgcolor("black")
        play_selected_song()

# 5. 건반 그리기
def draw_keys():
    key_turtles = {}
    for note, (x_pos, color) in key_data.items():
        key = turtle.Turtle()
        key.shape("square")
        key.shapesize(stretch_wid=6, stretch_len=2)
        key.color(color)
        key.penup()
        key.goto(x_pos, 0)
        
        key.goto(x_pos, -80)
        key.color("white")
        key.write(note, align="center", font=("Arial", 16, "normal"))
        key.goto(x_pos, 0)
        key.color(color)
        
        key_turtles[note] = key
    return key_turtles

# 6. 키 누름/뗌 함수
def press_key(note, key_turtles):
    if note in key_turtles:
        key_turtles[note].color("gray")

def release_key(note, key_turtles):
    if note in key_turtles:
        key_turtles[note].color(key_data[note][1])

# 7. 선택된 곡 연주
def play_selected_song():
    if selected_song is None:
        return
    
    song_info = songs[selected_song]
    
    # 건반 그리기
    key_turtles = draw_keys()
    
    # 제목 표시
    title_turtle = turtle.Turtle()
    title_turtle.hideturtle()
    title_turtle.color("white")
    title_turtle.penup()
    title_turtle.goto(0, 150)
    title_turtle.write(f"♪ {song_info['title']} ♪", align="center", font=("Arial", 24, "bold"))
    
    screen.update()
    time.sleep(1)
    
    # 연주 시작
    for note, duration in song_info['notes']:
        if note == 'R':
            time.sleep(beat_ms * duration / 1000)
            continue
        
        if note in key_turtles:
            freq = notes_freq[note]
            dur = int(beat_ms * duration)
            
            press_key(note, key_turtles)
            screen.update()
            
            winsound.Beep(freq, dur)
            
            release_key(note, key_turtles)
            screen.update()
    
    # 연주 종료 후 메뉴로 돌아가기
    time.sleep(2)
    screen.clear()
    screen.bgcolor("black")
    draw_menu()

# 8. 메뉴 표시 및 키 이벤트 등록
draw_menu()

screen.onkey(lambda: select_song('1'), '1')
screen.onkey(lambda: select_song('2'), '2')
screen.onkey(lambda: select_song('3'), '3')
screen.onkey(lambda: select_song('4'), '4')
screen.listen()

screen.mainloop()