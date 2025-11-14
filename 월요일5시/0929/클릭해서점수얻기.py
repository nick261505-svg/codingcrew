import turtle
import random

화면=turtle.Screen()
화면.title("클릭해서 점수 얻기!:제작자(진우와재선)")
turtle.bgcolor("skyblue")

먹북이=turtle.Turtle()#윌슨,홍땡땡
먹북이.shape("turtle")
먹북이.color("orange")
먹북이.shapesize(2)
먹북이.penup()

#점수 변수
score=0

#점수판 생성
점수판=turtle.Turtle()
점수판.penup()
점수판.hideturtle()
점수판.goto(0,260)
점수판.write(f"점수: {score}",align="center",font=("Arial",24,"normal"))

#거북이를 클릭하면 점수가 올라가요
#거북이를 클릭했을때 코드가 실행되는 함수
def 점수올려(x,y):
    global score 
    #score값을 1증가   
    score += 1 
    점수판.clear()
    점수판.write(f"점수: {score}",align="center",font=("Arial",24,"normal"))

    #거북이 위치 이동
    newx=random.randint(-300,300)
    newy=random.randint(-300,300)
    먹북이.goto(newx, newy)

먹북이.onclick(점수올려)

turtle.done()