import time
import turtle

# 게임 설정 변수
running=True
force=20

# 화면설정
screen=turtle.Screen()
screen.setup(width=800, height=600)
screen.title("제현이가 처음만드는 게임")
screen.tracer(0)
screen.listen() 

# 공 생성
ball=turtle.Turtle()
ball.shape("circle")
ball.shapesize(2,2)
ball.dy = force

# 함수
def start_bounce():
    #현재y좌표 + 20
    y=ball.ycor() + ball.dy
    ball.sety(y)
    ball.dy = ball.dy - 1

#메인 게임 루프(계속 반복)
while running:
    screen.update()
    start_bounce()
    time.sleep(0.02)

turtle.done()