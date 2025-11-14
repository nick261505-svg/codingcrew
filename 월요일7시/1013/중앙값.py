#중앙값: 작은 값부터 크기순으로 나열했을때 정확히 가운데 위치하는 값
#구하는 법:
# 개수가 홀수일때: 한간운데에 있는 값
# 개수가 짝수일때: 가운데에 있는 두 값의 평균
#     0 1 2 3 4
data=[5,3,1,8,9]
#오름차순으로 정렬
data.sort()
#가운데 위치 총개수//2 나누어서 몫
center=len(data) // 2

print(data[center])

# 0  1  2  3  4  5
#[1, 3, 5, 8, 9, 10]
data=[9,8,5,1,10,3]
data.sort()
print(data)
center_right=len(data)//2
center_left=center_right-1

median= (data[center_right] + data[center_left]) /2
print(f"{data}의 중앙값: {median}")
