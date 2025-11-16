import random
import time
import turtle

score=0

s=turtle.Screen()
s.setup(width=800, height=800)
s.register_shape("1102/recycle.gif")
s.tracer(0)

player=turtle.Turtle()
player.shape("1102/recycle.gif")
player.penup()
player.sety(-340)

score_board=turtle.Turtle()
score_board.penup()
score_board.hideturtle()
score_board.sety(350)
score_board.write(f"점수 : {score}",align="center",font=("Arial",32,"bold"))


def update_score_board():
    score_board.clear()
    score_board.write(f"점수 : {score}",align="center",font=("Arial",32,"bold"))

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
    #print(x)
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

def is_collision(trash):
    #쓰레기의 x좌표가 통의 크기 안쪽에 있는가?
    tx=trash.xcor()
    px=player.xcor()
    #p_left=px-50
    #p_right=px+50
    #if p_left < tx and tx < p_right and trash.ycor()-player.ycor() <= 50:
    if abs(px-tx) <= 50 and trash.ycor()-player.ycor() <= 50:
        return True
    return False

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
    #print(trash_spawn_timer)
    if trash_spawn_timer > 60:
        create_trash()
        trash_spawn_timer=0

    #쓰레기 투하
    for trash in trashes[:]:
        trash.sety( trash.ycor() - trash.speed )
        #쓰레기통에 닿으면 
        if is_collision(trash):
            trash.hideturtle()
            trashes.remove(trash)
            #점수 누적
            score = score + 1
            print("점수: ",score)
            update_score_board()

        #바닥에 닿으면
        elif trash.ycor() < -400:
            trash.hideturtle()
            trashes.remove(trash)

    time.sleep(0.02)


turtle.done()

