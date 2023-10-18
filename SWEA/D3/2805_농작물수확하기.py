T = int(input())
for t in range(1, T + 1):
    n = int(input())
    grid = []
    # grid = [[0] * n for _ in range(n)]
    for i in range(n):
        line = [int(x) for x in input()]
        grid.append(line)
    result = 0
    for i in range(n):
        mid = n // 2
        if i <= mid:
            result += sum(grid[i][mid - i : mid + i + 1])
        else:
            result += sum(grid[i][i - mid : n - i + mid])

    print(f"#{t} {result}")
