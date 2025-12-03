from collections import defaultdict
#목적: 그룹화,카운딩등 딕셔너리 초기화 및 키 존재여부확인 간소화
#서브클래스 ,미리 정의된 기본값을 사용하여 새 항목을 자동으로 생성
s=[('노랑',1),('파랑',2),('노랑',3),('빨강',4),('파랑',1)]
d=defaultdict(list)

for k,v  in s:
    d[k].append(v)#리스트 기본값 : []

print(d.items())