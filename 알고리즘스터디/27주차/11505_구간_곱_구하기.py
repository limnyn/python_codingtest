# https://www.acmicpc.net/problem/11505
import sys
input = sys.stdin.readline

MOD = 1_000_000_007

def seg_tree_init(idx, start, end):
    if start == end:
        tree[idx] = data[start]
    else:
        mid = (start + end) // 2
        left_idx = 2 * idx
        right_idx = 2 * idx + 1
        seg_tree_init(left_idx, start, mid)
        seg_tree_init(right_idx, mid + 1, end)
        tree[idx] = (tree[left_idx] * tree[right_idx]) % MOD

def seg_tree_section_product(idx, start, end, left, right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[idx]
    mid = (start + end) // 2
    left_idx = 2 * idx
    right_idx = 2 * idx + 1
    left_product = seg_tree_section_product(left_idx, start, mid, left, right)
    right_product = seg_tree_section_product(right_idx, mid + 1, end, left, right)
    return (left_product * right_product) % MOD

def seg_tree_update(idx, start, end, target_idx, value):
    if target_idx < start or target_idx > end:
        return
    if start == end:
        tree[idx] = value
        return
    mid = (start + end) // 2
    left_idx = 2 * idx
    right_idx = 2 * idx + 1
    seg_tree_update(left_idx, start, mid, target_idx, value)
    seg_tree_update(right_idx, mid + 1, end, target_idx, value)
    tree[idx] = (tree[left_idx] * tree[right_idx]) % MOD

# 데이터 입력
n, m, k = map(int, input().split())
data = [int(input()) for _ in range(n)]

# 세그먼트 트리 초기화
tree = [1] * (4 * n)
seg_tree_init(1, 0, n - 1)

# 명령 입력
result = []
for _ in range(m + k):
    a, b, c = map(int, input().split())
    b -= 1
    if a == 1:
        seg_tree_update(1, 0, n - 1, b, c)
        data[b] = c
    elif a == 2:
        c -= 1
        result.append(seg_tree_section_product(1, 0, n - 1, b, c))

for r in result:
    print(r)
