a = int(input())

#만약에 a를 2로나누어서 0이면 짝수

#파이썬의 삼항연산자
결과="even" if a%2==0 else "odd"
# 결과 = [참일 때 값] if [조건] else [거짓일 때 값]
print(f"{a} is {결과}")

'''
#파이썬의 print는 무조건 줄바꿈해준다
print(f"{a} is ",end="")
if a%2==0:
    print("even")
else:
    print("odd")
'''    


'''
if a%2==0:
    print(f"{a} is even")
else:
    print(f"{a} is odd")
'''    

'''
if a%2==0:
    print(a,"is even")
else:
    print(a,"is odd")
'''    