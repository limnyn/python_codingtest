for test_case in range(1, 11):
    t = int(input())
    result = 0
    grid = []
    for _ in range(100):
        line = list(map(int, input().split()))
        result = max(sum(line), result)
        grid.append(line)

    for i in range(100):
        result = max(result, sum([x[i] for x in grid]))
    diagonal_0 = 0
    diagonal_100 = 0
    for j in range(100):
        diagonal_0 += grid[i][j]
        diagonal_100 += grid[99 - i][j]
    result = max(diagonal_0, diagonal_100, result)

    print(f"#{t} {result}")
