a = int(input())
#홀짝구분
#어떤숫자를 홀수인지, 짝수인지 판별하는 식
#수를 2나누면 나머지는 나누어떨어지면 0(짝수) 아니면 1(홀수) 둘중의 하나
odd_even="odd"
if a%2==0 :
    odd_even="even"

print(a,'is',odd_even)