from collections import OrderedDict
#삽입된 순서를 기억하고 유지하는 딕셔너리
cache=OrderedDict()
cache['a']=1
cache['b']=2
cache['c']=3

print("처음순서:", list(cache.keys()))
#a키에 접근했다고 치고 a를 맨 끝으로 이동
print(cache['a'])
cache.move_to_end('a')

print("이동후순서:", list(cache.keys()))

