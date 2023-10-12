# https://www.acmicpc.net/problem/2630


n = int(input())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

white_square = 0
blue_square = 0


def is_square(r, c, n):
    global blue_square, white_square
    if n == 1:
        if grid[r][c] == 1:
            blue_square += 1
        else:
            white_square += 1
        return 0
    square = [r[c : c + n] for r in grid[r : r + n]]  # r,c에서 n*n사각형 그리드 자르기
    result = sum([sum(x) for x in square])
    if result == n**2:
        blue_square += 1
    elif result == 0:
        white_square += 1
    else:
        is_square(r, c, n // 2)
        is_square(r + n // 2, c, n // 2)
        is_square(r, c + n // 2, n // 2)
        is_square(r + n // 2, c + n // 2, n // 2)
        return 0


is_square(0, 0, n)
print(white_square)
print(blue_square)
