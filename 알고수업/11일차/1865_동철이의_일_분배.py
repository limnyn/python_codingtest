'''
백트래킹으로 짜기
    
    최대 깊이일 때 최대 값을 구하는 것이 목표
    0~1 사이의 값으로 계산하기 때문에 깊이가 깊어질 수록 작아진다.

    따라서 깊이별로 이미 현재까지의 최대값보다 작다면 더 깊어져도 작아진다

    백트래킹 dfs 시 내부에서
    if calc(nums) < result:
        break
    를 추가해서 깊이 상관없이 현재 값보다 작다면 탈출해서 해결할 수 있다.



'''

n = 0
grid = []
result = -1
visited = []


def calc(nums):
    answer = 1
    for num in nums:
        answer *= num
    return answer


def backtracking(nums, depth):
    global visited, result
    if depth == n:
        result = max(calc(nums), result)
        return
    
    if calc(nums) <= result:
        return
    
    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            backtracking(nums + [grid[depth][i]], depth+1)
            visited[i] = False



    
def solution():
    global n, grid, visited, result
    result = -1
    n = int(input())
    # grid = [list(map(int, input().split())) for _ in range(n)]
    grid = []
    for r in range(n):
        line = list(map(int, input().split()))
        l = []
        for c in range(n):
            l.append((0.01)*line[c])
        grid.append(l)
    # grid = [(0.01)*x for x in grid[r] for r in range(n)]

    # grid = [[round((0.01)*grid[r][c], 3) for c in range(n)] for r in range(n)]
    visited = [False] * n

    backtracking([], 0)    
    return "{0:.6f}".format(result*100)


for t_c in range(1, int(input()) + 1):
    print(f"#{t_c} {solution()}")


'''
1
4
98 13 75 48
94 0 6 79
75 3 43 34
91 73 49 48
'''
# n = 0
# grid = []
# result = -1
# visited = []


# def calc(nums):
#     answer = 1
#     depth = len(nums)
#     for num in nums:
#         answer *= (0.01)*num
#     return answer


# def backtracking(nums):
#     global visited, result
#     depth = len(nums)
#     if depth == n:
#         result = max(calc(nums), result)
#         return
    
#     if calc(nums) <= result:
#         return
    
#     for i in range(n):
#         if visited[i] == False:
#             visited[i] = True
#             backtracking(nums + [grid[depth][i]])
#             visited[i] = False



    
# def solution():
#     global n, grid, visited, result
#     result = -1
#     n = int(input())
#     grid = [list(map(int, input().split())) for _ in range(n)]
#     visited = [False] * n

#     backtracking([])    
#     return "{0:.6f}".format(result*100)


# for t_c in range(1, int(input()) + 1):
#     print(f"#{t_c} {solution()}")
