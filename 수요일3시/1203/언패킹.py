#함수를 호출할때 *을 사용하면 리스트나 딕셔너리 분리 전달

def add(a, b):
    return a+b

nums=[10,20]
#print(add(nums))
#print(add(nums[0], nums[1]))
print(add(*nums))

#k와 일치하는데이터 매핑
def info(age,name):
    print("name:",name)
    print("age:",age)

data={'name':'코딩크루','age':2025}

info(**data)

base={'엔진':'전기','auto':True}
option={'에어빽':True}
final={**base,**option}
print(final)