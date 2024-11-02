# https://www.acmicpc.net/problem/10999
import sys
input = sys.stdin.readline

# 세그먼트 트리 초기화 함수
def seg_tree_init(idx, start, end):
    if start == end:
        tree[idx] = data[start]
    else:
        mid = (start + end) // 2
        seg_tree_init(2 * idx, start, mid)
        seg_tree_init(2 * idx + 1, mid + 1, end)
        tree[idx] = tree[2 * idx] + tree[2 * idx + 1]

# Lazy propagation을 사용한 구간 업데이트 함수
def range_update(idx, start, end, left, right, value):
    # 현재 노드에 지연된 업데이트가 있다면 반영
    if lazy[idx] != 0:
        tree[idx] += (end - start + 1) * lazy[idx]
        # 자식 노드로 지연값 전파
        if start != end:
            lazy[2 * idx] += lazy[idx]
            lazy[2 * idx + 1] += lazy[idx]
        lazy[idx] = 0

    # 업데이트 범위를 벗어난 경우
    if right < start or end < left:
        return

    # 현재 구간이 업데이트 범위에 완전히 포함되는 경우
    if left <= start and end <= right:
        tree[idx] += (end - start + 1) * value
        # 자식 노드에 지연값 저장
        if start != end:
            lazy[2 * idx] += value
            lazy[2 * idx + 1] += value
        return

    # 구간이 걸쳐 있는 경우 재귀적으로 자식 노드 갱신
    mid = (start + end) // 2
    range_update(2 * idx, start, mid, left, right, value)
    range_update(2 * idx + 1, mid + 1, end, left, right, value)
    tree[idx] = tree[2 * idx] + tree[2 * idx + 1]

# Lazy propagation을 사용한 구간 합 구하기 함수
def range_sum_query(idx, start, end, left, right):
    # 현재 노드에 지연된 업데이트가 있다면 반영
    if lazy[idx] != 0:
        tree[idx] += (end - start + 1) * lazy[idx]
        # 자식 노드로 지연값 전파
        if start != end:
            lazy[2 * idx] += lazy[idx]
            lazy[2 * idx + 1] += lazy[idx]
        lazy[idx] = 0

    # 구간이 범위를 벗어난 경우
    if right < start or end < left:
        return 0

    # 구간이 범위에 완전히 포함되는 경우
    if left <= start and end <= right:
        return tree[idx]

    # 구간이 걸쳐 있는 경우 자식 노드에서 구간 합 계산
    mid = (start + end) // 2
    left_sum = range_sum_query(2 * idx, start, mid, left, right)
    right_sum = range_sum_query(2 * idx + 1, mid + 1, end, left, right)
    return left_sum + right_sum

# 입력
n, m, k = map(int, input().split())
data = [int(input().strip()) for _ in range(n)]
tree = [0] * (4 * n)
lazy = [0] * (4 * n)

# 세그먼트 트리 초기화
seg_tree_init(1, 0, n - 1)

# 명령 처리
result = []
for _ in range(m + k):
    command = list(map(int, input().split()))
    if command[0] == 1:
        # b번째 수부터 c번째 수에 d를 더하기
        a, b, c, d = command
        range_update(1, 0, n - 1, b - 1, c - 1, d)
    elif command[0] == 2:
        # b번째 수부터 c번째 수의 합 구하기
        a, b, c = command
        sum_result = range_sum_query(1, 0, n - 1, b - 1, c - 1)
        result.append(sum_result)

# 결과 출력
for res in result:
    print(res)
