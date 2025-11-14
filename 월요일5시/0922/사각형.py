import turtle
import math

# 거북이 객체 생성
t = turtle.Turtle()

t.shape("turtle") # 커서 모양을 거북이로 변경
t.speed(1)      # 거북이 속도 (1이 가장 느림)
radius = 360 / (2 * math.pi) # 약 57.3

# 3. 원의 상단 꼭짓점 (0, 반지름)으로 이동
t.goto(0, radius)
# 사각형 그리기 시작
# 반복문작성 재선이 잘해요, 진우도 잘해요
for _ in range(360): #0부터 4전까지
    t.forward(1) # 100만큼 앞으로 이동
    t.right(360/360)    # 오른쪽으로 90도 회전


# 그림이 완성된 후 창을 닫지 않고 유지
turtle.done()