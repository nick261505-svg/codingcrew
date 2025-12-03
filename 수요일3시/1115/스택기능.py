stack=[]

def push(item):
    stack.append(item)
    print(f"{item}이 스택에 추가되었습니다.")

#스택이 비어있는지 확인
def is_empty():
    return len(stack)==0

def pop():
    if is_empty():
        print("스택이 비어있습니다.")
        return None
    item=stack.pop()
    print(f"{item}이 스택에 제거되었습니다.")
    return item

def size():
    print(f"스택의 크기: {len(stack)}")
    return len(stack)

#스택의 최상단 요소
def peek():
    if is_empty():
        print("스택이 비어있습니다.")
        return None
    print(f"최상단 요소: {stack[-1]}")
    return stack[-1]

def clear():
    stack.clear()
    print("스택이 비워졌습니다.")

#스택의 모든 요소 출력
def display():
    if is_empty():
        print("스택이 비어있습니다.")
    else:
        print("현재 스택 상태 (위->아래):")
        for item in reversed(stack):
            print(f"    {item}")
        '''
        for item in stack[::-1]:
            print(f"    {item}")
        '''            
        '''
        for i in range(len(stack)-1, -1,-1):
            print(f"    [{i}] {stack[i]}")
        '''

def show_menu():
    print("\n"+"="*40)
    print("== 스택 프로그램")
    print("="*40)
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Size")
    print("6. Clear")
    print("7. Exit")
    print("-"*40)

def main():
    while True:
        show_menu()
        choice=input("선택하세요(1~7): ").strip()

        if choice == '1':
            item=input("스택에 넣을 요소를 입력하세요: ").split()
            if item:
                push(item)
            else:
                print("유효한 데이터를 입력하세요")
        elif choice == '2':
            pop()
        elif choice == '3':
            peek()
        elif choice == '4':
            display()
        elif choice == '5':
            size()
        elif choice == '6':
            confirm=input("정말로 스택을 비우시겠습니가?(y/n)").strip().lower()
            if confirm == 'y':
                clear()
        elif choice == '7':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다.1~7사이 숫자만 입력가능합니다.")

#프로그램 실행1
if __name__ == "__main__":
    main()