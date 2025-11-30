#함수(function)->어떤기능
#함수:
# 1.이미 만들어져있는 함수(파이썬에서 제공하는 라이브러리, print(), input())
# 2.사용자가 만드는 함수: 함수정의한 후 함수호출을 통해 사용
# 키워드 def -> define(정의하다)
# 함수이름은 사용자가 결정
# 매개변수 선택(없어도되고, 1,2,3개 선택사항)
'''
def 함수이름(매개변수):
    pass
'''
#solution함수 정의 : 내가 함수 코드를 만들었어 컴퓨터야 알고 있어라.
def solution(n, k):
    answer=[]
    for num in range(k,n+1,k):#3,4,5,6,7,8,9,10
        answer.append(num)
    '''
    for num in range(1,n+1):
        if num%k == 0:
            answer.append(num)
    '''            
    return answer

# 인수 10,3 을 넘겨줄테니 함수코드를 실행해줘~
# 함수정의코드의 매개변수에 각각 전달 n=10, k=3 이거와 동일

#함수코드를 실행하고, 함수가 리턴해준 값을 출력해!
#함수 코드에서 리턴이 있어야 출력가능!
print("함수실행결과:",solution(10, 3))
