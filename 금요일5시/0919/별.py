import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(10)

for i in range(360):      # 5번 반복
    t.forward(200)      # 200만큼 길게 이동
    t.right(181)        # 144도 회전 (360/5 * 2)

turtle.done()