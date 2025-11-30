import pygame
import sys

# 1. Pygame 초기화 (각 모듈 포함)
pygame.init()
pygame.mixer.init()
pygame.font.init()

# 2. 게임창 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Brick Breaker Game")

# 3. 게임 루프를 위한 시계 설정
clock = pygame.time.Clock()

# --- 폰트 정의 ---
score_font = pygame.font.Font(None, 36)
game_state_font = pygame.font.Font(None, 72)

# --- 색상 정의 ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BRICK_COLOR = (0, 200, 0)

'''
# --- 사운드 로드 ---
try:
    bounce_sound = pygame.mixer.Sound("bounce.wav") # 튕기는 소리
    break_sound = pygame.mixer.Sound("break.wav")   # 벽돌 깨지는 소리
except pygame.error:
    print("사운드 파일을 불러올 수 없습니다. (bounce.wav, break.wav)")
    bounce_sound = None
    break_sound = None
'''

# --- 패들(Paddle) 정의 ---
paddle_width = 100
paddle_height = 20
paddle_rect = pygame.Rect(screen_width // 2 - paddle_width // 2, screen_height - paddle_height - 10, paddle_width, paddle_height)
paddle_speed = 10

# --- 공(Ball) 정의 ---
ball_radius = 12
# ball_rect는 'ready' 상태에서 위치가 정해지므로 여기서는 (0,0)으로 초기화해도 무방합니다.
ball_rect = pygame.Rect(0, 0, ball_radius * 2, ball_radius * 2) 
ball_speed_x = 7
ball_speed_y = -7

# --- 벽돌(Bricks) 정의 ---
bricks = []
brick_rows = 5
brick_cols = 10
brick_width = 75
brick_height = 20
brick_padding = 5

for row in range(brick_rows):
    for col in range(brick_cols):
        brick_x = col * (brick_width + brick_padding) + (screen_width - (brick_cols * (brick_width + brick_padding))) // 2 + brick_padding // 2
        brick_y = row * (brick_height + brick_padding) + 50
        brick_rect = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
        bricks.append(brick_rect)

# --- 게임 변수 정의 ---
score = 0
lives = 3
game_state = "ready" # "ready", "playing", "game_over", "win"
running = True

# --- 메인 게임 루프 ---
while running:
    
    # 1. 이벤트 처리 (모든 상태에서 공통)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # [준비] 상태일 때 스페이스바를 누르면 [플레이] 상태로 변경
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_state == "ready":
                game_state = "playing"

    # 2. 화면 배경 채우기 (모든 상태에서 공통)
    screen.fill(BLACK)

    # --- 3. 게임 상태별 로직 및 그리기 ---

    # 3-1. [준비] 또는 [플레이] 상태 (패들 이동은 공통)
    if game_state == "ready" or game_state == "playing":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle_rect.x -= paddle_speed
        if keys[pygame.K_RIGHT]:
            paddle_rect.x += paddle_speed

        # 패들 화면 밖으로 나가지 않도록 제한
        if paddle_rect.left < 0:
            paddle_rect.left = 0
        if paddle_rect.right > screen_width:
            paddle_rect.right = screen_width

    # 3-2. [준비] 상태 로직
    if game_state == "ready":
        # 공을 패들 중앙 위에 고정
        ball_rect.centerx = paddle_rect.centerx
        ball_rect.bottom = paddle_rect.top

    # 3-3. [플레이] 상태 로직
    elif game_state == "playing":
        # 공 이동
        ball_rect.x += ball_speed_x
        ball_rect.y += ball_speed_y

        # 벽 충돌 감지 (좌/우)
        if ball_rect.left <= 0 or ball_rect.right >= screen_width:
            ball_speed_x *= -1
            #if bounce_sound: bounce_sound.play()
        # 벽 충돌 감지 (위)
        if ball_rect.top <= 0:
            ball_speed_y *= -1
            #if bounce_sound: bounce_sound.play()

        # 벽돌 충돌 감지
        for brick in bricks[:]: # 리스트 복사본 순회
            if ball_rect.colliderect(brick):
                bricks.remove(brick)
                ball_speed_y *= -1
                score += 10
                #if break_sound: break_sound.play()
                break # 한 프레임에 하나의 벽돌만 깨기

        # 승리 조건 (벽돌이 다 없어졌는지)
        if not bricks:
            game_state = "win"

        # 패들 충돌 감지
        if ball_rect.colliderect(paddle_rect):
            # (간단한 버전: 그냥 튕기기)
            ball_speed_y *= -1
            # (선택 사항) 패들 안에 갇히는 것을 방지
            ball_rect.bottom = paddle_rect.top 
            #if bounce_sound: bounce_sound.play()

        # 바닥 충돌 (생명 감소)
        if ball_rect.bottom >= screen_height:
            lives -= 1
            if lives > 0:
                # [준비] 상태로 되돌리기
                game_state = "ready"
                # 패들 위치 중앙으로 (공은 'ready' 로직이 알아서 붙여줌)
                paddle_rect.x = screen_width // 2 - paddle_width // 2
                pygame.time.wait(500) # 0.5초 대기
            else:
                game_state = "game_over" # 생명이 0이면 게임 오버

    # 3-4. 그리기 ([준비] 또는 [플레이] 상태)
    if game_state == "ready" or game_state == "playing":
        # 벽돌 그리기
        for brick in bricks:
            pygame.draw.rect(screen, BRICK_COLOR, brick)
        # 패들 그리기
        pygame.draw.rect(screen, BLUE, paddle_rect)
        # 공 그리기
        pygame.draw.circle(screen, WHITE, ball_rect.center, ball_radius)

        # (디버깅용) 공의 히트박스(ball_rect) 외각선 그리기
        RED = (255, 0, 0)
        pygame.draw.rect(screen, RED, ball_rect, 1) # 1픽셀 두께의 빨간색 사각형을 그림

        # 점수 표시
        score_text = score_font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        # 생명 표시
        lives_text = score_font.render(f"Lives: {lives}", True, WHITE)
        screen.blit(lives_text, (screen_width - lives_text.get_width() - 10, 10))

    # 3-5. [승리] 상태 그리기
    elif game_state == "win":
        win_text = game_state_font.render("YOU WIN!", True, GREEN)
        text_rect = win_text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(win_text, text_rect)
        
        # 마지막 점수 표시
        score_text_final = score_font.render(f"Score: {score}", True, WHITE)
        score_rect = score_text_final.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
        screen.blit(score_text_final, score_rect)

    # 3-6. [게임 오버] 상태 그리기
    elif game_state == "game_over":
        game_over_text = game_state_font.render("GAME OVER", True, RED)
        text_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(game_over_text, text_rect)

        # 마지막 점수 표시
        score_text_final = score_font.render(f"Score: {score}", True, WHITE)
        score_rect = score_text_final.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
        screen.blit(score_text_final, score_rect)

    # 4. 화면 업데이트 (모든 상태에서 공통)
    pygame.display.flip()

    # 5. 초당 프레임 수(FPS) 설정 (모든 상태에서 공통)
    clock.tick(60)

# --- 게임 종료 ---
pygame.quit()
sys.exit()