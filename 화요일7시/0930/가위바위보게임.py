#자 이제 우리는 가위 바위 보 게임을 시작하자
#키보드에 숫자입력해서 가위(0),바위(1),보(2)를 선택해
#대결상대는 컴퓨터 : 어떻게 선택-랜덤하게...
#파이썬에서는 숫자를 랜덤하게 선택 기능(funtion)을 제공하고있어
# random 모듈 사용해야해
# 정수를 랜덤하게 생성시키는 기능(function)(함수) 사용법
# random.randint(a, b)
# a와 b를 포함한 그 사이의 정수 중에서 랜덤한 값을 하나 반환(생성)

import random

#한글로 이루어진 데이터 집합
손모양=("가위","바위","보")#튜플(집합) HAND_MOTIONS
com=random.randint(0,2)
#사용자도 선택
print("키보드에 숫자입력해서 가위(0),바위(1),보(2)를 선택해!")
user = input("선택 > ")
# int("문자영로이루어진숫자")
user = int(user)
#TypeError: tuple indices must be integers or slices, not str
# 0 이 입력되는게아니고 문자열 "0" 됨 문자열->정수변환
print(type(user)) # <class 'str'>
#손모양[순서:0~]
print("user :", 손모양[user])
print("com :", 손모양[com])

##나머지는 다음주에...##