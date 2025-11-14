import math

n=int(input())

points=[]
for _ in range(n):
    x,y=map(int,input().strip().split())
    points.append([x,y])

#꼭지점이 위에있고 빗변 아래
min_y=min(p[1] for p in points)
'''
min_y=math.inf
for p in points:
    if min_y>p[1]:
        min_y=p[1]
print(min_y)
'''
a_x=math.inf#최소값
b_x=-math.inf#최대값

for x,y in points:
    #y(p[1])-min_y==빗변을 통과하는 중선의 높이
    #x(p[0]) 더하고 빼면된다.
    #x,y=p
    r_x=x+(y-min_y)
    if b_x < r_x:
        b_x=r_x
    l_x=x-(y-min_y)
    if a_x > l_x:
        a_x=l_x

#꼭지점위 위인 삼각형의 빗변의 길이
print(b_x-a_x)
