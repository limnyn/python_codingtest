
import sys
input = sys.stdin.readline

"세그먼트 트리 구현 문제"

def seg_tree_init(idx, start, end):
    global tree
    
    if start == end:
        tree[idx] = data[start]
    
    else:
        left_idx = 2*idx
        right_idx = 2*idx + 1
        mid = (start+end)//2
        seg_tree_init(left_idx, start, mid)
        seg_tree_init(right_idx, mid+1,end)
        tree[idx] = tree[left_idx] + tree[right_idx]
        
        

def seg_tree_section_sum(idx, start, end, left, right):
    if left > end or right < start:
        return 0
    
    if left <= start and end <= right:
        return tree[idx]
    
    left_idx = 2*idx
    right_idx = 2*idx + 1
    mid = (start+end)//2
    return seg_tree_section_sum(left_idx, start, mid, left,right) + seg_tree_section_sum(right_idx, mid +1, end, left, right)

def seg_tree_update(idx, start, end, before_idx, value):
    global tree
    if before_idx > end or before_idx < start:
        return
    
    tree[idx] += value
    if start == end:
        return

    left_idx = 2*idx
    right_idx = 2*idx + 1
    mid = (start+end)//2
    seg_tree_update(left_idx,start,mid,before_idx, value)
    seg_tree_update(right_idx,mid+1,end,before_idx, value)



#데이터 입력
n, m, k = map(int, input().split())
data = []
result = []

for i in range(n):
    data.append(int(input()))

#세그먼트 트리 초기화
tree = [0] * 4*n
seg_tree_init(1, 0, n-1) 
# 명령 입력
for k in range(m + k):
    a, b, c = map(int, input().split())
    b -= 1
    # b번째 수를 c로 바꾸기
    if a == 1:
        seg_tree_update(1,0,n-1,b,c-data[b])
        data[b] = c
        
    # b~c까지의 합을 구하여 출력
    elif a == 2:
        c -= 1
        result.append(seg_tree_section_sum(1,0,n-1,b,c))
        
for r in result:
    print(r)
    


