import time
import turtle

# 변수
floor = -270
running = True
force = 25       # 튀어 오르는 힘 (조금 줄였습니다)
gravity = 1      # 중력
move_speed = 8   # 좌우 이동 초기 속도 (마찰로 줄어드니 조금 키웠습니다)
friction = 0.95  # 마찰력 (1보다 작아야 함, 작을수록 빨리 멈춤)

screen = turtle.Screen()
screen.tracer(0)  # 자동업데이트 금지
screen.setup(width=800, height=600)
screen.listen()   # 키보드 감지기능 활성화

ball = turtle.Turtle()
ball.shape("circle")
ball.shapesize(2, 2)
ball.color("blue")
ball.penup()

# 초기 위치 및 속도 설정
ball.sety(floor)
ball.dy = force
ball.dx = 0

# 함수
def start():
    # 1. 수직이동 (중력, 바닥 튕기기)
    # 현재 위치에서 속도만큼 이동
    ball.sety(ball.ycor() + ball.dy)
    
    # 중력 적용
    ball.dy -= gravity

    # 바닥 체크
    if ball.ycor() < floor:
        ball.sety(floor)
        # 바닥에 닿을 때 튀어오르는 힘 (탄성 계수를 적용하면 더 자연스러움)
        ball.dy = force 

    # 2. 수평이동 (마찰력 적용)
    # 마찰력을 적용하여 속도를 자연스럽게 줄임
    ball.dx *= friction 
    
    # 속도가 너무 작아지면 완전히 0으로 만듦 (떨림 방지)
    if abs(ball.dx) < 0.1:
        ball.dx = 0

    x = ball.xcor() + ball.dx

    # 벽 충돌 체크 (화면 밖으로 나가지 않게)
    if x > 372: 
        x = 372
        ball.dx *= -1 # 벽에 부딪히면 튕기기 (선택사항)
    if x < -378: 
        x = -378
        ball.dx *= -1 # 벽에 부딪히면 튕기기 (선택사항)
    
    ball.setx(x)

def move_left():
    ball.dx = -move_speed

def move_right():
    ball.dx = move_speed

# 키 이벤트 설정
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# 반복문
while running:
    start()
    screen.update() # 변경 되면 반영해줘
    time.sleep(0.02)

turtle.done()