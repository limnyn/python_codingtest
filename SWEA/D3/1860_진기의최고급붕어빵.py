

for t_c in range(1, int(input())+1):
    n, m, k = map(int, input().split())
    #손님, m초동안 k개 붕어빵
    customers = list(map(int, input().split()))
    customers.sort()

    result = "Possible"
    for i in range(n):
        boong = (customers[i]//m)*k - (i+1)
        if boong < 0:
            result = "Impossible"
            break

    print(f'#{t_c} {result}')
        
        





# time = m
# count = k
# for c in customers:
#     if c < time:
#         count -= 1
        