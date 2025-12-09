import time
import turtle
#모듈

#변수
floor = -270
is_play = True
force = 30
gravity = 1


screen = turtle.Screen()
screen.setup(width=800,height=600)
screen.title("코딩크루의 점프게임")
screen.tracer(0)#그래픽 업데이트 안함

ball = turtle.Turtle()
ball.shape("circle")
ball.shapesize(2,2)
ball.color("pink")
ball.penup()
#y축으로 이동
ball.sety(floor)
ball.dy = force
ball.dx = 0

#함수 정의(생성)
def play():
    #좌우이동
    x= ball.xcor()

    #상하이동
    y= ball.ycor() + ball.dy
    ball.dy = ball.dy - gravity

    #공이 바닥 보다 내려가면
    if y < floor:
        y = floor#바닥에 멈춰
        #공에다 힘
        ball.dy = force


    # 공이동
    ball.goto(x,y)

#반복문(Loop)
while is_play:
    #그래픽 업데이트
    screen.update()
    play()
    time.sleep(0.02)

turtle.done()