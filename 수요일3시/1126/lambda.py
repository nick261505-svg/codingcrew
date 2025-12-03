#함수를 간결하게 표기하는 식
def 함수이름(a,b):
    return a+b

#일회용 함수-익명함수
add=lambda x,y:x+y
print(add(10,20))

students=[('철수',80),('영희',95),('광수',70)]
print(students)
students.sort(key=lambda student:student[0])
print(students)

'''
def mysort(s):
    return s[1]

students.sort(key=mysort)
print(students)
'''

