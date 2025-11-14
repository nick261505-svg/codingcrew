str = input()
print(str.swapcase())

'''
#문자열은 집합이므로 한글짜식 쪼갤수있어 
for 한글자 in str:# 문자열: 다르게해석하면 문자집합
    print(한글자.swapcase(),end="")#한글자가 소문자면 대문자로, 대문자면 소문자로 변경
'''    