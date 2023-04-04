# https://www.acmicpc.net/problem/1932

n = int(input())
stair = [[int(input())]]
for _ in range(1,n):
    level = list(map(int, input().split()))
    stair.append(level)
    
for i in range(1,n):
    for j in range(len(stair[i])):
        left, right = 0, 0
        if j != 0:
            left = stair[i-1][j-1]
        if j != len(stair[i]) - 1:
            right = stair[i-1][j]
        stair[i][j] = stair[i][j]+max(left, right)
print(max(stair[n-1]))