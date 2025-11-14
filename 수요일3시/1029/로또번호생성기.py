import random
#a={1,2,3}
#b={"1":"값",}
#c={} # 비어있으면 set이아니라 딕셔너리로 생성


lotto=set()
#6개의 번호를 생성해야한다.
#중복제거
# 반복문 활용
while len(lotto) < 6: 
    num=random.randint(1,45)
    print("중간과정 :",num)
    lotto.add(num)

result=sorted(lotto)
print(result)

data=[2,4,6,1,8]
data.sort()
print(data)
print(data[0])

#print(lotto[0]) : 순서가 없으므로 인덱스로 접근불가
for i in lotto:
    print(i, end=" ")
print()
#print(lotto.pop())
r=list(lotto)
print(r[0])
n=int(3.14)



