import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(10)


for i in range(6):      # 5번 반복
    t.forward(100)      # 100만큼 이동
    t.right(360 / 6)    # 오각형의 외각인 72도씩 회전

turtle.done()