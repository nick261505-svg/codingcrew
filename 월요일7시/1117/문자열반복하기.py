def solution(my_string, k):
    answer=""
    for _ in range(k): #
        #answer = answer + my_string
        answer += my_string
    return answer

r=solution("string", 3)
print(r)
r=solution("love", 10)
print(r)

str="s1d2f31sd23f1sd32f1s23df13sdf21s"
def length(sss):
    count=0
    for _ in sss:
        count +=1
    return count

print("my글자수:",length(str))
print("py글자수:",len(str))