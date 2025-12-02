import time
import turtle

시작=True
force=30 #위로 던지는 힘
gravity=1 #중력

s=turtle.Screen()
s.tracer(0)

ball=turtle.Turtle()
ball.shape("circle")
ball.shapesize(2,2)
ball.color("red")
ball.penup()
ball.sety(-250)
ball.dy=force

def start():
    y=ball.ycor()+ball.dy
    ball.sety(y)
    ball.dy=ball.dy-gravity
    if ball.ycor() < -250:
        ball.sety(-250)
        ball.dy=force

while 시작:
    start()
    s.update()
    time.sleep(0.02)

turtle.done()