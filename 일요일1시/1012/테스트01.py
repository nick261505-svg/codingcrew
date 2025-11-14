angle1 = int(input())
angle2 = int(input())

sum_angle = angle1 + angle2
# 그대로 출력하면 합이출력됨
# 360을 넘어가면 360만빼? 720만빼? 360의 배수 모두 처리해야함
# 파이썬의 산술연산자: + - * / // %
print(sum_angle%360)