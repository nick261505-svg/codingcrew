#함수란 기능을 정의하는것
#define -> def
'''
def 함수이름(매개변수):
    #들여쓰기 구간에 내용
'''
#식별자 : 변수이름,함수이름,클래스이름 개발자결정
print("프로그램시작")

#함수 정의
def add(a,b):
    return a+b

#함수 호출 결과가 return 값
print(add(10,20))
r1=add(3,5)#함수가 실행후 리턴한 결과를 r1 대입
print(r1)
r1=add(10,5)
print(r1)
print("END")
