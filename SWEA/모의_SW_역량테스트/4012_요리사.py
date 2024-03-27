'''
4 <= n <= 16
16에서 8개 뽑고, 나머지 중 8개를 뽑아서 비교하는 경우의 수
16c8*8c8 = 10920


즉, 10920 경우에 대해 16*16씩 비교하면 해결 가능하다.

테스트 케이스 당 입력 예제
4
0 5 3 8
4 0 4 1
2 5 0 3
7 2 3 0
'''

from itertools import combinations
def solution():
    result = 1e9
    n = int(input())
    grid = []
    for _ in range(n):
        grid.append(list(map(int,input().split())))
    
    combs_a = combinations([x for x in range(n)], n//2)
    for comb_a in combs_a:
        # print(comb_a)
        comb_b = [x for x in range(n) if x not in comb_a]


        sum_a = 0
        sum_b = 0 
        for i in range(n//2):
            for ingredient in comb_a:           
                if comb_a[i] != ingredient:
                    sum_a += grid[ingredient][comb_a[i]]
            for ingredient in comb_b:           
                if comb_b[i] != ingredient:
                    sum_b += grid[ingredient][comb_b[i]]
        
        result = min(result, abs(sum_a - sum_b))
    return result


for t_c in range(1, int(input())+1):
    print(f"#{t_c} {solution()}")