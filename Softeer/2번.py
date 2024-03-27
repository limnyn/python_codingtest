
'''
dp = 0부터 (n-1,n-1)까지 각 좌표까지 가는데 대한 최대 이득

dp_reverse = r,c부터 n-1,n-1 까지 가는 경로 중 최대 이득

dp_time = r,c에서 t만큼 갔을 때 최대 이득

'''

1000 * 1000 * 5*5
for r in range(n):
    for c in range(n):
        non_time_loop = dp[r][c] + dp_reverse[r][c]
        time_loop = non_time_loop + dp_time[r][c]
        result = max(result, non_time_loop, time_loop)

print(result)