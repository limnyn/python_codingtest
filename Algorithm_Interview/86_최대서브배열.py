# 합이 최대가 되는 연속 서브 배열을 찾아 합을 리턴하라.
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# pythonic way
def maxSubarray(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i-1] if nums[i-1] > 0 else 0
    return max(nums)

print(maxSubarray(nums))

def maxSubArray(nums):
    import sys
    best_sum = -sys.maxsize
    for num in nums:
        current_sum = 0
        current_sum = max(num, current_sum + num)
        best_sum = max(best_sum, current_sum)

    return best_sum

print(maxSubArray(nums))