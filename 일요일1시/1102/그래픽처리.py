import random
import time
import turtle

s=turtle.Screen()
s.setup(width=800, height=800)
s.register_shape("1102/recycle.gif")
s.tracer(0)

player=turtle.Turtle()
player.shape("1102/recycle.gif")
player.penup()
player.sety(-340)

trashes=[]

def create_trash():
    trash=turtle.Turtle()
    trash.shape("turtle")
    trash.color("red")
    trash.penup()
    trash.shapesize(2,2)
    #x = -350 ~ 350 구간에서 생성
    xpos = random.randint(-350,350)
    trash.goto(xpos,350)
    trash.speed=random.uniform(2,5)

    trashes.append(trash)


s.update()





#좌우로 이동: 

#왼쪽화살표키에 반응하는 함수

speed=10
def move_left():
    #x=현재위치-speed
    x=player.xcor() - speed
    print(x)
    if x < -350:
        x = -350
    player.setx(x)
    

def move_right():
    #x=현재위치-speed
    x=player.xcor() + speed
    if x > 350:
        x = 350
    player.setx(x)
    
    #여기에 코드를 작성

#키보드 이벤트처리
#키보드를 누를때 함수가 트리거된다.
s.listen()
s.onkeypress(move_left,"Left")
s.onkeypress(move_right,"Right")
s.onkeypress(move_left,"a")
s.onkeypress(move_right,"d")


trash_spawn_timer=0
while True:
    s.update()
    #쓰레기(거북이) 생성
    trash_spawn_timer +=1
    print(trash_spawn_timer)
    if trash_spawn_timer > 60:
        create_trash()
        trash_spawn_timer=0

    #쓰레기 투하
    for trash in trashes[:]:
        trash.sety( trash.ycor() - trash.speed )

        if trash.ycor() < -400:
            trash.hideturtle()
            trashes.remove(trash)

    time.sleep(0.02)


turtle.done()

