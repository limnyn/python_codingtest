# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWT-lPB6dHUDFAVT&categoryId=AWT-lPB6dHUDFAVT&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=2
# knapsack문제
for t_c in range(1, int(input())+1):
    n, l = map(int,input().split())
    points, cals = [], []
    dp = [[0] * (l+1) for _ in range(n+1)]
    for _ in range(n):
        point, cal = map(int, input().split())
        points.append(point)
        cals.append(cal)

    for food in range(1,n+1):
        for cal in range(1, l+1):
            if cal < cals[food-1]:
                dp[food][cal] = dp[food-1][cal]
            else:
                dp[food][cal] = max(dp[food-1][cal],
                    dp[food-1][cal-cals[food-1]]+points[food-1])

    print(f'#{t_c} {dp[n][l]}')



                
