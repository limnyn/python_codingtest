# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PobmqAPoDFAUq&categoryId=AV5PobmqAPoDFAUq&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    n = int(input())
    if n == 1:
        print("#" + str((test_case)))
        print("1")
        continue

    grid = [[0] * n for _ in range(n)]
    dir = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    r, c, d = 0, 0, 0
    grid[r][c] = 1
    while 1:
        nr = r + dir[d][0]
        nc = c + dir[d][1]
        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
            grid[nr][nc] = grid[r][c] + 1
            r = nr
            c = nc
            if grid[r][c] == n * n:
                break
        else:
            d = (d + 1) % 4

    print("#" + str((test_case)))
    for r in grid:
        for c in r:
            print(c, end=" ")
        print()
