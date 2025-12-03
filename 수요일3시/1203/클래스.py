class Point:
    #생성자(초기화 메서드)
    def __init__(self):
        self.x=100
        self.y=200

#클래스의 생성자를 호출 : 클래스이름()
p=Point()
print(p.x, p.y)

class Point2:
    #생성자(초기화 메서드)
    def __init__(self, x, y):
        self.x=x
        self.y=y
    
p2=Point2(10,20)
print(p2.x, p2.y)

class Point3:
    #생성자(초기화 메서드)
    def __init__(self, x=0, y=0,):
        self.x=x
        self.y=y
#매개변수전달이 되지않으면 default값으로 처리됨
p3=Point3()
print(p3.x, p3.y)
p33=Point3(1000)
print(p33.x, p33.y)

