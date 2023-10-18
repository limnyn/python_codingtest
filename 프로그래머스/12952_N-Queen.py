def solution(n):
    loc = []

    def check(loc, new):
        for i in range(len(loc)):
            if loc[i] == new:
                return False
            if abs(loc[i] - new) == len(loc) - i:
                return False
        return True

    def dfs(level, loc):
        if level == n:
            return 1
        cnt = 0
        for i in range(n):
            if check(loc, i):
                cnt += dfs(level + 1, loc + [i])

        return cnt

    return dfs(0, loc)


print(solution(int(input())))
