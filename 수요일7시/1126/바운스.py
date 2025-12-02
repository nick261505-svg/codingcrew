import time
import turtle

# 변수
floor = -270
running = True
force = 30
gravity = 1
move_speed = 5

screen = turtle.Screen()
screen.tracer(0)  # 자동업데이트 금지
screen.setup(width=800, height=600)
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
    if x > 380: x=380
    if x < -380: x=-380
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
