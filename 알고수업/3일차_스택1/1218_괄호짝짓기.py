


close_char = [')','}',']','>']
pair = {'(':')', '[':']', '<':'>', '{':'}'}

for t_c in range(1,11):
    result = 0
    close_stack = []
    
    n = int(input())
    stack = list(input())
    for _ in range(n):
        c = stack.pop()
        if c in close_char:
            close_stack.append(c)

        else:
            if close_stack:
                if pair[c] == close_stack.pop():
                    result = 1
                    continue

            result = 0
            break
            


    print(f'#{t_c} {result}')
    