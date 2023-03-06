


def rotate_2d(list_2d):
    """
    2차원 리스트를 입력받아 오른쪽으로 90도 회전시킨 후 그 결과(2차원 리스트)를 반환합니다
    """
    n = len(list_2d) # 행 길이 계산
    m = len(list_2d[0]) # 열 길이 계산
    new = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new[j][n-i-1] = list_2d[i][j]
    return new