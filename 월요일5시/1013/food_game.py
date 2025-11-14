import turtle
import random

#화면설정
screen=turtle.Screen()
screen.title("먹이 수집 게임 🍎🍎🍎")
screen.bgcolor("lightblue")
screen.setup(width=600, height=800)
screen.tracer(0)#기본값 1 자동업데이트 끄기

# 점수 변수
score=0
high_score=0
move_speed=20

#플레이어 터틀 생성
player=turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()
player.speed(0)
player.goto(0,0)

# 점수판 생성
score_display=turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0, 320)
score_display.color("black")
score_display.write(f"점수: {score}  최고점수: {high_score}", align="center", font=("Arial",16,"bold"))

# 좋은 먹이 리스트(초록색)
good_foods=[]
for _ in range(3):
    food = turtle.Turtle()
    food.shape("circle")
    food.color("green")
    food.penup()
    food.speed(0)
    x=random.randint(-280,280)
    y=random.randint(-280,300)
    food.goto(x,y)
    good_foods.append(food)

# 나쁜 먹이 리스트(빨간색)
bad_foods=[]
for _ in range(3):
    food = turtle.Turtle()
    food.shape("circle")
    food.color("red")
    food.penup()
    food.speed(0)
    x=random.randint(-280,280)
    y=random.randint(-300,300)
    food.goto(x,y)
    bad_foods.append(food)

# 이동시키는 함수들
def move_up():
    y = player.ycor()
    if y < 300:
        player.sety(y + move_speed)

def move_down():
    y = player.ycor()
    if y > -300:
        player.sety(y - move_speed)

def move_left():
    x = player.xcor()
    if x > -280:
        player.setx(x - move_speed)

def move_right():
    x = player.xcor()
    if x < 280:
        player.setx(x + move_speed)

# 키보드 바인딩
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# 점수 업데이트 함수
def update_score():
    global high_score
    if score > high_score:
        high_score=score
    score_display.clear()
    score_display.write(f"점수: {score}  최고점수: {high_score}", align="center", font=("Arial",16,"bold"))

# 충돌감지 함수(먹이를 먹었는지 감지)
def is_collision(t1,t2):
    distance=t1.distance(t2)
    return distance < 20

# 게임 설명 표시
instructions = turtle.Turtle()
instructions.hideturtle()
instructions.penup()
instructions.goto(0, -260)
instructions.color("darkblue")
instructions.write("방향키로 이동 | 초록색(+10점) | 빨간색(-5점)", align="center", font=("Arial", 12, "normal"))

# 메인 게임 루프
def game_loop():
    global score
    
    # 좋은 먹이와 충돌 체크
    for food in good_foods:
        if is_collision(player, food):
            # 새로운 위치로 이동
            x=random.randint(-280,280)
            y=random.randint(-300,300)
            food.goto(x, y)
            # 점수 증가
            score += 10
            update_score()
    
    # 나쁜 먹이와 충돌 체크
    for food in bad_foods:
        if is_collision(player, food):
            # 새로운 위치로 이동
            x=random.randint(-280,280)
            y=random.randint(-300,300)
            food.goto(x, y)
            # 점수 감소
            score -= 5
            if score < 0:
                score = 0
            update_score()
    
    # 화면 업데이트
    screen.update()
    
    # 게임 루프 계속 실행
    screen.ontimer(game_loop, 50)

# 게임 시작
game_loop()

# 화면 유지
screen.mainloop()