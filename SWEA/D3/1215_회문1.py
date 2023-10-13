# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV15Khn6AN0CFAYD&categoryId=AV15Khn6AN0CFAYD&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1


from collections import deque

answer = []
for t_c in range(10):
    n = int(input())
    result = 0
    grid_r = []
    grid_c = [[] for _ in range(8)]

    for row in range(8):
        line = input()
        grid_r.append([c for c in line])
        for i, c in enumerate(line):
            grid_c[i].append(c)

    for grid in [grid_r, grid_c]:
        for r in range(8):
            dq = deque()
            for x in grid[r][: n - 1]:
                dq.append(x)
            for c in range(n - 1, 8):
                dq.append(grid[r][c])
                ispalindrome = False
                for idx in range(n // 2):
                    if dq[idx] == dq[-1 - idx]:
                        ispalindrome = True
                    else:
                        ispalindrome = False
                        break
                if ispalindrome:
                    result += 1

                dq.popleft()

    print("#" + str(t_c + 1) + " " + str(result))


# 5
# AADSCSAB
# BABCBADD
# DADADVSS
# CABCDEFG
# ABCDEFGH
# ABCDEFGH
# ABCDEFGH
# ABCDEFGH
