#변하지 않으면 좋은 데이터 튜플
#      0 1 2 3
list1=[1,2,3,4,5,6,7,8,9,10]
list2=list(range(1,10))
#인덱싱 0~
# -1 ~ 가능 뒤부터
print(list1[-len(list1)])
print(list1[-10])
print(list1[0])
print(list1[10%10])

#슬라이싱[start:end:step]
#range(start,end,step) 비슷하다
print(list1[0:3])
print(list1[:3])
print(list1[3:])
print(list1[3:len(list1)])

print(list1[::2]) # [0],[2],[4],[6],[8]
print(list1[::-2]) # 스텝이 -이면 -범위(-1:-길이:)가 생략됨

