# https://www.acmicpc.net/problem/1270


import sys
from collections import Counter
def input(): return sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())

    for i in range(n):
        arr = list(map(int, input().split()))
        soldier_list = arr[1:]

        # Counter를 사용해 각 병사의 수를 효율적으로 계산합니다.
        soldier_cnt = Counter(soldier_list)
        
        target = len(soldier_list) // 2
        dominant_army = "SYJKGW"
        
        for k, v in soldier_cnt.items():
            if v > target:
                dominant_army = k
                break
        
        print(dominant_army)
    