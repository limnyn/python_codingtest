from itertools import combinations
for t_c in range(1, int(input())+1):
    n, k = map(int, input().split())
    
    nums = list(map(int, input().split()))
    count = 0
    for i in range(n):
        for cmb in combinations(nums,i):
            if sum(cmb) == k:
                count += 1
            
    print(f'#{t_c} {count}')