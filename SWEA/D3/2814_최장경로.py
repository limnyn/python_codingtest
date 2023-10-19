def dfs(start, visited):
    global result
    result = max(result, len(visited))
    for node in grid[start]:
        if node not in visited:
            dfs(node, visited + [node])


for t_c in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    visited = [0] * n
    grid = [[] for _ in range(n)]
    for _ in range(m):
        s, e = map(int, input().split())
        grid[s - 1].append(e - 1)
        grid[e - 1].append(s - 1)
    result = 0
    for i in range(n):
        dfs(i, [i])

    print(f"#{t_c} {result}")

# https://www.youtube.com/watch?v=Hj39HZhcnP4
