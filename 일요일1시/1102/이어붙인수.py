def solution(num_list):
    odd = 0 #351
    even = 0 #42
    for n in num_list:
        if n%2 == 0:
            even = even*10+n
        else:
            odd = odd*10+n

    return odd+even

data=[3, 4, 5, 2, 1]
#함수를 실행: 함수콜
return_data=solution(data)
print(return_data)
'''
#멀티라인주석 """  """ 사이에 는 여러줄 주석
data=[3, 4, 5, 2, 1] #인덱스번호:0~4, 역순: -1~-5
#순서가 있어요 인덱싱이 적용되었어요
print(data[0])
print(data[1])
#print(data[5])#IndexError: list index out of range
print('개수', len(data))
print(data[len(data)-1])

print(data[-1],data[-2],data[-3],data[-4],data[-5])
'''