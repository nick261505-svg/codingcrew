import random
import time
import turtle

스크린=turtle.Screen()
스크린.setup(width=800, height=600)
스크린.title("코딩크루의 거북이")
스크린.tracer(0)

거북이색상=["red","blue","orange","purple","green"]
#함수:한자
def 거북이만들기():
    거북이=turtle.Turtle()
    거북이.shape("turtle")
    거북이.shapesize(2,2)
    거북이.color(random.choice(거북이색상))
    거북이.penup()
    거북이.setx(random.randint(-350,350))
    스크린.update()
    
for _ in range(25):
    거북이만들기()
    time.sleep(2)




turtle.done()