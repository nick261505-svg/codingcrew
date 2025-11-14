# 게임방법: 컴퓨터가 1부터 100사이의 숫자중 하는 무작위로 정하면, 사용자는 그 숫자를 맞추는게임
# 사용자가 숫자를 입력할 때 마다 컴퓨터는 정답이 up,down의 힌트를 준다

import random

secret_number=random.randint(1,100)
#계속 질문하고 추측한값을 입력
#몇번 반복해야해? 최대100 최소1
#몇번을 반복해야할지 모르는 상황에서 반복문은 while
guess=0
'''
while 조건:
    반복구간
#조건의 결과가 Ture일때 반복구간(들여쓰기구간) 실행
#조건의 결과가 False일때 탈출
'''
while guess != secret_number:
    print('1부터 100사이의 숫자중 맞춰봐!')
    guess=int(input('입력 > '))
    if guess < secret_number:
        print("Up~")
    elif guess > secret_number:
        print("Down~")
    else:
        print("정답!")
    
