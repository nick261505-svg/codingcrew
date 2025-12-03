
class Person:
    def __init__(self, name, money):
        self.name=name
        self.__money=money#private(외부에서 불가능, 클래스 내부로 제한됨)
    def display(self):
        print(f"이름: {self.name}, 잔액: {self.__money}")

p=Person('길동', 100000)

print(p.name)
p.display()

class Character:
    def __init__(self, hp):
        self.__hp=hp
    
    #Getter 메서드 : 읽는 메서드
    def get_hp(self):
        return self.__hp
    def set_hp(self, hp):
        self.__hp=hp
#캡슐화: (데이터 하이딩) 속성은 private으로 선언하고
# 우회해서 접근가능한 getter,setter메서드로 처리

c=Character(100)
c.set_hp(90)
print(c.get_hp())

class Character2:
    def __init__(self, hp):
        self.__hp=hp

    @property
    def hp(self):
        return self.__hp
    
    @hp.setter
    def hp(self, hp):
        self.__hp=hp

c2=Character2(1000)
print(c2.hp)
c2.hp=9000
print(c2.hp)