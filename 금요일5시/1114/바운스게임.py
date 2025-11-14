import time
import turtle

# 1. 화면설정
screen=turtle.Screen()
screen.title("터틀 플랫포모 어드벤처")
screen.setup(width=800,height=600)
screen.bgcolor("skyblue")

# (필수) 화면 애니이션을 끈다(수동 업데이트 모드)
screen.tracer(0)

# 게임 주요코드 작성할 예정
# 2. 플레이어 생성
player=turtle.Turtle()
player.shape("circle")
player.color("navy")
player.penup()
player.goto(-250,250)

player.dx=0 # x방향 속도 (좌우 이동)
player.dy=0 # y방향 속도 (중력, 점프)

is_moving_left = False
is_moving_right = False

gravity=-0.01 # 중력 값

power=10
# 3. 키보드 조작 함수 정의
#define->def
def start_move_left():
    global is_moving_left
    is_moving_left = True

def stop_move_left():
    global is_moving_left
    is_moving_left = False

def start_move_right():
    global is_moving_right
    is_moving_right = True

def stop_move_right():
    global is_moving_right
    is_moving_right = False

# (점프 함수는 그대로 onkeypress 사용 - 점프는 '순간' 동작이므로)
def jump():
    # (4교시 내용: 바닥 또는 발판 위에서만 점프)
    if player.ycor() == -250: # (간단한 예시, 실제로는 4교시 코드)
        player.dy = 2


# 4. 키보드 연결
screen.listen() #키보드 입력을 받도록 설정
screen.listen()
screen.onkeypress(start_move_left, "a")
screen.onkeyrelease(stop_move_left, "a") # 'a'키를 뗐을 때

screen.onkeypress(start_move_right, "d")
screen.onkeyrelease(stop_move_right, "d") # 'd'키를 뗐을 때

screen.onkeypress(jump, "w") # 'w'키는 눌렀을 때만


# 메인게임 루프
while True:
    # 6. (수정) 플레이어 x방향 속도 결정
    if is_moving_left:
        player.dx = -0.3 # 왼쪽 키가 눌려있으면 속도를 -0.3
    elif is_moving_right:
        player.dx = 0.3 # 오른쪽 키가 눌려있으면 속도를 +0.3
    else:
        # (중요) 아무 키도 안 눌렸을 때만 마찰력 적용!
        player.dx = player.dx * 0.9

    # 플레이어 위치 업데이트(물리적용)
    player.setx(player.xcor()+player.dx)
    # 마찰력 적용(서서히 멈추도록)
    player.dx= player.dx * 0.9

    # 중력적용(y속도에 중력값을 계속 더해줘라)
    player.dy = player.dy+gravity
    player.sety(player.ycor()+player.dy)

    # 공의 y좌표가 -250보다 작아질수 없다.
    # 바닥(-250 임시수치) 착지 처리
    # player.ycor() : 공의 현재 y축 의 수치
    if player.ycor() < -250:
        player.sety(-250)
        player.dy=0

    screen.update()
    time.sleep(0.002)