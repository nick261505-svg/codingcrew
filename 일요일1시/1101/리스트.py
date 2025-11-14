data1 = [1,2,3]#list  ->mutable
data2 = (1,2,3)#tuple ->immutable
data3 = {10,20,30,10} #set ->중복불가, 순서가 없다
data4 = {} #dict {} 기본적으로 딕셔너리로 인식
# 둘다 {}사용해서 데이터를 표기한다.
# set {1,2,3} 데이터의 묶음
# dict {key1:value1,key2:value2} 데이터가 쌍으로 저장된다.
#데이터 구조 : key와value로 쌍으로 저장된다.
codingcrew={1:"조재청", 2:"한지용", 3:"김래현"}
person={"이름":"조재청","나이":20, "전화":"010-7758-2049"}

print(codingcrew.get(0))
#print(codingcrew[0])

#data2[0]=10

print(data1[0])
print(data2[0])
#print(data3[0])
for i in data3:
    print(i)
