#스택 생성
stack=[]

#Push:요소 추가
stack.append(1)
stack.append(2)
stack.append(3)
print("push 후:",stack)

#pop:
item=stack.pop()
item=stack.pop()
item=stack.pop()
print(f"pop된 요소: {item}")
print("push 후:",stack)

#마지막 데이터는?
#print(stack[len(stack)-1])#스택의 길이-1
#print(stack[-1])
if stack:
    print(f"최상단 요소 {stack[-1]}")
else:
    print("스택이 비어있네요")

