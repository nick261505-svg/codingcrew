# 함수의 정의
def solution(number, n, m):
    return 1 if number%n==0 and number%m==0 else 0

    '''
    if number%n==0 and number%m==0:
        return 1
    else:
        return 0
    '''
        
# 함수의 호출 : 이름()
# 매개변수: 함수를 실행하기위해서 필요한인수(재료)
# 정수 number와 n, m이 주어집니다
result=solution(60,2,3)
print(result)
result=solution(55,10,5)
print(result)