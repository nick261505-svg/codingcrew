import turtle

# 거북이 객체 생성
t = turtle.Turtle()

t.shape("turtle") # 커서 모양을 거북이로 변경
t.speed(1)      # 거북이 속도 (1이 가장 느림): 1~10 0

# 사각형 그리기 시작
t.right(90)
t.forward(100)

t.left(90)
t.forward(60)

t.left(90)
t.forward(100)

t.left(180)
t.forward(50)

t.right(90)
t.forward(60)




# 그림이 완성된 후 창을 닫지 않고 유지
turtle.done()