n = int(input())
triangle=[]
for _ in range(n):
    triangle.append(list(map(int, input().split())))
dp = [[] for _ in range(n)]

for r, tri in enumerate(triangle):
    if r == 0 :
        dp[r].append(triangle[0][0])
        continue

    for c, v in enumerate(tri):
        # 왼쪽 끝
        if c == 0:
            dp[r].append(tri[c]+dp[r-1][0])
        
        # 중간
        elif c == len(tri)-1:
            dp[r].append(tri[c]+dp[r-1][len(tri)-2])

        # 오른쪽 끝
        else:
            dp[r].append(max(
                dp[r-1][c-1], dp[r-1][c]
            ) + tri[c])
print(max(dp[n-1]))
        



    
        

# for tri in dp:
    # print(tri)