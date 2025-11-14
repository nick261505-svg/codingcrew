import random
# 주석: 코드가 아닌 설명글을 사용할때
# 가위(0), 바위(1), 보(2)  
options=["가위","바위","보"]
# options[0],options[1],options[2]

#게임설명
#컴퓨터(랜덤한 숫자 생성)vs사람(숫자를 입력) 

# 0에서 2 사이의 정수 중 하나 뽑기
com = random.randint(0, 2)

#유저 -키보드에서 입력
print("===가위(0), 바위(1), 보(2) 중 하나 선택===")
user = int(input("선택 > "))
print("user : ",options[user])
print("com : ",options[com])

# 무엇을 작성할까요?
# 이겼는지 졌는지 판단
# (user,com): 

# 비긴경우  (0,0), (1,1), (2,2) : 0,0,0
result = user-com
if result==0:
    print("비겼습니다")

# 진경우   (0,1), (1,2), (2,0) : -1,-1,2
elif result==-1 or result==2:
    print("내가졌음")

# 이긴경우 (0,2), (1,0), (2,1) : -2, 1, 1
else:
    print("승리")
