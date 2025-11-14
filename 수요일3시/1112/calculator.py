# 목적은 재사용을 위해
# 관련된 기능을 묶어서 하나의 파일로 관리
# 유지보수 용이
#-----------------
# 모듈 파이썬 코드를 담은 .py 파일
# import 문으로 모듈을 불러와 사용가능 as 별칭 (선택사항)
# from 모듈 import 함수 또는 클래스,... (*)

def sqrt(x):
    return x**0.5

def add(a, b):
    return a+b

def substract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    if b==0:
        return "0으로 나눌수 없습니다."
    return a/b

PI =3.141592