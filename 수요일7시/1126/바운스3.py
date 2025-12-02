import time
import turtle

# --- 1. 게임 설정 및 물리 변수 ---
floor = -270
running = True
force = 22          # 점프 힘
gravity = 1         # 중력
move_speed = 8      # 좌우 이동 속도
friction = 0.95     # 마찰력

current_level = 1   # 현재 라운드

screen = turtle.Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.title("Jump Game - Level 1")
screen.listen()

# --- 2. 레벨 데이터 ---
LEVEL_DATA = [
    # Level 1: 기본 계단
    ( [(-300, -200), (-150, -150), (0, -100), (150, -50)], (350, 0) ),
    # Level 2: 간격 넓음
    ( [(-350, -200), (-150, -180), (50, -160), (250, -140)], (350, -50) ),
    # Level 3: V자형
    ( [(-300, -50), (-150, -150), (0, -250), (150, -150), (300, -50)], (350, 50) ),
    # Level 4: 산 넘기
    ( [(-300, -200), (-100, 0), (0, 100), (100, 0), (300, -200)], (350, -200) ),
    # Level 5: 징검다리
    ( [(-350, -200), (-100, -150), (150, -100)], (350, 0) ),
    # Level 6: 고공 비행
    ( [(-350, 100), (-150, 100), (50, 100), (250, 100)], (380, 150) ),
    # Level 7: 지그재그
    ( [(-300, -250), (-200, -100), (-100, -250), (0, -100), (100, -250), (200, -100)], (350, 0) ),
    # Level 8: 멀리 뛰기
    ( [(-350, -100), (-50, -100), (250, -100)], (380, -50) ),
    # Level 9: 바늘 구멍
    ( [(-300, -250), (-100, -150), (100, -50), (200, 50), (100, 150)], (0, 250) ),
    # Level 10: 최악의 난이도
    #( [(-350, -200), (-200, 50), (0, -200), (200, 50)], (380, -100) )
    ( [(-350, -200), (-200, 50), (0, -200), (250, 20)], (380, -150) )
]

# --- 3. 객체 생성 ---
ball = turtle.Turtle()
ball.shape("circle")
ball.shapesize(2, 2)
ball.color("blue")
ball.penup()

goal = turtle.Turtle()
goal.shape("square")
goal.color("red")
goal.shapesize(stretch_wid=1, stretch_len=3)
goal.penup()

panels = [] 

# --- 4. 스테이지 세팅 함수 ---
def set_stage(level_num):
    global panels, running
    
    if level_num > len(LEVEL_DATA):
        screen.title("ALL CLEAR !!!")
        ball.hideturtle()
        goal.hideturtle()
        for p in panels: p.hideturtle()
        panels.clear()
        msg = turtle.Turtle()
        msg.hideturtle()
        msg.color("black")
        msg.write("축하합니다!\n모든 단계를 클리어했습니다!\n손가락 마스터 등극!!!", align="center", font=("Malgun Gothic", 24, "bold"))
        
        return

    screen.title(f"Jump Game - Level {level_num} / 10")

    for p in panels:
        p.hideturtle()
    panels.clear()
    
    stage_data = LEVEL_DATA[level_num - 1]
    panel_coords = stage_data[0]
    goal_coord = stage_data[1]
    
    goal.goto(goal_coord)
    
    for pos in panel_coords:
        p = turtle.Turtle()
        p.shape("square")
        p.color("green")
        p.shapesize(stretch_wid=1, stretch_len=5)
        p.penup()
        p.goto(pos)
        panels.append(p)
    
    # 공 위치 초기화
    if panels:
        ball.showturtle()
        ball.goto(panels[0].xcor(), panels[0].ycor() + 40)
        ball.dy = 0
        ball.dx = 0

set_stage(current_level)

# --- 5. 게임 로직 ---
def start():
    global current_level
    
    if current_level > len(LEVEL_DATA):
        return

    # 1. 수직 이동
    ball.dy -= gravity
    # 낙하 속도 제한 (최대 속도 제한)
    # 공이 너무 빨라지면(-20 이상) 강제로 -15로 고정합니다.
    # 이렇게 하면 감지 범위를 건너뛰지 않습니다.
    if ball.dy < -15: 
        ball.dy = -15
    ball.sety(ball.ycor() + ball.dy)

    # [핵심 수정 부분] 바닥 충돌 시 레벨 1로 초기화
    if ball.ycor() < floor:
        #print("바닥에 닿았습니다! 처음부터 다시 시작합니다.") # 디버깅용 메시지
        #current_level = 1     # 레벨을 무조건 1로 변경
        set_stage(current_level) # 1단계 스테이지 다시 그리기

    # 패널 충돌 체크 (순서 상관없이 밟기만 하면 됨)
    if ball.dy < 0:
        for p in panels:
            if (p.xcor() - 60 < ball.xcor() < p.xcor() + 60):
                if p.ycor() + 20 < ball.ycor() < p.ycor() + 40:
                    ball.sety(p.ycor() + 30)
                    ball.dy = force
    
    elif ball.dy > 0:
        for p in panels:
            if (p.xcor() - 60 < ball.xcor() < p.xcor() + 60):
                if p.ycor() - 40 < ball.ycor() < p.ycor() - 20:
                    ball.sety(p.ycor() - 35)
                    ball.dy = -5

    # 2. 목표 충돌 체크
    if ball.distance(goal) < 40:
        current_level += 1
        set_stage(current_level)

    # 3. 수평 이동
    ball.dx *= friction
    if abs(ball.dx) < 0.1: ball.dx = 0
    
    x = ball.xcor() + ball.dx

    # 오른쪽 벽 충돌
    if x > 380: 
        x = 380
        ball.dx *= -1  # [추가] 이동 방향 반대로 (튕기기)
        
    # 왼쪽 벽 충돌
    if x < -380: 
        x = -380
        ball.dx *= -1  # [추가] 이동 방향 반대로 (튕기기)

    ball.setx(x)

def move_left():
    ball.dx = -move_speed

def move_right():
    ball.dx = move_speed

screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

while running:
    start()
    screen.update()
    time.sleep(0.02)

turtle.done()