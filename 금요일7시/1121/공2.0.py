import time
import turtle

MOVE=15
WIDTH=800
HEIGHT=600
SIDE_POS=WIDTH//2 #800나누기2 한 몫 
FLOOR=-200
gravity=20

screen=turtle.Screen()
screen.setup(width=WIDTH,height=HEIGHT)
screen.title("바운스")
screen.tracer(0)
screen.listen()


#########################
floor=turtle.Turtle()
floor.penup()
floor.setposition(-SIDE_POS,FLOOR)
floor.pendown()
floor.setx(SIDE_POS)
floor.hideturtle()

ball=turtle.Turtle()
ball.shape("circle")
ball.shapesize(2,2)
ball.penup()
ball.sety(FLOOR)
ball.dy=gravity
ball.dx=0 #가로방향(x축) 속도 변수

game_running=True

def start_bounce(): #함수이름(): 괄호콜론
    #indent 4칸들여쓰기 구간이 함수의 영역
    ##########################
    #1. 세로(y출) 움직임
    y=ball.ycor()+ball.dy
    ball.sety(y)
    ball.dy=ball.dy-1

    #계속 - 가 되므로  if 제한을
    if ball.dy < -gravity:
        ball.dy = gravity
    
    
    
def game_over():
    global game_running
    turtle.Turtle().write("GAME OVER",
                          align="center",font=("Arial",32,"bold"))
    game_running=False

def move_left():
    if ball.ycor() < FLOOR+50:
        ball.dx = -MOVE

def move_Right():
    if ball.ycor() < FLOOR+50:
        ball.dx = MOVE

def movement():
    #위치이동
    ball.setx(ball.xcor() + ball.dx)
    #반복문이 돌아가므로 계속이동하지 않게 하기위해 마찰계수 적용
    #수학적으로는 영원히 0이 되지않지만, 컴퓨터에서는 결국 0이된다
    #숫자는 메모리공간에 한정되어있다.(64비트,1byte==8bit)
    #언더플로우:숫자가 너무 작아져서 컴퓨터가 표현할 수 있는 가장
    #작은 소숫점 단위보다 더 작아지면 강제로0.0으로 만든다
    ball.dx = ball.dx * 0.9
    #왼쪽 화면밖으로 나가지 않게처리
    if ball.xcor() < -SIDE_POS:
        ball.setx(-SIDE_POS)#위치보정 -400 -399 -409 -401 -411 
        ball.dx *= -1
    #오른쪽 화면밖으로 나가지 않게처리
    if ball.xcor() > SIDE_POS:
        ball.setx(SIDE_POS)#위치보정
        ball.dx *= -1
    
    ##선택사항 
    if abs(ball.dx) < 0.1:
        ball.dx=0


#########################
screen.onkey(game_over,"x")
screen.onkey(move_left,"Left")
screen.onkey(move_Right,"Right")

##########################
while game_running:
    screen.update()
    start_bounce()
    movement()
    time.sleep(0.02)
    
turtle.done()