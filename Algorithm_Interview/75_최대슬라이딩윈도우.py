# 배열 nums가 주어졌을 때 k 크기의 슬라이딩 윈도우를 
# 오른쪽 끝까지 이동하면서 최대 슬라이딩 윈도우를 구하라.

nums = [1,3,-1,-3,5,3,6,7]
k = 3
# 슬라이싱 기법
def slidingWindowMaxsum(nums, k):
    if not nums:
        return -1
    result = []
    for i in range(0,len(nums)-2):
        result.append(max(nums[i:i+3]))
    return result

print(slidingWindowMaxsum(nums, k))

# 큐를 이용한 최적화 -> max 연산을 줄이기 위해 큐 삽입시 이전값의 max와 비
def slidingWindowMaxsum(nums, k):
    import collections
    window =collections.deque()

    if not nums:
        return -1
    result = []
    for i in nums[0:3]:
        window.append(i)
    result.append(max(nums[:3]))

    for i in range(3,len(nums)):
        if window.popleft() >nums[i]:
            result.append(result[-1])
        else:
            result.append(nums[i])
        window.append(nums[i])
    return result

print(slidingWindowMaxsum(nums, k))
