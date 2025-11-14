number = int(input())

answer = 0

#맞았으나 똥코딩 : 성능이 좋지않아! 무조건5번 돌기때문에
# for loop, while loop
#for i in range(5):
while number>0:
    #2자리씩 잘라서 누적(100으로 나누어서 나머지를 누적)
    answer += number % 100
    #number(입력된값)을100으로 나누어서 정수만(몫)
    number //= 100
    #number를 계속100으로 나누면 몫은 0이된다.
    #number가 0이면 반복하는 의미가 없다.


print(answer)