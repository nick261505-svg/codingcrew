from collections import Counter
# 문자열,리스트,튜플 내의 요소들의 출현빈도를 계산한는데 최적화된 딕셔너리 서브클래스
c1=Counter('aaabbc')
c2=Counter('bbccd')
print(c1.most_common(2))#빈도수가 높은 순서대로 상위 n개의 요소와 개수를 튜플리스트로 반환
print(c1+c2)
print(c1-c2)
for c in c1.elements(): #요소를 반복하는 이터레이터를 반환
    print(c)
