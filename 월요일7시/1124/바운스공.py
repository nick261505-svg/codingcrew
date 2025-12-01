import time
import turtle
s=turtle.Screen()
s.listen()
s.tracer(0)

#변수
gravity = 1 #중력 값
force = 30 #바닥에서 위로 올라가는 초기 힘 
floor = -250
SIZE=2#constant(상수)

#공만들기
ball=turtle.Turtle()
ball.shape("circle")
ball.shapesize(SIZE,SIZE)
ball.color("red")
ball.penup()
ball.setposition(0,floor)
ball.dy=force

def bounce_start():
    y = ball.ycor() + ball.dy
    
    ball.dy = ball.dy - gravity

    #바닥감지
    if ball.ycor() <= floor:
        ball.sety(floor)
        ball.dy=force

    x=ball.xcor()
    ball.goto(x,y)

running=True
while running:
    bounce_start()
    s.update()
    time.sleep(0.02)

turtle.done()