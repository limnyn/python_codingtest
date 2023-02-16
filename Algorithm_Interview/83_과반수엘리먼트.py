# 과반수를 차지하는(절반을 초과하는) 엘리먼트를 출력하라.
import collections

nums = [3, 2, 3]

# 다이나믹 프로그래밍
def majorityElement(nums):
    counts = collections.defaultdict(int)
    for num in nums:
        if counts[num] == 0:
            counts[num] = nums.count(num)
        
        if counts[num] > len(nums) // 2:
            return num
print(majorityElement(nums))

# pythonic way
def majorityElement(nums):
    return sorted(nums)[len(nums)//2]
print(majorityElement(nums))