# 정렬된 배열을 받아 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
# 주의 : 이 문제에서 배열은 0이 아닌 1부터  시작하는 것으로 한다

numbers = [2, 7, 11, 15]
target = 9


# 투 포인터
def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1
    while not left == right:
        if numbers[left] + numbers[right] < target:
            left += 1
        elif numbers[left] + numbers[right] > target:
            right -= 1
        else:
            return left + 1, right + 1

print(twoSum(numbers,target))

# bisect모듈, 슬라이싱제거
def twoSum(numbers, target):
    import bisect
    for k, v, in enumerate(numbers):
        expected = target - v
        i = bisect.bisect_left(numbers, expected, k+ 1)
        if i < len(numbers) and numbers[i] == expected:
            return k+1, i+ 1

print(twoSum(numbers,target))

