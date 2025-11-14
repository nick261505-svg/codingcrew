import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(2)
length=200

for i in range(3):      # 5번 반복
    t.forward(length)      # 200만큼 길게 이동
    t.left(120)        # 144도 회전 (360/5 * 2)

t.penup()
t.forward(length/3)
t.right(60)
t.forward(length/3)
t.left(120)
# t.color("red")
t.pendown()

for i in range(3):      # 5번 반복
    t.forward(length)      # 200만큼 길게 이동
    t.left(120)

turtle.done()