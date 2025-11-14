'''
: 다음줄은 함수의 구간설정의 의미로 들여쓰기(indent)가 되어야한다.
def 함수이름():
    pass
'''
#자주사용하는 코드를 정의해놓고 호출하면 자동으로 실행되도록
# 함수의 정의 : 이게 내가 만든 함수야!
def solution(num_list):
    odd=0 #351
    even=0 #42
    for num in num_list:
        if num%2==1:
            #홀수 : 홀수숫자를 이어붙이기
            odd=odd*10+num #3 -> 35
        else:
            #짝수 : 짝수숫자를 이어붙이기
            even=even*10+num
    return odd+even 
# 함수 내부코드는 함수호출을 통해서 실행된다.
# 호출하는 방법: 이름(인수)
# c언어의 배열비슷 ->리스트[] 순서가 있다 0~
data1=[3, 4, 5, 2, 1]# 홀수: 351 , 짝수: 42
data2=[5, 7, 8, 3]
result = solution(data1)
print(result) # 393

result = solution(data2)
print(result) # 581



