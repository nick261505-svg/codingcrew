#부모클래스(공통 기능을 모아높은 클래스)
class Character:
    def __init__(self, nick):
        self.nick=nick

    def move(self):
        print(f"{self.nick}이(가) 이동")

#부모클래스를 상혹한 자식클래스    
class Wizard(Character):
    def magic(self):
        print(f"{self.nick}이(가) 마법 공격")

class Warrior(Character):
    def slash(self):
        print(f"{self.nick}이(가) 대검 공격")


c1=Wizard("구름")
c1.move()
c1.magic()

c2=Warrior("재선")
c2.move()
c2.slash()