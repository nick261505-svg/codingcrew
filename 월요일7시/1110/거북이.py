import turtle

s=turtle.Screen()
s.setup(width=800,height=600)
s.title("거북이 움직이기 게임")
s.listen()#리스너 #이벤트 #센서기능 활성화


t1=turtle.Turtle()
t1.shape('turtle')#메서드(클래스 멤버함수)
#t1.penup()
#t1.sety(100)
#t2=turtle.Turtle()
#t2.shape('turtle')
#함수의 정의: 함수를 생성하는것
#키워드 define(정의하다) ->def
#파이썬에 알려야한다(선언)
speed=10
def move_left():
    #거북이를 왼쪽 일정간격으로 이동해
    #현재거북이 x좌표-speed
    x=t1.xcor()-speed
    #만약에 x값이 -390 보다작아지면(-400되면) x=-390
    # 조건식 True일때 : 들여쓰기구간이 실행됨
    if x < -390:
        x = -390
        print("벽에닿았어")
    print(x)
    t1.setx(x)

def move_right():
    pass


s.onkeypress(move_left,"Left")
s.onkeypress(move_left,"a")
s.onkeypress(move_right,"Right")
s.onkeypress(move_right,"d")




turtle.done()


