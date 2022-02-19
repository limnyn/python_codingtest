# 스택 == FILO , 선입후출/후입선출

# 예제1 /가상의 스택을 준비
# 삽입5-삽입2-삽입3-삽입7-삭제-삽입1-삽입4-삭제 표현

stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1]) #역순으로 출력

