# 빨간색을 0, 흰색을 1, 파란색을 2라 할 때
# 순서대로 인접하는 제자리 정렬을 수행하라

nums = [2, 0, 2, 1, 1, 0]
# output = [0, 0, 1, 1, 2, 2]

# 네덜란드 국기 문제를 응용한 풀이
def sortColors(nums):
    red,white, blue = 0, 0, len(nums)
    while white < blue:
        if nums[white] < 1:
            nums[red], nums[white] = nums[white], nums[red]
            white += 1
            red += 1
        elif nums [white] > 1:
            blue -= 1
            nums[white], nums[blue] = nums[blue], nums[white]
        else:
            white += 1
sortColors(nums)
print(nums)

            