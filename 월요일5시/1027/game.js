// game.js

// DOM 요소 가져오기
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const scoreDisplay = document.getElementById('score');
const statusDisplay = document.getElementById('status');

// 웹소켓 연결 (ws://는 웹소켓 프로토콜)
const ws = new WebSocket('ws://localhost:8000/ws');

// 클릭 효과를 저장하는 배열
let clickEffects = [];

// ========================================
// 웹소켓 이벤트 핸들러
// ========================================

// 연결이 성공했을 때
ws.onopen = function() {
    console.log('서버에 연결되었습니다!');
    statusDisplay.textContent = '✅ 연결됨';
    statusDisplay.className = 'connected';
};

// 서버로부터 메시지를 받았을 때
ws.onmessage = function(event) {
    const data = JSON.parse(event.data);

    if (data.type === 'init') {
        // 초기 점수 설정
        scoreDisplay.textContent = data.score;

    } else if (data.type === 'click') {
        // 점수 업데이트
        scoreDisplay.textContent = data.score;

        // 클릭 효과 추가
        addClickEffect(data.x, data.y);
    }
};

// 연결이 끊겼을 때
ws.onclose = function() {
    console.log('서버 연결이 끊겼습니다.');
    statusDisplay.textContent = '❌ 연결 끊김';
    statusDisplay.className = 'disconnected';
};

// 에러가 발생했을 때
ws.onerror = function(error) {
    console.error('웹소켓 에러:', error);
};

// ========================================
// 캔버스 클릭 이벤트 처리
// ========================================

canvas.addEventListener('click', function(event) {
    // 캔버스 내에서의 클릭 위치 계산
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;

    // 서버로 클릭 이벤트 전송
    const message = {
        type: 'click',
        x: x,
        y: y
    };

    ws.send(JSON.stringify(message));
});

// ========================================
// 클릭 효과 애니메이션
// ========================================

function addClickEffect(x, y) {
    // 새로운 클릭 효과 추가
    clickEffects.push({
        x: x,
        y: y,
        radius: 5,
        opacity: 1,
        maxRadius: 50
    });
}

function animateClickEffects() {
    // 캔버스 지우기
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // 각 클릭 효과 그리기 및 업데이트
    clickEffects = clickEffects.filter(effect => {
        // 원 그리기
        ctx.beginPath();
        ctx.arc(effect.x, effect.y, effect.radius, 0, Math.PI * 2);
        ctx.strokeStyle = `rgba(76, 175, 80, ${effect.opacity})`;
        ctx.lineWidth = 3;
        ctx.stroke();

        // 효과 업데이트
        effect.radius += 2;
        effect.opacity -= 0.02;

        // 효과가 아직 보이면 계속 유지
        return effect.opacity > 0;
    });

    // 다음 프레임 요청
    requestAnimationFrame(animateClickEffects);
}

// 애니메이션 시작
animateClickEffects();
