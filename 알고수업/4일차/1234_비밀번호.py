
for t_c in range(1, 11):
    num, password_left = input().split()
    num = int(num)
    password_left = list(map(int, list(password_left)))
    
    
    password_right = []
    
    while password_left:
        
        c_left = password_left.pop()
        if password_right:
            if c_left == password_right[-1]:
                password_right.pop()
                continue
        password_right.append(c_left)
    password_right.reverse()
    password_right = ''.join(map(str, password_right))
    print(f'#{t_c} {password_right}')

