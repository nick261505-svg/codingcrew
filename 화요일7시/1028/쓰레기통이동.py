import time
import turtle
import random

# 화면 설정
screen = turtle.Screen()
screen.title("쓰레기 분리수거 게임")
screen.bgcolor("skyblue")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.register_shape("1028/recycle.gif")

#쓰레기통 생성
통=turtle.Turtle()
통.shape("1028/recycle.gif")
통.penup()
통.sety(-300+60)


# 개발자 만든 함수
# define : 정의하다 ->만들었다로 해석하자

쓰레기_리스트=[]
쓰레기_색상=["red","blue","orange","purple","brown"]

def 쓰레기_생성():
    쓰레기=turtle.Turtle()
    쓰레기.shape("circle")
    쓰레기.shapesize(1.5)
    쓰레기.color(random.choice(쓰레기_색상))
    쓰레기.penup()
    #random integer
    x = random.randint(-350,350)
    쓰레기.goto(x,300)
    쓰레기.speed=random.randint(2,5)
    #함수가 끝나면 함수안쪽에서 만든코드는 사라진다
    #쓰레기_리스트에 추가한다.
    쓰레기_리스트.append(쓰레기)


speed = 40
def 왼쪽이동():
    x = 통.xcor()#재활용통의 현재의 x좌표값 # x coordinate : x좌표 
    x = x - speed
    #쓰레기통이 화면밖으로 나가지 않게 하기위해서
    if x < -350:
        x = -350
    통.setx(x)

def 오른쪽이동():
    x = 통.xcor()#재활용통의 현재의 x좌표값 # x coordinate : x좌표 
    x = x + speed
    #쓰레기통이 화면밖으로 나가지 않게 하기위해서
    if x > 340:
        x = 340
    통.setx(x)

#함수는 호출하기전에는 실행되지 않음

# 키보드에서 왼쪽화살표를 누르면 왼쪽이동해

screen.listen()
screen.onkeypress(왼쪽이동,"Left")#키가 눌러진상태일떄
screen.onkeypress(오른쪽이동,"Right")#키가 눌러진상태일떄

게임실행=True
프레임=0

#충돌감지 함수
def 충돌감지(쓰레기, 통):
    #피타고라스의 정리
    #거리=((쓰레기.xcor()-통.xcor())**2 + (쓰레기.ycor()-통.ycor())**2)**0.5
    #절대값 : 음수를 양수바꿔줘요 abs(-10) == |-10|==> 10
    if abs(쓰레기.xcor()-통.xcor()) < 50 and  abs(쓰레기.ycor()-통.ycor()) < 50:
        return True
    else:
        return False

#반복해 게임실행True이면 계속반복해
while 게임실행:
    screen.update()
    프레임 = 프레임+1 # 프레임값을 1증가해
    # 만약 조건이 True이면 들여쓰기실행
    #
    if 프레임 == 100:
        쓰레기_생성()
        프레임=0
    
    #쓰레기 낙하
    for 쓰레기 in 쓰레기_리스트[:]:
        y = 쓰레기.ycor()
        y = y - 쓰레기.speed
        쓰레기.sety(y)
        
        #충돌감지
        if 충돌감지(쓰레기,통):
            쓰레기.hideturtle()
            쓰레기_리스트.remove(쓰레기)
            #점수증가
            #점수표시

        #바닥에 떨어짐
        elif y < -300:
            쓰레기.hideturtle()
            쓰레기_리스트.remove(쓰레기)
        
        


    time.sleep(0.01)
    #screen.delay(100)# 10/1000==0.01초
#'''    



turtle.done()