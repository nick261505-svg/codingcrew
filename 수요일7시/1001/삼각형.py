import turtle
import math

t1=turtle.Turtle()
t1.color("red")
t1.shape("turtle")

t2=turtle.Turtle()
t2.color("blue")
t2.shape("circle")

r=200
#s=r*루트3
s=r*math.sqrt(3)
t1.penup()
t1.goto(0,r)
t1.right(60)
t1.pendown()

for _ in range(3):
    t1.forward(s)
    t1.right(120)


turtle.done()
