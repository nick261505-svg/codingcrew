#위치 가변변수
#튜플
def add_all(*args):
    print("타입",type(args))
    print("데이터",args)

#키워드 가변변수
#딕셔너리
def print_info(**kwargs):
    print("타입",type(kwargs))
    print("데이터",kwargs)

#필수,*선택,**선택 : 순서가 중요!!!!
def mixed_params(n, m, *args, **kwargs):
    print(n+m)
    for ar in args:
        print(ar)
    for k in kwargs.keys():
        print(k, kwargs[k])

mixed_params(10,20,aaa=10,bbb=20)
print_info()