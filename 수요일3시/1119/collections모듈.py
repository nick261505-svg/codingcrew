from collections import namedtuple
#튜플의 불변성유지 인덱스,필드이름으로 접근가능

# Point라는 새 튜플 서브클래스 생성, 필드는 x,y
Point=namedtuple('Pint',['x','y'])
p=Point(10,20)
print(p.x)
print(p.y)
