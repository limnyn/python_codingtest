# 딱 하나를 제외하고 모든 엘리먼트는 2개씩 있다. 1개인 엘리먼트를 찾아라.
nums = [2, 2, 1]

# 비트 연산을 통한 XOR 풀이
def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
print(singleNumber(nums))
