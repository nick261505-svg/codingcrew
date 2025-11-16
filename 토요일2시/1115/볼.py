import time
import turtle

# ========== 게임 설정 변수 ==========
gravity = 1  # 중력 값 (프레임당 dy에서 빼지는 값)
force = 30  # 바닥에서 튕길 때 위로 올라가는 초기 힘
horizontal_speed = 8  # 좌우로 이동할 때의 수평 속도
ground_level = -270  # 바닥의 y좌표 위치

# ========== 화면 설정 ==========
screen = turtle.Screen()
screen.setup(width=800, height=600)  # 화면 크기 설정 (가로 800, 세로 600)
screen.tracer(0)  # 자동 화면 업데이트 끄기 (수동으로 update() 호출해야 함 - 부드러운 애니메이션 위해)
screen.listen()  # 키보드 이벤트 감지 활성화

# ========== 공 객체 생성 및 초기 설정 ==========
ball = turtle.Turtle()  # 거북이 객체 생성 (공으로 사용)
ball.shape("circle")  # 모양을 원으로 설정
ball.shapesize(2, 2)  # 크기를 2배로 확대 (가로, 세로)
ball.penup()  # 펜을 들어서 이동할 때 선이 그려지지 않게 함
ball.sety(ground_level)  # 공의 시작 위치를 바닥으로 설정
ball.dy = force  # y축 이동 속도 (양수면 위로, 음수면 아래로) - 처음에 위로 튕기게 설정
ball.dx = 0  # x축 이동 속도 (양수면 오른쪽, 음수면 왼쪽) - 처음에는 좌우 이동 없음

# ========== 키 입력 상태 추적 딕셔너리 ==========
# 키가 현재 눌려있는지 여부를 저장 (True: 눌림, False: 안 눌림)
keys = {"Right": False, "Left": False}

# ========== 키보드 이벤트 핸들러 함수들 ==========
def key_press_right():
    """오른쪽 화살표 키를 누를 때 호출"""
    keys["Right"] = True  # 오른쪽 키가 눌렸다고 표시

def key_press_left():
    """왼쪽 화살표 키를 누를 때 호출"""
    keys["Left"] = True  # 왼쪽 키가 눌렸다고 표시

def key_release_right():
    """오른쪽 화살표 키를 뗄 때 호출"""
    keys["Right"] = False  # 오른쪽 키가 떼졌다고 표시

def key_release_left():
    """왼쪽 화살표 키를 뺄 때 호출"""
    keys["Left"] = False  # 왼쪽 키가 떼졌다고 표시

# ========== 메인 게임 로직 함수 ==========
def start_bounce():
    """공의 위치를 업데이트하고 물리 법칙을 적용하는 함수"""
    
    # ----- Y축 이동 (수직 운동) -----
    ypos = ball.ycor() + ball.dy  # 현재 y좌표에 dy(수직 속도)를 더해서 새 위치 계산
    ball.sety(ypos)  # 공의 y좌표를 새 위치로 이동
    
    ball.dy = ball.dy - gravity  # 중력 적용: 매 프레임마다 dy에서 gravity를 빼서 아래로 떨어지게 함
    
    # ----- 바닥 충돌 감지 및 처리 -----
    if ball.ycor() <= ground_level:  # 공이 바닥에 닿거나 바닥보다 아래로 내려갔으면
        ball.sety(ground_level)  # 공을 정확히 바닥 위치로 설정 (바닥 아래로 빠지지 않게)
        ball.dy = force  # dy를 양수(force)로 설정해서 위로 튕기게 함
        
        # ----- 바닥에 닿는 순간에만 좌우 키 입력 확인 -----
        # 이 시점에 어떤 키가 눌려있는지 확인해서 수평 속도(dx)를 결정
        if keys["Right"]:  # 오른쪽 화살표가 눌려있으면
            ball.dx = horizontal_speed  # dx를 양수로 설정 (오른쪽으로 이동)
        elif keys["Left"]:  # 왼쪽 화살표가 눌려있으면
            ball.dx = -horizontal_speed  # dx를 음수로 설정 (왼쪽으로 이동)
        else:  # 아무 키도 안 눌려있으면
            ball.dx = 0  # dx를 0으로 설정 (좌우 이동 없음, 제자리에서 튕김)
    
    # ----- X축 이동 (수평 운동) -----
    # 공중에 있든 바닥에 있든, 설정된 dx 속도로 계속 이동 (포물선 운동)
    xpos = ball.xcor() + ball.dx  # 현재 x좌표에 dx(수평 속도)를 더해서 새 위치 계산
    
    # ----- 화면 경계 체크 (벽 충돌) - 튕기기 -----
    if xpos > 380:  # 오른쪽 벽을 넘어가려고 하면
        xpos = 380  # x좌표를 벽 위치로 고정
        ball.dx = -ball.dx  # 수평 속도를 반대 방향으로 바꿔서 튕기게 함 (오른쪽 → 왼쪽)
    elif xpos < -380:  # 왼쪽 벽을 넘어가려고 하면
        xpos = -380  # x좌표를 벽 위치로 고정
        ball.dx = -ball.dx  # 수평 속도를 반대 방향으로 바꿔서 튕기게 함 (왼쪽 → 오른쪽)
    
    ball.setx(xpos)  # 공의 x좌표를 새 위치로 이동

# ========== 키보드 이벤트 등록 ==========
# onkeypress: 키를 누르는 순간 함수 호출
screen.onkeypress(key_press_right, "Right")  # 오른쪽 화살표 누르면 key_press_right 실행
screen.onkeypress(key_press_left, "Left")  # 왼쪽 화살표 누르면 key_press_left 실행

# onkeyrelease: 키를 떼는 순간 함수 호출
screen.onkeyrelease(key_release_right, "Right")  # 오른쪽 화살표 떼면 key_release_right 실행
screen.onkeyrelease(key_release_left, "Left")  # 왼쪽 화살표 떼면 key_release_left 실행

# ========== 메인 게임 루프 ==========
while True:  # 무한 반복
    screen.update()  # 화면을 업데이트해서 변경사항을 실제로 보여줌
    start_bounce()  # 공의 위치 업데이트 및 물리 법칙 적용
    time.sleep(0.02)  # 0.02초 대기 (약 50 FPS) - 애니메이션 속도 조절

turtle.done()  # 프로그램이 종료되지 않고 창이 열려있게 유지