#함수 만들었어요: 함수의 정의 define
def solution(a, b, c):
    #s=set(a,b,c) #생성자를 활요하는 방법
    ea=len({a,b,c}) # 길이(length)정보 알려주는 함수

    r1, r2, r3 = a+b+c, a*a+b*b+c*c, a*a*a+b*b*b+c*c*c
    return r1 if ea==3 else r1*r2 if ea==2 else r1*r2*r3

r = solution(2,6,1)
print(r)
r = solution(5,3,3)
print(r)
r = solution(4,4,4)
print(r)

