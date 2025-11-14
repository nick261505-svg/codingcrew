import turtle

# 거북이 객체 생성
t = turtle.Turtle()

t.shape("turtle") # 커서 모양을 거북이로 변경
t.speed(10)      # 거북이 속도 (1이 가장 느림)
#0,1~10 

# 사각형 그리기 시작
    

#시작(0)~끝(4)전까지
for 숫자 in range(50):
    t.forward(10) 
    t.right(360/50)


# 그림이 완성된 후 창을 닫지 않고 유지
turtle.done()