# 정렬된 nums를 입력받아 이진 검색으로 target에 해당하는 인덱스를 찾아라.

nums = [-1, 0, 3, 5 ,9, 12]
target = 9


# 재귀 풀이
def search(nums, target):
    def binanrySearch(left, right):
        if left<= right:
            mid = (left+right)//2
            
            if target < nums[mid]:
                return binanrySearch(left, mid-1)
            elif target > nums[mid]:
                return binanrySearch(mid+1, right)
            else:
                return mid
        else:
            return -1
    return binanrySearch(0, len(nums)-1)      
print(search(nums, target))

# 반복문 풀이
def search(nums, target):
    left, right = 0, len(nums)-1
    
    while left<= right:
        mid = (left+right)//2

        if target < nums[mid]:
            right =  mid-1
        elif target > nums[mid]:
            left = mid+1
        else:
            return mid
    return -1
        


print(search(nums, target))

# 이진 검색 모듈
import bisect
def search(nums, target):
    index = bisect.bisect_left(nums, target)

    if index < len(nums) and nums[index] == target:
        return index
    else:
        return -1

print(search(nums, target))

# 이진 검색 사용하지 않는 index풀이
def search(nums, target):
    try:
        return nums.index(target)
    except ValueError:
        return -1

print(search(nums, target))
    
