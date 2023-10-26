# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWT-lPB6dHUDFAVT&categoryId=AWT-lPB6dHUDFAVT&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2
# knapsack문제
for t_c in range(1, int(input())+1):
    n, l = map(int,input().split())
    dp = [[0]*(l+1) for _ in range(n+1)]
    points = []
    cals = []
    for i in range(n):
        point, cal = map(int, input().split())
        points.append(point)
        cals.append(cal)
        
    for r in range(1, n+1):
        for c in range(1, l+1):
            if cals[r-1] > c:
                dp[r][c] = dp[r-1][c]
            else:
                dp[r][c] = max(dp[r-1][c], dp[r-1][c - cals[r-1]] + points[r-1])
                
    print(f'#{t_c} {dp[n][l]}')
                
                
