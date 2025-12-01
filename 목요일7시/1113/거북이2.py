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

#####################################
# 적 관련 변수 및 함수
# 적들을 생성후 담을 리스트
enemies=[]#brackets
# 적 내려오는 속도
enemy_speed=1
colors=["red","blue","orange","green","yellow"]
# 적생성 함수
def 적생성():
    # 확률(1/50)로 적생성
    if random.randint(1,50) == 1:
        enemy = turtle.Turtle()
        enemy.shape("turtle")
        enemy.color(random.choice(colors))
        enemy.penup()
        enemy.setheading(270)

        x_pos=random.randint(-380,380)
        enemy.setposition(x_pos, 300)
        enemies.append(enemy)
#적이동 함수        
def 적이동():
    for enemy in enemies[:]:
        y = enemy.ycor() - enemy_speed
        enemy.sety(y)
        enemy.left(45)

        # 화면 바닥에 닿으면 삭제
        if y < -300:
            enemy.hideturtle()
            enemies.remove(enemy)
###################################
# 총알 적 충돌처리
def 충돌체크():
    #점수처리는 나중에
    #모든 총알 과 모든 적을 비교:
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            #두 물체 사이의 거리가 20미만이면 충돌로 간주
            if bullet.distance(enemy) < 20:

                #1. 적 제거
                enemy.hideturtle()
                if enemy in enemies: 
                    enemies.remove(enemy)

                #2. 총알 제거
                bullet.hideturtle()
                if bullet in bullets: 
                    bullets.remove(bullet)

                #3. 점수 증가(나중에) 
                break


s.listen()
s.onkeypress(왼쪽이동,"Left")
s.onkeypress(오른쪽이동,"Right")
s.onkeypress(총알생성,"space")

# 
while True:
    총알이동()
    적생성()
    적이동()
    충돌체크()
    s.update()
    time.sleep(0.02)#100f

turtle.done()