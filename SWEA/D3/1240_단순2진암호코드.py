code = [
    "0001101",
    "0011001",
    "0010011",
    "0111101",
    "0100011",
    "0110001",
    "0101111",
    "0111011",
    "0110111",
    "0001011",
]

T = int(input())
for t in range(1, T + 1):
    r, c = map(int, input().split())
    x, y = 0, 0
    grid = []
    for i in range(r):
        line = list(input())
        grid.append(line)
        for j in range(c):
            if line[j] == "1":
                x = i
                y = j

    nums = list(grid[x][y - 55 : y + 1])

    x = [code.index(("".join(nums[0:7])))]

    for i in range(1, 8):
        x.append(code.index(("".join(nums[i * 7 : (i + 1) * 7]))))

    odd, even = 0, 0
    for i, num in enumerate(x):
        if i % 2 == 0:
            odd += num
        else:
            even += num
    result = odd * 3 + even
    if result % 10 != 0:
        result = 0
    else:
        result = sum(x)

    print(f"#{t} {result}")


# 0111011
# 0110001
# 0111011
# 0110001
# 0110001
# 0001101
# 0010011
# 0111011
