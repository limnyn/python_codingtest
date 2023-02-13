# 두배열의 교집합을 구하라

# 입력
nums1 = [4, 9, 5]
nums2= [9,4,9,8,4]

# 파이썬 내장 모듈
print(list(set.intersection(set(nums1), set(nums2))))

# 이진 검색으로 일치 여부 판별

def intersection(nums1, nums2):
    import bisect
    result = set()
    nums2.sort()
    for n1 in nums1:
        # 이진검색으로 일치 여부 판별
        i2 = bisect.bisect_left(nums2, n1)
        if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
            result.add(n1)

    return result

print(intersection(nums1,nums2))
    
# 투 포인터로 일치 여부 판

def intersection(nums1, nums2):
    result = set()
    nums1.sort()
    nums2.sort()
    i = j = 0
    # 투 포인터 우측으로 이동하며 일치 여부 판별
    while i < len(nums1) and j < len(nums2):
        if nums1[i] > nums2[j]:
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            result.add(nums1[i])
            i += 1
            j += 1
    return result

print(intersection(nums1,nums2))
    
