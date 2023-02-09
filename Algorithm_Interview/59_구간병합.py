# 겹치는 구간을 병합하라
nums = [[1,3],[2,6],[8,10],[15,18]]
nums = sorted(nums, key= lambda x :x[0])

merged = []
for i in sorted(nums, key=lambda x : x[0]):
    if merged and i[0] <= merged[-1][1]:
        merged[-1][1] = max(merged[-1][1], i[1])
    else:
        merged += i,
print(merged)