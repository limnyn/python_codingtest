# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PzOCKAigDFAUq&categoryId=AV5PzOCKAigDFAUq&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    result = 0
    n, m = map(int, input().split())

    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))

    for r in range(n - m + 1):
        for c in range(n - m + 1):
            flies = sum([sum(r[c : c + m]) for r in grid[r : r + m]])
            result = max(flies, result)

    print("#" + str((test_case)) + " " + str(result))
