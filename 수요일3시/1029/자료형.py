data1=[1,2,3]#수정가능
data2=(1,2,3)#수정불가능

print(type(data1))
print(type(data2))

data1[0]=10
print(data1)

data2[0]=100
print(data2)

