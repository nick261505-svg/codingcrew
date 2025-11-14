lst=[1,2,3]

#추가
lst.append(4)#마지막에 추가
print(lst)
#1번위치에 100삽입 나머지는 뒤로 밀려난다
lst.insert(1,100)
print(lst)
#여러개추가
lst.extend([5,6])
print(lst)

#삭제
lst.remove(100) # 100이라는 값을 삭제
print(lst)
pooped=lst.pop()
print(lst, pooped)
pooped=lst.pop(0) #0번인덱스 제거 나머지가 앞으로 당겨진다
print(lst, pooped)
lst.clear() #모두삭제 []
print(lst)

#검색
lst=[1,2,3,2,4,2,5]
print(lst.index(2)) #첫번째의 2 의 인덱스
#print(lst[2])
print(lst.count(2))
print(3 in lst)# lst 안에 3이 있니?
print(10 in lst)# lst 안에 10이 있니?

#정렬
lst=[3,1,4,1,5,9,2,6]
print(lst)
lst.reverse()
print(lst)
lst.sort() #오름차순 정렬
print(lst)
#lst.sort(reverse=True) #내림차순
lst.reverse()
print(lst)
print(lst[::-1])

lst=[1,5,2,6,3,4]
#lst.sort()#원본을(lst) 정렬시킨다.

#sorted함수는 원본을 유지하고 새로운 정렬된리스트를 제공한다
lst2=sorted(lst)
print(lst)#원본이 나온다
print(lst2)

#복사

lst3=lst.copy() #얕은복사
print(lst3)
lst4=lst[:]#슬라이싱으로복사
print(lst4)
print("lst == lst3 ? ",lst == lst3)

import copy
lst5=copy.deepcopy(lst)#깊은복사
print(lst5)
print("lst == lst5 ? ",lst == lst5)
#깊은복사와 얕은복사의 차이점
#얕은복사 :주소만복사
#깊은복사 :실제데이터복사

list1=[1,2,3]
list2=list1
list3=copy.deepcopy(list1);
print(list1 is list2)
print(list1 == list2)#실제데이터비교
print(list1 is list3)#단순비교
print(list1 == list3)

