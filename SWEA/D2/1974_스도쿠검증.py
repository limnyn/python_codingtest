

def sudoku_row(sudoku):
    for i in range(9):
        cnt = [0] * 9
        for j in range(9):
            num = sudoku[i][j] - 1
            if cnt[num] > 0:
                return False
            else:
                cnt[num] = 1
    return True


def sudoku_col(sudoku):
    for i in range(9):
        cnt = [0] * 9
        for j in range(9):
            num = sudoku[j][i] - 1
            if cnt[num] > 0:
                return False
            else:
                cnt[num] = 1
    return True


def sudoku_3x3(sudoku):
    for k in range(9):
        r = k//3
        c = k%3
        cnt = [0]*9
        for i in range(3):
            for j in range(3):
                num = sudoku[r*3+i][c*3+j] - 1
                if cnt[num] > 0:
                    return False
                else:
                    cnt[num] = 1

    return True
    
for t_c in range(1, int(input())+1):
    sudoku = []
    for _ in range(9):
        sudoku.append(list(map(int, input().split())))

    
    if sudoku_3x3(sudoku) and sudoku_row(sudoku) and sudoku_col(sudoku):
        result = 1
    else:
        result = 0

    print(f'#{t_c} {result}')

        

# 1
# 7 3 6 4 2 9 5 8 1
# 5 8 9 1 6 7 3 2 4
# 2 1 4 5 8 3 6 9 7
# 8 4 7 9 3 6 1 5 2
# 1 5 3 8 4 2 9 7 6
# 9 6 2 7 5 1 8 4 3
# 4 2 1 3 9 8 7 6 5
# 3 9 5 6 7 4 2 1 8
# 6 7 8 2 1 5 4 3 9
# 7 3 6 4 8 9 2 5 1

# 격자

# 가로

# 세로

