# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AW8Wj7cqbY0DFAXN&categoryId=AW8Wj7cqbY0DFAXN&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=3
# 파이썬으로 검사하지 않는 문제

for t_c in range(1,int(input())+1):
    n, m = map(int, input().split())
    
    result = 1e9

    nums = list(map(int, input().split()))
        
    for i in range(n-1):
        for j in range(i+1, n):
            tmp = nums[i] + nums[j]
            if tmp <= m:
                result = min(m-tmp, result)
    if result == 1e9:
        print(f'#{t_c} {-1}')
    else:
        print(f'#{t_c} {m-result}')
            