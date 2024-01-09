
# zip 함수로 개선

def rotate_90degree(grid):

    n = len(grid)
    new_grid = [['']*n for _ in range(n)]
    for c in range(n):
        for r in range(n):

            new_grid[c][r] = grid[n-r-1][c]
            

    return new_grid


for t_c in range(1, int(input())+1):

    n = int(input())
    grid = []
    for _ in range(n):
        grid.append(list(input().split()))

    deg90 = rotate_90degree(grid)
    deg180 = rotate_90degree(deg90)
    deg270 = rotate_90degree(deg180)


    print(f'#{t_c}')
    for a, b, c in zip(deg90, deg180, deg270):
        a1 = ''.join(a)
        b1 = ''.join(b)
        c1 = ''.join(c)
        print(a1, b1, c1)




'''
# 이전 코드
    


def rotate_90degree(grid):

    n = len(grid)
    new_grid = [[0]*n for _ in range(n)]
    for c in range(n):
        for r in range(n):
        # for c in range(n-1, -1, -1):
            new_grid[c][r] = grid[n-r-1][c]
            

    return new_grid

def grid_result(grid):

    result = []
    for line in grid:
        res = ""
        for x in line:
            res += str(x)
        result.append(res)
    return result

for t_c in range(1, int(input())+1):

    n = int(input())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))

    deg90 = rotate_90degree(grid)
    deg180 = rotate_90degree(deg90)
    deg270 = rotate_90degree(deg180)

    result_90 = grid_result(deg90)
    result_180 = grid_result(deg180)
    result_270 = grid_result(deg270)


    print(f'#{t_c}')
    for r in range(n):
        print(result_90[r], end=" ")
        print(result_180[r], end=" ")
        print(result_270[r], end=" ")
        print()

    
'''