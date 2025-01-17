# https://www.acmicpc.net/problem/1043
"""
진실을 알고있는 사람, 그리고 그 사람과 같은 그룹에 포함된 사람들을 찾고
그 사람들이 포함되지 않은 파티 갯수를 구하기

[연산]
1. 각 행에 대해 진실을 알고 있는 사람들과 같은 파티원들을 Union 한다.
2. Union 된 사람들이 존재하는 파티를 제외한 나머지 파티 갯수가 정답 
"""
import sys
def input(): return sys.stdin.readline().rstrip()

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # 경로 압축
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a != b:
        parent[b] = a

if __name__ == "__main__":
    n, m = map(int, input().split())
    truth = list(map(int, input().split()))

    if len(truth) > 1:
        truth = truth[1:]
    else:
        truth = []

    parties = []
    for _ in range(m):
        data = list(map(int, input().split()))
        parties.append(data[1:])

    # 초기화
    parent = list(range(n + 1))

    # Union-Find로 그룹화
    for party in parties:
        for i in range(1, len(party)):
            union(parent, party[0], party[i])

    # 진실을 아는 그룹의 루트를 계산
    truth_root = {find(parent, person) for person in truth}

    # 거짓말 가능한 파티 계산
    lie_count = 0
    for party in parties:
        if all(find(parent, person) not in truth_root for person in party):
            lie_count += 1

    print(lie_count)
