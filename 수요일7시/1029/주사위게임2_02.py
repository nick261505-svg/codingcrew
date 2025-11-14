#함수 만들었어요: 함수의 정의 define
def solution(a, b, c):
    r1=a+b+c
    r2=a*a+b*b+c*c
    r3=a*a*a+b*b*b+c*c*c

    if a==b and a==c:
        return r1*r2*r3
    if a !=b and a!=c and b!=c:
        return r1
    
    return r1*r2

r = solution(2,6,1)
print(r)
r = solution(5,3,3)
print(r)
r = solution(4,4,4)
print(r)

