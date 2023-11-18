
for t_c in range(1, int(input())+1):
    l, u, x = map(int, input().split())
    result = 0
    if x > u:
        result = -1
    elif x < l:
        result = l - x
    print(f'#{t_c} {result}')
