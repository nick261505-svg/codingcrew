#zip-두개 이상의 리스트를 같은 인덱스끼리 짝을 지어 묶어주는 함수
names=['철수','영희','광수']
scores=[90,80,95]
#두 리스트를 묶어서 처리
for name, score in zip(names,scores):
    print(name, score)

# 딕셔너리로 변활할 때 사용
score_board=dict(zip(names,scores))  
print(score_board) 

'''
for i in range(len(names)):
    print(names[i], scores[i])
'''