# 특정 피벗을 기준으로 회전하여 정렬된 배열에서 target 값의 인덱스를 출력하라.

nums = [4, 5, 6, 7, 0, 1, 2]
target = 1

def search(nums, target):
    if not nums :
        return -1

    # 최솟값을 찾아 피벗 설정
    left, right = 0, len(nums)-1

    while left < right:
        mid = left + (right-left)//2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    pivot = left

    # 피벗 기준 이진 검색
    left, right = 0, len(nums)-1

    while left <= right:
        mid = left + (right-left)//2
        mid_pivot = (mid + pivot) % len(nums)

        if nums[mid_pivot] < target:
            left = mid + 1
        elif nums[mid_pivot] > target:
            right = mid - 1
        else:
            return mid_pivot
    return -1

print(search(nums,target))

    


