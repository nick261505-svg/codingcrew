
nums=[1,2,3,4,5]
'''
#모든요소를 출력
for n in nums:
    print(n)    
'''
#최단산(+,-,*,/,%,//)쉬관비리삼대
'''
for n in nums:
    if 1 == n % 2 :# and or
        print(n)
'''
for n in nums:
    if 0 == n%2:
        continue #다음 요소 : 아래코드 실행안함.
    print(n)

str="abcxdef"

for ch in str:
    if ch=='x':
        break
    print(ch)

'''
for c in str:
    print(c)
'''



