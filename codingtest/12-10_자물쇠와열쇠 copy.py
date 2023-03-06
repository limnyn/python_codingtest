# https://school.programmers.co.kr/learn/courses/30/lessons/60059

# 2020 카카오 신입 공채


# 2차원 회전 문제
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]


def rotate_2d(list_2d):
    n = len(list_2d) # 행 길이 계산
    m = len(list_2d[0]) # 열 길이 계산
    new = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new[j][n-i-1] = list_2d[i][j]
    return new

def unlock(newLock, lenLock):
    for i in range(lenLock):
        for j in range(lenLock):
            if newLock[i+lenLock][j+lenLock] != 1:
                return False
    return True
    

def solution(key, lock):
    lenLock = len(lock)
    lenKey = len(key)
    
    newLock =[[0] * (lenLock*3) for _ in range(lenLock*3)]

    for i in range(lenLock):
        for j in range(lenLock):
            newLock[i+lenLock][j+lenLock]=lock[i][j]
    
    print(newLock)

    for _ in range(4):
        newLock = rotate_2d(newLock)
        for x in range(lenLock*2):
            for y in range(lenLock*2):

                for i in range(lenKey):
                    for j in range(lenKey):

                        newLock[x+i][y+j] += key[i][j]
                
                if unlock(newLock, lenLock) == True:
                    return True

                for i in range(lenKey):
                    for j in range(lenKey):
                        newLock[x+i][y+j] -= key[i][j]

    return False

print(solution(key,lock))
