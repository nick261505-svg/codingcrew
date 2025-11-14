import time
import turtle

screen=turtle.Screen()
screen.setup(width=800,height=600)
screen.title("바운스")
screen.tracer(0)
screen.listen()


gravity=20
#########################
ball=turtle.Turtle()
ball.shape("circle")
ball.shapesize(2,2)
ball.penup()
ball.sety(-200)
ball.dy=gravity

game_running=True

def start_bounce(): #함수이름(): 괄호콜론
    #indent 4칸들여쓰기 구간이 함수의 영역
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

#########################
screen.onkey(game_over,"x")

##########################
while game_running:
    screen.update()
    start_bounce()
    time.sleep(0.01)
    
turtle.done()