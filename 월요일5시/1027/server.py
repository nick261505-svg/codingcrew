from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, HTMLResponse
from typing import List
import json

app = FastAPI()

game_score=0

print("서버가 시작되었습니다.")
# ConnectionManager: 모든 웹소켓 연결을 관리하는 클래스
class ConnectionManager:
    def __init__(self):
        # 활성화된 웹소켓 연결들을 저장하는 리스트
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        """새로운 클라이언트 연결을 수락하고 리스트에 추가"""
        await websocket.accept()
        self.active_connections.append(websocket)
        print(f"새 연결! 현재 접속자: {len(self.active_connections)}명")

    def disconnect(self, websocket: WebSocket):
        """연결이 끊긴 클라이언트를 리스트에서 제거"""
        self.active_connections.remove(websocket)
        print(f"연결 종료. 현재 접속자: {len(self.active_connections)}명")

    async def broadcast(self, message: dict):
        """모든 연결된 클라이언트에게 메시지 전송"""
        # JSON 형태로 변환
        message_text = json.dumps(message)

        # 각 클라이언트에게 메시지 전송
        for connection in self.active_connections:
            await connection.send_text(message_text)

# ConnectionManager 인스턴스 생성
manager = ConnectionManager()
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """웹소켓 연결을 처리하는 엔드포인트"""
    global game_score

    # 1. 새 클라이언트 연결 수락
    await manager.connect(websocket)

    # 2. 현재 점수를 새 클라이언트에게 전송
    await websocket.send_text(json.dumps({
        "type": "init",
        "score": game_score
    }))

    try:
        # 3. 클라이언트로부터 메시지를 계속 받음
        while True:
            # 클라이언트가 보낸 메시지 수신
            data = await websocket.receive_text()
            message = json.loads(data)

            # 4. 메시지 타입이 'click'인 경우 처리
            if message.get("type") == "click":                
                game_score += 1  # 점수 증가

                # 5. 모든 클라이언트에게 새 점수와 클릭 위치 브로드캐스트
                await manager.broadcast({
                    "type": "click",
                    "score": game_score,
                    "x": message.get("x"),
                    "y": message.get("y")
                })

    except WebSocketDisconnect:
        # 6. 연결이 끊기면 리스트에서 제거
        manager.disconnect(websocket)

@app.get("/")
async def get():
    """메인 페이지를 반환"""
    # HTML 파일 읽기
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)
    
@app.get("/game.js")
async def get_game_js():
    return FileResponse("game.js", media_type="application/javascript")