# 전체 수 n을 입력받아 k개의 조합을 리턴하라

import itertools
n, k = map(int,input().split())
print(list(map(list, itertools.combinations(range(1, n+1), k))))
