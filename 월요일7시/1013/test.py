#평균: 모든 자료의 값을 더한후 자료의 개수로 나눈 값
data=[1,2,3,4,6]
sum=sum(data)
length=len(data)
print(f"평균: {sum/length}")

hap=0
for num in data:
    #hap = hap +num
    hap += num

print(f"평균: {hap/length}")


#중앙값

#최빈값