import time
import turtle

# 변수
floor = -270
running = True
force = 20
gravity = 1
move_speed = 5
friction = 0.9

current_level = 1

# 리스트 : [1,2,3]
# 튜플 : (1,2,3)
LEVEL_DATA=[
    # Level 1: LEVEL_DATA[0]
    ( 
        [(-300, -200), (-150, -150), (0, -100), (150, -50)],
        (350, 0) 
    ),
    # Level 2: LEVEL_DATA[1]
    ( 
        [(-300, -200), (-150, -150), (0, -100), (150, -50)],
        (350, 0) 
    ),
]
# LEVEL_DATA[0] -> 집합에서 첫번째 데이터
panels=[]

screen = turtle.Screen()
screen.tracer(0)  # 자동업데이트 금지
screen.setup(width=800, height=600)
screen.title("Jump Game - Level 1")
screen.listen()#키보드 감지기능 활성화


ball = turtle.Turtle()
ball.shape("circle")
ball.shapesize(2, 2)
ball.color("blue")
ball.penup()
# 이동
ball.sety(floor)
ball.dy = force
ball.dx = 0


goal = turtle.Turtle()
goal.shape("square")
goal.color("red")
goal.shapesize(stretch_wid=1, stretch_len=3)
goal.penup()

#스테이지를 그리는 함수
def set_stage(level_num):
    tot=len(LEVEL_DATA)
    screen.title(f"Jump Game - Level {level_num} / {tot}")

    for p in panels:
        p.hideturtle()
    panels.clear()

    # 현실에서는 1 -> 컴퓨터의 집합에서는 0
    stage_data=LEVEL_DATA[level_num-1]
    panel_coords=stage_data[0]#일반패널들
    goal_coord=stage_data[1]#마지막통과패널

    #골 패널 위치
    goal.goto(goal_coord)
    #나머지 패널들
    for coord in panel_coords:
        p = turtle.Turtle()
        p.shape("square")
        p.color("green")
        p.shapesize(stretch_wid=1, stretch_len=5)
        p.penup()
        p.goto(coord)
        panels.append(p)


set_stage(current_level)
#함수
def  start():
    
    #1. 수직이동(중력, 바닥 튕기기)
    y = ball.ycor() + ball.dy
    ball.dy -= gravity
    #바닥체크
    if ball.ycor() < floor:
        ball.sety(floor)
        ball.dy = force
    #ball.sety(y)

    #2. 수평이동
    x = ball.xcor() + ball.dx
    #dx감소해->마찰력 적용
    ball.dx = ball.dx * friction

    #오른쪽
    if x > 380: 
        x=380
        ball.dx = ball.dx * -1
    #왼쪽
    if x < -380: 
        x=-380
        ball.dx = ball.dx * -1
    #ball.setx(x)

    ball.goto(x, y)

def move_left():
    ball.dx = -move_speed

def move_right():
    ball.dx = move_speed

screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")





#반복문
while running:

    start()
    screen.update() #변경 되면 반영해줘
    time.sleep(0.02)

turtle.done()
