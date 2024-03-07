


# data = [1,2,3,4,5,6,7,8,9,10] 

data = [2,4,6,8,10,12,14,16,18,20]
tree = [0] * (len(data) * 4)


def seg_tree_init(idx, start, end):
    global tree
    if (start == end):
        tree[idx] = data[start]
        
    else:
        left_idx = 2*idx
        right_idx = 2*idx+1
        mid = (end+start)//2
        seg_tree_init(left_idx, start, mid)
        seg_tree_init(right_idx, mid+1, end)
        tree[idx] = tree[left_idx] + tree[right_idx]


seg_tree_init(1,0,9)
print(tree)
    

def seg_tree_section_sum(idx, start,end,left,right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[idx]
    
    left_idx = 2*idx
    right_idx = 2*idx + 1
    mid = (end+start)//2
    return seg_tree_section_sum(left_idx, start, mid, left,right) + seg_tree_section_sum(right_idx, mid +1, end, left, right)

section_sum = seg_tree_section_sum(1,0,9,6,9)
print(section_sum) # 68
        

# 특정 값이 before에서 value만큼 더해졌을 때 세그먼트 트리 전체 갱신
def seg_tree_update(idx, start, end, before_idx, value):
    # 바꾸려는 값이 범위에 없으면 pass
    if before_idx > end or before_idx < start:
        return 
    
    #범위에 있으면 해당 값만큼 추가해준다.
    tree[idx] += value
    if start == end:
        return
    

    left_idx = 2*idx
    right_idx = 2*idx + 1
    mid = (end+start)//2
    seg_tree_update(left_idx, start, mid, before_idx, value)
    seg_tree_update(right_idx, mid + 1, end, before_idx, value)

# idx는 항상 1, 데이터 전체 구간에 대해 data[8]번 값을 +4 해준 상태로 세그먼트 트리 update
seg_tree_update(1,0,len(data)-1,8,4)
data[8] += 4 # 값 갱신을 해주어야 한다.
print(seg_tree_section_sum(1,0,9,6,9)) # 72

