# https://www.acmicpc.net/problem/1074

N, r, c = map(int, input().split())

# 56에 대해
# n=3일때 4사분면
# n=2일때 3사분면
# n=1일때 2사분면

# 0+8+48 = 56이네

# 57에 대해
# n = 3 3
# n = 2 2
# n = 1 1

# 1 + 8 + 48 =

# 각 시작점만 구해보기
# n = 1
#     0 1 2 3
# n = 2
#     0 4 8 12
# n = 3
#     0 16 32 48

# 0 1 2 3
# 4**(n-1)*1
# 4**(n-1)*2
# 4**(n-1)*3


def func(N, r, c):
    num = 0
    for n in range(N, 0, -1):
        loc = -1
        edge = 2 ** (n - 1)
        if r < edge:
            if c < edge:
                loc = 0
            else:
                loc = 1
                c -= edge
        else:
            if c < edge:
                loc = 2
                r -= edge
            else:
                loc = 3
                r -= edge
                c -= edge
        num += 4 ** (n - 1) * loc

    return num


print(func(N, r, c))
