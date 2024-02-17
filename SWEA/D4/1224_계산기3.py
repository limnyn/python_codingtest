# https://dream-and-develop.tistory.com/93


"""
# 중위 표기식 -> 후위 표기식으로 바꾸기
1. 여는 괄호는 스택에 추가
2. 여는 괄호 다음에 오는 연산자는 스택에 추가
3. 닫는 괄호 차례에 여는괄호가 나올 때 까지 pop 하여 출력한다.
    3-1. pop 도중 괄호는 출력하지 않는다.
"""
for t_c in range(1,11):
    n = int(input())    
    line = list(input())
    
    stack_post = []
    stack = []
    is_opend = False
    for c in line:
        if c.isdigit():
            stack_post.append(c)
        else:
            if c == '(':
                stack.append(c)
            elif c == '*':
                while stack and stack[-1] == '*':
                    stack_post.append(stack.pop())
                stack.append(c)
            elif c == '+':
                while stack and stack[-1] != '(':
                    stack_post.append(stack.pop())
                stack.append(c)
            elif c == ')':
                while stack and stack[-1] != '(':
                    stack_post.append(stack.pop())
                stack.pop()

    while stack:
        stack_post.append(stack.pop())
    

    result =[]
    
    for c in stack_post:
            
        if c == '+':
            result.append(result.pop() + result.pop())
        elif c == '*':
            result.append(result.pop() * result.pop())    
        else:
            result.append(int(c))
    
        
    

    print(f'#{t_c} {result[0]}')
    