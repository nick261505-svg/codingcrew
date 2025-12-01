import random
import time
import turtle
s=turtle.Screen()
s.setup(width=800,height=600)
s.title("자기이름")
s.bgcolor("black")
s.register_shape("1113/alien100.png")
s.tracer(0)

c=turtle.Turtle()
c.shape("1113/alien100.png")
c.shapesize(2,2)
c.penup()
c.sety(-240)

speed=20


def 왼쪽이동():
    #현재x좌표
    x=c.xcor()-speed
    #x값이 -380을 넘어가면 화면밖으로 나감
    if x < -380:
        x=-380
    c.setx(x)
def 오른쪽이동():
    #현재x좌표
    x=c.xcor()+speed
    #x값이 -380을 넘어가면 화면밖으로 나감
    if x > 380:
        x=380
    c.setx(x)  

#리스트:다른언어의 배열
bullets=[]
bullet_speed=15

def 총알이동():
    #현재총알 위치+15
    for bullet in bullets[:]:
        ypos=bullet.ycor()+bullet_speed
        bullet.sety(ypos)
        if ypos>300:
            bullet.hideturtle()
            bullets.remove(bullet)

def 총알생성():
    bullet=turtle.Turtle()
    bullet.shape("circle")
    bullet.color("yellow")
    bullet.penup()
    bullet.setposition(c.xcor(), c.ycor())
    bullets.append(bullet)
##########################
# 적 생성
# [] : 리스트   
# 

enemies=[]

colors=["red","blue","yellow","white","orange"]


def 적생성():
    #지역변수(local variable)
    num=random.randint(0,10)
    if num!=0:
        return
    enemy = turtle.Turtle()
    enemy.shape("turtle")
    enemy.color(random.choice(colors))
    enemy.penup()
    enemy.setposition(random.randint(-380,380),300)
    enemy.dy=random.randint(2,4)
    #만들어진 적을 리스트 enemies[] 추가
    enemies.append(enemy)

def 적이동():
    for enemy in enemies[:]:
        y=enemy.ycor() - enemy.dy#변경될 y축값
        enemy.sety(y)#y축변경
        #제어문
        if y < -200:
            enemy.hideturtle()
            enemies.remove(enemy)




s.listen()
s.onkeypress(왼쪽이동,"Left")
s.onkeypress(오른쪽이동,"Right")
s.onkeypress(총알생성,"space")

# 
while True:
    총알이동()
    적생성()
    적이동()
    #충돌체크()
    s.update()
    time.sleep(0.02)#100f

turtle.done()