import time
import turtle

running = True
floor = -270
force = 30  # 공을 위로 올리는 힘
gravity = 1 # 중력
move_speed = 8 #좌우 이동
friction = 0.95 #마찰력

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("바운스공")
screen.tracer(0)
screen.listen()#키보드 이벤트 감지 활성화


ball = turtle.Turtle()
ball.shape("circle")
ball.shapesize(2, 2)
ball.penup()
ball.color("blue")
ball.setposition(0, floor)
ball.dy = force
ball.dx = 0


# 함수
def play():
    # 1. 수직이동
    # 위쪽
    ball.dy -= gravity #중력적용
    y = ball.ycor() + ball.dy
   
    if y < floor:
        y = floor
        ball.dy = force

    # 2. 좌우이동(화살표키보드)
    ball.dx *= friction
    x = ball.xcor() + ball.dx
    if x < -378:
        x = -378
        ball.dx *= -1
    
    if x > 372:
        x = 372
        ball.dx *= -1

    # 3. 공 이동
    ball.goto(x, y)

def move_left():
    ball.dx = -move_speed

def move_right():
    ball.dx = move_speed
#키보드 이벤트 등록
screen.onkeypress(move_left,"Left")
screen.onkeypress(move_right,"Right")

while running:
    play()
    screen.update()
    time.sleep(0.02)

turtle.done()
