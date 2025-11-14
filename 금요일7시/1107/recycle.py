import random
import time
import turtle

#화면설정
screen=turtle.Screen()
screen.title("재활용쓰레기수집")
screen.setup(width=800, height=600)
screen.register_shape("1107/recycle.gif")
screen.tracer(0)#변경사항 적용하지마(그림이 안그려짐)

#쓰레기통생서
통=turtle.Turtle()
통.shape("1107/recycle.gif")
통.penup()

통.sety(-240)
y=통.ycor()
print(y)

#쓰레기 리스트
trashes=[]

#쓰레기 생성함수
def create_trash():
    trash=turtle.Turtle()
    trash.shape("turtle")
    trash.color("red")
    trash.penup()
    trash.shapesize(1.5,1.5)
    xpos=random.randint(-350,350)
    trash.goto(xpos, 280)
    trash.speed=random.uniform(2,5)
    #생성한 쓰레기 리스트에 저장
    trashes.append(trash)

speed=30
#왼쪽이동 함수
def move_left():
    x=통.xcor()
    if x > -350: #화면 밖으로 나가지 않도록
        통.setx(x-speed)
    

#오른쪽이동 함수
def move_right():
    x=통.xcor()
    if x < 350: #화면 밖으로 나가지 않도록
        통.setx(x+speed)

#충돌 감지 함수
def check_collision(trash):
    trash_x=trash.xcor()
    trash_y=trash.ycor()
    통_x=통.xcor()
    통_y=통.ycor()

    if abs(trash_x-통_x)<50 and abs(trash_y - 통_y)<50:
        return True
    return False


screen.listen()
screen.onkeypress(move_left,"Left")
screen.onkeypress(move_right,"Right")

#쓰레기 생성 타이머
trash_spawn_timer=0

while True:
    screen.update()

    # 일정시간마다 쓰레기 생성
    trash_spawn_timer += 1
    if trash_spawn_timer > 60: #1초마다 생성
        create_trash()
        trash_spawn_timer=0
    
    
    score=0
    # 쓰레기 이동 및 충돌 (복사복으로 반복)
    for trash in trashes[:]:
        trash.sety(trash.ycor() - trash.speed)

        if check_collision(trash):
            trash.hideturtle()
            trashes.remove(trash)
            #점수처리-다음주에
            score += 10
            print("점수: ",score)

        elif trash.ycor() < -300:
            trash.hideturtle()
            trashes.remove(trash)


    time.sleep(0.02)


screen.update()
turtle.done()