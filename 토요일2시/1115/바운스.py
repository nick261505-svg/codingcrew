import time
import turtle


gravity=1
force=30
horizontal_speed=5 #x축 이동속도
####################
screen=turtle.Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.listen()#이벤트 감시활성화

####################
#공 생성
ball=turtle.Turtle()
ball.shape("circle")
ball.shapesize(2,2)
ball.penup()
ball.sety(-270)#300-22=278, -270
ball.dy=force #y축으로 이동하는 거리(힘)
ball.dx=force

def start_bounce():
    xpos=ball.xcor()
    ypos=ball.ycor()+ball.dy
    ball.goto(xpos ,ypos)

    ball.dy=ball.dy-gravity#중력만큼 힘이 줄어듦
    #######################
    #일단 바닥위치 -270이라고하자
    #만약에 공이 바닥에 닿으면: 
    #   반대로 힘(팅기는힘)을부여하자
    if ball.ycor() <= -270:
        #위로 올라가게 해야함
        ball.dy=force


def move_right():
    xpos=ball.xcor() + ball.dx
    ypos=ball.ycor()
    ball.goto(xpos, ypos)

def move_left():
    xpos=ball.xcor() - ball.dx
    ypos=ball.ycor()
    ball.goto(xpos, ypos)


#오른쪽 활살표 키보드가 눌러지면 함수가 자동으로 호출됨
screen.onkeyrelease(move_right,"Right")
screen.onkeyrelease(move_left,"Left")

while True:
    screen.update()
    #함수호출->함수의 내용이 실행
    start_bounce()
    time.sleep(0.02)

turtle.done()