# 여러 번의 거래로 낼 수 있는 최대 이익을 산출하라.
nums = [7,1,5,3,6,4]

def maxProfit(nums):
    result = 0
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            result += nums[i+1] -nums[i]
    return result

print(maxProfit(nums)) 

# pythonic way
def maxProfit(nums):
    # 0보다 크면 무조건 합산
    return sum(max(nums[i + 1] - nums[i], 0) for i in range(len(nums) - 1))
print(maxProfit(nums))