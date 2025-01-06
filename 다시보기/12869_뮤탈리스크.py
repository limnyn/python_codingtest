# https://www.acmicpc.net/problem/12869
"""
뮤탈리스크가 공격을할 때 한 번에 세 개의 SCV를 공격할 수 있다.

9, 3, 1 순으로 체력이 감소된다

[조건]
1. SCV는 최대 3마리
2. 체력은 60보다 작거나 같은 자연수

[접근] - BFS
1. 각 SCV 별 BFS로 공격을 수행한다,
2. 가장 먼저 모든 SCV가 죽었을 때 반복을 종료한다.
"""
from collections import deque
from itertools import permutations
import sys
def input(): return sys.stdin.readline().rstrip()

if __name__ == "__main__":
    
    n = int(input())
    scvs = list(map(int, input().split()))

    while len(scvs) < 3:
        scvs.append(0)
        
    damage_list = [9, 3, 1]

    dq = deque([])
    visited = set()
    dq.append((scvs[0], scvs[1], scvs[2], 0))
    visited.add((scvs[0],scvs[1], scvs[2]))

    attack_patterns = list(permutations([9, 3, 1], 3))

    while dq:
        a, b, c, count = dq.popleft()
        
        if a <= 0 and b <= 0 and c <= 0:
            print(count)
            break
        for pattern in attack_patterns:
            na = max(0, a - pattern[0])
            nb = max(0, b - pattern[1])
            nc = max(0, c - pattern[2])

            if (na, nb, nc) not in visited:
                visited.add((na, nb, nc))
                dq.append((na, nb, nc, count + 1))


"""
문제를 풀면서 어떻게 접근해야하는지는 쉽게 생각할 수 있었다.
대신 구체적인 구현에서 생각할 점이 많았다

1. 3개 이하의 갯수이기 때문에 각 경우별로 처리해야하는지 3개로 맞춰줘서 처리해야하는지
- 이 경우는 0을 채워넣어 항상 3가지 경우일 때 처리하게 하였다.

2. visited 처리 경우
- visited를 어떻게 처리해야할 지 생각이 안났는데 set을 사용해서 코드를 쉽고 간결하게 짤 수 있었다.

3. permutation
- 6가지 경우라서 수를 사용해서 직접 구현하려다가 그냥 permutation을 사용했다.
라이브러리를 통해 코드 가독성을 높이고 실수를 줄일 수 있었다.

직접적인 구현에 대해 복습할만한 문제인 것 같다.
"""


        




    
        





