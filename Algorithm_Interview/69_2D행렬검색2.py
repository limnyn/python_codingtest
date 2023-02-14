# m*n 행렬에서 값을 찾아내는 ㅎ율적인 알고맂므을 구현하라.
# 행렬은 왼쪽에서 오른쪽, 위에서 아래, 오름차순으로 정렬되어 있다.

mat =   [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]

# def serachMatrix(mat, target):
#     if not mat:
#         return False
#     row, col = 0, len(mat[0])-1
#     while True:
#         # print("row : ", row,"col : ",col, "mat : ", mat[row][col])
#         if target < mat[row][col]:
#             col-=1
#         elif mat[row][col] < target:
#             row+=1
#         elif mat[row][col] == target:
#             return True        
        
    
# print(serachMatrix(mat, 5))


# Pythonic Way
def searchMatrix(mat, target):
    return any(target in row for row in mat)
print(searchMatrix(mat, 5))