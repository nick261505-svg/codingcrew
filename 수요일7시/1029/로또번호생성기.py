import random
#숫자 6개의 랜덤한숫자가 필요해
#각 숫자는 중복되면 안됨 : set활용
#오름차순 정렬해서 출력

#lotto={}#dict 딕셔너리 {"key":"value",}
lotto=set() #비어있는 set 은 생성자를 이용해서 만든다.

while len(lotto) < 6:
    num=random.randint(1,45)
    lotto.add(num)


sortedLotto=sorted(lotto)
print(lotto)
print(sortedLotto)

