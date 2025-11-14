import turtle
import random

# 화면 설정
screen = turtle.Screen()
screen.title("쓰레기 분리수거 게임")
screen.bgcolor("skyblue")
screen.setup(width=800, height=600)
screen.tracer(0)

# 이미지 등록
try:
    screen.register_shape("1021/recycle.gif")
    has_custom_shape = True
except:
    has_custom_shape = False
    print("recycle.gif 파일을 찾을 수 없습니다. 기본 도형을 사용합니다.")

# 바구니 캐릭터 생성
basket = turtle.Turtle()
if has_custom_shape:
    basket.shape("1021/recycle.gif")
else:
    basket.shape("square")
    basket.color("green")
    basket.shapesize(stretch_wid=2, stretch_len=3)
basket.penup()
basket.goto(0, -250)

# 쓰레기 객체 생성
trash = turtle.Turtle()
trash.shape("square")
trash.color("brown")
trash.shapesize(stretch_wid=1.5, stretch_len=1.5)
trash.penup()
trash.goto(random.randint(-350, 350), 300)
trash.speed(0)
rotation_angle = 0

# 중력 관련 변수
gravity = 0.0005  # 중력 가속도 (0.2 -> 0.05로 감소)
fall_speed = 0  # 현재 낙하 속도 (초기값 0)

# 쓰레기 대기 시간 관련 변수
wait_time = 200  # 프레임 단위 대기 시간 (약 0.9초로 증가)
wait_counter = 0  # 대기 카운터
is_falling = False  # 쓰레기가 떨어지는 중인지 여부

# 점수 표시
score = 0
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0, 260)
score_display.color("black")
score_display.write(f"점수: {score}", align="center", font=("Arial", 24, "bold"))

# 게임 오버 텍스트
game_over_display = turtle.Turtle()
game_over_display.hideturtle()
game_over_display.penup()

# 게임 상태
game_running = True
initial_trash_speed = 0  # 초기 속도를 0으로 변경 (중력으로 가속)

# 바구니 이동 함수
def move_left():
    x = basket.xcor()
    if x > -350:
        basket.setx(x - 30)

def move_right():
    x = basket.xcor()
    if x < 350:
        basket.setx(x + 30)

# 키보드 입력 설정
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")

# 충돌 감지 함수
def check_collision():
    distance = basket.distance(trash)
    return distance < 40

# 점수 업데이트 함수
def update_score():
    global score
    score_display.clear()
    score_display.write(f"점수: {score}", align="center", font=("Arial", 24, "bold"))

# 쓰레기 리셋 함수
def reset_trash():
    global rotation_angle, fall_speed, wait_counter, is_falling
    trash.goto(random.randint(-350, 350), 300)
    rotation_angle = 0
    trash.setheading(0)
    fall_speed = 0  # 낙하 속도 초기화
    wait_counter = 0  # 대기 카운터 초기화
    is_falling = False  # 대기 상태로 설정

# 쓰레기 떨어뜨리기 함수
def drop_trash():
    global fall_speed, rotation_angle, wait_counter, is_falling
    
    # 대기 시간 체크
    if not is_falling:
        wait_counter += 1
        # 대기 중에는 살짝 흔들리는 효과
        trash.sety(300 + 5 * (wait_counter % 10 - 5) * 0.1)
        
        if wait_counter >= wait_time:
            is_falling = True  # 대기 완료, 낙하 시작
        return  # 아직 대기 중이면 여기서 종료
    
    # 중력 적용: 낙하 속도가 점점 증가
    fall_speed += gravity
    
    # 최대 낙하 속도 제한 (너무 빨라지지 않도록)
    if fall_speed > 0.5:
        fall_speed = 0.5
    
    # 쓰레기 떨어뜨리기 (중력이 적용된 속도로)
    trash.sety(trash.ycor() - fall_speed)
    
    # 쓰레기 회전 효과 (속도에 비례하여 회전 속도도 증가)
    rotation_angle += 3 + (fall_speed * 0.2)  # 회전 속도 감소
    trash.setheading(rotation_angle)

# 게임 오버 함수
def game_over():
    global game_running
    game_running = False
    game_over_display.goto(0, 0)
    game_over_display.color("red")
    game_over_display.write("게임 오버!", align="center", font=("Arial", 36, "bold"))
    game_over_display.goto(0, -50)
    game_over_display.write(f"최종 점수: {score}", align="center", font=("Arial", 24, "normal"))

# 메인 게임 루프
while game_running:
    screen.update()
    
    # 쓰레기 떨어뜨리기 함수 호출
    drop_trash()
    
    # 충돌 감지 (쓰레기가 떨어지는 중일 때만)
    if is_falling and check_collision():
        score += 10
        update_score()
        reset_trash()
        '''
        # 난이도 증가 (중력 가속도 증가)
        if score % 50 == 0 and gravity < 0.15:  # 중력 최대값 제한
            gravity += 0.005  # 증가폭 감소 (0.05 -> 0.02)
        '''
    
    # 바닥에 닿으면 게임 오버 (쓰레기가 떨어지는 중일 때만)
    if is_falling and trash.ycor() < -280:
        game_over()
    
    # 게임 속도 조절
    screen.delay(10)

# 종료 대기
screen.exitonclick()