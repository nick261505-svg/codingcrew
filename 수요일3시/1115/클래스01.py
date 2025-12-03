s1_name="조코딩"
s1_age=20
s1_score=80

s2_name="박코딩"
s2_age=21
s2_score=90
##변수가 많아지면 관리가 어려워요, 관련함수를 찾기힘듦
#클래스로 학생 정보관리(효율적)

class Student:
    #생성자
    def __init__(self, name, age=None, addr=None):
        print("생성자가 실행됨")
        #self.변수명=값 (인스턴스 변수: 각 객체가 독립적으로 소유)
        self.name=name
        self.age=age
    

s=Student("조코딩",10)#=>__init__() 호출
print(s.name)
s1=Student("박코딩")
print(s1.name)

