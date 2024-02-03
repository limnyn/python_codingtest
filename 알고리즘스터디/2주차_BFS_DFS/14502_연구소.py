# https://www.acmicpc.net/problem/14502

from itertools import combinations
from collections import deque
n, m = map(int, input().split())
grid = [list(map(int,input().split())) for _ in range(n)]

spot_2 = []
spot_1 = []
spot_0 = []

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            pass