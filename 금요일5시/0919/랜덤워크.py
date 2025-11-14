import turtle
import random

t = turtle.Turtle()
t.shape("turtle")
t.speed(0)
t.width(5)

directions = [0, 90, 180, 270] # 동, 북, 서, 남 방향

for _ in range(200):
    # 랜덤 색상 설정
    r = random.random() # 0.0 ~ 1.0 사이의 랜덤 실수
    g = random.random()
    b = random.random()
    t.pencolor(r, g, b)

    # 랜덤 방향과 거리 설정
    t.setheading(random.choice(directions))
    t.forward(20)

turtle.done()