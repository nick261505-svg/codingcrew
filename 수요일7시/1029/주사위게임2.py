#함수 만들었어요: 함수의 정의 define
def solution(a, b, c):
    answer=0
    if a != b and a != c and b !=c :
        answer=a+b+c
    if a==b and a!=c or a==c and a!=b or b==c and b!=a:
        answer=(a+b+c)*(a*a+b*b+c*c)
    if a==b and a==c:
        answer=(a+b+c)*(a*a+b*b+c*c)*(a*a*a+b*b*b+c*c*c)
    return answer

r = solution(2,6,1)
print(r)
r = solution(5,3,3)
print(r)
r = solution(4,4,4)
print(r)

