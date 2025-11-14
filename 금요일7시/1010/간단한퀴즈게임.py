#미리 만들어둔 질문과 답을 이용하여 간단한 퀴즈를 푸는게임
#데이터를 쌍(키,값)으로 저장하는 데이터타입
#{ key1:value1, key2:value2, key3:value3, ... }
#딕셔너리
questions={
    "H":"수소",
    "He":"헬륨",
    "Li":"리튬",
    
}
score=0

for q,a in questions.items():
    user_answer=input(f"{q} ")
    if user_answer == a:
        print("정답입니다.")
        #score += 1
        score = score+1
    else:
        print(f"틀렸습니다. 정답은 {a}입니다.")

print(f"총 {len(questions)} 문제 중 {score} 문제를 맞혔습니다.!")