for t_c in range(1, int(input())+1):
    n = int(input())
    
    cards = list(input().split())
    center = n//2 if n % 2 == 1 else n // 2 - 1

    left, right = cards[:center+1], cards[center+1:]
    result = []
    for i in range(n):
        result.append(left[i//2]) if i % 2 == 0 else result.append(right[i//2])
        
            
    
    print(f'#{t_c} {" ".join(result)}')

    
# 1
# 6
# A B C D E F