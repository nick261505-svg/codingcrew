#문자열 입력된다
str=input()
#문자열을 한글자씩 접근해서 소문자->대문자, 대문자->소문자로 변경
#문자열 문자들의 집합
# 집합을 구성하는 구성요소를 하나씩 순회하는~동안 ch(변수) 넣어줘요
# 글자수 만큼 들여쓰기(indent)구간을 반복한다.
# 단지 반복으로만 사용할꺼야 할떄 변수('_')
for ch in str:
    temp=ord(ch)
    if  temp < 97 :
        temp=chr(temp+32)
    else: #
        temp=chr(temp-32)
    print(temp,end="")
#print(str)
#print(str.upper())
#print(str.lower())
#print(str.swapcase())

