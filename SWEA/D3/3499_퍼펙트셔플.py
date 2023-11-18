for t_c in range(1, int(input())+1):
    n = int(input())
    
    cards = list(input().split())
    center = n//2 if n % 2 == 1 else n // 2 - 1

    left = cards[:center+1]
    right = cards[center+1:]
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(left[i//2])
        else:
            result.append(right[i//2])
    
    print(f'#{t_c}',end=' ')
    for r in result:
        print(r, end=' ')
    print()
    
# 1
# 6
# A B C D E F