def is_promissing(level):
    for i in range(level):
        if loc[i] == loc[level]:
            return False
        if abs(loc[i] - loc[level]) == level - i:
            return False
    return True


def dfs(level):
    global count
    if level == n:
        count += 1
        return

    for i in range(n):
        loc[level] = i
        if is_promissing(level):
            dfs(level + 1)


for t_c in range(1, int(input()) + 1):
    n = int(input())

    count = 0
    loc = [0] * n
    dfs(0)
    print(f"#{t_c} {count}")
