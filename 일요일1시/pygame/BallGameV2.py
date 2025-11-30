"""
벽돌 깨기 게임 (Brick Breaker)
- Pygame을 사용한 클래식 아케이드 게임
- 패들로 공을 튕겨서 모든 벽돌을 깨는 것이 목표
"""

import pygame
import sys

# ==================== 게임 설정 상수 ====================

# 화면 설정
SCREEN_WIDTH = 800      # 게임 화면 너비 (픽셀)
SCREEN_HEIGHT = 600     # 게임 화면 높이 (픽셀)
FPS = 60                # 초당 프레임 수 (Frame Per Second)

# 색상 정의 (RGB 형식)
BLACK = (0, 0, 0)           # 배경색
WHITE = (255, 255, 255)     # 공 색상
BLUE = (0, 0, 255)          # 패들 색상
RED = (255, 0, 0)           # 게임 오버 텍스트 및 히트박스 색상
GREEN = (0, 255, 0)         # 승리 텍스트 색상
BRICK_COLOR = (0, 200, 0)   # 벽돌 색상

# 패들(Paddle) 설정
PADDLE_WIDTH = 100      # 패들 너비
PADDLE_HEIGHT = 20      # 패들 높이
PADDLE_SPEED = 10       # 패들 이동 속도 (픽셀/프레임)

# 공(Ball) 설정
BALL_RADIUS = 12        # 공의 반지름
BALL_SPEED_X = 7        # 공의 수평 속도 (픽셀/프레임)
BALL_SPEED_Y = -7       # 공의 수직 속도 (음수 = 위쪽)

# 벽돌(Brick) 설정
BRICK_ROWS = 5          # 벽돌 행의 개수
BRICK_COLS = 10         # 벽돌 열의 개수
BRICK_WIDTH = 75        # 각 벽돌의 너비
BRICK_HEIGHT = 20       # 각 벽돌의 높이
BRICK_PADDING = 5       # 벽돌 사이의 간격

# 게임 규칙
STARTING_LIVES = 3      # 시작 시 생명 개수


# ==================== 게임 객체 클래스 ====================

class Paddle:
    """
    패들 클래스 - 플레이어가 조작하는 가로 막대
    
    공을 튕겨내어 게임을 진행시키는 핵심 오브젝트
    좌우 방향키로 이동 가능
    """
    
    def __init__(self, x, y):
        """
        패들 초기화
        
        Args:
            x: 패들의 초기 x 좌표
            y: 패들의 초기 y 좌표
        """
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = PADDLE_SPEED
    
    def move(self, keys):
        """
        키보드 입력에 따라 패들 이동
        
        Args:
            keys: pygame.key.get_pressed()로 얻은 키 상태
        """
        # 왼쪽 방향키: 패들을 왼쪽으로 이동
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        # 오른쪽 방향키: 패들을 오른쪽으로 이동
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        
        # 패들이 화면 밖으로 나가지 않도록 제한
        # clamp_ip: 사각형을 지정된 영역 안에 강제로 위치시킴 (in-place)
        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
    
    def draw(self, screen):
        """
        패들을 화면에 그리기
        
        Args:
            screen: 그릴 pygame 화면 객체
        """
        pygame.draw.rect(screen, BLUE, self.rect)
    
    def reset_position(self):
        """패들을 화면 중앙으로 재배치 (라운드 재시작 시 사용)"""
        self.rect.x = SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2


class Ball:
    """
    공 클래스 - 게임의 핵심 오브젝트
    
    벽, 패들, 벽돌과 충돌하며 튕겨다니는 공
    바닥에 떨어지면 생명이 감소
    """
    
    def __init__(self):
        """
        공 초기화
        
        Note: 실제 위치는 게임 상태에 따라 attach_to_paddle()로 설정됨
        """
        # 공의 충돌 감지를 위한 사각형 영역 (원을 감싸는 정사각형)
        self.rect = pygame.Rect(0, 0, BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.speed_x = BALL_SPEED_X  # 수평 이동 속도
        self.speed_y = BALL_SPEED_Y  # 수직 이동 속도 (음수 = 위쪽)
    
    def move(self):
        """공을 현재 속도에 따라 이동"""
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
    
    def bounce_x(self):
        """수평 방향 반전 (좌/우 벽 충돌 시)"""
        self.speed_x *= -1
    
    def bounce_y(self):
        """수직 방향 반전 (위 벽, 패들, 벽돌 충돌 시)"""
        self.speed_y *= -1
    
    def check_wall_collision(self):
        """벽과의 충돌 감지 및 처리"""
        # 좌측 벽 또는 우측 벽 충돌
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.bounce_x()
        # 상단 벽 충돌
        if self.rect.top <= 0:
            self.bounce_y()
    
    def check_floor_collision(self):
        """
        바닥 충돌 여부 확인
        
        Returns:
            bool: 바닥에 닿았으면 True, 아니면 False
        """
        return self.rect.bottom >= SCREEN_HEIGHT
    
    def attach_to_paddle(self, paddle):
        """
        공을 패들 위 중앙에 고정 (ready 상태에서 사용)
        
        Args:
            paddle: 공을 부착할 Paddle 객체
        """
        self.rect.centerx = paddle.rect.centerx  # 패들의 중앙 x 좌표에 맞춤
        self.rect.bottom = paddle.rect.top       # 공의 아래쪽을 패들 위쪽에 맞춤
    
    def draw(self, screen):
        """
        공을 화면에 그리기
        
        Args:
            screen: 그릴 pygame 화면 객체
        """
        # 흰색 원으로 공 그리기
        pygame.draw.circle(screen, WHITE, self.rect.center, BALL_RADIUS)
        # 디버깅용: 충돌 감지 영역(히트박스)을 빨간 테두리로 표시
        pygame.draw.rect(screen, RED, self.rect, 1)


class Brick:
    """
    벽돌 클래스 - 공으로 깨뜨려야 하는 목표물
    
    게임 화면 상단에 격자 형태로 배치됨
    공과 충돌 시 사라지고 점수 획득
    """
    
    def __init__(self, x, y):
        """
        벽돌 초기화
        
        Args:
            x: 벽돌의 x 좌표
            y: 벽돌의 y 좌표
        """
        self.rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)
    
    def draw(self, screen):
        """
        벽돌을 화면에 그리기
        
        Args:
            screen: 그릴 pygame 화면 객체
        """
        pygame.draw.rect(screen, BRICK_COLOR, self.rect)


class Game:
    """
    게임 메인 클래스 - 전체 게임 로직과 상태 관리
    
    게임 초기화, 이벤트 처리, 상태 업데이트, 화면 그리기 등
    모든 게임 흐름을 총괄하는 클래스
    """
    
    def __init__(self):
        """
        게임 초기화
        - Pygame 초기화
        - 게임 화면 생성
        - 모든 게임 오브젝트 초기화
        - 게임 변수 초기화
        """
        # Pygame 모듈 초기화
        pygame.init()
        pygame.font.init()
        
        # 게임 화면 생성
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("My Brick Breaker Game")
        
        # 프레임 레이트 제어를 위한 시계 객체
        self.clock = pygame.time.Clock()
        
        # 폰트 설정 (None = 기본 폰트)
        self.score_font = pygame.font.Font(None, 36)  # 점수/생명 표시용
        self.state_font = pygame.font.Font(None, 72)  # 게임 상태 메시지용
        
        # 게임 오브젝트 생성
        self.paddle = Paddle(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, 
                            SCREEN_HEIGHT - PADDLE_HEIGHT - 10)
        self.ball = Ball()
        self.bricks = self.create_bricks()
        
        # 게임 변수 초기화
        self.score = 0              # 현재 점수
        self.lives = STARTING_LIVES # 남은 생명
        self.state = "ready"        # 게임 상태: ready, playing, game_over, win
        self.running = True         # 게임 실행 여부
    
    def create_bricks(self):
        """
        벽돌 격자 생성
        
        화면 중앙 상단에 BRICK_ROWS x BRICK_COLS 크기의 격자로
        벽돌들을 배치
        
        Returns:
            list: 생성된 Brick 객체들의 리스트
        """
        bricks = []
        
        # 벽돌 격자를 화면 중앙에 배치하기 위한 x 오프셋 계산
        offset_x = (SCREEN_WIDTH - (BRICK_COLS * (BRICK_WIDTH + BRICK_PADDING))) // 2
        
        # 행(row)과 열(col)을 순회하며 벽돌 생성
        for row in range(BRICK_ROWS):
            for col in range(BRICK_COLS):
                # 각 벽돌의 x, y 좌표 계산
                x = col * (BRICK_WIDTH + BRICK_PADDING) + offset_x + BRICK_PADDING // 2
                y = row * (BRICK_HEIGHT + BRICK_PADDING) + 50  # 상단 여백 50픽셀
                bricks.append(Brick(x, y))
        
        return bricks
    
    def handle_events(self):
        """
        이벤트 처리 (모든 게임 상태에서 공통)
        - 창 닫기 이벤트
        - 키보드 입력 이벤트
        """
        for event in pygame.event.get():
            # 창 닫기 버튼 클릭 시
            if event.type == pygame.QUIT:
                self.running = False
            
            # 키보드 입력 처리
            if event.type == pygame.KEYDOWN:
                # ready 상태에서 스페이스바 누르면 게임 시작
                if event.key == pygame.K_SPACE and self.state == "ready":
                    self.state = "playing"
    
    def update_ready_state(self):
        """
        준비(ready) 상태 업데이트
        - 패들 이동 가능
        - 공은 패들 위에 고정
        - 스페이스바를 누르면 playing 상태로 전환
        """
        # 방향키 입력 받아 패들 이동
        keys = pygame.key.get_pressed()
        self.paddle.move(keys)
        
        # 공을 패들 위 중앙에 계속 붙여둠
        self.ball.attach_to_paddle(self.paddle)
    
    def update_playing_state(self):
        """
        플레이(playing) 상태 업데이트
        - 공이 자동으로 이동
        - 모든 충돌 감지 및 처리
        - 게임 종료 조건 체크
        """
        # 패들 이동 처리
        keys = pygame.key.get_pressed()
        self.paddle.move(keys)
        
        # 공 이동
        self.ball.move()
        
        # 벽과의 충돌 감지 (좌, 우, 상단)
        self.ball.check_wall_collision()
        
        # 벽돌과의 충돌 감지
        # [:] 슬라이싱으로 리스트 복사본 순회 (순회 중 원본 수정 가능)
        for brick in self.bricks[:]:
            if self.ball.rect.colliderect(brick.rect):
                self.bricks.remove(brick)  # 벽돌 제거
                self.ball.bounce_y()       # 공 반사
                self.score += 10           # 점수 증가
                break  # 한 프레임에 하나의 벽돌만 처리 (다중 충돌 방지)
        
        # 승리 조건: 모든 벽돌 제거
        if not self.bricks:
            self.state = "win"
        
        # 패들과의 충돌 감지
        if self.ball.rect.colliderect(self.paddle.rect):
            self.ball.bounce_y()
            # 공이 패들 안에 갇히는 것 방지 (공을 패들 위로 강제 이동)
            self.ball.rect.bottom = self.paddle.rect.top
        
        # 바닥 충돌 감지 (생명 감소)
        if self.ball.check_floor_collision():
            self.lives -= 1  # 생명 감소
            
            if self.lives > 0:
                # 아직 생명이 남았으면 준비 상태로 리셋
                self.state = "ready"
                self.paddle.reset_position()  # 패들 중앙 배치
                pygame.time.wait(500)         # 0.5초 대기 (플레이어 준비 시간)
            else:
                # 생명이 0이 되면 게임 오버
                self.state = "game_over"
    
    def draw_gameplay(self):
        for brick in self.bricks:
            brick.draw(self.screen)
        
        self.paddle.draw(self.screen)
        self.ball.draw(self.screen)
        
        score_text = self.score_font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        lives_text = self.score_font.render(f"Lives: {self.lives}", True, WHITE)
        self.screen.blit(lives_text, (SCREEN_WIDTH - lives_text.get_width() - 10, 10))
    
    def draw_end_screen(self, message, color):
        text = self.state_font.render(message, True, color)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(text, text_rect)
        
        score_text = self.score_font.render(f"Score: {self.score}", True, WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        self.screen.blit(score_text, score_rect)
    
    def run(self):
        while self.running:
            self.handle_events()
            self.screen.fill(BLACK)
            
            if self.state == "ready":
                self.update_ready_state()
                self.draw_gameplay()
            
            elif self.state == "playing":
                self.update_playing_state()
                self.draw_gameplay()
            
            elif self.state == "win":
                self.draw_end_screen("YOU WIN!", GREEN)
            
            elif self.state == "game_over":
                self.draw_end_screen("GAME OVER", RED)
            
            pygame.display.flip()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

# 현재 __name__의 값: __main__
# "현재 파일이 직접 실행되었다면" 이라는 뜻
if __name__ == "__main__":
    game = Game()
    game.run()