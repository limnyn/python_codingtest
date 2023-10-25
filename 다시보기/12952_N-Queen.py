# https://school.programmers.co.kr/learn/courses/30/lessons/12952
def solution(n):
    def is_promissing(loc, new):
        for i in range(len(loc)):
            if loc[i] == new or abs(loc[i] - new) == len(loc) - i:
                return False
        return True

    def dfs(level, loc):
        if level == n:
            return 1
        cnt = 0
        for i in range(n):
            if is_promissing(loc, i):
                cnt += dfs(level + 1, loc + [i])
        return cnt

    return dfs(0, [])
