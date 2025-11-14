#딕셔너리
#키와 값 싸으로 저장하는 자료구조
#키는 저장할때 중복 저장불가
#키를 이용해서 값을 읽어온다
com={'name':'코딩크루', 'age': 2025, 'city':'경기광주',}
print(com)
person=dict(name='코딩', age=2025, school='태전중')

com['phone']='031-768-2048'
print(com)
com['phone']='010-7758-2049'#중복불가이므로 이코드는 기존키의 값이 수정된다
print(com)

print("회사명 :", com['name'])
#print("회사명 :",com['name1']) #존재하지 않은 키로 접근하면 KeyError
#get()
print("회사명 :",com.get('name'))
print("회사명 :",com.get('name1'))#존재하지 않은 키로 접근하면 None

#del com['phone']

print("삭제하는데이터:",com.pop('phone'))
print(com)
com.clear()
print(com)
#############################################
#쌍으로 저장되어있기에 Key만 따로, Value만따로 뽑아낼수 있어요
print(person)
for k in person.keys():
    print(k,person[k])

print("------------")
for k,v in person.items():# key와 value를 동시에 처리해준다
    print(k,v)
######
# 딕셔너리 컴프리헨션
# 중첩 딕셔너리
# JSON
d={
    1:{'name': '홍길동','age':20},
    2:{'name': '조코딩','age':45},
}
print(d[1]['name']) 
print(d[1]['age']) 

#
ar=[1,2,3,4]
#리스트
arr=[1,2.0,"ㅁㅁㅁ"]
