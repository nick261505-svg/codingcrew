# 몇번 반복하는지 결정하는 코드
i=0
print(i)
i += 1 #  i=i+1 -->다른언어에서는 i++,++i
print(i)#1
i += 1 #
print(i)#2
i += 1
print(i)#3
i += 1
print(i)
i += 1

j=0
while j < 5:
    #조건식이 True 들여쓰기구간 반복
    print(j)
    j += 1
    # 조건식으로 넘어감

print("조건이 False일때 실행됨", j)
