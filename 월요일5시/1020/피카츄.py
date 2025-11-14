import turtle
import random

# 화면 설정
screen = turtle.Screen()
screen.register_shape("1020/pokemon.gif")  # 피카츄 이미지 등록
screen.title("코딩크루 코딩수업")

# 피카츄 캐릭터 생성
pokemon = turtle.Turtle()
pokemon.shape("1020/pokemon.gif")  # 피카츄 이미지를 모양으로 설정

# 텍스트 출력용 터틀 생성
text_turtle = turtle.Turtle()
text_turtle.hideturtle()  # 터틀 모양 숨기기 (화살표 안 보이게)
text_turtle.penup()  # 펜을 들어서 이동할 때 선이 안 그려지게

# 전기 그리기용 터틀 생성
electric_turtle = turtle.Turtle()
electric_turtle.hideturtle()  # 터틀 모양 숨기기
electric_turtle.speed(0)  # 가장 빠른 속도로 설정
electric_turtle.pensize(3)  # 선 두께를 3으로 설정
electric_turtle.color("yellow")  # 전기 색상을 노란색으로

def draw_electric_line(start_x, start_y, end_x, end_y):
    """
    지그재그 전기 모양 그리기
    
    Parameters:
    start_x, start_y: 전기가 시작되는 좌표 (피카츄 위치)
    end_x, end_y: 전기가 끝나는 좌표 (목표 지점)
    """
    # 시작 위치로 이동 (선 안 그리면서)
    electric_turtle.penup()
    electric_turtle.goto(start_x, start_y)
    electric_turtle.pendown()  # 펜 내려서 이제부터 선 그리기
    
    # 시작점에서 끝점까지의 거리를 15개의 구간으로 나누기
    segments = 15  # 전기 번개의 지그재그 개수
    
    for i in range(segments):
        # 현재 진행률 계산 (0.0 ~ 1.0)
        progress = i / segments
        
        # 시작점에서 끝점 사이의 중간 지점 계산
        x = start_x + (end_x - start_x) * progress
        y = start_y + (end_y - start_y) * progress
        
        # 랜덤하게 좌우상하로 흔들림 추가 (지그재그 효과)
        # -15 ~ +15 픽셀 범위에서 랜덤하게 이동
        x += random.randint(-15, 15)
        y += random.randint(-15, 15)
        
        # 계산된 위치로 선 그으면서 이동
        electric_turtle.goto(x, y)
    
    # 마지막은 정확히 끝점으로 이동
    electric_turtle.goto(end_x, end_y)

def attack():
    """
    스페이스바를 누르면 실행되는 백만볼트 공격 함수
    """
    # 이전에 그려진 텍스트와 전기 모두 지우기
    text_turtle.clear()
    electric_turtle.clear()
    
    # "백만볼트!" 텍스트를 화면 위쪽(y=150)에 표시
    text_turtle.goto(0, 150)  # 화면 중앙 위쪽으로 이동
    text_turtle.write("진우 천만볼트!", align="center", 
                     font=("맑은 고딕", 30, "bold"))
    # align="center": 텍스트를 중앙 정렬
    # font: (폰트이름, 크기, 스타일)
    
    # 피카츄의 현재 x, y 좌표 가져오기
    pika_x, pika_y = pokemon.pos()
    
    # 좌상단 방향으로 전기 2줄 그리기
    # 첫 번째 줄: 왼쪽으로 150, 위로 150 이동
    draw_electric_line(pika_x, pika_y, pika_x - 150, pika_y + 150)
    # 두 번째 줄: 왼쪽으로 200, 위로 100 이동
    draw_electric_line(pika_x, pika_y, pika_x - 200, pika_y + 100)
    
    # 우상단 방향으로 전기 2줄 그리기
    # 첫 번째 줄: 오른쪽으로 150, 위로 150 이동
    draw_electric_line(pika_x, pika_y, pika_x + 150, pika_y + 150)
    # 두 번째 줄: 오른쪽으로 200, 위로 100 이동
    draw_electric_line(pika_x, pika_y, pika_x + 200, pika_y + 100)

# 키보드 이벤트 연결
# 스페이스바("space")를 누르면 attack 함수 실행
screen.onkey(attack, "space")
screen.listen()  # 키보드 입력을 받을 수 있게 활성화

# 프로그램이 종료되지 않고 계속 실행되도록 유지
turtle.done()