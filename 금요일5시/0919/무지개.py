import turtle

t = turtle.Turtle()
colors = ["red", "orange", "yellow", "green", "gold", "purple"]

t.speed(0) # 0이 가장 빠른 속도
t.width(3) # 펜 두께 설정
#turtle.bgcolor("black") # 배경색을 검은색으로 변경

for i in range(180):
    t.pencolor(colors[i % len(colors)]) # 펜 색상을 리스트에서 순환하며 선택
    t.right(2)
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)

t.hideturtle() # 작업 완료 후 거북이 숨기기
turtle.done()