import pygame
import sys
import random

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 게임 제목
pygame.display.set_caption("과일 받기 게임")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
SKY_BLUE = (135, 206, 235)
GREEN = (0, 255, 0)

# 폰트 설정
font_large = pygame.font.Font(None, 70)
font_medium = pygame.font.Font(None, 50)
font_small = pygame.font.Font(None, 35)

# 시계 설정
clock = pygame.time.Clock()

# 바구니 설정
basket_width = 120
basket_height = 30
basket_x = screen_width // 2 - basket_width // 2
basket_y = screen_height - 100
basket_speed = 8

# 과일 리스트 (여러 개의 과일)
fruits = []
fruit_radius = 20

# 게임 변수
score = 0
missed = 0
game_over = False
level = 1  # 레벨 시스템
base_fruit_speed = 4

# 과일 생성 함수
def create_fruit():
    fruit_colors = [RED, YELLOW, ORANGE, GREEN]
    fruit = {
        'x': random.randint(fruit_radius, screen_width - fruit_radius),
        'y': -fruit_radius,
        'speed': base_fruit_speed + (level - 1) * 0.5,  # 레벨에 따라 속도 증가
        'color': random.choice(fruit_colors)
    }
    return fruit

# 초기 과일 생성
fruits.append(create_fruit())

# 충돌 감지 함수
def check_collision(fruit_x, fruit_y, basket_x, basket_y):
    if fruit_y + fruit_radius >= basket_y:
        if basket_x <= fruit_x <= basket_x + basket_width:
            return True
    return False

# 배경 별 그리기 (장식용)
stars = []
for i in range(30):
    star_x = random.randint(0, screen_width)
    star_y = random.randint(0, screen_height)
    stars.append((star_x, star_y))

# 게임 시작 시간
start_ticks = pygame.time.get_ticks()

# 게임 루프
running = True
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_over:
                # 게임 재시작
                score = 0
                missed = 0
                game_over = False
                level = 1
                fruits = [create_fruit()]
                start_ticks = pygame.time.get_ticks()
    
    # 게임 오버가 아닐 때만 게임 진행
    if not game_over:
        # 키보드 입력 확인
        keys = pygame.key.get_pressed()
        
        # 바구니 이동 (A, D 키도 추가)
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            basket_x -= basket_speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            basket_x += basket_speed
        
        # 바구니 화면 밖으로 나가지 않도록
        if basket_x < 0:
            basket_x = 0
        if basket_x > screen_width - basket_width:
            basket_x = screen_width - basket_width
        
        # 레벨업 시스템 (점수 10점마다)
        new_level = (score // 10) + 1
        if new_level > level:
            level = new_level
        
        # 레벨에 따라 과일 개수 증가
        if len(fruits) < level and len(fruits) < 5:
            fruits.append(create_fruit())
        
        # 모든 과일 이동 및 충돌 체크
        for fruit in fruits[:]:  # 복사본으로 순회
            fruit['y'] += fruit['speed']
            
            # 충돌 감지
            if check_collision(fruit['x'], fruit['y'], basket_x, basket_y):
                score += 1
                fruits.remove(fruit)
                fruits.append(create_fruit())
            
            # 과일이 화면 아래로 떨어지면
            elif fruit['y'] > screen_height:
                missed += 1
                fruits.remove(fruit)
                fruits.append(create_fruit())
                
                # 5번 놓치면 게임 오버
                if missed >= 5:
                    game_over = True
    
    # 화면을 하늘색으로 채우기
    screen.fill(SKY_BLUE)
    
    # 배경 별 그리기
    for star in stars:
        pygame.draw.circle(screen, WHITE, star, 2)
    
    # 바구니 그리기 (입체감 추가)
    pygame.draw.rect(screen, BROWN, (basket_x, basket_y, basket_width, basket_height))
    pygame.draw.rect(screen, BLACK, (basket_x, basket_y, basket_width, basket_height), 3)
    
    # 모든 과일 그리기
    for fruit in fruits:
        pygame.draw.circle(screen, fruit['color'], (fruit['x'], int(fruit['y'])), fruit_radius)
        pygame.draw.circle(screen, BLACK, (fruit['x'], int(fruit['y'])), fruit_radius, 2)
    
    # 점수 표시
    score_text = font_medium.render(f'Score: {score}', True, BLACK)
    screen.blit(score_text, (10, 10))
    
    # 레벨 표시
    level_text = font_small.render(f'Level: {level}', True, BLACK)
    screen.blit(level_text, (10, 60))
    
    # 놓친 개수 표시
    missed_text = font_small.render(f'Missed: {missed}/5', True, RED if missed >= 3 else BLACK)
    screen.blit(missed_text, (10, 95))
    
    # 게임 시간 표시
    if not game_over:
        seconds = (pygame.time.get_ticks() - start_ticks) // 1000
        time_text = font_small.render(f'Time: {seconds}s', True, BLACK)
        screen.blit(time_text, (screen_width - 150, 10))
    
    # 게임 오버 메시지
    if game_over:
        # 반투명 배경
        overlay = pygame.Surface((screen_width, screen_height))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))
        
        game_over_text = font_large.render('GAME OVER!', True, RED)
        final_score_text = font_medium.render(f'Final Score: {score}', True, WHITE)
        restart_text = font_small.render('Press SPACE to restart', True, WHITE)
        
        screen.blit(game_over_text, (screen_width // 2 - 200, screen_height // 2 - 100))
        screen.blit(final_score_text, (screen_width // 2 - 150, screen_height // 2 - 20))
        screen.blit(restart_text, (screen_width // 2 - 170, screen_height // 2 + 40))
    
    # 화면 업데이트
    pygame.display.flip()
    
    # FPS 설정
    clock.tick(60)

# 게임 종료
pygame.quit()
sys.exit()